"""Fixtures for pyilcd"""

import os
import zipfile

import pytest

from pyeilcd.contact_dataset import ContactDataSet
from pyeilcd.core import (
    parse_file_contact_dataset,
    parse_file_flow_dataset,
    parse_file_flow_property_dataset,
    parse_file_process_dataset,
    parse_file_source_dataset,
    parse_file_unit_group_dataset,
)
from pyeilcd.flow_dataset import FlowDataSet
from pyeilcd.flow_property_dataset import FlowPropertyDataSet
from pyeilcd.process_dataset import ProcessDataSet
from pyeilcd.source_dataset import SourceDataSet
from pyeilcd.unit_group_dataset import UnitGroupDataSet

from . import (
    DIR_CONTACT_DATASET,
    DIR_FLOW_DATASET,
    DIR_FLOW_PROPERTY_DATASET,
    DIR_PROCESS_DATASET,
    DIR_SOURCE_DATASET,
    DIR_UNIT_GROUP_DATASET,
    FILE_CONTACT_DATASET,
    FILE_FLOW_DATASET,
    FILE_FLOW_PROPERTY_DATASET,
    FILE_PROCESS_DATASET,
    FILE_SOURCE_DATASET,
    FILE_UNIT_GROUP_DATASET,
)


@pytest.fixture(name="process_dataset")
def _process_dataset() -> ProcessDataSet:
    return parse_file_process_dataset(FILE_PROCESS_DATASET)


@pytest.fixture(name="flow_dataset")
def _flow_dataset() -> FlowDataSet:
    return parse_file_flow_dataset(FILE_FLOW_DATASET)


@pytest.fixture(name="flow_property_dataset")
def _flow_property_dataset() -> FlowPropertyDataSet:
    return parse_file_flow_property_dataset(FILE_FLOW_PROPERTY_DATASET)


@pytest.fixture(name="unit_group_dataset")
def _unit_group_dataset() -> UnitGroupDataSet:
    return parse_file_unit_group_dataset(FILE_UNIT_GROUP_DATASET)


@pytest.fixture(name="contact_dataset")
def _contact_dataset() -> ContactDataSet:
    return parse_file_contact_dataset(FILE_CONTACT_DATASET)


@pytest.fixture(name="source_dataset")
def _source_dataset() -> SourceDataSet:
    return parse_file_source_dataset(FILE_SOURCE_DATASET)


def __zip_data(tmpdir, data_dir: str, file_name: str = "data.zip") -> str:
    zipFilePath = os.path.join(tmpdir, file_name)
    with zipfile.ZipFile(zipFilePath, "w", zipfile.ZIP_DEFLATED) as zipFile:
        for root, _, files in os.walk(data_dir):
            for file in files:
                zipFile.write(os.path.join(root, file), file)
    return zipFilePath


@pytest.fixture(name="process_dataset_zip")
def _process_dataset_zip(tmpdir) -> ProcessDataSet:
    return __zip_data(tmpdir, DIR_PROCESS_DATASET)


@pytest.fixture(name="flow_dataset_zip")
def _flow_dataset_zip(tmpdir) -> FlowDataSet:
    return __zip_data(tmpdir, DIR_FLOW_DATASET)


@pytest.fixture(name="flow_property_dataset_zip")
def _flow_property_dataset_zip(tmpdir) -> FlowPropertyDataSet:
    return __zip_data(tmpdir, DIR_FLOW_PROPERTY_DATASET)


@pytest.fixture(name="unit_group_dataset_zip")
def _unit_group_dataset_zip(tmpdir) -> UnitGroupDataSet:
    return __zip_data(tmpdir, DIR_UNIT_GROUP_DATASET)


@pytest.fixture(name="contact_dataset_zip")
def _contact_dataset_zip(tmpdir) -> ContactDataSet:
    return __zip_data(tmpdir, DIR_CONTACT_DATASET)


@pytest.fixture(name="source_dataset_zip")
def _source_dataset_zip(tmpdir) -> SourceDataSet:
    return __zip_data(tmpdir, DIR_SOURCE_DATASET)
