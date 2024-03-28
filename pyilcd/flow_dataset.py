"""Custom ILCD Python classes for FlowDataSet of ILCD schema."""

from typing import List

from lxml import etree
from lxmlh import get_element, get_element_list
from pycasreg.validation import validate_cas

from .common import (
    ComplianceDeclarations,
    DataEntryByGroup1,
    DataEntryByGroup2,
    FlowCategoryInformation,
    GlobalReference,
    PublicationAndOwnershipGroup1,
)
from .helpers import (
    create_attribute_flow_dataset,
    create_attribute_list_flow_dataset,
    create_element_text_flow_dataset,
)


class FlowDataSet(etree.ElementBase):
    """Covers the INvariable flow information addressed in ISO/TS
    14048's section "Inputs and outputs" """

    version = create_attribute_flow_dataset("version", str)
    """Indicates, which version of the ILCD format is used."""

    locations = create_attribute_flow_dataset("locations", str)
    """Contains reference to used location table for this dataset."""

    @property
    def flowInformation(self) -> "FlowInformation":
        """Covers the INvariable flow information addressed in ISO/TS
        14048's section "Inputs and outputs" """
        return get_element(self, "flowInformation")

    @property
    def modellingAndValidation(self) -> "ModellingAndValidation":
        """Covers the five sub-sections 1) LCI method, 2) Data sources,
        treatment and representativeness (not used for flows),
        3) Completeness (not used for flows), 4) Validation (not
        used for flows), and 5) Compliance."""
        return get_element(self, "modellingAndValidation")

    @property
    def administrativeInformation(self) -> "AdministrativeInformation":
        """Information on data set management and administration."""
        return get_element(self, "administrativeInformation")

    @property
    def flowProperties(self) -> "FlowProperties":
        """List of flow properties (with all variable information
        linked to that respective flow)."""
        return get_element(self, "flowProperties")


class FlowInformation(etree.ElementBase):
    """Covers the INvariable flow information addressed in ISO/TS
    14048's section "Inputs and outputs" """

    @property
    def dataSetInformation(self) -> "DataSetInformation":
        """General data set information. Covers the ISO/TS 14048 fields
        1.2.1, 1.2.3, 1.2.4, 1.2.5, (1.2.6), (1.2.7),1.2.10.1, 1.2.10.2,
        1.2.10.3, and references to 1.2.11 (Flow property) and 1.2.11.2
        (Unit)."""
        return get_element(self, "dataSetInformation")

    @property
    def quantitativeReference(self) -> "QuantitativeReference":
        """This section names the type of quantitative reference used for
        this Flow data set, which is always one of the Flow's Flow
        properties (see section "Flow properties")."""
        return get_element(self, "quantitativeReference")

    @property
    def geography(self) -> "Geography":
        """Provides information about the geographical representativeness
        of the data set."""
        return get_element(self, "geography")

    @property
    def technology(self) -> "Technology":
        """Provides information about the technological representativeness
        of the flow in case it is a product or waste flow."""
        return get_element(self, "technology")


class ModellingAndValidation(etree.ElementBase):
    """Covers the five sub-sections 1) LCI method, 2) Data sources,
    treatment and representativeness (not used for flows),
    3) Completeness (not used for flows), 4) Validation (not
    used for flows), and 5) Compliance."""

    @property
    def lciMethod(self) -> "LCIMethod":
        """LCI methodological modelling aspects."""
        return get_element(self, "LCIMethod")

    @property
    def complianceDeclarations(self) -> "ComplianceDeclarations":
        """Statements on compliance of several data set aspects with compliance
        requirements as defined by the referenced compliance system (e.g. an
        EPD scheme, handbook of a national or international data network such
        as the ILCD, etc.)."""
        return get_element(self, "complianceDeclarations")


class AdministrativeInformation(etree.ElementBase):
    """Information on data set management and administration."""

    @property
    def dataEntryBy(self) -> "DataEntryBy":
        """Staff or entity, that documented the generated data set, entering
        the information into the database; plus administrative information
        linked to the data entry activity.."""
        return get_element(self, "dataEntryBy")

    @property
    def publicationAndOwnership(self) -> "PublicationAndOwnership":
        """Information related to publication and version management of the
        data set including copyright and access restrictions."""
        return get_element(self, "publicationAndOwnership")


class FlowProperties(etree.ElementBase):
    """List of flow properties (with all variable information
    linked to that respective flow)."""

    @property
    def flowProperties(self) -> List["FlowProperty"]:
        """One flow property."""
        return get_element_list(self, "flowProperty")


