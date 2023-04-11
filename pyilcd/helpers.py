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


def create_element_text_process_dataset(name: str, element_type: type) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Process Dataset element text"""
    return create_element_text(name, element_type, Defaults.SCHEMA_PROCESS_DATASET)


def create_attribute_list_process_dataset(name: str, attr_type: type) -> property:
    """Helper wrapper method for creating setters and getters for an ilcd
    Process Dataset element text list"""
    return create_attribute_list(name, attr_type, Defaults.SCHEMA_PROCESS_DATASET)
