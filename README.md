
# Paypal Django Example

This is a basic example of how to use the django-paypal library.

# Configuration

##Postgresql basic configuration.

    $ sudo apt-get update
    $ sudo apt-get install libpq-dev python-dev
    $ sudo apt-get install postgresql postgresql-contrib
    $ sudo su - postgres
    $ createdb mydb
    $ createuser -P userexample
    $ psql
    $ GRANT ALL PRIVILEGES ON DATABASE mydb TO userexample;
    (ctrl-d then type "exit" )

    $ sudo pip install psycopg2
    
    And then put this on the settings.py file.
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'mydb',# database name
            'USER': 'userexample', # username
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '',
        }
    }


## Django-paypal instalation :

    $ pip install django-paypal
    
    
## References :

    https://django-paypal.readthedocs.io/en/stable/