# -*- coding: utf-8 -*-
"""
    flawcode Tests
    ~~~~~~~~~~~~

    Tests the flawcode application.

    :copyright: (c) 2016 by Joydeep Bhattacharjee.
    :license: MIT, see LICENSE for more details.
"""

import os
import tempfile
import pytest
from flawcode import flawcode


@pytest.fixture
def client(request):
    flawcode.app.config['TESTING'] = True
    client = flawcode.app.test_client()

    def teardown():
        pass
    request.addfinalizer(teardown)

    return client


def test_webpage(client):
    """Just test if there is a webpage"""
    rv = client.get('/')
    assert b'No entries here so far' in rv.data


# def login(client, username, password):
#     return client.post('/login', data=dict(
#         username=username,
#         password=password
#     ), follow_redirects=True)


# def logout(client):
#     return client.get('/logout', follow_redirects=True)


# def test_empty_db(client):
#     """Start with a blank database."""
#     rv = client.get('/')
#     assert b'No entries here so far' in rv.data


# def test_login_logout(client):
#     """Make sure login and logout works"""
#     rv = login(client, flawcode.app.config['USERNAME'],
#                flawcode.app.config['PASSWORD'])
#     assert b'You were logged in' in rv.data
#     rv = logout(client)
#     assert b'You were logged out' in rv.data
#     rv = login(client, flawcode.app.config['USERNAME'] + 'x',
#                flawcode.app.config['PASSWORD'])
#     assert b'Invalid username' in rv.data
#     rv = login(client, flawcode.app.config['USERNAME'],
#                flawcode.app.config['PASSWORD'] + 'x')
#     assert b'Invalid password' in rv.data


# def test_messages(client):
#     """Test that messages work"""
#     login(client, flawcode.app.config['USERNAME'],
#           flawcode.app.config['PASSWORD'])
#     rv = client.post('/add', data=dict(
#         title='<Hello>',
#         text='<strong>HTML</strong> allowed here'
#     ), follow_redirects=True)
#     assert b'No entries here so far' not in rv.data
#     assert b'&lt;Hello&gt;' in rv.data
#     assert b'<strong>HTML</strong> allowed here' in rv.data