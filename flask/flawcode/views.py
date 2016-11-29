# -*- coding: utf-8 -*-
"""
    FlawCode
    ~~~~~~
    This is the podcast website written in Flask
    :copyright: (c) 2016 by Joydeep Bhattacharjee.
    :license: MIT, see LICENSE for more details.
"""

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for


@app.route('/')
def index():
    return redirect(url_for('shows', ep_no='4'))


@app.route('/episode/show/<ep_no>')
def shows(ep_no):
    return render_template("shows.html", name=ep_no)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404