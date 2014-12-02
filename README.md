# restful

## Description

A test for RESTful API service to receive HTTP requests.
The server can automatically parse request and store it 
appropriately, and send an email notification to the 
sender and a dedicated email account immediately.

## Requirements

* Python (2.6.5+, 2.7)
* Django (1.4.2+, 1.5, 1.6, 1.7)
* Django REST framework
You can use pip to install Django REST framework like this:

  $ pip install djangorestframework

## How to test?

First, you should modify the content about sending mails 
in settings.py.

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST='smtp.163.com'

EMAIL_PORT = '25'

EMAIL_HOST_USER='sender@163.com'

EMAIL_HOST_PASSWORD='******'

DEFAULT_FROM_EMAIL='sender@163.com'

DEDICATED_EMAIL='dedicated_email@qq.com'

EMAIL_USE_TLS = True

Change EMAIL_HOST_USER and DEFAULT_FROM_EMAIL to your 
account,  EMAIL_HOST_PASSWORD is your password. 

Second, start the server:

  $ python manage.py runserver

Third, open your brower and enter http://localhost:8000/requests/,
you can login with "user:admin; password:password". 

Then drag the page to the bottom, fill in the form with the data below:

  Media type : application/json

  content : 
  {
    "email": "tester@test.com",
    "first_name": "Peter",
    "last_name": "Pan",
    "contact_number": "86-13227892789",
    "title": "Request Title",
    "content": "Request Content",
    "link": "https://github.com"
  }
  
Then click the post button to send the request. You can also post
request with the tool curl








