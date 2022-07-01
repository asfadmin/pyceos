import argparse
import json
import sys
from binascii import hexlify
from enum import Enum
from typing import Any

from pyceos.ceos import Ceos

try:
    import jmespath
except ImportError:
    jmespath = None


def to_json(obj: Any):
    """Transform the object into something that is json.dumps compatible"""

    if isinstance(obj, (bool, int, float, str)) or obj is None:
        return obj

    if isinstance(obj, bytes):
        if len(obj) < 100:
            try:
                return obj.decode()
            except UnicodeDecodeError:
                return "0x" + hexlify(obj).decode()
        else:
            return f"<bytes {len(obj)}>"

    if isinstance(obj, Enum):
        return obj.name

    if isinstance(obj, (list, tuple)):
        return [to_json(item) for item in obj]

    if isinstance(obj, dict):
        return {k: to_json(v) for k, v in obj.items()}

    return {
        k: to_json(v)
        for k, v in obj.__dict__.items()
        if not k.startswith("_")
    }


def serialize_json(obj: Any):
    encoder = json.JSONEncoder(indent=2)
    for chunk in encoder.iterencode(obj):
        sys.stdout.write(chunk)
    print()


def serialize_text(obj: Any):
    raise NotImplementedError("use --json")


SERIALIZERS = {
    "text": serialize_text,
    "json": serialize_json,
}


def add_parser(subparsers: argparse._SubParsersAction):
    parser: argparse.ArgumentParser = subparsers.add_parser("dump", help="Dump record contents to standard output")
    parser.set_defaults(func=dump)
    parser.add_argument("file", help="file to read")
    if jmespath:
        parser.add_argument(
            "filter",
            help="a JMESPath filter expression",
            nargs="?",
            type=jmespath.compile
        )

    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument(
        "--output",
        help="set the output type. defaults to human readable output (text)",
        choices=list(SERIALIZERS.keys())
    )
    output_group.add_argument(
        "--json",
        help="dump output as JSON data",
        action="store_const",
        dest="output",
        const="json"
    )

    return parser


def dump(args: argparse.Namespace):
    serializer = SERIALIZERS.get(args.output, serialize_text)

    with Ceos.from_file(args.file) as obj:
        json_obj = to_json(obj)

    if args.filter:
        json_obj = args.filter.search(json_obj)

    serializer(json_obj)
