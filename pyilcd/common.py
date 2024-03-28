"""Common custom ILCD Python classes."""

from datetime import datetime
from typing import List

from lxml import etree
from lxmlh import get_element, get_element_list

from .helpers import (
    create_attribute_list_process_dataset,
    create_attribute_process_dataset,
    create_element_text_process_dataset,
)


class GlobalReference(etree.ElementBase):
    """Represents a reference to another dataset or file. Either refObjectId
    and version, or uri, or both have to be specified."""

    subReference = create_attribute_list_process_dataset("subReference", str)
    """Valid only for references of type "source data set". Allows to make
    references to sections, pages etc. within a source."""

    shortDescription = create_attribute_list_process_dataset("shortDescription", str)
    """Short, clear-text summary of the referenced object that can be
    used as a hint what to expect behind the reference in cases where it
    cannot be resolved."""

    type = create_attribute_process_dataset("type", str)
    """(required) - indicates the type of the referenced dataset/file.
    One of GlobalReferenceTypeValues."""

    refObjectId = create_attribute_process_dataset("refObjectId", str)
    """UUID of the referenced object"""

    version = create_attribute_process_dataset("version", str)
    """version number of the referenced object"""

    uri = create_attribute_process_dataset("uri", str)
    """URI of the referenced object"""


class ClassificationInformation(etree.ElementBase):
    """Hierarchical classification of the good, service, or process.
    (Note: This entry is NOT required for the identification of a Process. It should
    nevertheless be avoided to use identical names for Processes in the same
    category."""

    @property
    def classifications(self) -> List["Classification"]:
        """Optional statistical or other classification of the data set.
        Typically also used for structuring LCA databases."""
        return get_element_list(self, "common:classification")


class Classification(etree.ElementBase):
    """Optional statistical or other classification of the data set.
    Typically also used for structuring LCA databases."""

    name = create_attribute_process_dataset("name", str)
    """Name of the classification system."""

    classes = create_attribute_process_dataset("classes", str)
    """URL or file name of a file listing all classes of this
    classification system. [Notes: the referenced file has to be
    in form of the "ILCDClassification.xml" format. If a
    classification file is specified, the "class" entry should
    correspond to the classes defined in the classification
    file.]"""

    @property
    def classesList(self) -> List["Class"]:
        """Name of the class."""
        return get_element_list(self, "common:class")


class Class(etree.ElementBase):
    """Name of the class."""

    level = create_attribute_process_dataset("level", int)
    """If more than one class is specified in a hierachical classification
    system, the hierarchy level (1,2,...) could be specified with this
    attribute of class."""

    classId = create_attribute_process_dataset("classId", str)
    """Unique identifier for the class. [Notes: If such identifiers are
    also defined in the referenced category file, they should be identical.
    Identifiers can be UUID's, but also other forms are allowed.]"""


class Scope(etree.ElementBase):
    """Scope of review regarding which aspects and components
    of the data set was reviewed or verified. In case of
    aggregated e.g. LCI results also and on which level of
    detail (e.g. LCI results only, included unit processes, ...)
    the review / verification was performed."""

    name = create_attribute_process_dataset("name", str)
    """Scope name"""

    @property
    def method(self) -> List["Method"]:
        """Validation method(s) used in the respective "Scope of review"."""
        return get_element_list(self, "common:method")


class Method(etree.ElementBase):
    """Validation method(s) used in the respective "Scope of review"."""

    name = create_attribute_process_dataset("name", str)
    """Method name"""


class DataQualityIndicators(etree.ElementBase):
    """Data quality indicators serve to provide the reviewed key
    information on the data set in a defined, computer-readable
    (and hence searchable) form. This serves to support LCA practitioners
    to identify/select the highest quality and most appropriate data sets."""

    @property
    def dataQualityIndicators(self) -> List["DataQualityIndicator"]:
        """Data quality indicators serve to provide the reviewed key
        information on the data set in a defined, computer-readable
        (and hence searchable) form. This serves to support LCA practitioners
        to identify/select the highest quality and most appropriate data sets."""
        return get_element_list(self, "common:dataQualityIndicator")


class DataQualityIndicator(etree.ElementBase):
    """Data quality indicators serve to provide the reviewed key information
    on the data set in a defined, computer-readable (and hence searchable) form.
    This serves to support LCA practitioners to identify/select the highest quality
    and most appropriate data sets."""

    name = create_attribute_process_dataset("name", str)
    """Name of indicator"""

    value = create_attribute_process_dataset("value", str)
    """Value of indicator"""


