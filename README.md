# ComunicationLTD


## Installation

1) Create a folder named "securityCommunicationLTD"-

```mkdir securityCommunicationLTD```

2) Change the current working directory to "securityCommunicationLTD"-

```cd securityCommunicationLTD```

3) Clone the repository from GitHub-

```git clone https://github.com/OrShaharr/ComunicationLTD.git```

4) Change to the following path-
     
```cd C:\Users\{YOUR USER NAME}\Desktop\securityCommunicationLTD```

5) Create a Python virtual environment-

```python -m venv env```


```env\Scripts\activate```

6) Install all Django framework dependencies-
   		
```pip install -r requirements.txt```

7) Install the django-sslserver package-

```pip install django-sslserver```

8) Navigate to the "settings.py" file and update the following paths using your favorite text editor-
			
```SSL_CERTIFICATE = 'C:\Users\{YOUR USER NAME}\Desktop\sec\ComunicationLTD\localhost.crt'```

```SSL_PRIVATE_KEY = 'C:\Users\{YOUR USER NAME}\Desktop\securityCommunicationLTD\ComunicationLTD\localhost.key'```

9) Back in the terminal, Change to the following path-

 ```C:\Users\{YOUR USER NAME}\Desktop\securityCommunicationLTD\ComunicationLTD ```

10) Turn on the server-

```python manage.py runsslserver```

11) You can now navigate on your browser to ```https://localhost:8000``` to access the website


## Attacks Flags

### To perform an XSS attack-

1. Navigate to the "settings.py" file
2. Scroll to the bottom of the file
3. Change ```XSS = FALSE``` to ```XSS = TRUE```
4. Create a user
5. Log in to the created user
6. Navigate to Customers list via button

###  To perform an SQLi attack-

1. Navigate to the "settings.py" file
2. Scroll to the bottom of the file
3. Change ```SQLI = False``` to ```SQLI = False```
4. you can now try the SQLi on the Register, Login or Customers registration screens


* You will see the output of the attacks on your terminal

                              
