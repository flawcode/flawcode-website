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
import flawcode


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
    assert rv.status_code == 302