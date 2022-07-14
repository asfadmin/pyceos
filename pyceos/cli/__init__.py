import argparse
import sys

from . import dump, slice


def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        metavar="subcommand",
        required=True
    )

    dump.add_parser(subparsers)
    slice.add_parser(subparsers)

    return parser


def main():
    parser = get_parser()

    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}", file=sys.stderr)
        exit(-1)
