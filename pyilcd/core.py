"""Core ILCD module containing parsing and saving functionalities."""

from io import StringIO
from pathlib import Path
from typing import Dict, List, Tuple, Union

from lxml import etree
from lxmlh import (
    parse_directory,
    parse_file,
    parse_zip_file,
    save_file,
    validate_directory,
    validate_file,
    validate_zip_file,
)

from .common import (
    Category,
    Class,
    Classification,
    ClassificationInformation,
    CommissionerAndGoal,
    Compliance,
    ComplianceDeclarations,
    DataQualityIndicator,
    DataQualityIndicators,
    FlowCategorization,
    FlowCategoryInformation,
    GlobalReference,
    Method,
    Scope,
)
from .config import Defaults
from .contact_dataset import (
    AdministrativeInformation as ContactAdministrativeInformation,
)
from .contact_dataset import ContactDataSet, ContactInformation
from .contact_dataset import DataEntryBy as ContactDataEntryBy
from .contact_dataset import DataSetInformation as ContactDataSetInformation
from .contact_dataset import PublicationAndOwnership as ContactPublicationAndOwnership
from .flow_dataset import AdministrativeInformation as FlowAdministrativeInformation
from .flow_dataset import DataEntryBy as FlowDataEntryBy
from .flow_dataset import DataSetInformation as FlowDataSetInformation
from .flow_dataset import FlowDataSet, FlowInformation, FlowProperties, FlowProperty
from .flow_dataset import Geography as FlowGeography
from .flow_dataset import LCIMethod
from .flow_dataset import ModellingAndValidation as FlowModellingAndValidation
from .flow_dataset import Name as FlowName
from .flow_dataset import PublicationAndOwnership as FlowPublicationAndOwnership
from .flow_dataset import QuantitativeReference as FlowQuantitativeReference
from .flow_dataset import Technology as FlowTechnology
from .flow_property_dataset import (
    AdministrativeInformation as FlowPropertyAdministrativeInformation,
)
from .flow_property_dataset import DataEntryBy as FlowPropertyDataEntryBy
from .flow_property_dataset import DataSetInformation as FlowPropertyDataSetInformation
from .flow_property_dataset import DataSourcesTreatmentAndRepresentativeness as FPDSTAR
from .flow_property_dataset import FlowPropertiesInformation, FlowPropertyDataSet
from .flow_property_dataset import (
    ModellingAndValidation as FlowPropertyModellingAndValidation,
)
from .flow_property_dataset import (
    PublicationAndOwnership as FlowPropertyPublicationAndOwnership,
)
from .flow_property_dataset import (
    QuantitativeReference as FlowPropertyQuantitativeReference,
)
from .process_dataset import (
    AdministrativeInformation as ProcessAdministrativeInformation,
)
from .process_dataset import (
    Allocation,
    Allocations,
    ComplementingProcesses,
    Completeness,
    CompletenessElementaryFlows,
)
from .process_dataset import Compliance as ProcessCompliance
from .process_dataset import ComplianceDeclarations as ProcessComplianceDeclarations
from .process_dataset import DataEntryBy as ProcessDataEntryBy
from .process_dataset import DataGenerator
from .process_dataset import DataSetInformation as ProcessDataSetInformation
from .process_dataset import DataSourcesTreatmentAndRepresentativeness as PDSTAR
from .process_dataset import Exchange, Exchanges
from .process_dataset import Geography as ProcessGeography
from .process_dataset import (
    LCIAResult,
    LCIAResults,
    LCIMethodAndAllocation,
    LocationOfOperationSupplyOrProduction,
    MathematicalRelations,
)
from .process_dataset import ModellingAndValidation as ProcessModellingAndValidation
from .process_dataset import Name as ProcessName
from .process_dataset import ProcessDataSet, ProcessInformation
from .process_dataset import PublicationAndOwnership as ProcessPublicationAndOwnership
from .process_dataset import QuantitativeReference as ProcessQuantitativeReference
from .process_dataset import (
    ReferencesToDataSource,
    Review,
    SubLocationOfOperationSupplyOrProduction,
)
from .process_dataset import Technology as ProcessTechnology
from .process_dataset import Time, Validation, VariableParameter
from .source_dataset import AdministrativeInformation as SourceAdministrativeInformation
from .source_dataset import DataEntryBy as SourceDataEntryBy
from .source_dataset import DataSetInformation as SourceDataSetInformation
from .source_dataset import PublicationAndOwnership as SourcePublicationAndOwnership
from .source_dataset import ReferenceToDigitalFile, SourceDataSet, SourceInformation
from .unit_group_dataset import (
    AdministrativeInformation as UnitGroupAdministrativeInformation,
)
from .unit_group_dataset import DataEntryBy as UnitGroupDataEntryBy
from .unit_group_dataset import DataSetInformation as UnitGroupDataSetInformation
from .unit_group_dataset import (
    ModellingAndValidation as UnitGroupModellingAndValidation,
)
from .unit_group_dataset import (
    PublicationAndOwnership as UnitGroupPublicationAndOwnership,
)
from .unit_group_dataset import QuantitativeReference as UnitGroupQuantitativeReference
from .unit_group_dataset import Unit, UnitGroupDataSet, UnitGroupInformation, Units

