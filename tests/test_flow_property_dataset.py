"""Test cases for the __flow_property_dataset__ module."""

from pyilcd.common import ClassificationInformation, GlobalReference
from pyilcd.flow_property_dataset import (
    ComplianceDeclarations,
    DataEntryBy,
    FlowPropertyDataSet,
)


def test_flow_properties_information(
    flow_property_dataset: FlowPropertyDataSet,
) -> None:
    """It parses attributes correctly."""
    flowPropertiesInformation = flow_property_dataset.flowPropertiesInformation
    dataSetInformation = flowPropertiesInformation.dataSetInformation
    quantitativeReference = flowPropertiesInformation.quantitativeReference

    assert isinstance(
        dataSetInformation.classificationInformation, ClassificationInformation
    )
    assert isinstance(
        quantitativeReference.referenceToReferenceUnitGroup, GlobalReference
    )


def test_modelling_and_validation(flow_property_dataset: FlowPropertyDataSet) -> None:
    """It parses attributes correctly."""
    modellingAndValidation = flow_property_dataset.modellingAndValidation
    dataSourcesTreatmentAndRepresentativeness = (
        modellingAndValidation.dataSourcesTreatmentAndRepresentativeness
    )

    assert isinstance(
        modellingAndValidation.complianceDeclarations, ComplianceDeclarations
    )
    assert isinstance(
        dataSourcesTreatmentAndRepresentativeness.referenceToDataSources[0],
        GlobalReference,
    )


def test_administrative_information(flow_property_dataset: FlowPropertyDataSet) -> None:
    """It parses attributes correctly."""
    administrativeInformation = flow_property_dataset.administrativeInformation
    dataEntryBy = administrativeInformation.dataEntryBy
    publicationAndOwnership = administrativeInformation.publicationAndOwnership

    assert isinstance(dataEntryBy, DataEntryBy)
    assert isinstance(
        publicationAndOwnership.referenceToOwnershipOfDataSet, GlobalReference
    )