class DataSetInformation(etree.ElementBase):
    """General data set information. Covers the ISO/TS 14048 fields
    1.2.1, 1.2.3, 1.2.4, 1.2.5, (1.2.6), (1.2.7),1.2.10.1, 1.2.10.2,
    1.2.10.3, and references to 1.2.11 (Flow property) and 1.2.11.2
    (Unit)."""

    commonUUID = create_attribute_flow_dataset("common:UUID", str)
    """Automatically generated Universally Unique Identifier of this data
    set. Together with the "Data set version", the UUID uniquely identifies each data
    set."""

    synonyms = create_attribute_list_flow_dataset("common:synonyms", str)
    """Synonyms / alternative names / brands of the good, service, or
    process. Separated by semicolon."""

    casNumber = create_attribute_flow_dataset("CASNumber", str, validate_cas)
    """Chemical Abstract Systems Number of the substance. [Note: Should only be
    given for (virtually) pure substances, but NOT also for the main constituent of a
    material or product etc.]"""

    sumFormula = create_element_text_flow_dataset("sumFormula", str)
    """Chemical sum formula of the substance."""

    generalComments = create_attribute_list_flow_dataset("common:generalComment", str)
    """Free text for general information about the Flow data set. It may contain
    information about e.g. the use of the substance, good, service or process in
    a specific technology or industry-context, information sources used, data
    selection principles etc."""

    @property
    def name(self) -> "Name":
        """General descriptive and specifying name of the flow."""
        return get_element(self, "name")

    @property
    def classificationInformation(self) -> "FlowCategoryInformation":
        """Hierarchical classification of the good, service, or process.
        (Note: This entry is NOT required for the identification of a Process. It should
        nevertheless be avoided to use identical names for Processes in the same
        category."""
        return get_element(self, "classificationInformation")


class QuantitativeReference(etree.ElementBase):
    """This section names the type of quantitative reference used for
    this Flow data set, which is always one of the Flow's Flow
    properties (see section "Flow properties")."""

    referenceToReferenceFlowProperty = create_element_text_flow_dataset(
        "referenceToReferenceFlowProperty", int
    )
    """One of the Flow's Flow properties, which is set as the default
    flow property in which the flow measured. (Data set internal
    reference to one of the flow properties in section "Quantitative
    flow properties".)"""


class Geography(etree.ElementBase):
    """Provides information about the geographical representativeness
    of the data set."""

    locationOfSupply = create_attribute_list_flow_dataset("locationOfSupply", str)
    """Only used for product or waste flows and only required for
    matrix-type databases. Location or region of supply / consumption
    or production of the good or service, or operation of the process.
    Note 1: Entry can be of type "two-letter ISO 3166 country code"
    for countries, "seven-letter regional codes" for regions or continents,
    or "market areas and market organisations", as predefined for the ILCD.
    Also a name for e.g. a specific plant etc. can be given here (e.g. "FR,
    Lyon, XY Company, Z Site"; user defined). Note 2: The fact whether the
    entry refers to production or to consumption / supply has to be stated
    in the name-field "Mix and location types" e.g. as "Production mix".]"""


class Technology(etree.ElementBase):
    """Provides information about the technological representativeness
    of the flow in case it is a product or waste flow."""

    technologicalApplicability = create_attribute_list_flow_dataset(
        "technologicalApplicability", str
    )
    """Description of the intended / possible applications of the good
    or service, or waste. E.g. for which type of products the material,
    represented by this data set, is used. Examples: "This high purity
    chemical is used for analytical laboratories only." or "This
    technical quality bulk chemical is used for large scale synthesis
    in chemical industry.". Or: "This type of biowaste is typically
    composted or biodigested as the water content is too high for
    efficient combustion"."""

    @property
    def referenceToTechnicalSpecification(self) -> List["GlobalReference"]:
        """ "Source data set(s)" of the product's or waste's technical
        specification, waste data sheet, safety data sheet, etc."""
        return get_element_list(self, "referenceToTechnicalSpecification")


class LCIMethod(etree.ElementBase):
    """LCI methodological modelling aspects."""

    typeOfDataSet = create_element_text_flow_dataset("typeOfDataSet", str)
    """Names the basic type of the flow."""


class DataEntryBy(DataEntryByGroup1, DataEntryByGroup2):
    """Staff or entity, that documented the generated data set, entering
    the information into the database; plus administrative information
    linked to the data entry activity.."""