COMMON_LOOK_UP: Dict[str, type] = {
    "allocation": Allocation,
    "allocations": Allocations,
    "category": Category,
    "class": Class,
    "classification": Classification,
    "completeness": Completeness,
    "completenessElementaryFlows": CompletenessElementaryFlows,
    "complementingProcesses": ComplementingProcesses,
    "compliance": Compliance,
    "complianceDeclarations": ComplianceDeclarations,
    "commissionerAndGoal": CommissionerAndGoal,
    "contactDataSet": ContactDataSet,
    "contactInformation": ContactInformation,
    "dataGenerator": DataGenerator,
    "dataQualityIndicator": DataQualityIndicator,
    "dataQualityIndicators": DataQualityIndicators,
    "elementaryFlowCategorization": FlowCategorization,
    "flowDataSet": FlowDataSet,
    "flowInformation": FlowInformation,
    "flowProperties": FlowProperties,
    "flowPropertiesInformation": FlowPropertiesInformation,
    "flowProperty": FlowProperty,
    "flowPropertyDataSet": FlowPropertyDataSet,
    "method": Method,
    "scope": Scope,
    "exchange": Exchange,
    "exchanges": Exchanges,
    "LCIAResult": LCIAResult,
    "LCIAResults": LCIAResults,
    "LCIMethod": LCIMethod,
    "LCIMethodAndAllocation": LCIMethodAndAllocation,
    "locationOfOperationSupplyOrProduction": (LocationOfOperationSupplyOrProduction),
    "mathematicalRelations": MathematicalRelations,
    "processDataSet": ProcessDataSet,
    "processInformation": ProcessInformation,
    "referenceToContact": GlobalReference,
    "referenceToCommissioner": GlobalReference,
    "referenceToComplementingProcess": GlobalReference,
    "referenceToCompleteReviewReport": GlobalReference,
    "referenceToComplianceSystem": GlobalReference,
    "referenceToConvertedOriginalDataSetFrom": GlobalReference,
    "referenceToDataHandlingPrinciples": GlobalReference,
    "referenceToDataSetFormat": GlobalReference,
    "referenceToDataSetUseApproval": GlobalReference,
    "referenceToDataSource": GlobalReference,
    "referenceToDigitalFile": ReferenceToDigitalFile,
    "referenceToEntitiesWithExclusiveAccess": GlobalReference,
    "referenceToExternalDocumentation": GlobalReference,
    "referenceToFlowDataSet": GlobalReference,
    "referenceToFlowPropertyDataSet": GlobalReference,
    "referenceToIncludedProcesses": GlobalReference,
    "referenceToLCAMethodDetails": GlobalReference,
    "referenceToLCIAMethodDataSet": GlobalReference,
    "referenceToLogo": GlobalReference,
    "referenceToNameOfReviewerAndInstitution": GlobalReference,
    "referenceToOwnershipOfDataSet": GlobalReference,
    "referenceToPersonOrEntityEnteringTheData": GlobalReference,
    "referenceToPersonOrEntityGeneratingTheDataSet": GlobalReference,
    "referenceToPrecedingDataSetVersion": GlobalReference,
    "referenceToReferenceUnitGroup": GlobalReference,
    "referenceToRegistrationAuthority": GlobalReference,
    "referenceToSupportedImpactAssessmentMethods": GlobalReference,
    "referenceToTechnicalSpecification": GlobalReference,
    "referenceToTechnologyFlowDiagrammOrPicture": GlobalReference,
    "referenceToTechnologyPictogramme": GlobalReference,
    "referenceToUnchangedRepublication": GlobalReference,
    "referencesToDataSource": ReferencesToDataSource,
    "review": Review,
    "sourceDataSet": SourceDataSet,
    "sourceInformation": SourceInformation,
    "subLocationOfOperationSupplyOrProduction": (
        SubLocationOfOperationSupplyOrProduction
    ),
    "time": Time,
    "unit": Unit,
    "units": Units,
    "unitGroupDataSet": UnitGroupDataSet,
    "unitGroupInformation": UnitGroupInformation,
    "validation": Validation,
    "variableParameter": VariableParameter,
}


