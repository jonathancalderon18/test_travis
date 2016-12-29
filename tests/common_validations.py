"""
This module provides functions for performing some common validations during tests, like checking the Content-Type
header, and the status code returned.
"""

from nose.tools import *


def check_content_type(response, content_type='application/json'):
    """
     Validates that the Content-Type of some response is of the expected type (default: application/json)
    """
    eq_(response.headers['Content-Type'], content_type)


def check_status_code(response, code=200):
    """
     Validates that the status code of some response is of the expected kind (default: 200)
    """
    eq_(response.status_code, code)
