"""Test cases for the __contact_dataset__ module."""

from pyilcd.common import ClassificationInformation, GlobalReference
from pyilcd.source_dataset import DataEntryBy, ReferenceToDigitalFile, SourceDataSet


def test_contact_information(source_dataset: SourceDataSet) -> None:
    """It parses attributes correctly."""
    sourceInformation = source_dataset.sourceInformation
    dataSetInformation = sourceInformation.dataSetInformation

    assert isinstance(
        dataSetInformation.classificationInformation, ClassificationInformation
    )
    assert isinstance(
        dataSetInformation.referenceToDigitalFiles[0], ReferenceToDigitalFile
    )
    assert isinstance(dataSetInformation.referenceToContact[0], GlobalReference)
    assert isinstance(dataSetInformation.referenceToLogo, GlobalReference)


def test_administrative_information(source_dataset: SourceDataSet) -> None:
    """It parses attributes correctly."""
    administrativeInformation = source_dataset.administrativeInformation

    assert isinstance(administrativeInformation.dataEntryBy, DataEntryBy)
    assert isinstance(
        administrativeInformation.publicationAndOwnership.referenceToOwnershipOfDataSet,
        GlobalReference,
    )
