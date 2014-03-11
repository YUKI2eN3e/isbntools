#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def quiet_errors(exc_type, exc_value, traceback):
    """ An error format suitable for end user scripts

        Usage: enter the following lines in your script
               from isbntools import quiet_errors
               sys.excepthook = quiet_errors
    """
    sys.stderr.write('Error: %s\n' % exc_value)


class ISBNToolsException(Exception):
    """ Base class for isbntools exceptions

    This exception should not be raised directly,
    only subclasses of this exception should be used!
    """
    
    def __str__(self):
        return getattr(self, 'message', '')


class NotRecognizedServiceError(ISBNToolsException):
    """ Exception raised when the service is not in registry.py
    """
    
    def __init__(self, service):
        self.message = "(%s) is not a recognized service" % service


class NotValidISBNError(ISBNToolsException):
    """ Exception raised when the ISBN is not valid
    """
    
    def __init__(self, isbnlike):
        self.message = "(%s) is not a valid ISBN" % isbnlike
