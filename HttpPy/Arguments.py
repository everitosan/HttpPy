"""
Parse parameters
"""
import argparse
import sys


def __is_param_absent(abrv, cplt):
    is_in = abrv in sys.argv or cplt in sys.argv
    return not is_in

def parse():
    """
    Main parser for inline params
    """
    parser = argparse.ArgumentParser(description="Parse arguments to make requests")
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=__is_param_absent("-t", "--type")
    )
    parser.add_argument(
        "-t",
        "--type",
        type=str,
        required=__is_param_absent("-i", "--input")
    )
    parser.add_argument(
        "-u",
        "--url",
        type=str,
        required=__is_param_absent("-i", "--input")
    )
    parser.add_argument(
        "-d",
        "--data",
        type=str,
        required=False
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        required=False
    )

    parser.add_argument(
        "-p",
        "--parallel",
        action="store_true",
        required=False
    )

    return parser.parse_args()