def _check_common_lookup(name: str) -> type:
    try:
        return COMMON_LOOK_UP[name]
    except KeyError:
        return None


class ProcessDatasetLookup(etree.CustomElementClassLookup):
    """Custom XML lookup class for ILCD ProcessDataset files."""

    def lookup(self, unused_node_type, unused_document, unused_namespace, name) -> type:
        """Maps ILCD ProcessDataset XML elements to custom ProcessDataset classes."""
        lookupMap: Dict[str, type] = {
            "administrativeInformation": ProcessAdministrativeInformation,
            "dataEntryBy": ProcessDataEntryBy,
            "dataSetInformation": ProcessDataSetInformation,
            "dataSourcesTreatmentAndRepresentativeness": PDSTAR,
            "classificationInformation": ClassificationInformation,
            "compliance": ProcessCompliance,
            "complianceDeclarations": ProcessComplianceDeclarations,
            "geography": ProcessGeography,
            "modellingAndValidation": ProcessModellingAndValidation,
            "name": ProcessName,
            "publicationAndOwnership": ProcessPublicationAndOwnership,
            "quantitativeReference": ProcessQuantitativeReference,
            "technology": ProcessTechnology,
        }
        try:
            return lookupMap[name]
        except KeyError:
            return _check_common_lookup(name)


class FlowDatasetLookup(etree.CustomElementClassLookup):
    """Custom XML lookup class for ILCD FlowDataset files."""

    def lookup(
        self, unused_node_type, unused_document, unused_namespace, name: str
    ) -> type:
        """Maps ILCD FlowDataset XML elements to custom FlowDataset classes."""
        lookupMap: Dict[str, type] = {
            "administrativeInformation": FlowAdministrativeInformation,
            "classificationInformation": FlowCategoryInformation,
            "dataEntryBy": FlowDataEntryBy,
            "dataSetInformation": FlowDataSetInformation,
            "geography": FlowGeography,
            "modellingAndValidation": FlowModellingAndValidation,
            "name": FlowName,
            "publicationAndOwnership": FlowPublicationAndOwnership,
            "quantitativeReference": FlowQuantitativeReference,
            "technology": FlowTechnology,
        }
        try:
            return lookupMap[name]
        except KeyError:
            return _check_common_lookup(name)


