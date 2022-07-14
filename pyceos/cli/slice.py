import argparse
import pathlib

from construct import Container

from pyceos import CeosRaw

try:
    import jmespath
except ImportError:
    jmespath = None


def add_parser(subparsers: argparse._SubParsersAction):
    parser: argparse.ArgumentParser = subparsers.add_parser(
        "slice",
        help="Extract portions of a CEOS file"
    )
    parser.set_defaults(func=slice)
    parser.add_argument("infile", help="file to read", type=pathlib.Path)
    parser.add_argument("outfile", help="file to write", type=pathlib.Path)

    if jmespath:
        parser.add_argument(
            "filter",
            help="a JMESPath filter expression",
            type=jmespath.compile
        )
    else:
        parser.add_argument(
            "record",
            help="sequence number of the record to extract",
            type=int
        )

    return parser


def slice(args: argparse.Namespace):
    obj = CeosRaw.parse_file(args.infile)

    if hasattr(args, "record") and args.record is not None:
        generator = (
            record
            for record in obj.records
            if record.value.header.sequence_number == args.record
        )
        obj = next(generator, None)
    elif hasattr(args, "filter") and args.filter:
        obj.records = [
            Container(
                **record.value,
                data=record.data
            )
            for record in obj.records
        ]
        obj = args.filter.search(obj)

    with open(args.outfile, "wb") as f:
        written = write_out(f, obj)

    print("wrote", written, "bytes to", args.outfile)


def write_out(f, obj) -> int:
    if isinstance(obj, dict):
        return f.write(obj.data)
    elif isinstance(obj, list):
        total = 0
        for record in obj:
            total += write_out(f, record)
        return total
