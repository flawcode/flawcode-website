# -*- coding: utf-8 -*-
"""
    FlawCode
    ~~~~~~
    This is the podcast website written in Flask
    :copyright: (c) 2016 by Joydeep Bhattacharjee.
    :license: MIT, see LICENSE for more details.
"""

import markdown
from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import Markup

from flawcode import app
from flawcode.helpers import show_notes
from flawcode.helpers import directly_linked_old


EPISODE_COUNT = 4


@app.route('/')
def index():
    return redirect(url_for('shows', ep_no='4'))


@app.route('/episode/show/<ep_no>')
def shows(ep_no):
    # show_notes_text = show_notes(ep_no)
    content = Markup(markdown.markdown(show_notes(ep_no)))
    print(content)
    # return render_template("shows.html", name=ep_no,
    #                        show_notes_text=show_notes_text,
    #                        episodes=directly_linked_old(EPISODE_COUNT))
    return render_template("shows.html", name=ep_no,
                           episodes=directly_linked_old(EPISODE_COUNT),
                           **locals())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
