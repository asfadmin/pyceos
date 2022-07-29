# PyCeos
A Python library and tool for reading Committee on Earth Observation Satellites
(CEOS) files.

## Installation
The project can be installed directly from the git repo. The CLI can be easily
installed with [pipx](https://pypi.org/project/pipx/).
```
pip install git+ssh://git@github.com:asfadmin/pyceos
```

When installing the CLI, the `jmespath` extra can be specified to enable
advanced output filtering.
```
pipx install "git+ssh://git@github.com:asfadmin/pyceos[jmespath]"
```

## Library
The library uses [construct](https://pypi.org/project/construct/) to handle
parsing boilerplate. Containers returned by construct parsing functions are
subclasses of builtin `dict` which also support getting keys through attribute
access.

Example:
```python
from pyceos import Ceos

obj = Ceos.parse_file("CEOS_FILE")

for record in obj.records:
    if record.header.type == "data_set_summary":
        print(record.body.mission_id, record.body.lev_code, "product")
```

## Command Line Interface
The CLI can be used to aid in development by providing a way to view and
manipulate CEOS files.

To print out all records to stdout (only JSON format is currently
implemented):
```
pyceos dump --json CEOS_FILE
```

To extract the first record to a separate file (non-JMESPath only, see below):
```
pyceos slice CEOS_FILE new_file.dat 1
```

### JMESPath filtering
The following command forms require `jmespath` to be installed (see
[Installation](#installation)). Note that the `jmespath` syntax uses a number
of special characters that also have meaning in a lot of common shells, so you
will need to take care to properly escape the filter argument.

To print only record headers:
```
pyceos dump --json CEOS_FILE "records[*].header"
```

To print only the facility related data record with sequence number 5:
```
pyceos dump --json CEOS_FILE $'records[?header.type == \'facility_related\' && body.sequence_number == `5`]'
```

To extract the first record to a separate file:
```
pyceos slice CEOS_FILE new_file.dat "records[0]"
```
