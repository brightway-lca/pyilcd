"""Test cases for the __core__ module."""
import os
import tempfile
from io import StringIO

import pytest

from pyilcd.core import (
    ProcessDatasetLookup,
    parse_file_process_dataset,
    save_ilcd_file,
    validate_file_process_dataset,
)


def test_parse_file_process_dataset_key_error() -> None:
    """It validates file successfully."""
    with pytest.raises(KeyError):
        ProcessDatasetLookup().lookup("", "", "", "undefined")


def test_validate_file_process_dataset_success() -> None:
    """It validates file successfully."""
    assert validate_file_process_dataset("data/sample_process.xml") is None


def test_validate_file_process_dataset_fail() -> None:
    """It validates file successfully."""
    xml = StringIO("<ilcd></ilcd>")
    errorExpected = (
        "<string>:1:0:ERROR:SCHEMASV:SCHEMAV_CVC_ELT_1: Element 'ilcd': "
        "No matching global declaration available for the validation root."
    )
    errorActual = validate_file_process_dataset(xml)
    assert errorActual is not None
    assert str(errorActual[0]) == errorExpected


def test_save_ilcd_file() -> None:
    """It saves read file correctly."""
    inputPath = "data/sample_process.xml"
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
    inputPath = "data/sample_process.xml"
    expectedOutputPath = "data/sample_process.xml"
    processDataset = parse_file_process_dataset(inputPath)
    outputPath = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
    save_ilcd_file(processDataset, outputPath, fill_defaults=True)

    with open(expectedOutputPath, encoding="utf-8") as inputFile:
        with open(outputPath, encoding="utf-8") as outputFile:
            mapping = {ord(c): "" for c in [" ", "\t", "\n"]}
            translatedOutput = outputFile.read().translate(mapping)
            translatedInput = inputFile.read().translate(mapping)
            assert translatedOutput == translatedInput
