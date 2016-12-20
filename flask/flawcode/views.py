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

from flawcode import app
from flawcode.helpers import show_notes


@app.route('/')
def index():
    return redirect(url_for('shows', ep_no='4'))


@app.route('/episode/show/<ep_no>')
def shows(ep_no):
    show_notes_text = show_notes(ep_no)
    return render_template("shows.html", name=ep_no,
                           show_notes_text=show_notes_text,
                           episodes=[1, 2, 3, 4])


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
