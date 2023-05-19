from django.urls import path
from .views import home, RegisterView,RegisterCustomerView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('customers_register',RegisterCustomerView.as_view(),name='customers_register')
]
