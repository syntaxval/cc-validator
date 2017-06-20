#### Credit card number validator with a built-in sanity check.
Performs sanity check on supplied credit card number(s) displaying summary for each:
- issuing company (AMEX, Discover, Visa, MasterCard)
- number and validity

#### Usage
To execute it from command line:

    cd bin
    python credit_card_validation.py credit-card-number [additional numbers]

Credit card number(s) argument(s) can be supplied as Integer or String type.


#### License
This software is released under the BSD 2-Clause license.
See the LICENSE file for more details.

#### Notes
The script was tested and is known to work with python versions 2.7.13 on
windows, but theoretically it should work with all Python 2.7.x installations on Windows and Linux.
