"""Test cases for the __contact_dataset__ module."""

from pyilcd.common import ClassificationInformation, GlobalReference
from pyilcd.contact_dataset import ContactDataSet, DataEntryBy


def test_contact_information(contact_dataset: ContactDataSet) -> None:
    """It parses attributes correctly."""
    unitGroupInformation = contact_dataset.contactInformation
    dataSetInformation = unitGroupInformation.dataSetInformation

    assert isinstance(
        dataSetInformation.classificationInformation, ClassificationInformation
    )
    assert isinstance(dataSetInformation.referenceToContact[0], GlobalReference)
    assert isinstance(dataSetInformation.referenceToLogo, GlobalReference)
    assert dataSetInformation.UUID == "00000000-0000-0000-0000-000000000000"


def test_administrative_information(contact_dataset: ContactDataSet) -> None:
    """It parses attributes correctly."""
    administrativeInformation = contact_dataset.administrativeInformation

    assert isinstance(administrativeInformation.dataEntryBy, DataEntryBy)
    assert isinstance(
        administrativeInformation.publicationAndOwnership.referenceToOwnershipOfDataSet,
        GlobalReference,
    )
