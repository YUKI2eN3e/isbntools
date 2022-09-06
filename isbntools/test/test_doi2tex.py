# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""nose tests for doi2tex."""

from nose.tools import assert_equals

from ..app import doi2tex


def test_doi2tex():
    """Test the doi2tex service."""
    assert (len(repr(doi2tex('10.2139/ssrn.2411669'))) > 50) == True
