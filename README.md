# pyeilcd User Guide

[![PyPI](https://img.shields.io/pypi/v/pyeilcd.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/pyeilcd)][pypi status]

[pypi status]: https://pypi.org/project/pyeilcd/

[English](https://github.com/linancn/pyilcd/blob/main/README.md) | [中文](https://github.com/linancn/pyilcd/blob/main/README_CN.md)

**Note:** This package supports Python versions 3.8 to 3.12 only.

## 1. Introduction

pyeilcd is a Python package that provides a simple interface to validate extended-ILCD (eILCD) XML files against the ILCD schemas. It is built on top of the [pyilcd](https://github.com/brightway-lca/pyilcd) library.

---

## 2. pyeilcd Usage

### (1) Installation Instructions

You can install _pyeilcd_ via [pip] from [PyPI]:

```console
$ pip install pyeilcd
```
### (2) Functionalities

pyeilcd offers the following key functionalities:

- Performs schema validation on eILCD XML files.

- Supports multiple ILCD standard-compliant dataset types (e.g., ContactDataset, ProcessDataset, etc.).

- ​Leverages core validation capabilities from [pyilcd](https://github.com/brightway-lca/pyilcd).    

### (3) Usage Examples

```python
from pyeilcd import validate_file_contact_dataset, Defaults

# Override defaults if needed, else skip. Defaults are already set.
Defaults.config_defaults("config.ini")  # Replace with your own config file

# Validate the ContactDataset class against the ContactDataset schema.
validate_file_contact_dataset("data/invalid/sample_contact_invalid.xml")  # Replace with your own XML file
>> data/contact/sample_contact_invalid.xml:17:0:ERROR:SCHEMASV:SCHEMAV_CVC_DATATYPE_VALID_1_2_1: Element '{http://lca.jrc.it/ILCD/Common}class', attribute 'level': 'a' is not a valid value of the atomic type '{http://lca.jrc.it/ILCD/Common}LevelType'. data/contact/sample_contact_invalid.xml:17:0:ERROR:SCHEMASV:SCHEMAV_CVC_IDC: Element '{http://lca.jrc.it/ILCD/Common}class', attribute 'level': Warning: No precomputed value available, the value was either invalid or something strange happened.
```

## 3. Automatic Building and Publishing (CI/CD)

This project supports automatic building and publishing. When you push a git tag named with the v<version> format to the repository, it will trigger the workflow automatically. For example:

```bash
#list existing tags
git tag
#creat a new tag
git tag v7.0.12
#push this tag to origin
git push origin v7.0.12

```

## 4. License

Distributed under the terms of the GPL 3.0 license,
_pyeilcd_ is free and open source software.


[pip]: https://pip.pypa.io/en/stable/
[PyPI]: https://pypi.org/project/pyeilcd/
