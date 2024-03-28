"""Test cases for the __flow_dataset__ module."""

from pyilcd.common import GlobalReference
from pyilcd.flow_dataset import (
    ComplianceDeclarations,
    DataEntryBy,
    FlowCategoryInformation,
    FlowDataSet,
    Geography,
    LCIMethod,
    Name,
    QuantitativeReference,
)


def test_flow_information(flow_dataset: FlowDataSet) -> None:
    """It parses attributes correctly."""
    flowInformation = flow_dataset.flowInformation
    datasetInformation = flowInformation.dataSetInformation
    quantitativeReference = flowInformation.quantitativeReference
    technology = flowInformation.technology
    geography = flowInformation.geography

    assert isinstance(datasetInformation.name, Name)
    assert isinstance(
        datasetInformation.classificationInformation, FlowCategoryInformation
    )
    assert isinstance(quantitativeReference, QuantitativeReference)
    assert isinstance(geography, Geography)
    assert isinstance(technology.referenceToTechnicalSpecification[0], GlobalReference)


def test_modelling_and_validation(flow_dataset: FlowDataSet) -> None:
    """It parses attributes correctly."""
    modellingAndValidation = flow_dataset.modellingAndValidation

    assert isinstance(modellingAndValidation.lciMethod, LCIMethod)
    assert isinstance(
        modellingAndValidation.complianceDeclarations, ComplianceDeclarations
    )


def test_administrative_information(flow_dataset: FlowDataSet) -> None:
    """It parses attributes correctly."""
    administrativeInformation = flow_dataset.administrativeInformation

    assert isinstance(administrativeInformation.dataEntryBy, DataEntryBy)
    assert isinstance(
        administrativeInformation.publicationAndOwnership.referenceToOwnershipOfDataSet,
        GlobalReference,
    )


def test_flow_properties(flow_dataset: FlowDataSet) -> None:
    """It parses attributes correctly."""
    flowProperty = flow_dataset.flowProperties.flowProperties[0]

    assert isinstance(flowProperty.referenceToFlowPropertyDataSet, GlobalReference)
