"""Fixtures for pyilcd"""
import pytest

from pyilcd.contact_dataset import ContactDataSet
from pyilcd.core import (
    parse_file_contact_dataset,
    parse_file_flow_dataset,
    parse_file_flow_property_dataset,
    parse_file_process_dataset,
    parse_file_source_dataset,
    parse_file_unit_group_dataset,
)
from pyilcd.flow_dataset import FlowDataSet
from pyilcd.flow_property_dataset import FlowPropertyDataSet
from pyilcd.process_dataset import ProcessDataSet
from pyilcd.source_dataset import SourceDataSet
from pyilcd.unit_group_dataset import UnitGroupDataSet


@pytest.fixture(name="process_dataset")
def _process_dataset() -> ProcessDataSet:
    return parse_file_process_dataset("data/process/sample_process.xml")


@pytest.fixture(name="flow_dataset")
def _flow_dataset() -> FlowDataSet:
    return parse_file_flow_dataset("data/flow/sample_flow.xml")


@pytest.fixture(name="flow_property_dataset")
def _flow_property_dataset() -> FlowPropertyDataSet:
    return parse_file_flow_property_dataset(
        "data/flow_property/sample_flow_property.xml"
    )


@pytest.fixture(name="unit_group_dataset")
def _unit_group_dataset() -> UnitGroupDataSet:
    return parse_file_unit_group_dataset("data/unit_group/sample_unit_group.xml")


@pytest.fixture(name="contact_dataset")
def _contact_dataset() -> ContactDataSet:
    return parse_file_contact_dataset("data/contact/sample_contact.xml")


@pytest.fixture(name="source_dataset")
def _source_dataset() -> SourceDataSet:
    return parse_file_source_dataset("data/source/sample_source.xml")
