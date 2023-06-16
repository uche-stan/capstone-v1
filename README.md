# capstone-v1

1. mysql database configuration:

go to Settings.py and update the database as shown below

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'booking_db',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'admindjango',
        'PASSWORD': 'employee123!'
    }
}


2. API ENDPOINTS

Create a user: method: POST
http://127.0.0.1:8000/auth/users/

Create a user token: method: POST
http://127.0.0.1:8000/auth/token/login

View Menu items: method: GET
http://127.0.0.1:8000/api/menu-items
