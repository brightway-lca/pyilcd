"""Fixtures for pyilcd"""
import pytest

from pyilcd.contact_dataset import ContactDataSet
from pyilcd.core import (
    parse_file_contact_dataset,
    parse_file_flow_dataset,
    parse_file_flow_property_dataset,
    parse_file_process_dataset,
    parse_file_unit_group_dataset,
)
from pyilcd.flow_dataset import FlowDataSet
from pyilcd.flow_property_dataset import FlowPropertyDataSet
from pyilcd.process_dataset import ProcessDataSet
from pyilcd.unit_group_dataset import UnitGroupDataSet


@pytest.fixture(name="process_dataset")
def _process_dataset() -> ProcessDataSet:
    return parse_file_process_dataset("data/sample_process.xml")


@pytest.fixture(name="flow_dataset")
def _flow_dataset() -> FlowDataSet:
    return parse_file_flow_dataset("data/sample_flow.xml")


@pytest.fixture(name="flow_property_dataset")
def _flow_property_dataset() -> FlowPropertyDataSet:
    return parse_file_flow_property_dataset("data/sample_flowproperty.xml")


@pytest.fixture(name="unit_group_dataset")
def _unit_group_dataset() -> UnitGroupDataSet:
    return parse_file_unit_group_dataset("data/sample_unitgroup.xml")


@pytest.fixture(name="contact_dataset")
def _contact_dataset() -> ContactDataSet:
    return parse_file_contact_dataset("data/sample_contact.xml")
