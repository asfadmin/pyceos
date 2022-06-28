import argparse

from pyceos import CEOSFile


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="CEOS file to list")

    return parser


def main():
    parser = make_parser()
    args = parser.parse_args()

    with CEOSFile(args.file) as f:
        for record in f:
            print(record)
