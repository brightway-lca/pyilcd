"""Internal helper classes."""

from typing import Callable, Optional

from lxmlh import create_attribute, create_attribute_list, create_element_text

from .config import Defaults


def create_attribute_process_dataset(
    name: str, attr_type: type, validator: Optional[Callable] = None
) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Process Dataset attribute"""
    return create_attribute(name, attr_type, Defaults.SCHEMA_PROCESS_DATASET, validator)


def create_attribute_flow_dataset(
    name: str, attr_type: type, validator: Optional[Callable] = None
) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Flow Dataset attribute"""
    return create_attribute(name, attr_type, Defaults.SCHEMA_FLOW_DATASET, validator)


def create_attribute_flow_property_dataset(
    name: str, attr_type: type, validator: Optional[Callable] = None
) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Flow Property Dataset attribute"""
    return create_attribute(
        name, attr_type, Defaults.SCHEMA_FLOW_PROPERTY_DATASET, validator
    )


def create_attribute_unit_group_dataset(
    name: str, attr_type: type, validator: Optional[Callable] = None
) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Unit Group Dataset attribute"""
    return create_attribute(
        name, attr_type, Defaults.SCHEMA_UNIT_GROUP_DATASET, validator
    )


def create_attribute_contact_dataset(
    name: str, attr_type: type, validator: Optional[Callable] = None
) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Contact Dataset attribute"""
    return create_attribute(name, attr_type, Defaults.SCHEMA_CONTACT_DATASET, validator)


def create_attribute_source_dataset(
    name: str, attr_type: type, validator: Optional[Callable] = None
) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Source Dataset attribute"""
    return create_attribute(name, attr_type, Defaults.SCHEMA_SOURCE_DATASET, validator)


def create_element_text_process_dataset(name: str, element_type: type) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Process Dataset element text"""
    return create_element_text(name, element_type, Defaults.SCHEMA_PROCESS_DATASET)


def create_element_text_flow_dataset(name: str, element_type: type) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Flow Dataset element text"""
    return create_element_text(name, element_type, Defaults.SCHEMA_FLOW_DATASET)


def create_element_text_unit_group_dataset(name: str, element_type: type) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Unit Group element text"""
    return create_element_text(name, element_type, Defaults.SCHEMA_UNIT_GROUP_DATASET)


def create_element_text_contact_dataset(name: str, element_type: type) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Contact element text"""
    return create_element_text(name, element_type, Defaults.SCHEMA_CONTACT_DATASET)


def create_attribute_list_process_dataset(name: str, attr_type: type) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Process Dataset element text list"""
    return create_attribute_list(name, attr_type, Defaults.SCHEMA_PROCESS_DATASET)


def create_attribute_list_flow_dataset(name: str, attr_type: type) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Flow Dataset element text list"""
    return create_attribute_list(name, attr_type, Defaults.SCHEMA_FLOW_DATASET)


def create_attribute_list_flow_property_dataset(name: str, attr_type: type) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Flow Property Dataset element text list"""
    return create_attribute_list(name, attr_type, Defaults.SCHEMA_FLOW_PROPERTY_DATASET)


def create_attribute_list_unit_group_dataset(name: str, attr_type: type) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Unit Group Dataset element text list"""
    return create_attribute_list(name, attr_type, Defaults.SCHEMA_UNIT_GROUP_DATASET)


def create_attribute_list_contact_dataset(name: str, attr_type: type) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Contact Dataset element text list"""
    return create_attribute_list(name, attr_type, Defaults.SCHEMA_CONTACT_DATASET)


def create_attribute_list_source_dataset(name: str, attr_type: type) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Source Dataset element text list"""
    return create_attribute_list(name, attr_type, Defaults.SCHEMA_SOURCE_DATASET)
