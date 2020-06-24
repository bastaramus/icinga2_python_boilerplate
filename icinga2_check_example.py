#!/usr/bin/env python3

"""
Boilerplate Icinga2 check script.
"""

__author__ = "Dmytro Khomenko"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import logging
import os, sys

icinga_codes = {'OK': 0, 
    			'WARNING': 1, 
				'CRITICAL': 2,
				'UNKNOWN': 3}

def icinga_return(code, response, perfdata=None):
    if perfdata is not None:
        print(code + ": " + response + " | " + perfdata)
    else:
        print(code + ": " + response)
    sys.exit(icinga_codes[code])

def check_condition():
    """ Put some logic here
        Return check status code and message.
    """
    return dict(code = "OK", message = "This host or service is okay.")

def parse_args():
    parser = argparse.ArgumentParser(
        description='Script usage'
    )

    # Required positional argument
    parser.add_argument("arg", help="Required positional argument")

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag", action="store_true", dest='flag', default=False)

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-n", "--name", action="store", dest="name")

    parser.add_argument(
        '-w', '--warning',
        metavar='warning_threshold',
        required=False,
        help='Define warning threshold'
    )

    parser.add_argument(
        '-c', '--critical',
        metavar='critical_threshold',
        required=False,
        help='Define critical threshold'
    )

    # Optional verbosity (for debug)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        dest="debug_level",
        default=0,
        help="Verbosity. Enable debug mode in your script.")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    return parser.parse_args()

def main():
    try:
        args = parse_args()
        # Create logger
        # Usually we don't need any other logging level except of debug in Icinga2 check scripts
        if args.debug_level != 0 :
            logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    except:
        icinga_return('UNKNOWN', "Wrong usage")
    logging.debug(args)
    result = check_condition()
    icinga_return(result['code'],result['message'])


if __name__ == "__main__":
    main()