class FlowPropertyDatasetLookup(etree.CustomElementClassLookup):
    """Custom XML lookup class for ILCD FlowPropertyDataset files."""

    def lookup(
        self, unused_node_type, unused_document, unused_namespace, name: str
    ) -> type:
        """Maps ILCD FlowPropertyDataset XML elements to custom FlowPropertyDataset
        classes."""
        lookupMap: Dict[str, type] = {
            "administrativeInformation": FlowPropertyAdministrativeInformation,
            "classificationInformation": ClassificationInformation,
            "dataEntryBy": FlowPropertyDataEntryBy,
            "dataSetInformation": FlowPropertyDataSetInformation,
            "dataSourcesTreatmentAndRepresentativeness": FPDSTAR,
            "modellingAndValidation": FlowPropertyModellingAndValidation,
            "publicationAndOwnership": FlowPropertyPublicationAndOwnership,
            "quantitativeReference": FlowPropertyQuantitativeReference,
        }
        try:
            return lookupMap[name]
        except KeyError:
            return _check_common_lookup(name)


class UnitGroupDatasetLookup(etree.CustomElementClassLookup):
    """Custom XML lookup class for ILCD UnitGroupDataset files."""

    def lookup(
        self, unused_node_type, unused_document, unused_namespace, name: str
    ) -> type:
        """Maps ILCD UnitGroupDataset XML elements to custom UnitGroupDataset
        classes."""
        lookupMap: Dict[str, type] = {
            "administrativeInformation": UnitGroupAdministrativeInformation,
            "classificationInformation": ClassificationInformation,
            "dataEntryBy": UnitGroupDataEntryBy,
            "dataSetInformation": UnitGroupDataSetInformation,
            "modellingAndValidation": UnitGroupModellingAndValidation,
            "publicationAndOwnership": UnitGroupPublicationAndOwnership,
            "quantitativeReference": UnitGroupQuantitativeReference,
        }
        try:
            return lookupMap[name]
        except KeyError:
            return _check_common_lookup(name)


class ContactDatasetLookup(etree.CustomElementClassLookup):
    """Custom XML lookup class for ILCD ContactDataset files."""

    def lookup(
        self, unused_node_type, unused_document, unused_namespace, name: str
    ) -> type:
        """Maps ILCD ContactDataset XML elements to custom ContactDataset classes."""
        lookupMap: Dict[str, type] = {
            "administrativeInformation": ContactAdministrativeInformation,
            "dataEntryBy": ContactDataEntryBy,
            "dataSetInformation": ContactDataSetInformation,
            "classificationInformation": ClassificationInformation,
            "publicationAndOwnership": ContactPublicationAndOwnership,
        }
        try:
            return lookupMap[name]
        except KeyError:
            return _check_common_lookup(name)


class SourceDatasetLookup(etree.CustomElementClassLookup):
    """Custom XML lookup class for ILCD SourceDataset files."""

    def lookup(
        self, unused_node_type, unused_document, unused_namespace, name: str
    ) -> type:
        """Maps ILCD SourceDataset XML elements to custom SourceDataset classes."""
        lookupMap: Dict[str, type] = {
            "administrativeInformation": SourceAdministrativeInformation,
            "dataEntryBy": SourceDataEntryBy,
            "dataSetInformation": SourceDataSetInformation,
            "classificationInformation": ClassificationInformation,
            "publicationAndOwnership": SourcePublicationAndOwnership,
        }
        try:
            return lookupMap[name]
        except KeyError:
            return _check_common_lookup(name)


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


def validate_file_flow_dataset(
    file: Union[str, Path, StringIO]
) -> Union[None, List[str]]:
    """Validates an ILCD Flow Dataset XML file against schema.
    Parameters:
    file: the str|Path path to the ILCD Flow Dataset XML file or its StringIO
    representation.
    Returns ``None`` if valid or a list of error strings.
    """
    return validate_file(file, Defaults.SCHEMA_FLOW_DATASET)


def validate_file_flow_property_dataset(
    file: Union[str, Path, StringIO]
) -> Union[None, List[str]]:
    """Validates an ILCD Flow Property Dataset XML file against schema.
    Parameters:
    file: the str|Path path to the ILCD Flow Property Dataset XML file or its StringIO
    representation.
    Returns ``None`` if valid or a list of error strings.
    """
    return validate_file(file, Defaults.SCHEMA_FLOW_PROPERTY_DATASET)


