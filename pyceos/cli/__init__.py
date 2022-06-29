import argparse

from . import dump


def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        metavar="subcommand",
        required=True
    )

    dump.add_parser(subparsers)

    return parser


def main():
    parser = get_parser()

    args = parser.parse_args()
    args.func(args)
