"""Fixtures for pyilcd"""
import pytest

from pyilcd.core import (
    parse_file_flow_dataset,
    parse_file_flow_property_dataset,
    parse_file_process_dataset,
)
from pyilcd.flow_dataset import FlowDataSet
from pyilcd.flow_property_dataset import FlowPropertyDataSet
from pyilcd.process_dataset import ProcessDataSet


@pytest.fixture(name="process_dataset")
def _process_dataset() -> ProcessDataSet:
    return parse_file_process_dataset("data/sample_process.xml")


@pytest.fixture(name="flow_dataset")
def _flow_dataset() -> FlowDataSet:
    return parse_file_flow_dataset("data/sample_flow.xml")


@pytest.fixture(name="flow_property_dataset")
def _flow_property_dataset() -> FlowPropertyDataSet:
    return parse_file_flow_property_dataset("data/sample_flowproperty.xml")