def validate_file_unit_group_dataset(
    file: Union[str, Path, StringIO]
) -> Union[None, List[str]]:
    """Validates an ILCD Unit Group Dataset XML file against schema.
    Parameters:
    file: the str|Path path to the ILCD Unit Group Dataset XML file or its StringIO
    representation.
    Returns ``None`` if valid or a list of error strings.
    """
    return validate_file(file, Defaults.SCHEMA_UNIT_GROUP_DATASET)


def validate_file_contact_dataset(
    file: Union[str, Path, StringIO]
) -> Union[None, List[str]]:
    """Validates an ILCD Contact Dataset XML file against schema.
    Parameters:
    file: the str|Path path to the ILCD Contact Dataset XML file or its StringIO
    representation.
    Returns ``None`` if valid or a list of error strings.
    """
    return validate_file(file, Defaults.SCHEMA_CONTACT_DATASET)


def validate_file_source_dataset(
    file: Union[str, Path, StringIO]
) -> Union[None, List[str]]:
    """Validates an ILCD Source Dataset XML file against schema.
    Parameters:
    file: the str|Path path to the ILCD Source Dataset XML file or its StringIO
    representation.
    Returns ``None`` if valid or a list of error strings.
    """
    return validate_file(file, Defaults.SCHEMA_SOURCE_DATASET)


def validate_directory_process_dataset(
    dir_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, Union[None, List[str]]]]:
    """Validates a directory of ILCD Process Dataset XML files.
    Parameters:
    dir_path: the directory path, should contain ILCD Process Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding list of errors, which
    is ``None`` if no errors.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return validate_directory(
        dir_path=dir_path,
        schema_path=Defaults.SCHEMA_PROCESS_DATASET,
        valid_suffixes=valid_suffixes,
    )


def validate_directory_flow_dataset(
    dir_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, Union[None, List[str]]]]:
    """Validates a directory of ILCD Flow Dataset XML files.
    Parameters:
    dir_path: the directory path, should contain ILCD Flow Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding list of errors, which
    is ``None`` if no errors.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return validate_directory(
        dir_path=dir_path,
        schema_path=Defaults.SCHEMA_FLOW_DATASET,
        valid_suffixes=valid_suffixes,
    )


def validate_directory_flow_property_dataset(
    dir_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, Union[None, List[str]]]]:
    """Validates a directory of ILCD Flow Property Dataset XML files.
    Parameters:
    dir_path: the directory path, should contain ILCD Flow Property Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding list of errors, which
    is ``None`` if no errors.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return validate_directory(
        dir_path=dir_path,
        schema_path=Defaults.SCHEMA_FLOW_PROPERTY_DATASET,
        valid_suffixes=valid_suffixes,
    )


def validate_directory_unit_group_dataset(
    dir_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, Union[None, List[str]]]]:
    """Validates a directory of ILCD Unit Group Dataset XML files.
    Parameters:
    dir_path: the directory path, should contain ILCD Unit Group Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding list of errors, which
    is ``None`` if no errors.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return validate_directory(
        dir_path=dir_path,
        schema_path=Defaults.SCHEMA_UNIT_GROUP_DATASET,
        valid_suffixes=valid_suffixes,
    )


def validate_directory_contact_dataset(
    dir_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, Union[None, List[str]]]]:
    """Validates a directory of ILCD Contact Dataset XML files.
    Parameters:
    dir_path: the directory path, should contain ILCD Contact Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding list of errors, which
    is ``None`` if no errors.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return validate_directory(
        dir_path=dir_path,
        schema_path=Defaults.SCHEMA_CONTACT_DATASET,
        valid_suffixes=valid_suffixes,
    )


def validate_directory_source_dataset(
    dir_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, Union[None, List[str]]]]:
    """Validates a directory of ILCD Source Dataset XML files.
    Parameters:
    dir_path: the directory path, should contain ILCD Source Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding list of errors, which
    is ``None`` if no errors.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return validate_directory(
        dir_path=dir_path,
        schema_path=Defaults.SCHEMA_SOURCE_DATASET,
        valid_suffixes=valid_suffixes,
    )


