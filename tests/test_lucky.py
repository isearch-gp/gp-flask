#import os
#import tempfile

import pytest

#import lucky  E   ModuleNotFoundError: No module named 'lucky'
#import ../lucky  E   SyntaxError: invalid syntax
#from . import lucky  E   ImportError: attempted relative import with no known parent package
#from .. import lucky  E   ImportError: attempted relative import with no known parent package
#from lucky import app  E   ModuleNotFoundError: No module named 'lucky'
from lucky import app
#import app


@pytest.fixture
def client():
    #db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        #flaskr.init_db()
        print("in app_context")

    yield client

    #os.close(db_fd)
    #os.unlink(flaskr.app.config['DATABASE'])

