# -*- coding: utf-8 -*-
"""
    flawcode Tests
    ~~~~~~~~~~~~

    Tests the flawcode application.

    :copyright: (c) 2016 by Joydeep Bhattacharjee.
    :license: MIT, see LICENSE for more details.
"""

import pytest
import core


@pytest.fixture
def client(request):
    core.app.config['TESTING'] = True
    client = core.app.test_client()

    def teardown():
        pass
    request.addfinalizer(teardown)

    return client


def test_webpage(client):
    """Just test if there is a webpage"""
    rv = client.get('/')
    assert rv.status_code == 302


def test_webpage_all(client):
    """this is to test the 4th page"""
    for ep in range(1, 5):
        rv = client.get('/episode/show/%s' % ep)
        assert rv.status_code == 200


def test_webpage_invalid(client):
    """test the 404 webpages"""
    rv_invalid = client.get('/invalid')
    assert rv_invalid.status_code == 404
