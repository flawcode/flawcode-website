# flawcode

Source code for the technology podcast

www.flawcode.com

Thank you for listening

# Build instructions:

## Ubuntu install node and npm

    sudo apt-get update
    sudo apt-get install nodejs
    sudo apt-get install npm

## pull project files

    git clone git@github.com:flawcode/website.git

## pull the player and install

    cd core/static
    git clone git@github.com:flawcode/paper-audio-player.git

    npm install -g bower
    bower install paper-audio-player --save
    
## this server runs on nginx + gunicorn

the documentation is from this https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04

## Python

we are using python3.6 on ubuntu 16.10

to install python3.6 on ubuntu use the following tutorial

http://askubuntu.com/a/865569/499889
