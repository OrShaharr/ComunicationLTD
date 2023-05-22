from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.views.generic import FormView
from django.contrib.auth import authenticate,login
from django.db import connection
from .forms import RegisterForm, LoginForm,RegisterCustomerForm
from .models import Customer
from django.conf import settings
from django.db import connections



def home(request):
    return render(request, 'users/home.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            if settings.SQLI:
                with connections['default'].cursor() as cursor:
                    first_name = form.data.get('first_name')
                    query = f"SELECT * FROM auth_user WHERE first_name='{first_name}'"
                    cursor.execute(query)
                    response = cursor.fetchall()
                    print(str(response))
            else:
                form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm
    
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')

class RegisterCustomerView(View):
    form_class = RegisterCustomerForm
    initial = {'key': 'value'}
    template_name = 'users/registerCustomer.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            Name = form.cleaned_data.get('name')
            Email = form.cleaned_data.get('email')
            Phone = form.cleaned_data.get('phone')
            my_instance = Customer(name=Name,email=Email,phone=Phone)
            if settings.SQLI:
                with connections['default'].cursor() as cursor:
                    name = form.data.get('name')
                    query = f"SELECT * FROM users_customer WHERE name='{name}'"
                    cursor.execute(query)
                    response = cursor.fetchall()
                    print(str(response))
            else:
                my_instance.save(using='default')
            messages.success(request, f'Account created for {Name}')
        return render(request, self.template_name, {'form': form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'users/customer_list.html', {'customers':customers})