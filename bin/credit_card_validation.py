#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Perform sanity check against credit card numbers. """

__all__ = [
    "company",
    "luhn_number_check",
    "validate_credit_card"
]

__author__ = "syntaxval"
__copyright__ = "copyright (c) 2017"
__version__ = "0.0.1"
__license__ = "BSD 2-Clause license"



# ...
def company(number):
    """ Determine issuing company based on some number rules. """

    # AMEX
    if (
            (number.startswith("34")
             or number.startswith("37"))
            and len(number) == 15
        ):
        return "AMEX"

    # Discover
    if number.startswith("6011") and len(number) == 16:
        return "Discover"

    # MasterCard
    if int(number[0:2]) in range(51, 56) and len(number) == 16:
        return "MasterCard"

    # Visa
    if (
            number.startswith("4") and (
                len(number) == 13 or len(number) == 16)
        ):
        return "VISA"

    return "Unknown"




# ...
def luhn_number_check(number):
    """ Determine if the number is valid using Luhn algorithm """

    def sum_double_digits(number):
        """ Sum up digits of numbers composed of more than one digit. """

        return reduce(lambda x, y: int(x)+int(y), str(number), 0)


    # 0. get check digit (for clarity's sake)
    check_digit = int(number[-1])

    # 1. create a list of digits out of the number string and reverse it
    # skip the last check digit.
    reversed_no_check_digit = [int(c) for c in list(reversed(number[0:-1]))]

    # 2. create a list of untouched digits (will sum those up later on)
    # (every odd-th digit, when looking at the reversed list)
    untouched_digits = [int(d) for d in reversed_no_check_digit[1::2]]

    # 3. create a list of digits to double on (every even-th digit when looking
    # at the reversed list)
    digits_to_double = [int(d) for d in reversed_no_check_digit[::2]]

    # 4. create a list of doubled digits based on the list of digits to double up
    doubled_digits = [d+d for d in digits_to_double]

    # 5. create a list of digits that is 'flattened' to all single digits.
    # All numbers consisting of double digits have their digits split and added
    # together (i.e. 17 --> 1+7 = 8)
    summed_double_digits = [sum_double_digits(num) for num in doubled_digits]

    # 6. Determine if the credit card number is valid based on sum
    # of the following:
    #    untouched_digits
    #    summed_double_digits
    #    check_digit
    # then check if the sum of the above is a multiple of 10 (valid number)
    if (sum(untouched_digits) + sum(summed_double_digits) + check_digit) % 10 == 0:
        return "valid"

    return "invalid"




# ...
def validate_credit_card(number):
    """ Provides formatted string with information about
        supplied credit card number """

    number = str(number).replace(" ", "")
    if number.isdigit():
        return "{0}: {1} ({2})".format(
            company(number), number, luhn_number_check(number))

    return "non numeric input"




# When executed from the command line. (provide credit card number(s) as an
# argument list.
if __name__ == "__main__":
    import sys
    for arg in sys.argv[1::]:
        print validate_credit_card(arg)
