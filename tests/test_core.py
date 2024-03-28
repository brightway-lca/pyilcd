"""Test cases for the __core__ module."""

import os
import tempfile
from io import StringIO
from pathlib import Path
from typing import Callable, List, Tuple, Union

from lxml import etree

from pyilcd import (
    ContactDataSet,
    FlowDataSet,
    FlowPropertyDataSet,
    ProcessDataSet,
    SourceDataSet,
    UnitGroupDataSet,
    parse_directory_contact_dataset,
    parse_directory_flow_dataset,
    parse_directory_flow_property_dataset,
    parse_directory_process_dataset,
    parse_directory_source_dataset,
    parse_directory_unit_group_dataset,
    parse_file_process_dataset,
    parse_zip_file_contact_dataset,
    parse_zip_file_flow_dataset,
    parse_zip_file_flow_property_dataset,
    parse_zip_file_process_dataset,
    parse_zip_file_source_dataset,
    parse_zip_file_unit_group_dataset,
    save_ilcd_file,
    validate_directory_contact_dataset,
    validate_directory_flow_dataset,
    validate_directory_flow_property_dataset,
    validate_directory_process_dataset,
    validate_directory_source_dataset,
    validate_directory_unit_group_dataset,
    validate_file_contact_dataset,
    validate_file_flow_dataset,
    validate_file_flow_property_dataset,
    validate_file_process_dataset,
    validate_file_source_dataset,
    validate_file_unit_group_dataset,
    validate_zip_file_contact_dataset,
    validate_zip_file_flow_dataset,
    validate_zip_file_flow_property_dataset,
    validate_zip_file_process_dataset,
    validate_zip_file_source_dataset,
    validate_zip_file_unit_group_dataset,
)

from . import (
    FILE_CONTACT_DATASET,
    FILE_FLOW_DATASET,
    FILE_FLOW_PROPERTY_DATASET,
    FILE_PROCESS_DATASET,
    FILE_SOURCE_DATASET,
    FILE_UNIT_GROUP_DATASET,
)


def test_validate_file_process_dataset_success() -> None:
    """It validates file successfully."""
    assert validate_file_process_dataset(FILE_PROCESS_DATASET) is None


def test_validate_file_flow_dataset_success() -> None:
    """It validates file successfully."""
    assert validate_file_flow_dataset(FILE_FLOW_DATASET) is None


def test_validate_file_flow_property_dataset_success() -> None:
    """It validates file successfully."""
    assert validate_file_flow_property_dataset(FILE_FLOW_PROPERTY_DATASET) is None


def test_validate_file_unit_group_dataset_success() -> None:
    """It validates file successfully."""
    assert validate_file_unit_group_dataset(FILE_UNIT_GROUP_DATASET) is None


def test_validate_file_contact_dataset_success() -> None:
    """It validates file successfully."""
    assert validate_file_contact_dataset(FILE_CONTACT_DATASET) is None


def test_validate_file_source_dataset_success() -> None:
    """It validates file successfully."""
    assert validate_file_source_dataset(FILE_SOURCE_DATASET) is None


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
    inputPath = FILE_PROCESS_DATASET
    expectedOutputPath = FILE_PROCESS_DATASET
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
    dirPath = os.path.join(Path(__file__).parents[1], "data", dataset_name)
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


def _validate_directory(
    dataset_name: str,
    validator: Callable[
        [Union[str, Path], Union[List[str], None]], List[Tuple[Path, etree.ElementBase]]
    ],
) -> None:
    """It reads all files successfully."""
    dirPath = os.path.join(Path(__file__).parents[1], "data", dataset_name)
    files = [os.path.join(dirPath, f"sample_{dataset_name}.xml")]
    result = validator(dirPath)

    assert len(result) == len(files)
    assert result[0][0] == Path(files[0])
    assert result[0][1] is None


def test_validate_directory_process_dataset() -> None:
    "It validates directory successfully."
    _validate_directory("process", validate_directory_process_dataset)


