"""Test cases for the __unit_group_dataset__ module."""

from pyilcd.common import ClassificationInformation, GlobalReference
from pyilcd.unit_group_dataset import (
    DataEntryBy,
    QuantitativeReference,
    Unit,
    UnitGroupDataSet,
)


def test_unit_group_information(unit_group_dataset: UnitGroupDataSet) -> None:
    """It parses attributes correctly."""
    unitGroupInformation = unit_group_dataset.unitGroupInformation
    dataSetInformation = unitGroupInformation.dataSetInformation
    quantitativeReference = unitGroupInformation.quantitativeReference

    assert isinstance(
        dataSetInformation.classificationInformation, ClassificationInformation
    )
    assert isinstance(quantitativeReference, QuantitativeReference)


def test_administrative_information(unit_group_dataset: UnitGroupDataSet) -> None:
    """It parses attributes correctly."""
    administrativeInformation = unit_group_dataset.administrativeInformation

    assert isinstance(administrativeInformation.dataEntryBy, DataEntryBy)
    assert isinstance(
        administrativeInformation.publicationAndOwnership.referenceToOwnershipOfDataSet,
        GlobalReference,
    )


def test_units(unit_group_dataset: UnitGroupDataSet) -> None:
    """It parses attributes correctly."""
    units = unit_group_dataset.units

    assert isinstance(units.units[0], Unit)