def validate_zip_file_process_dataset(
    file_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, Union[None, List[str]]]]:
    """Validates a ZIP FILE of ILCD Process Dataset XML files.
    Parameters:
    file_path: the ZIP file path, should contain ILCD Process Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding list of errors, which
    is ``None`` if no errors.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return validate_zip_file(
        file_path=file_path,
        schema_path=Defaults.SCHEMA_PROCESS_DATASET,
        valid_suffixes=valid_suffixes,
    )


def validate_zip_file_flow_dataset(
    file_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, Union[None, List[str]]]]:
    """Validates a ZIP FILE of ILCD Flow Dataset XML files.
    Parameters:
    file_path: the ZIP file path, should contain ILCD Flow Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding list of errors, which
    is ``None`` if no errors.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return validate_zip_file(
        file_path=file_path,
        schema_path=Defaults.SCHEMA_FLOW_DATASET,
        valid_suffixes=valid_suffixes,
    )


def validate_zip_file_flow_property_dataset(
    file_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, Union[None, List[str]]]]:
    """Validates a ZIP FILE of ILCD Flow Property Dataset XML files.
    Parameters:
    file_path: the ZIP file path, should contain ILCD Flow Property Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding list of errors, which
    is ``None`` if no errors.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return validate_zip_file(
        file_path=file_path,
        schema_path=Defaults.SCHEMA_FLOW_PROPERTY_DATASET,
        valid_suffixes=valid_suffixes,
    )


def validate_zip_file_unit_group_dataset(
    file_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, Union[None, List[str]]]]:
    """Validates a ZIP FILE of ILCD Unit Group Dataset XML files.
    Parameters:
    file_path: the ZIP file path, should contain ILCD Unit Group Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding list of errors, which
    is ``None`` if no errors.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return validate_zip_file(
        file_path=file_path,
        schema_path=Defaults.SCHEMA_UNIT_GROUP_DATASET,
        valid_suffixes=valid_suffixes,
    )


def validate_zip_file_contact_dataset(
    file_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, Union[None, List[str]]]]:
    """Validates a ZIP FILE of ILCD Contact Dataset XML files.
    Parameters:
    file_path: the ZIP file path, should contain ILCD Contact Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding list of errors, which
    is ``None`` if no errors.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return validate_zip_file(
        file_path=file_path,
        schema_path=Defaults.SCHEMA_CONTACT_DATASET,
        valid_suffixes=valid_suffixes,
    )


def validate_zip_file_source_dataset(
    file_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, Union[None, List[str]]]]:
    """Validates a ZIP FILE of ILCD Source Dataset XML files.
    Parameters:
    file_path: the ZIP file path, should contain ILCD Source Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding list of errors, which
    is ``None`` if no errors.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return validate_zip_file(
        file_path=file_path,
        schema_path=Defaults.SCHEMA_SOURCE_DATASET,
        valid_suffixes=valid_suffixes,
    )


def parse_file_process_dataset(file: Union[str, Path, StringIO]) -> ProcessDataSet:
    """Parses an ILCD Process Dataset XML file to custom ILCD classes.
    Parameters:
    file: the str|Path path to the ProcessDataset XML file or its StringIO
    representation.
    Returns a ProcessDataset class representing the root of the XML file.
    """
    return parse_file(file, Defaults.SCHEMA_PROCESS_DATASET, ProcessDatasetLookup())


def parse_file_flow_dataset(file: Union[str, Path, StringIO]) -> FlowDataSet:
    """Parses an ILCD Flow DataSet XML file to custom ILCD classes.
    Parameters:
    file: the str|Path path to the Flow DataSet XML file or its StringIO
    representation.
    Returns a FlowDataSet class representing the root of the XML file.
    """
    return parse_file(file, Defaults.SCHEMA_FLOW_DATASET, FlowDatasetLookup())


def parse_file_flow_property_dataset(
    file: Union[str, Path, StringIO]
) -> FlowPropertyDataSet:
    """Parses an ILCD Flow Property DataSet XML file to custom ILCD classes.
    Parameters:
    file: the str|Path path to the Flow Property DataSet XML file or its StringIO
    representation.
    Returns a FlowPropertyDataSet class representing the root of the XML file.
    """
    return parse_file(
        file, Defaults.SCHEMA_FLOW_PROPERTY_DATASET, FlowPropertyDatasetLookup()
    )


