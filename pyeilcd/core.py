"""Core eILCD module containing valiate functionalities."""

from io import StringIO
from pathlib import Path
from typing import List, Union

from lxmlh import (
    validate_file,
)

from .config import Defaults


def validate_file_process_dataset(
    file: Union[str, Path, StringIO]
) -> Union[None, List[str]]:
    """Validates an ILCD Process Dataset XML file against schema.
    Parameters:
    file: the str|Path path to the ILCD Process Dataset XML file or its StringIO
    representation.
    Returns ``None`` if valid or a list of error strings.
    """
    return validate_file(file, Defaults.SCHEMA_PROCESS_DATASET)


def validate_file_flow_dataset(
    file: Union[str, Path, StringIO]
) -> Union[None, List[str]]:
    """Validates an ILCD Flow Dataset XML file against schema.
    Parameters:
    file: the str|Path path to the ILCD Flow Dataset XML file or its StringIO
    representation.
    Returns ``None`` if valid or a list of error strings.
    """
    return validate_file(file, Defaults.SCHEMA_FLOW_DATASET)


def validate_file_flow_property_dataset(
    file: Union[str, Path, StringIO]
) -> Union[None, List[str]]:
    """Validates an ILCD Flow Property Dataset XML file against schema.
    Parameters:
    file: the str|Path path to the ILCD Flow Property Dataset XML file or its StringIO
    representation.
    Returns ``None`` if valid or a list of error strings.
    """
    return validate_file(file, Defaults.SCHEMA_FLOW_PROPERTY_DATASET)


def validate_file_unit_group_dataset(
    file: Union[str, Path, StringIO]
) -> Union[None, List[str]]:
    """Validates an ILCD Unit Group Dataset XML file against schema.
    Parameters:
    file: the str|Path path to the ILCD Unit Group Dataset XML file or its StringIO
    representation.
    Returns ``None`` if valid or a list of error strings.
    """
    return validate_file(file, Defaults.SCHEMA_UNIT_GROUP_DATASET)


def validate_file_contact_dataset(
    file: Union[str, Path, StringIO]
) -> Union[None, List[str]]:
    """Validates an ILCD Contact Dataset XML file against schema.
    Parameters:
    file: the str|Path path to the ILCD Contact Dataset XML file or its StringIO
    representation.
    Returns ``None`` if valid or a list of error strings.
    """
    return validate_file(file, Defaults.SCHEMA_CONTACT_DATASET)


def validate_file_source_dataset(
    file: Union[str, Path, StringIO]
) -> Union[None, List[str]]:
    """Validates an ILCD Source Dataset XML file against schema.
    Parameters:
    file: the str|Path path to the ILCD Source Dataset XML file or its StringIO
    representation.
    Returns ``None`` if valid or a list of error strings.
    """
    return validate_file(file, Defaults.SCHEMA_SOURCE_DATASET)


def validate_file_model_dataset(
    file: Union[str, Path, StringIO]
) -> Union[None, List[str]]:
    """Validates an ILCD Model Dataset XML file against schema.
    Parameters:
    file: the str|Path path to the ILCD Source Dataset XML file or its StringIO
    representation.
    Returns ``None`` if valid or a list of error strings.
    """
    return validate_file(file, Defaults.SCHEMA_MODEL_DATASET)
