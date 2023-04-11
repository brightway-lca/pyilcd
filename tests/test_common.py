"""Test cases for the __common__ module."""
from pyilcd.common import Class, DataQualityIndicator, GlobalReference, Method
from pyilcd.process_dataset import ProcessDataSet


def test_process_information(process_dataset: ProcessDataSet) -> None:
    """It parses attributes correctly."""
    dataSetInformation = process_dataset.processInformation.dataSetInformation
    classificationInformation = dataSetInformation.classificationInformation

    assert isinstance(
        classificationInformation.classifications[0].classesList[0], Class
    )


def test_modelling_and_validation(process_dataset: ProcessDataSet) -> None:
    """It parses attributes correctly."""
    modellingAndValidation = process_dataset.modellingAndValidation
    review = modellingAndValidation.validation.reviews[0]
    compliance = modellingAndValidation.complianceDeclarations.compliances[0]

    assert isinstance(review.scope.method[0], Method)
    assert isinstance(
        review.dataQualityIndicators.dataQualityIndicators[0], DataQualityIndicator
    )
    assert isinstance(review.referenceToCompleteReviewReport, GlobalReference)
    assert isinstance(review.referenceToNameOfReviewerAndInstitution, GlobalReference)
    assert isinstance(compliance.referenceToComplianceSystem, GlobalReference)


def test_administrative_information(process_dataset: ProcessDataSet) -> None:
    """It parses attributes correctly."""
    administrativeInformation = process_dataset.administrativeInformation
    commissionerAndGoal = administrativeInformation.commissionerAndGoal
    dataEntryBy = administrativeInformation.dataEntryBy
    publicationAndOwnership = administrativeInformation.publicationAndOwnership

    assert isinstance(commissionerAndGoal.referenceToCommissioner[0], GlobalReference)
    assert isinstance(dataEntryBy.referenceToDataSetFormat[0], GlobalReference)
    assert isinstance(
        dataEntryBy.referenceToPersonOrEntityEnteringTheData, GlobalReference
    )
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
