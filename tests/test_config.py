"""Test cases for the __config__ module."""

import os
from pathlib import Path

from pyilcd.config import Defaults


def test_config_defaults() -> None:
    """It overrides defaults variables."""
    rootDir = Path(__file__).parent.parent.resolve()

    configFileDir = os.path.join(rootDir, "out", "tests")
    configFilePath = os.path.join(configFileDir, "config.ini")
    os.makedirs(configFileDir, exist_ok=True)

    schemaDir = os.path.join(rootDir, "pyilcd", "schemas")
    schemaProcessDataset = os.path.join(schemaDir, "ILCD_ProcessDataSet.xsd")
    classificationName = "ILCD"

    with open(configFilePath, "w", encoding="utf-8") as configFile:
        configFile.write("[parameters]\n")
        configFile.write(f"SCHEMA_PROCESS_DATASET={schemaProcessDataset}\n")
        configFile.write(f"[Classification]\nname={classificationName}\n")

    Defaults.config_defaults(configFilePath)

    assert Defaults.STATIC_DEFAULTS["Classification"]["name"] == classificationName

    Defaults.config_defaults("config.init")
