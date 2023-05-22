# ComunicationLTD

1) To create a folder named "securityCommunicationLTD":

mkdir securityCommunicationLTD

2) Change the current working directory to "securityCommunicationLTD" "securityCommunicationLTD"

cd securityCommunicationLTD

3) Clone the repository from GitHub:

 https://github.com/OrShaharr/ComunicationLTD.git

Change to the following path: C:\Users\{YOUR USER NAME}\Desktop\securityCommunicationLTD and create a Python virtual environment:

python -m venv env
env\Scripts\activate

6) Install all Django framework dependencies:
pip install -r requirements.txt


7)Install the django-sslserver package:

 pip install django-sslserver

8) Navigate to the "settings.py" file and update the following paths:
SSL_CERTIFICATE = 'C:\Users\{YOUR USER NAME}\Desktop\sec\ComunicationLTD\localhost.crt'

SSL_PRIVATE_KEY = 'C:\Users\{YOUR USER NAME}\Desktop\securityCommunicationLTD\ComunicationLTD\localhost.key'

9) Change to the following path: C:\Users\Eden\Desktop\securityCommunicationLTD\ComunicationLTD and bring up the server: 

python manage.py runsslserver


10)To perform an XSS attack:
a) Navigate to the "settings.py" file.
b) Scroll to the bottom of the file.
c) Change XSS = FALSE to XSS = TRUE.
d) Create a user.
e) Log in to the created user.
f) Navigate to https://localhost:8000/customer_list/.

11)To perform an SQLi attack:
a) Navigate to the "settings.py" file.
b) Scroll to the bottom of the file.
c) Change SQLI = False to SQLI = False.



                              
