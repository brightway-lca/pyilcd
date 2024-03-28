"""Test cases for the __process_dataset__ module."""

from pyilcd.common import ClassificationInformation, GlobalReference
from pyilcd.process_dataset import (
    Allocation,
    CommissionerAndGoal,
    CompletenessElementaryFlows,
    Compliance,
    LocationOfOperationSupplyOrProduction,
    Name,
    ProcessDataSet,
    QuantitativeReference,
    Review,
    SubLocationOfOperationSupplyOrProduction,
    Time,
    VariableParameter,
)


def test_process_information(process_dataset: ProcessDataSet) -> None:
    """It parses attributes correctly."""
    processInformation = process_dataset.processInformation
    geography = processInformation.geography
    technology = processInformation.technology

    assert isinstance(
        processInformation.quantitativeReference,
        QuantitativeReference,
    )
    assert isinstance(processInformation.time, Time)
    assert isinstance(
        geography.locationOfOperationSupplyOrProduction,
        LocationOfOperationSupplyOrProduction,
    )
    assert isinstance(
        geography.subLocationOfOperationSupplyOrProduction[0],
        SubLocationOfOperationSupplyOrProduction,
    )
    assert isinstance(technology.referenceToIncludedProcesses[0], GlobalReference)
    assert isinstance(technology.referenceToTechnologyPictogramme, GlobalReference)
    assert isinstance(
        technology.referenceToTechnologyFlowDiagrammOrPicture[0], GlobalReference
    )
    assert isinstance(
        processInformation.mathematicalRelations.variableParameter[0], VariableParameter
    )


def test_modelling_and_validation(process_dataset: ProcessDataSet) -> None:
    """It parses attributes correctly."""
    modellingAndValidation = process_dataset.modellingAndValidation
    dataSourcesTreatmentAndRepresentativeness = (
        modellingAndValidation.dataSourcesTreatmentAndRepresentativeness
    )
    lciMethodAndAllocation = modellingAndValidation.lciMethodAndAllocation

    assert isinstance(
        lciMethodAndAllocation.referenceToLCAMethodDetails[0], GlobalReference
    )
    assert isinstance(
        dataSourcesTreatmentAndRepresentativeness.referenceToDataHandlingPrinciples[0],
        GlobalReference,
    )
    assert isinstance(
        dataSourcesTreatmentAndRepresentativeness.referenceToDataSource[0],
        GlobalReference,
    )
    assert isinstance(
        modellingAndValidation.completeness.completenessElementaryFlows[0],
        CompletenessElementaryFlows,
    )
    assert isinstance(
        modellingAndValidation.completeness.referenceToSupportedImpactAssessmentMethods,
        GlobalReference,
    )
    assert isinstance(modellingAndValidation.validation.reviews[0], Review)
    assert isinstance(
        modellingAndValidation.complianceDeclarations.compliances[0], Compliance
    )


def test_administrative_information(process_dataset: ProcessDataSet) -> None:
    """It parses attributes correctly."""
    administrativeInformation = process_dataset.administrativeInformation
    publicationAndOwnership = administrativeInformation.publicationAndOwnership
    dataEntryBy = administrativeInformation.dataEntryBy
    dataGenerator = administrativeInformation.dataGenerator

    assert isinstance(
        administrativeInformation.commissionerAndGoal, CommissionerAndGoal
    )
    assert isinstance(
        publicationAndOwnership.referenceToRegistrationAuthority, GlobalReference
    )
    assert isinstance(
        publicationAndOwnership.referenceToOwnershipOfDataSet,
        GlobalReference,
    )
    assert isinstance(
        dataEntryBy.referenceToConvertedOriginalDataSetFrom, GlobalReference
    )
    assert isinstance(dataEntryBy.referenceToDataSetUseApproval[0], GlobalReference)
    assert isinstance(
        dataGenerator.referenceToPersonOrEntityGeneratingTheDataSet[0], GlobalReference
    )


def test_lcia_result(process_dataset: ProcessDataSet) -> None:
    """It parses attributes correctly."""
    lciaResult = process_dataset.lciaResults.lciaResults[0]

    assert isinstance(lciaResult.referenceToLCIAMethodDataSets, GlobalReference)


def test_dataset_information(process_dataset: ProcessDataSet) -> None:
    """It parses attributes correctly."""
    datasetInformation = process_dataset.processInformation.dataSetInformation

    assert isinstance(datasetInformation.name, Name)
    assert isinstance(
        datasetInformation.complementingProcesses.referenceToComplementingProcesses[0],
        GlobalReference,
    )
    assert isinstance(
        datasetInformation.classificationInformation,
        ClassificationInformation,
    )
    assert isinstance(
        datasetInformation.referenceToExternalDocumentation,
        GlobalReference,
    )


def test_exchange(process_dataset: ProcessDataSet) -> None:
    """It parses attributes correctly."""
    exchange = process_dataset.exchanges.exchanges[0]

    assert isinstance(exchange.allocations.allocations[0], Allocation)
    assert isinstance(
        exchange.referencesToDataSource.referenceToDataSources[0], GlobalReference
    )
    assert isinstance(exchange.referenceToFlowDataSet, GlobalReference)
