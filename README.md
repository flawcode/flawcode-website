# flawcode

Source code for the technology podcast

www.flawcode.com

Thank you for listening

# Build instructions:

## pull project files

    git clone git@github.com:flawcode/website.git
    
    
## install dependencies

    pip install -r requirements.txt
    
    
## initialise database and create migrations repository

create the database needed to store email addresses and initialise it.

    python manage.py create_db
    python manage.py db init
    python manage.py db migrate
    
migration is done using the [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/) module.


## sending email

some variables in `settings.py` need to be configured to be able to send emails.
    
    MAIL_USERNAME = 'your@email.com'
    MAIL_PASSWORD = 'yourpassword'
    MAIL_DEFAULT_SENDER = 'your@email.com'
    
default smtp server is set to gmail.com and TLS is enabled. To change these settings edit the following variables:

    MAIL_SERVER = 'your.smtpserver.com'

define port according to your server in `MAIL_PORT`

to enable TLS set `MAIL_USE_TLS` to `True`

to enable SSL set `MAIL_USE_SSL` to `True`

    
## this server runs on nginx + gunicorn

the documentation is from this

* https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04
* https://www.nginx.com/blog/free-certificates-lets-encrypt-and-nginx/


## Python

we are using python3.6 on ubuntu 16.10

to install python3.6 on ubuntu use the following tutorial

http://askubuntu.com/a/865569/499889

# player design

http://www.eighty8design.co.uk/blog/build-responsive-audio-player-html5-sass-js-part-2/
