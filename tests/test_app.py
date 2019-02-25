#import os
#import tempfile

import pytest

#import lucky  E   ModuleNotFoundError: No module named 'lucky'
#import ../lucky  E   SyntaxError: invalid syntax
#from . import lucky  E   ImportError: attempted relative import with no known parent package
#from .. import lucky  E   ImportError: attempted relative import with no known parent package
#from lucky import app  E   ModuleNotFoundError: No module named 'lucky'
#from lucky import app
#import app

from pws_api.app import create_app


@pytest.yield_fixture(scope='session')
def app():
    """
    Setup our flask test app, this only gets executed once.
    :return: Flask app
    """
    params = {
        'DEBUG': False,
        'TESTING': True,
        'WTF_CSRF_ENABLED': False
    }

    _app = create_app(settings_override=params)

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test function.
    :param app: Pytest fixture
    :return: Flask app client
    """
yield app.test_client()

