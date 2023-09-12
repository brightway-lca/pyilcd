"""Test cases for the __core__ module."""
import os
import tempfile
from io import StringIO
from pathlib import Path
from typing import Callable, List, Tuple, Union

from lxml import etree

from pyilcd.core import (
    parse_directory_contact_dataset,
    parse_directory_flow_dataset,
    parse_directory_flow_property_dataset,
    parse_directory_process_dataset,
    parse_directory_source_dataset,
    parse_directory_unit_group_dataset,
    parse_file_process_dataset,
    save_ilcd_file,
    validate_file_contact_dataset,
    validate_file_flow_dataset,
    validate_file_flow_property_dataset,
    validate_file_process_dataset,
    validate_file_source_dataset,
    validate_file_unit_group_dataset,
)


def test_validate_file_process_dataset_success() -> None:
    """It validates file successfully."""
    assert validate_file_process_dataset("data/process/sample_process.xml") is None


def test_validate_file_flow_dataset_success() -> None:
    """It validates file successfully."""
    assert validate_file_flow_dataset("data/flow/sample_flow.xml") is None


def test_validate_file_flow_property_dataset_success() -> None:
    """It validates file successfully."""
    assert (
        validate_file_flow_property_dataset(
            "data/flow_property/sample_flow_property.xml"
        )
        is None
    )


def test_validate_file_unit_group_dataset_success() -> None:
    """It validates file successfully."""
    assert (
        validate_file_unit_group_dataset("data/unit_group/sample_unit_group.xml")
        is None
    )


def test_validate_file_contact_dataset_success() -> None:
    """It validates file successfully."""
    assert validate_file_contact_dataset("data/contact/sample_contact.xml") is None


def test_validate_file_source_dataset_success() -> None:
    """It validates file successfully."""
    assert validate_file_source_dataset("data/source/sample_source.xml") is None


def _validate_file_fail(
    validator: Callable[[Union[str, Path, StringIO]], Union[None, List[str]]]
) -> None:
    xml = StringIO("<ilcd></ilcd>")
    errorExpected = (
        "<string>:1:0:ERROR:SCHEMASV:SCHEMAV_CVC_ELT_1: Element 'ilcd': "
        "No matching global declaration available for the validation root."
    )
    errorActual = validator(xml)
    assert errorActual is not None
    assert str(errorActual[0]) == errorExpected


def test_validate_file_process_dataset_fail() -> None:
    """It validates file successfully."""
    _validate_file_fail(validate_file_process_dataset)


def test_validate_file_flow_dataset_fail() -> None:
    """It validates file successfully."""
    _validate_file_fail(validate_file_flow_dataset)


def test_validate_file_flow_property_dataset_fail() -> None:
    """It validates file successfully."""
    _validate_file_fail(validate_file_flow_property_dataset)


def test_validate_file_unit_group_dataset_fail() -> None:
    """It validates file successfully."""
    _validate_file_fail(validate_file_unit_group_dataset)


def test_validate_file_contact_dataset_fail() -> None:
    """It validates file successfully."""
    _validate_file_fail(validate_file_contact_dataset)


def test_validate_file_source_dataset_fail() -> None:
    """It validates file successfully."""
    _validate_file_fail(validate_file_source_dataset)


def test_save_ilcd_file() -> None:
    """It saves read file correctly."""
    inputPath = "data/process/sample_process.xml"
    processDataset = parse_file_process_dataset(inputPath)
    outputPath = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
    save_ilcd_file(processDataset, outputPath, fill_defaults=False)

    with open(inputPath, encoding="utf-8") as inputFile:
        with open(outputPath, encoding="utf-8") as outputFile:
            mapping = {ord(c): "" for c in [" ", "\t", "\n"]}
            translatedOutput = outputFile.read().translate(mapping)
            translatedInput = inputFile.read().translate(mapping)
            assert translatedOutput == translatedInput


def test_save_file_defaults() -> None:
    """It saves read file correctly."""
    inputPath = "data/process/sample_process.xml"
    expectedOutputPath = "data/process/sample_process.xml"
    processDataset = parse_file_process_dataset(inputPath)
    outputPath = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
    save_ilcd_file(processDataset, outputPath, fill_defaults=True)

    with open(expectedOutputPath, encoding="utf-8") as inputFile:
        with open(outputPath, encoding="utf-8") as outputFile:
            mapping = {ord(c): "" for c in [" ", "\t", "\n"]}
            translatedOutput = outputFile.read().translate(mapping)
            translatedInput = inputFile.read().translate(mapping)
            assert translatedOutput == translatedInput


def _parse_directory(
    dataset_name: str,
    parser: Callable[
        [Union[str, Path], Union[List[str], None]], List[Tuple[Path, etree.ElementBase]]
    ],
) -> None:
    """It reads all files successfully."""
    dirPath = os.path.join(Path(__file__).parent.parent.resolve(), "data", dataset_name)
    files = [os.path.join(dirPath, f"sample_{dataset_name}.xml")]
    result = parser(dirPath)

    assert len(result) == len(files)
    assert result[0][0] == Path(files[0])


def test_parse_directory_process_dataset() -> None:
    "It parses directory successfully."
    _parse_directory("process", parse_directory_process_dataset)


def test_parse_directory_flow_dataset() -> None:
    "It parses directory successfully."
    _parse_directory("flow", parse_directory_flow_dataset)


def test_parse_directory_flow_property_dataset() -> None:
    "It parses directory successfully."
    _parse_directory("flow_property", parse_directory_flow_property_dataset)


def test_parse_directory_unit_group_dataset() -> None:
    "It parses directory successfully."
    _parse_directory("unit_group", parse_directory_unit_group_dataset)


def test_parse_directory_contact_dataset() -> None:
    "It parses directory successfully."
    _parse_directory("contact", parse_directory_contact_dataset)


def test_parse_directory_source_dataset() -> None:
    "It parses directory successfully."
    _parse_directory("source", parse_directory_source_dataset)