class ValidationGroup1(etree.ElementBase):
    """Common group."""

    reviewDetails = create_attribute_list_process_dataset("common:reviewDetails", str)
    """Summary of the review. All the following items should be explicitly
    addressed: Representativeness, completeness, and precision of Inputs and
    Outputs for the process in its documented location, technology and time
    i.e. both completeness of technical model (product, waste, and elementary
    flows) and completeness of coverage of the relevant problem fields
    (environmental, human health, resource use) for this specific good, service,
    or process. Plausibility of data. Correctness and appropriateness of the
    data set documentation. Appropriateness of system boundaries, cut-off rules,
    LCI modelling choices such as e.g. allocation, consistency of included
    processes and of LCI methodology. If the data set comprises pre-calculated
    LCIA results, the correspondence of the Input and Output elementary flows
    (including their geographical validity) with the applied LCIA method(s)
    should be addressed by the reviewer. An overall quality statement on the
    data set may be included here."""

    @property
    def scope(self) -> "Scope":
        """Scope of review regarding which aspects and components
        of the data set was reviewed or verified. In case of
        aggregated e.g. LCI results also and on which level of
        detail (e.g. LCI results only, included unit processes, ...)
        the review / verification was performed."""
        return get_element(self, "common:scope")

    @property
    def dataQualityIndicators(self) -> "DataQualityIndicators":
        """Data quality indicators serve to provide the reviewed key
        information on the data set in a defined, computer-readable
        (and hence searchable) form. This serves to support LCA practitioners
        to identify/select the highest quality and most appropriate data sets."""
        return get_element(self, "common:dataQualityIndicators")


class ValidationGroup3(etree.ElementBase):
    """Common group."""

    otherReviewDetails = create_attribute_list_process_dataset(
        "common:otherReviewDetails", str
    )
    """Further information from the review process, especially comments received
    from third parties once the data set has been published or additional reviewer
    comments from an additional external review."""

    @property
    def referenceToNameOfReviewerAndInstitution(self) -> "GlobalReference":
        """ "Contact data set" of reviewer. The full name of reviewer(s) and
        institution(s) as well as a contact address and/or email should be
        provided in that contact data set."""
        return get_element(self, "common:referenceToNameOfReviewerAndInstitution")

    @property
    def referenceToCompleteReviewReport(self) -> "GlobalReference":
        """ ""Source data set" of the complete review report."""
        return get_element(self, "common:referenceToCompleteReviewReport")


class ComplianceGroup(etree.ElementBase):
    """Common group."""

    approvalOfOverallCompliance = create_element_text_process_dataset(
        "approvalOfOverallCompliance", str
    )
    """Official approval whether or not and in how far the data set meets
    all the requirements of the "Compliance system" refered to. This
    approval should be issued/confirmed by the owner of that compliance
    system, who is identified via the respective "Contact data set"."""

    @property
    def referenceToComplianceSystem(self) -> "GlobalReference":
        """Source data set" of the "Compliance system" that is declared to
        be met by the data set."""
        return get_element(self, "common:referenceToComplianceSystem")


class CommissionerAndGoal(etree.ElementBase):
    """Basic information about goal and scope of the data set."""

    project = create_attribute_list_process_dataset("common:project", str)
    """Project within which the data set was modelled in its present
    version. [Note: If the project was published e.g. as a report,
    this can be referenced in the "Publication of data set in:" field in
    the "Publication and ownership" sub-section."""

    intendedApplications = create_attribute_list_process_dataset(
        "common:intendedApplications", str
    )
    """Documentation of the intended application(s) of data collection
    and data set modelling. This indicates / includes information on
    the level of detail, the specifidity, and the quality ambition inthe effort."""

    @property
    def referenceToCommissioner(self) -> List["GlobalReference"]:
        """ "Contact data set" of the commissioner / financing party
        of the data collection / compilation and of the data set
        modelling. For groups of commissioners, each single organisation
        should be named. For data set updates and for direct use of data
        from formerly commissioned studies, also the original commissioner
        should be named."""
        return get_element_list(self, "common:referenceToCommissioner")


class DataEntryByGroup1(etree.ElementBase):
    """Common group."""

    timeStamp = create_element_text_process_dataset("common:timeStamp", datetime)
    """Date and time stamp of data set generation, typically an automated
    entry ("last saved")."""

    @property
    def referenceToDataSetFormat(self) -> List["GlobalReference"]:
        """ "Source data set" of the used version of the ILCD format.
        If additional data format fields have been integrated into the
        data set file, using the "namespace" option, the used format
        namespace(s) are to be given. This is the case if the data sets
        carries additional information as specified by other, particular
        LCA formats, e.g. of other database networks or LCA softwares."""
        return get_element_list(self, "common:referenceToDataSetFormat")


class DataEntryByGroup2(etree.ElementBase):
    """Common group."""

    @property
    def referenceToPersonOrEntityEnteringTheData(self) -> "GlobalReference":
        """ ""Contact data set" of the responsible person or entity that
        has documented this data set, i.e. entered the data and the
        descriptive information."""
        return get_element(self, "common:referenceToPersonOrEntityEnteringTheData")