def parse_file_unit_group_dataset(file: Union[str, Path, StringIO]) -> UnitGroupDataSet:
    """Parses an ILCD Unit Group DataSet XML file to custom ILCD classes.
    Parameters:
    file: the str|Path path to the Unit Group DataSet XML file or its StringIO
    representation.
    Returns a UnitGroupDataSet class representing the root of the XML file.
    """
    return parse_file(
        file, Defaults.SCHEMA_UNIT_GROUP_DATASET, UnitGroupDatasetLookup()
    )


def parse_file_contact_dataset(file: Union[str, Path, StringIO]) -> ContactDataSet:
    """Parses an ILCD Contact DataSet XML file to custom ILCD classes.
    Parameters:
    file: the str|Path path to the Contact DataSet XML file or its StringIO
    representation.
    Returns a ContactDataSet class representing the root of the XML file.
    """
    return parse_file(file, Defaults.SCHEMA_CONTACT_DATASET, ContactDatasetLookup())


def parse_file_source_dataset(file: Union[str, Path, StringIO]) -> SourceDataSet:
    """Parses an ILCD Source DataSet XML file to custom ILCD classes.
    Parameters:
    file: the str|Path path to the Source DataSet XML file or its StringIO
    representation.
    Returns a SourceDataSet class representing the root of the XML file.
    """
    return parse_file(file, Defaults.SCHEMA_SOURCE_DATASET, SourceDatasetLookup())


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


def parse_directory_flow_dataset(
    dir_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, FlowDataSet]]:
    """Parses a directory of ILCD Flow Dataset XML files to a list of
    custom ILCD classes.
    Parameters:
    dir_path: the directory path, should contain ILCD Flow Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding ILCD classes
    representing the root of the XML file.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return parse_directory(
        dir_path=dir_path,
        schema_path=Defaults.SCHEMA_FLOW_DATASET,
        lookup=FlowDatasetLookup(),
        valid_suffixes=valid_suffixes,
    )


def parse_directory_flow_property_dataset(
    dir_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, FlowPropertyDataSet]]:
    """Parses a directory of ILCD Flow Property Dataset XML files to a list of
    custom ILCD classes.
    Parameters:
    dir_path: the directory path, should contain ILCD Flow Property Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding ILCD classes
    representing the root of the XML file.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return parse_directory(
        dir_path=dir_path,
        schema_path=Defaults.SCHEMA_FLOW_PROPERTY_DATASET,
        lookup=FlowPropertyDatasetLookup(),
        valid_suffixes=valid_suffixes,
    )


def parse_directory_unit_group_dataset(
    dir_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, UnitGroupDataSet]]:
    """Parses a directory of ILCD Unit Group Dataset XML files to a list of
    custom ILCD classes.
    Parameters:
    dir_path: the directory path, should contain ILCD Unit Group Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding ILCD classes
    representing the root of the XML file.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return parse_directory(
        dir_path=dir_path,
        schema_path=Defaults.SCHEMA_UNIT_GROUP_DATASET,
        lookup=UnitGroupDatasetLookup(),
        valid_suffixes=valid_suffixes,
    )


def parse_directory_contact_dataset(
    dir_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, ContactDataSet]]:
    """Parses a directory of ILCD Contact Dataset XML files to a list of
    custom ILCD classes.
    Parameters:
    dir_path: the directory path, should contain ILCD Contact Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding ILCD classes
    representing the root of the XML file.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return parse_directory(
        dir_path=dir_path,
        schema_path=Defaults.SCHEMA_CONTACT_DATASET,
        lookup=ContactDatasetLookup(),
        valid_suffixes=valid_suffixes,
    )


