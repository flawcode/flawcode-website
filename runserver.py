"""
The driver of the flawcode application.
Make changes here in case you want to change the settings.
"""

__author__ = 'joydeep bhattacharjee'

from core.api import app

if __name__ == '__main__':
    app.run(host='0.0.0.0')
