# -*- coding: utf-8 -*-
"""
    FlawCode
    ~~~~~~
    This is the podcast website written in Flask
    :copyright: (c) 2016 by Joydeep Bhattacharjee.
    :license: MIT, see LICENSE for more details.
"""

import markdown
from flask import render_template
from flask import redirect
from flask import url_for
from flask import Markup
from flask import Flask

from core.helpers import show_notes
from core.helpers import get_last_4episode_num
from core.helpers import get_archives_content
from core.settings import EPISODE_COUNT

app = Flask(__name__)
app.config.from_object('core.settings')


@app.route('/')
def index():
    return redirect(url_for('shows', ep_no=str(EPISODE_COUNT)))


@app.route('/who_we_are')
def who_we_are():
    return render_template("who_we_are.html", episodes=get_last_4episode_num(EPISODE_COUNT))


@app.route('/archives')
def archives():
    return render_template(
            "archives.html", episodes=get_last_4episode_num(EPISODE_COUNT),
            archives=get_archives_content(EPISODE_COUNT)
    )


@app.route('/episode/show/<ep_no>')
def shows(ep_no):
    content = Markup(markdown.markdown(show_notes(ep_no)))
    return render_template("layout.html", name=ep_no,
                           episodes=get_last_4episode_num(EPISODE_COUNT),
                           content=content)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
