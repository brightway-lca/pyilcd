"""Test cases for the __common__ module."""

from pyilcd.common import (
    Category,
    Class,
    Classification,
    DataQualityIndicator,
    GlobalReference,
    Method,
)
from pyilcd.flow_dataset import FlowDataSet
from pyilcd.process_dataset import ProcessDataSet
from pyilcd.unit_group_dataset import UnitGroupDataSet


def test_classification_information(process_dataset: ProcessDataSet) -> None:
    """It parses attributes correctly."""
    dataSetInformation = process_dataset.processInformation.dataSetInformation
    classificationInformation = dataSetInformation.classificationInformation

    assert isinstance(
        classificationInformation.classifications[0].classesList[0], Class
    )


def test_review(process_dataset: ProcessDataSet) -> None:
    """It parses attributes correctly."""
    modellingAndValidation = process_dataset.modellingAndValidation
    review = modellingAndValidation.validation.reviews[0]

    assert isinstance(review.scope.method[0], Method)
    assert isinstance(
        review.dataQualityIndicators.dataQualityIndicators[0], DataQualityIndicator
    )
    assert isinstance(review.referenceToCompleteReviewReport, GlobalReference)
    assert isinstance(review.referenceToNameOfReviewerAndInstitution, GlobalReference)


def test_compliance(unit_group_dataset: UnitGroupDataSet) -> None:
    """It parses attributes correctly."""
    modellingAndValidation = unit_group_dataset.modellingAndValidation
    compliance = modellingAndValidation.complianceDeclarations.compliances[0]

    assert isinstance(compliance.referenceToComplianceSystem, GlobalReference)


def test_commissioner_and_goal(process_dataset: ProcessDataSet) -> None:
    """It parses attributes correctly."""
    administrativeInformation = process_dataset.administrativeInformation
    commissionerAndGoal = administrativeInformation.commissionerAndGoal

    assert isinstance(commissionerAndGoal.referenceToCommissioner[0], GlobalReference)


def test_data_entry_by(process_dataset: ProcessDataSet) -> None:
    """It parses attributes correctly."""
    administrativeInformation = process_dataset.administrativeInformation
    dataEntryBy = administrativeInformation.dataEntryBy

    assert isinstance(dataEntryBy.referenceToDataSetFormat[0], GlobalReference)
    assert isinstance(
        dataEntryBy.referenceToPersonOrEntityEnteringTheData, GlobalReference
    )


def test_publication_and_ownership(process_dataset: ProcessDataSet) -> None:
    """It parses attributes correctly."""
    administrativeInformation = process_dataset.administrativeInformation
    publicationAndOwnership = administrativeInformation.publicationAndOwnership

    assert isinstance(
        publicationAndOwnership.referenceToPrecedingDataSetVersion[0], GlobalReference
    )
    assert isinstance(
        publicationAndOwnership.referenceToUnchangedRepublication, GlobalReference
    )
    assert isinstance(
        publicationAndOwnership.referenceToEntitiesWithExclusiveAccess[0],
        GlobalReference,
    )


def test_flow_category_information(flow_dataset: FlowDataSet) -> None:
    """It parses attributes correctly."""
    dataSetInformation = flow_dataset.flowInformation.dataSetInformation
    flowCategoryInformation = dataSetInformation.classificationInformation

    assert isinstance(
        flowCategoryInformation.elementaryFlowCategorization[0].categoryList[0],
        Category,
    )
    assert isinstance(flowCategoryInformation.classifications[0], Classification)
