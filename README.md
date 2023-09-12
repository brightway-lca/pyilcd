# pyilcd

[![PyPI](https://img.shields.io/pypi/v/pyilcd.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/pyilcd.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/pyilcd)][pypi status]
[![License](https://img.shields.io/pypi/l/pyilcd)][license]

[![Read the documentation at https://pyilcd.readthedocs.io/](https://img.shields.io/readthedocs/pyilcd/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/sami-m-g/pyilcd/actions/workflows/python-test.yml/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/sami-m-g/pyilcd/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/pyilcd/
[read the docs]: https://pyilcd.readthedocs.io/
[tests]: https://github.com/sami-m-g/pyilcd/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/sami-m-g/pyilcd
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Installation

You can install _pyilcd_ via [pip] from [PyPI]:

```console
$ pip install pyilcd
```

## Usage

```python
from pyilcd import parse_file_contact_dataset, validate_file_contact_dataset, save_ilcd_file, Defaults

# Override defaults if needed, else skip. Defaults are already set.
Defaults.config_defaults("config.ini")  # Replace with your own config file

# Validate the ContactDataset class against the ContactDataset schema.
validate_file_contact_dataset("data/invalid/sample_contact_invalid.xml")  # Replace with your own XML file
>> data/contact/sample_contact_invalid.xml:17:0:ERROR:SCHEMASV:SCHEMAV_CVC_DATATYPE_VALID_1_2_1: Element '{http://lca.jrc.it/ILCD/Common}class', attribute 'level': 'a' is not a valid value of the atomic type '{http://lca.jrc.it/ILCD/Common}LevelType'. data/contact/sample_contact_invalid.xml:17:0:ERROR:SCHEMASV:SCHEMAV_CVC_IDC: Element '{http://lca.jrc.it/ILCD/Common}class', attribute 'level': Warning: No precomputed value available, the value was either invalid or something strange happened.

# Parse the required XML file to ContactDataset class.
contactDataset = parse_file_contact_dataset("data/contact/sample_contact.xml")  # Replace with your own XML file
contactDataset
>> <Element {http://lca.jrc.it/ILCD/Contact}contactDataSet at 0x1c85f20c780>

## Change whatever attributes you need changing.
dataSetInformation = contactDataset.contactInformation.dataSetInformation
dataSetInformation.UUID
>> 00000000-0000-0000-0000-000000000000
dataSetInformation.UUID = "10000000-0000-0000-0000-000000000000"
dataSetInformation.UUID
>> 10000000-0000-0000-0000-000000000000

## Save final ContactDataset class as an XML file, make sure root directory exists.
save_ilcd_file(contactDataset, "out/sample_contact_new.xml")  # Replace with your own path
```

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide][Contributor Guide].

## License

Distributed under the terms of the [GPL 3.0 license][License],
_pyilcd_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue][Issue Tracker] along with a detailed description.


<!-- github-only -->

[command-line reference]: https://pyilcd.readthedocs.io/en/latest/usage.html
[License]: https://github.com/sami-m-g/pyilcd/blob/main/LICENSE
[Contributor Guide]: https://github.com/sami-m-g/pyilcd/blob/main/CONTRIBUTING.md
[Issue Tracker]: https://github.com/sami-m-g/pyilcd/issues
