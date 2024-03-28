"""Defaults configuration."""

import configparser
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, ClassVar, Dict

from lxml import etree


@dataclass
class Defaults:
    """Stores default values for ILCD attributes used when no value exists."""

    SCHEMA_DIR: ClassVar[str] = os.path.join(Path(__file__).parent.resolve(), "schemas")
    SCHEMA_PROCESS_DATASET: ClassVar[str] = os.path.join(
        SCHEMA_DIR, "ILCD_ProcessDataSet.xsd"
    )
    SCHEMA_FLOW_DATASET: ClassVar[str] = os.path.join(
        SCHEMA_DIR, "ILCD_FlowDataSet.xsd"
    )
    SCHEMA_FLOW_PROPERTY_DATASET: ClassVar[str] = os.path.join(
        SCHEMA_DIR, "ILCD_FlowPropertyDataSet.xsd"
    )
    SCHEMA_UNIT_GROUP_DATASET: ClassVar[str] = os.path.join(
        SCHEMA_DIR, "ILCD_UnitGroupDataSet.xsd"
    )
    SCHEMA_CONTACT_DATASET: ClassVar[str] = os.path.join(
        SCHEMA_DIR, "ILCD_ContactDataSet.xsd"
    )
    SCHEMA_SOURCE_DATASET: ClassVar[str] = os.path.join(
        SCHEMA_DIR, "ILCD_SourceDataSet.xsd"
    )

    DYNAMIC_DEFAULTS: ClassVar[
        Dict[str, Dict[str, Callable[[etree.ElementBase], str]]]
    ] = {}
    STATIC_DEFAULTS: ClassVar[Dict[str, Dict[str, str]]] = {
        "Classification": {
            "name": "ILCD",
        },
        "FlowCategorization": {
            "name": "ILCD",
        },
        "ProcessDataset": {
            "metaDataOnly": "false",
        },
    }

    @classmethod
    def config_defaults(cls, config_file: str) -> None:
        """Fully/ partially overrides defaults.
        Parameters:
        config_file: path for config file.
        """
        config = configparser.ConfigParser()
        config.optionxform = lambda optionstr: optionstr
        config.read(config_file)

        if config.has_section("parameters"):
            for key, value in dict(config["parameters"]).items():
                setattr(cls, key, value)

        staticDefaults = {
            name: dict(section)
            for name, section in config.items()
            if name not in ["parameters"]
        }
        cls.static_defaults = staticDefaults
