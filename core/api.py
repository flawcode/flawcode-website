# -*- coding: utf-8 -*-
"""
    FlawCode
    ~~~~~~
    This is the podcast website written in Flask
    :copyright: (c) 2016 by Joydeep Bhattacharjee.
    :license: MIT, see LICENSE for more details.
"""

import datetime
import markdown

from threading import Thread

from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
from flask import Markup
from flask import Flask

from itsdangerous import URLSafeTimedSerializer

from flask_sqlalchemy import SQLAlchemy

from flask_mail import Message

from core import app, db, mail

from .helpers import show_notes
from .helpers import get_last_4episode_num
from .helpers import get_archives_content
from .helpers import mp3_file_sizes
from .settings import EPISODE_COUNT
from .settings import SECRET_KEY
from .settings import SUBSCRIBE_TOKEN_SALT
from .settings import UNSUBSCRIBE_TOKEN_SALT
from .settings import MAIL_DEFAULT_SENDER

from .models import User
from .forms import EmailForm

mp3files = mp3_file_sizes()

serializer = URLSafeTimedSerializer(SECRET_KEY)


def gen_sub_unsub_url(target, email, salt):
    token = serializer.dumps(email, salt=salt)
    return url_for(target, token=token, _external=True)


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
        
        
def send_email(email, subject, template):
    msg = Message(
        subject,
        recipients=[email],
        html=template,
        sender=MAIL_DEFAULT_SENDER
    )
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()


@app.route('/')
def index():
    return redirect(url_for('shows', ep_no=str(EPISODE_COUNT)))


@app.route('/who_we_are')
def who_we_are():
    return render_template(
        "who_we_are.html",
        episodes=get_last_4episode_num(EPISODE_COUNT))


@app.route('/archives')
def archives():
    form = EmailForm()
    return render_template(
        "archives.html", 
        episodes=get_last_4episode_num(EPISODE_COUNT),
        archives=get_archives_content(EPISODE_COUNT),
        form=form)


@app.route('/episode/show/<ep_no>')
def shows(ep_no):
    form = EmailForm()
    show_notes_md = show_notes(ep_no).format(file_size=mp3files[ep_no])
    content = Markup(markdown.markdown(show_notes_md))
    return render_template(
        "layout.html", 
        name=ep_no,
        episodes=get_last_4episode_num(EPISODE_COUNT),
        content=content,
        form=form)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = EmailForm()
    if form.validate_on_submit():
        user_email = form.email.data

        if User.query.filter_by(email=user_email).first() is None:
            db.session.add(User(
                email = user_email,
                confirmation_sent_on = datetime.datetime.now())
            )
            db.session.commit()
            confirm_url = gen_sub_unsub_url('confirm_url', user_email, SUBSCRIBE_TOKEN_SALT)
            remove_url = gen_sub_unsub_url('remove_url', user_email, UNSUBSCRIBE_TOKEN_SALT)
            html = render_template('email_confirm.html', confirm_url=confirm_url, remove_url=remove_url)
            send_email(user_email, "Confirm your Email with FlawCode Podcasts", html)
            flash('Thanks for subscribing! Please check your email to confirm your email address.', 'alert-success')
        else:
            flash('Email address you entered is already registered. Please submit a different email address.', 'alert-warning')
    return redirect('/')


@app.route('/subscribe/<token>')
def confirm_url(token):
    try:
        email = serializer.loads(token, salt=SUBSCRIBE_TOKEN_SALT, max_age=86400)
    except:
        flash('The confirmation link is either invalid or has expired', 'alert-danger')
        return redirect('/')
    user = User.query.filter_by(email=email).first_or_404()
    if user is not None:
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        remove_url = gen_sub_unsub_url('remove_url', user.email, UNSUBSCRIBE_TOKEN_SALT)
        html = render_template('email_subscribed.html', remove_url=remove_url)
        send_email(email, "Thank you for subscribing to FlawCode Podcasts", html)
        flash('Thank you for confirming your email address. You will now start receiving updates from FlawCode!', 'alert-success')
    return redirect('/')


@app.route('/unsubscribe/<token>')
def remove_url(token):
    try:
        email = serializer.loads(token, salt=UNSUBSCRIBE_TOKEN_SALT, max_age=86400)
    except:
        return render_template('404.html'), 404
    user = User.query.filter_by(email=email).first_or_404()
    if user is not None:
        db.session.delete(user)
        db.session.commit()
        html = render_template('email_unsubscribed.html')
        send_email(email, 'You have been unsubscribed from FlawCode Podcasts', html)
        flash('You have been unsubscribed from FlawCode Podcasts', 'alert-warning')
    return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
