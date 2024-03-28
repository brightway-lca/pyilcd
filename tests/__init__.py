"""Test suite for the pyilcd package."""

from pathlib import Path

DIR_DATA = Path(__file__).parents[1] / "data"
DIR_CONTACT_DATASET = DIR_DATA / "contact"
DIR_FLOW_DATASET = DIR_DATA / "flow"
DIR_FLOW_PROPERTY_DATASET = DIR_DATA / "flow_property"
DIR_PROCESS_DATASET = DIR_DATA / "process"
DIR_SOURCE_DATASET = DIR_DATA / "source"
DIR_UNIT_GROUP_DATASET = DIR_DATA / "unit_group"

FILE_CONTACT_DATASET = DIR_CONTACT_DATASET / "sample_contact.xml"
FILE_FLOW_DATASET = DIR_FLOW_DATASET / "sample_flow.xml"
FILE_FLOW_PROPERTY_DATASET = DIR_FLOW_PROPERTY_DATASET / "sample_flow_property.xml"
FILE_PROCESS_DATASET = DIR_PROCESS_DATASET / "sample_process.xml"
FILE_SOURCE_DATASET = DIR_SOURCE_DATASET / "sample_source.xml"
FILE_UNIT_GROUP_DATASET = DIR_UNIT_GROUP_DATASET / "sample_unit_group.xml"
