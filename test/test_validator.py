#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Test cases for Validator class. """


import sys
sys.path.append("bin/")

from credit_card_validation import validate_credit_card

__all__ = ["test_credit_card_validation"]

__author__ = "syntaxval"
__copyright__ = "copyright (c) 2017"
__version__ = "0.0.1"
__license__ = "BSD 2-Clause license"


def test_credit_card_validation():

    """ Tests several edge cases and correctness of encoding
        for this function. """

    assert validate_credit_card(4111111111111111) == "VISA: 4111111111111111 (valid)"
    assert validate_credit_card(4111111111111) == "VISA: 4111111111111 (invalid)"
    assert validate_credit_card(4012888888881881) == "VISA: 4012888888881881 (valid)"
    assert validate_credit_card(378282246310005) == "AMEX: 378282246310005 (valid)"
    assert validate_credit_card(6011111111111117) == "Discover: 6011111111111117 (valid)"
    assert validate_credit_card(5105105105105100) == "MasterCard: 5105105105105100 (valid)"
    assert validate_credit_card("5105 1051 0510 5106") == "MasterCard: 5105105105105106 (invalid)"
    assert validate_credit_card(9111111111111111) == "Unknown: 9111111111111111 (invalid)"
