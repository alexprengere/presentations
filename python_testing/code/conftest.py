
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import pytest


@pytest.fixture
def flights():
    return StringIO('NCE^ORY^4')


@pytest.fixture
def empty_flights():
    return StringIO()
