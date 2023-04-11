"""Core ILCD module containing parsing and saving functionalities."""
from io import StringIO
from pathlib import Path
from typing import List, Tuple, Union

from lxml import etree
from lxmlh.parsers import parse_directory, parse_file, save_file, validate_file

from .common import (
    Class,
    Classification,
    ClassificationInformation,
    CommissionerAndGoal,
    DataQualityIndicator,
    DataQualityIndicators,
    GlobalReference,
    Method,
    Scope,
)
from .config import Defaults
from .process_dataset import (
    AdministrativeInformation,
    Allocation,
    Allocations,
    ComplementingProcesses,
    Completeness,
    CompletenessElementaryFlows,
    Compliance,
    ComplianceDeclarations,
    DataEntryBy,
    DataGenerator,
    DataSetInformation,
    DataSourcesTreatmentAndRepresentativeness,
    Exchange,
    Exchanges,
    Geography,
    LCIAResult,
    LCIAResults,
    LCIMethodAndAllocation,
    LocationOfOperationSupplyOrProduction,
    MathematicalRelations,
    ModellingAndValidation,
    Name,
    ProcessDataSet,
    ProcessInformation,
    PublicationAndOwnership,
    QuantitativeReference,
    ReferencesToDataSource,
    Review,
    SubLocationOfOperationSupplyOrProduction,
    Technology,
    Time,
    Validation,
    VariableParameter,
)


class ProcessDatasetLookup(etree.CustomElementClassLookup):
    """Custom XML lookup class for ILCD ProcessDataset files."""

    def lookup(self, unused_node_type, unused_document, unused_namespace, name):
        """Maps ILCD ProcessDataset XML elements to custom ProcessDataset classes."""
        lookupMap = {
            "administrativeInformation": AdministrativeInformation,
            "allocation": Allocation,
            "allocations": Allocations,
            "dataEntryBy": DataEntryBy,
            "dataGenerator": DataGenerator,
            "dataSetInformation": DataSetInformation,
            "dataSourcesTreatmentAndRepresentativeness": (
                DataSourcesTreatmentAndRepresentativeness
            ),
            "class": Class,
            "classification": Classification,
            "classificationInformation": ClassificationInformation,
            "completeness": Completeness,
            "completenessElementaryFlows": CompletenessElementaryFlows,
            "complementingProcesses": ComplementingProcesses,
            "compliance": Compliance,
            "complianceDeclarations": ComplianceDeclarations,
            "commissionerAndGoal": CommissionerAndGoal,
            "dataQualityIndicator": DataQualityIndicator,
            "dataQualityIndicators": DataQualityIndicators,
            "method": Method,
            "scope": Scope,
            "exchange": Exchange,
            "exchanges": Exchanges,
            "geography": Geography,
            "LCIAResult": LCIAResult,
            "LCIAResults": LCIAResults,
            "LCIMethodAndAllocation": LCIMethodAndAllocation,
            "locationOfOperationSupplyOrProduction": (
                LocationOfOperationSupplyOrProduction
            ),
            "mathematicalRelations": MathematicalRelations,
            "modellingAndValidation": ModellingAndValidation,
            "name": Name,
            "processDataSet": ProcessDataSet,
            "processInformation": ProcessInformation,
            "publicationAndOwnership": PublicationAndOwnership,
            "quantitativeReference": QuantitativeReference,
            "referenceToCommissioner": GlobalReference,
            "referenceToComplementingProcess": GlobalReference,
            "referenceToCompleteReviewReport": GlobalReference,
            "referenceToComplianceSystem": GlobalReference,
            "referenceToConvertedOriginalDataSetFrom": GlobalReference,
            "referenceToDataHandlingPrinciples": GlobalReference,
            "referenceToDataSetFormat": GlobalReference,
            "referenceToDataSetUseApproval": GlobalReference,
            "referenceToDataSource": GlobalReference,
            "referenceToEntitiesWithExclusiveAccess": GlobalReference,
            "referenceToExternalDocumentation": GlobalReference,
            "referenceToFlowDataSet": GlobalReference,
            "referenceToIncludedProcesses": GlobalReference,
            "referenceToLCAMethodDetails": GlobalReference,
            "referenceToLCIAMethodDataSet": GlobalReference,
            "referenceToNameOfReviewerAndInstitution": GlobalReference,
            "referenceToOwnershipOfDataSet": GlobalReference,
            "referenceToPersonOrEntityEnteringTheData": GlobalReference,
            "referenceToPersonOrEntityGeneratingTheDataSet": GlobalReference,
            "referenceToPrecedingDataSetVersion": GlobalReference,
            "referenceToRegistrationAuthority": GlobalReference,
            "referenceToSupportedImpactAssessmentMethods": GlobalReference,
            "referenceToTechnologyFlowDiagrammOrPicture": GlobalReference,
            "referenceToTechnologyPictogramme": GlobalReference,
            "referenceToUnchangedRepublication": GlobalReference,
            "referencesToDataSource": ReferencesToDataSource,
            "review": Review,
            "subLocationOfOperationSupplyOrProduction": (
                SubLocationOfOperationSupplyOrProduction
            ),
            "technology": Technology,
            "time": Time,
            "validation": Validation,
            "variableParameter": VariableParameter,
        }
        try:
            return lookupMap[name]
        except KeyError as exc:
            raise KeyError("Element {name} can't be found in {__class__}.") from exc


def validate_file_process_dataset(
    file: Union[str, Path, StringIO]
) -> Union[None, List[str]]:
    """Validates an ILCD Process Dataset XML file against schema.
    Parameters:
    file: the str|Path path to the ILCD Process Dataset XML file or its StringIO
    representation.
    Returns ``None`` if valid or a list of error strings.
    """
    return validate_file(file, Defaults.SCHEMA_PROCESS_DATASET)


def parse_file_process_dataset(file: Union[str, Path, StringIO]) -> ProcessDataSet:
    """Parses an ILCD ProcessDataset XML file to custom ILCD classes.
    Parameters:
    file: the str|Path path to the ProcessDataset XML file or its StringIO
    representation.
    Returns a ProcessDataset class representing the root of the XML file.
    """
    return parse_file(file, Defaults.SCHEMA_PROCESS_DATASET, ProcessDatasetLookup())


def parse_directory_process_dataset(
    dir_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, ProcessDataSet]]:
    """Parses a directory of ILCD Process Dataset XML files to a list of
    custom ILCD classes.
    Parameters:
    dir_path: the directory path, should contain ILCD Process Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding ILCD classes
    representing the root of the XML file.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return parse_directory(
        dir_path=dir_path,
        schema_path=Defaults.SCHEMA_PROCESS_DATASET,
        lookup=ProcessDatasetLookup(),
        valid_suffixes=valid_suffixes,
    )


def save_ilcd_file(
    root: etree.ElementBase, path: str, fill_defaults: bool = False
) -> None:
    """Saves an ILCD class to an XML file.
    Parameters:
    root: the ILCD class representing the root of the XML file.
    path: the path to save the ILCD XML file.
    fill_defaults: whether to fill defaults values for attributes or not.
    """
    if not fill_defaults:
        staticDefaults = None
        dynamicDefaults = None
    else:
        staticDefaults = Defaults.STATIC_DEFAULTS
        dynamicDefaults = Defaults.DYNAMIC_DEFAULTS

    save_file(
        root, path, static_defaults=staticDefaults, dynamic_defaults=dynamicDefaults
    )
