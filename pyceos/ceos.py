from types import TracebackType
from typing import Optional, Type

from pyceos import data_format as df


class CEOSFile:
    """
    TODO(reweeden): Docstring
    """

    def __init__(self, name: str, mode: str = "rb", *args, **kwargs):
        self.name = name
        self.f = open(self.name, mode, *args, **kwargs)

    # Iterator protocol
    def __iter__(self):
        return self

    def __next__(self):
        header = df.Header.read(self.f)
        print(header)
        data = self.f.read(header.size)
        print(df.ImageryOptionsRecord.unpack(data[:df.ImageryOptionsRecord._struct.size]))
        raise StopIteration()

    # Context manager protocol
    def __enter__(self):
        return self

    def __exit__(
        self,
        t: Optional[Type[BaseException]],
        value: Optional[BaseException],
        traceback: Optional[TracebackType]
    ):
        return self.f.__exit__(t, value, traceback)
