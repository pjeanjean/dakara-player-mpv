#!/usr/bin/env python3
from argparse import ArgumentParser

from dakara_player_vlc.tests.tests import DakaraTestRunner


def get_parser():
    parser = ArgumentParser(
        description="Interface to test the Dakara player"
    )

    parser.add_argument(
        'target',
        nargs='?',
        help="select which test to run (by default, all tests are run)",
        default=None
    )

    parser.add_argument(
        '-v',
        '--verbose',
        help="enable verbose output",
        action="store_true"
    )

    return parser


def test(args):
    dakara_test_runner = DakaraTestRunner(args.target, args.verbose)
    print("Running tests for the Dakara player")
    ok = dakara_test_runner.run()
    exit(not ok)


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    test(args)