def test_validate_directory_flow_dataset() -> None:
    "It validates directory successfully."
    _validate_directory("flow", validate_directory_flow_dataset)


def test_validate_directory_flow_property_dataset() -> None:
    "It validates directory successfully."
    _validate_directory("flow_property", validate_directory_flow_property_dataset)


def test_validate_directory_unit_group_dataset() -> None:
    "It validates directory successfully."
    _validate_directory("unit_group", validate_directory_unit_group_dataset)


def test_validate_directory_contact_dataset() -> None:
    "It validates directory successfully."
    _validate_directory("contact", validate_directory_contact_dataset)


def test_validate_directory_source_dataset() -> None:
    "It validates directory successfully."
    _validate_directory("source", validate_directory_source_dataset)


def test_validate_zip_file_process_dataset(process_dataset_zip) -> None:
    """It validates zip file successfully."""
    assert validate_zip_file_process_dataset(process_dataset_zip)[0][1] is None


def test_validate_zip_file_flow_dataset(flow_dataset_zip) -> None:
    """It validates zip file successfully."""
    assert validate_zip_file_flow_dataset(flow_dataset_zip)[0][1] is None


def test_validate_zip_file_flow_property_dataset(flow_property_dataset_zip) -> None:
    """It validates zip file successfully."""
    assert (
        validate_zip_file_flow_property_dataset(flow_property_dataset_zip)[0][1] is None
    )


def test_validate_zip_file_unit_group_dataset(unit_group_dataset_zip) -> None:
    """It validates zip file successfully."""
    assert validate_zip_file_unit_group_dataset(unit_group_dataset_zip)[0][1] is None


def test_validate_zip_file_contact_dataset(contact_dataset_zip) -> None:
    """It validates zip file successfully."""
    assert validate_zip_file_contact_dataset(contact_dataset_zip)[0][1] is None


def test_validate_zip_file_source_dataset(source_dataset_zip) -> None:
    """It validates zip file successfully."""
    assert validate_zip_file_source_dataset(source_dataset_zip)[0][1] is None


def _parse_zip_file(
    file_path: str,
    parser: Callable[
        [Union[str, Path], Union[List[str], None]], List[Tuple[Path, etree.ElementBase]]
    ],
    root_class: etree.ElementBase,
) -> None:
    """It reads zip file successfully."""
    results = parser(file_path)

    assert len(results) == 1
    assert isinstance(results[0][1], root_class)


def test_parse_zip_file_process_dataset(process_dataset_zip) -> None:
    """It reads zip file successfully."""
    _parse_zip_file(process_dataset_zip, parse_zip_file_process_dataset, ProcessDataSet)


def test_parse_zip_file_flow_dataset(flow_dataset_zip) -> None:
    """It reads zip file successfully."""
    _parse_zip_file(flow_dataset_zip, parse_zip_file_flow_dataset, FlowDataSet)


def test_parse_zip_file_flow_property_dataset(flow_property_dataset_zip) -> None:
    """It reads zip file successfully."""
    _parse_zip_file(
        flow_property_dataset_zip,
        parse_zip_file_flow_property_dataset,
        FlowPropertyDataSet,
    )


def test_parse_zip_file_unit_group_dataset(unit_group_dataset_zip) -> None:
    """It reads zip file successfully."""
    _parse_zip_file(
        unit_group_dataset_zip, parse_zip_file_unit_group_dataset, UnitGroupDataSet
    )


def test_parse_zip_file_contact_dataset(contact_dataset_zip) -> None:
    """It reads zip file successfully."""
    _parse_zip_file(contact_dataset_zip, parse_zip_file_contact_dataset, ContactDataSet)


def test_parse_zip_file_source_dataset(source_dataset_zip) -> None:
    """It reads zip file successfully."""
    _parse_zip_file(source_dataset_zip, parse_zip_file_source_dataset, SourceDataSet)