class PublicationAndOwnership(PublicationAndOwnershipGroup1):
    """Information related to publication and version management of the
    data set including copyright and access restrictions."""

    @property
    def referenceToOwnershipOfDataSet(self) -> "GlobalReference":
        """ "Contact data set" of the person or entity who owns this data set.
        (Note: this is not necessarily the publisher of the data set.)"""
        return get_element(self, "common:referenceToOwnershipOfDataSet")


class FlowProperty(etree.ElementBase):
    """One flow property."""

    dataSetInternalID = create_attribute_flow_dataset("dataSetInternalID", int)
    """Automated entry: internal ID, used in the "Quantitative reference"
    section to identify the reference flow property."""

    meanValue = create_element_text_flow_dataset("meanValue", float)
    """Value for the flow expressed in this flow property in relationship
    to the the value of the flow expressed in its reference flow property
    (see field "Reference to reference flow property" in the "Quantitative
    reference" section). [Notes and examples: If the product flow "Diesel"
    is expressed by default in "Mass" (= reference flow property) and "kg"
    (= corresponding reference unit), the value that would be stated here
    for an additional flow property e.g. "Net calorific value" would be
    "42.5", as this flow property has the reference unit "MJ" and Diesel
    has a net calorific value of 42.5 MJ per 1 kg. It is recommended to
    report only significant digits of the value.]"""

    minimumValue = create_element_text_flow_dataset("minimumValue", float)
    """Minimum value of this flow property in case uncertainty distribution
    is uniform or triangular."""

    maximumValue = create_element_text_flow_dataset("maximumValue", float)
    """Maximum value of this flow property in case uncertainty distribution
    is uniform or triangular."""

    uncertaintyDistributionType = create_element_text_flow_dataset(
        "uncertaintyDistributionType", str
    )
    """Defines the kind of uncertainty distribution that is valid for this
    particular object or parameter."""

    relativeStandardDeviation95In = create_element_text_flow_dataset(
        "relativeStandardDeviation95In", float
    )
    """The resulting overall uncertainty of the calculated variable value
    considering uncertainty of measurements, modelling, appropriateness etc.
    [Notes: For log-normal distribution the square of the geometric standard
    deviation (SDg^2) is stated. Mean value times SDg^2 equals the 97.5% value
    (= Maximum value), Mean value divided by SDg^2 equals the 2.5% value
    (= Minimum value). For normal distribution the doubled standard deviation
    value (2*SD) is entered. Mean value plus 2*SD equals 97.5% value
    (= Maximum value), Mean value minus 2*SD equals 2.5% value (= Minimum value).
    This data field remains empty when uniform or triangular uncertainty
    distribution is applied.]"""

    dataDerivationTypeStatus = create_element_text_flow_dataset(
        "dataDerivationTypeStatus", str
    )
    """Identifies the way by which the Flow property value was derived (e.g.
    measured, estimated etc.), respectively the status and relevancy of missing
    data."""

    generalComment = create_attribute_list_flow_dataset("generalComment", str)
    """General comment on each single flow property (if necessary) referring
    to specifc data sources used, or for workflow purposes about status of
    "finalisation" of an entry etc."""

    @property
    def referenceToFlowPropertyDataSet(self) -> "GlobalReference":
        """ "Flow property data set."""
        return get_element(self, "referenceToFlowPropertyDataSet")


class Name(etree.ElementBase):
    """General descriptive and specifying name of the flow."""

    baseName = create_attribute_list_flow_dataset("baseName", str)
    """General descriptive name of the elementary, waste or product flow,
    for the latter including it's level of processing."""

    treatmentStandardsRoutes = create_attribute_list_flow_dataset(
        "treatmentStandardsRoutes", str
    )
    """Specifying information on the (product or waste) flow in technical
    term(s): treatment received, standard fulfilled, product quality, use
    information, production route name, educt name, primary / secondary etc.
    Separated by commata.."""

    mixAndLocationTypes = create_attribute_list_flow_dataset("mixAndLocationTypes", str)
    """Specifying information on the good, service, or process whether
    being a production mix or consumption mix, location type of
    availability (such as e.g. "to consumer" or "at plant"). Separated
    by commata."""

    flowProperties = create_attribute_list_flow_dataset("flowProperties", str)
    """Further, quantitative specifying information on the (product or
    waste) flow, in technical term(s): qualifying constituent(s)-content
    and / or energy-content per unit etc. as appropriate. Separated by
    commata. (Note: non-qualifying flow properties, CAS No, Synonyms,
    Chemical formulas etc. are documented exclusively in the respective
    fields.)"""