class PublicationAndOwnershipGroup1(etree.ElementBase):
    """Common group."""

    dataSetVersion = create_element_text_process_dataset("common:dataSetVersion", str)
    """Version number of data set. First two digits refer to
    major updates, the second two digits to minor revisions and
    error corrections etc. The third three digits are intended for
    automatic and internal counting of versions during data set
    development. Together with the data set's UUID, the "Data set
    version" uniquely identifies each data set."""

    permanentDataSetURI = create_element_text_process_dataset(
        "common:permanentDataSetURI", str
    )
    """URI (i.e. an internet address) of the original of this data set
    [Note: This equally globally unique identifier supports users and software
    tools to identify and retrieve the original version of a data set via the
    internet or to check for available updates. The URI must not represent an
    existing WWW address, but it should be unique and point to the data access
    point, e.g. by combining the data owner's www path with the data set's UUID, e.g.
    http://www.mycompany.com/lca/processes/50f12420-8855-12db-b606-0900210c9a66.]"""

    @property
    def referenceToPrecedingDataSetVersion(self) -> List["GlobalReference"]:
        """Last preceding data set, which was replaced by this version.
        Either a URI of that data set (i.e. an internet address) or its
        UUID plus version number is given (or both)."""
        return get_element_list(self, "common:referenceToPrecedingDataSetVersion")


class PublicationAndOwnershipGroup2(etree.ElementBase):
    """Common group."""

    workflowAndPublicationStatus = create_element_text_process_dataset(
        "common:workflowAndPublicationStatus", str
    )
    """Workflow or publication status of data set. Details e.g. of
    foreseen publication dates should be provided on request by th
    "Data set owner"."""

    @property
    def referenceToUnchangedRepublication(self) -> "GlobalReference":
        """ "Source data set" of the publication, in which this
        data set was published for the first time. [Note: This
        refers to exactly this data set as it is, without any format
        conversion, adjustments, flow name mapping, etc. In case this
        data set was modified/converted, the original source is
        documented in "Converted original data set from:" in section
        "Data entry by".]"""
        return get_element(self, "common:referenceToUnchangedRepublication")


class PublicationAndOwnershipGroup3(etree.ElementBase):
    """Common group."""

    copyright = create_element_text_process_dataset("common:copyright", bool)
    """Indicates whether or not a copyright on the data set exists.
    Decided upon by the "Owner of data set". [Note: See also field
    "Access and use restrictions".]"""

    licenseType = create_element_text_process_dataset("common:licenseType", str)
    """Type of license that applies to the access and use of this data set."""

    accessRestrictions = create_attribute_list_process_dataset(
        "common:accessRestrictions", str
    )
    """Access restrictions / use conditions for this data set as free text
    or referring to e.g. license conditions. In case of no restrictions
    "None" is entered."""

    @property
    def referenceToEntitiesWithExclusiveAccess(self) -> List["GlobalReference"]:
        """ "Contact data set" of those entities or persons (or
        groups of these), to which an exclusive access to this
        data set is granted. Mainly intended to be used in
        confidentiality management in projects. [Note: See also
        field "Access and use restrictions".]"""
        return get_element_list(self, "common:referenceToEntitiesWithExclusiveAccess")


class FlowCategoryInformation(etree.ElementBase):
    """Hierachical classification of the Flow property foreseen to be used
    to structure the Flow property content of the database. (Note: This entry
    is NOT required for the identification of the Flow property data set. It
    should nevertheless be avoided to use identical names for Flow properties
    in the same class."""

    @property
    def elementaryFlowCategorization(self) -> List["FlowCategorization"]:
        """Identifying category/compartment information exclusively used for
        elementary flows. E.g. "Emission to air", "Renewable resource", etc."""
        return get_element_list(self, "common:elementaryFlowCategorization")

    @property
    def classifications(self) -> List["Classification"]:
        """Optional statistical or other classification of the data set.
        Typically also used for structuring LCA databases."""
        return get_element_list(self, "common:classification")


class FlowCategorization(etree.ElementBase):
    """Identifying category/compartment information exclusively used for
    elementary flows. E.g. "Emission to air", "Renewable resource", etc."""

    name = create_attribute_process_dataset("name", str)
    """Name of the categorization system. E.g. "ILCD 1.1" or another
    elementary flow categorization/compartment scheme applied, as
    defined e.g. in other LCA database (systems)."""

    categories = create_attribute_process_dataset("categories", str)
    """URL or file name of a file containing all categories of this
    categorization system. [Note: The file is to be in form of the
    "ILCDCategories.xml" format. If a category file is specified, only
    categories of the referenced categories file should be used.]"""

    @property
    def categoryList(self) -> List["Category"]:
        """Name of the category of this elementary flow.."""
        return get_element_list(self, "common:category")


class Category(etree.ElementBase):
    """Name of the category of this elementary flow."""

    level = create_attribute_process_dataset("level", str)
    """Hierarchy level (1,2,...), if the categorization system
    is hierachical, otherwise emtpy or not used."""

    catId = create_attribute_process_dataset("catId", str)
    """Unique identifier of the category. [Note: May be used by LCA
    software for it's category system. If used the identifer should
    be identical to the on defined in the referenced category file.
    Identifiers can be UUIDs, but also other forms are possible.]"""


class ComplianceDeclarations(etree.ElementBase):
    """Statements on compliance of several data set aspects with compliance
    requirements as defined by the referenced compliance system (e.g. an
    EPD scheme, handbook of a national or international data network such
    as the ILCD, etc.)."""

    @property
    def compliances(self) -> List["Compliance"]:
        """One compliance declaration"""
        return get_element_list(self, "compliance")


class Compliance(ComplianceGroup):
    """One compliance declaration"""