def parse_directory_source_dataset(
    dir_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, SourceDataSet]]:
    """Parses a directory of ILCD Source Dataset XML files to a list of
    custom ILCD classes.
    Parameters:
    dir_path: the directory path, should contain ILCD Source Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding ILCD classes
    representing the root of the XML file.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return parse_directory(
        dir_path=dir_path,
        schema_path=Defaults.SCHEMA_SOURCE_DATASET,
        lookup=SourceDatasetLookup(),
        valid_suffixes=valid_suffixes,
    )


def parse_zip_file_process_dataset(
    file_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, ProcessDataSet]]:
    """Parses a ZIP file of ILCD Process Dataset XML files to a list of
    custom ILCD classes.
    Parameters:
    file_path: the ZIP file path, should contain ILCD Process Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding ILCD classes
    representing the root of the XML file.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return parse_zip_file(
        file_path=file_path,
        schema_path=Defaults.SCHEMA_PROCESS_DATASET,
        lookup=ProcessDatasetLookup(),
        valid_suffixes=valid_suffixes,
    )


def parse_zip_file_flow_dataset(
    file_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, FlowDataSet]]:
    """Parses a ZIP file of ILCD Flow Dataset XML files to a list of
    custom ILCD classes.
    Parameters:
    file_path: the ZIP file path, should contain ILCD Flow Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding ILCD classes
    representing the root of the XML file.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return parse_zip_file(
        file_path=file_path,
        schema_path=Defaults.SCHEMA_FLOW_DATASET,
        lookup=FlowDatasetLookup(),
        valid_suffixes=valid_suffixes,
    )


def parse_zip_file_flow_property_dataset(
    file_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, FlowPropertyDataSet]]:
    """Parses a ZIP file of ILCD Flow Property Dataset XML files to a list of
    custom ILCD classes.
    Parameters:
    file_path: the ZIP file path, should contain ILCD Flow Property Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding ILCD classes
    representing the root of the XML file.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return parse_zip_file(
        file_path=file_path,
        schema_path=Defaults.SCHEMA_FLOW_PROPERTY_DATASET,
        lookup=FlowPropertyDatasetLookup(),
        valid_suffixes=valid_suffixes,
    )


def parse_zip_file_unit_group_dataset(
    file_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, UnitGroupDataSet]]:
    """Parses a ZIP file of ILCD Unit Group Dataset XML files to a list of
    custom ILCD classes.
    Parameters:
    file_path: the ZIP file path, should contain ILCD Unit Group Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding ILCD classes
    representing the root of the XML file.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return parse_zip_file(
        file_path=file_path,
        schema_path=Defaults.SCHEMA_UNIT_GROUP_DATASET,
        lookup=UnitGroupDatasetLookup(),
        valid_suffixes=valid_suffixes,
    )


def parse_zip_file_contact_dataset(
    file_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, ContactDataSet]]:
    """Parses a ZIP file of ILCD Contact Dataset XML files to a list of
    custom ILCD classes.
    Parameters:
    file_path: the ZIP file path, should contain ILCD Contact Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding ILCD classes
    representing the root of the XML file.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return parse_zip_file(
        file_path=file_path,
        schema_path=Defaults.SCHEMA_CONTACT_DATASET,
        lookup=ContactDatasetLookup(),
        valid_suffixes=valid_suffixes,
    )


def parse_zip_file_source_dataset(
    file_path: Union[str, Path], valid_suffixes: Union[List[str], None] = None
) -> List[Tuple[Path, SourceDataSet]]:
    """Parses a ZIP file of ILCD Source Dataset XML files to a list of
    custom ILCD classes.
    Parameters:
    file_path: the ZIP file path, should contain ILCD Source Dataset files.
    valid_suffixes: a list of valid file suffixes which will only be considered for
    parsing. If None, defaults to [".xml", ".ilcd"].
    Returns a list of tuples of file paths and corresponding ILCD classes
    representing the root of the XML file.
    """
    if valid_suffixes is None:
        valid_suffixes = [".xml", ".ilcd"]

    return parse_zip_file(
        file_path=file_path,
        schema_path=Defaults.SCHEMA_SOURCE_DATASET,
        lookup=SourceDatasetLookup(),
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
