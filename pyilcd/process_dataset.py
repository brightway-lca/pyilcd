"""Custom ILCD Python classes for ProcessDataSet of ILCD schema."""

from typing import List

from lxml import etree
from lxmlh import get_element, get_element_list

from .common import (
    CommissionerAndGoal,
    ComplianceGroup,
    DataEntryByGroup1,
    DataEntryByGroup2,
    FlowCategoryInformation,
    GlobalReference,
    PublicationAndOwnershipGroup1,
    PublicationAndOwnershipGroup2,
    PublicationAndOwnershipGroup3,
    ValidationGroup1,
    ValidationGroup3,
)
from .helpers import (
    create_attribute_list_process_dataset,
    create_attribute_process_dataset,
    create_element_text_process_dataset,
)


class ProcessDataSet(etree.ElementBase):
    """Data set for unit processes, partly terminated systems, and LCI results.
    May contain LCIA results as well."""

    version = create_attribute_process_dataset("version", str)
    """Indicates, which version of the ILCD format is used."""

    locations = create_attribute_process_dataset("locations", str)
    """Contains reference to used location table for this dataset."""

    metaDataOnly = create_attribute_process_dataset("metaDataOnly", bool)
    """Indicates whether this data set contains only meta data (no exchanges
    section)."""

    @property
    def processInformation(self) -> "ProcessInformation":
        """Corresponds to the ISO/TS 14048 section "Process description". It
        comprises the following six sub-sections: 1) "Data set information" for
        data set identification and overarching information items, 2) "Quantitative
        reference", 3) "Time", 4) "Geography", 5) "Technology" and 6) "Mathematical
        relations"."""
        return get_element(self, "processInformation")

    @property
    def modellingAndValidation(self) -> "ModellingAndValidation":
        """Covers the five sub-sections 1) LCI method and allocation, 2) Data
        sources, treatment and representativeness, 3) Completeness, 4) Validation,
        and 5) Compliance. (Section refers to LCI modelling and data treatment
        aspects etc., NOT the modeling of e.g. the input/output-relationships of a
        parameterised data set.)"""
        return get_element(self, "modellingAndValidation")

    @property
    def administrativeInformation(self) -> "AdministrativeInformation":
        """Information on data set management and administration."""
        return get_element(self, "administrativeInformation")

    @property
    def exchanges(self) -> "Exchanges":
        """Input/Output list of exchanges with the quantitative inventory data,
        as well as pre-calculated LCIA results."""
        return get_element(self, "exchanges")

    @property
    def lciaResults(self) -> "LCIAResults":
        """List with the pre-calculated LCIA results of the Input/Output list
        of this data set. May contain also inventory-type results such as primary
        energy consumption etc."""
        return get_element(self, "LCIAResults")


class ProcessInformation(etree.ElementBase):
    """Corresponds to the ISO/TS 14048 section "Process description". It
    comprises the following six sub-sections: 1) "Data set information" for
    data set identification and overarching information items, 2) "Quantitative
    reference", 3) "Time", 4) "Geography", 5) "Technology" and 6) "Mathematical
    relations"."""

    @property
    def dataSetInformation(self) -> "DataSetInformation":
        """General data set information. Section covers all single fields in
        the ISO/TS 14048 "Process description", which are not part of the other
        sub-sections. In ISO/TS 14048 no own sub-section is foreseen for these
        entries."""
        return get_element(self, "dataSetInformation")

    @property
    def quantitativeReference(self) -> "QuantitativeReference":
        """This section names the quantitative reference used for this data
        set, i.e. the reference to which the inputs and outputs quantiatively
        relate."""
        return get_element(self, "quantitativeReference")

    @property
    def time(self) -> "Time":
        """Provides information about the time representativeness of the dataset."""
        return get_element(self, "time")

    @property
    def geography(self) -> "Geography":
        """Provides information about the geographical representativeness of
        the dataset."""
        return get_element(self, "geography")

    @property
    def technology(self) -> "Technology":
        """Provides information about the technological representativeness of
        the data set."""
        return get_element(self, "technology")

    @property
    def mathematicalRelations(self) -> "MathematicalRelations":
        """A set of formulas that allows to model the amount of single
        exchanges in the input and output list in dependency of each other and/or
        in dependency of parameters. Used to provide a process model ("parameterized
        process") for calculation of inventories in dependency of user settings of e.g.
        yield, efficiency of abatement measures, processing of different educts, etc."""
        return get_element(self, "mathematicalRelations")


class ModellingAndValidation(etree.ElementBase):
    """Covers the five sub-sections 1) LCI method and allocation, 2) Data
    sources, treatment and representativeness, 3) Completeness, 4) Validation,
    and 5) Compliance. (Section refers to LCI modelling and data treatment aspects
    etc., NOT the modeling of e.g. the input/output-relationships of a parameterised
    data set.)"""

    @property
    def lciMethodAndAllocation(self) -> "LCIMethodAndAllocation":
        """LCI methodological modelling aspects including allocation /
        substitution information."""
        return get_element(self, "LCIMethodAndAllocation")

    @property
    def dataSourcesTreatmentAndRepresentativeness(
        self,
    ) -> "DataSourcesTreatmentAndRepresentativeness":
        """Data selection, completeness, and treatment principles and
        procedures, data sources and market coverage information."""
        return get_element(self, "dataSourcesTreatmentAndRepresentativeness")

    @property
    def completeness(self) -> "Completeness":
        """Data completeness aspects for this specific data set."""
        return get_element(self, "completeness")

    @property
    def validation(self) -> "Validation":
        """Review / validation information on data set."""
        return get_element(self, "validation")

    @property
    def complianceDeclarations(self) -> "ComplianceDeclarations":
        """Statements on compliance of several data set aspects with
        compliance requirements as defined by the referenced compliance system
        (e.g. an EPD scheme, handbook of a national or international data network
        such as the ILCD, etc.)."""
        return get_element(self, "complianceDeclarations")


class AdministrativeInformation(etree.ElementBase):
    """Information on data set management and administration."""

    @property
    def commissionerAndGoal(self) -> "CommissionerAndGoal":
        """Basic information about goal and scope of the data set."""
        return get_element(self, "common:commissionerAndGoal")

    @property
    def dataGenerator(self) -> "DataGenerator":
        """Expert(s), that compiled and modelled the data set as well as
        internal administrative information linked to the data generation
        activity."""
        return get_element(self, "dataGenerator")

    @property
    def dataEntryBy(self) -> "DataEntryBy":
        """Staff or entity, that documented the generated data set, entering
        the information into the database; plus administrative information
        linked to the data entry activity."""
        return get_element(self, "dataEntryBy")

    @property
    def publicationAndOwnership(self) -> "PublicationAndOwnership":
        """Information related to publication and version management of the
        data set including copyright and access restrictions."""
        return get_element(self, "publicationAndOwnership")


class Exchanges(etree.ElementBase):
    """Input/Output list of exchanges with the quantitative inventory data,
    as well as pre-calculated LCIA results."""

    @property
    def exchanges(self) -> List["Exchange"]:
        """Input/Output list of exchanges with the quantitative inventory data
        as well as pre-calculated LCIA results."""
        return get_element_list(self, "exchange")


class LCIAResults(etree.ElementBase):
    """List with the pre-calculated LCIA results of the Input/Output list
    of this data set. May contain also inventory-type results such as primary
    energy consumption etc."""

    @property
    def lciaResults(self) -> List["LCIAResult"]:
        """Single LCIA result"""
        return get_element_list(self, "LCIAResult")


class DataSetInformation(etree.ElementBase):
    """General data set information. Section covers all single fields in
    the ISO/TS 14048 "Process description", which are not part of the other
    sub-sections. In ISO/TS 14048 no own sub-section is foreseen for these entries."""

    commonUUID = create_attribute_process_dataset("common:UUID", str)
    """Automatically generated Universally Unique Identifier of this data
    set. Together with the "Data set version", the UUID uniquely identifies each data
    set."""

    identifierOfSubDataSet = create_attribute_process_dataset(
        "identifierOfSubDataSet", str
    )
    """Identifier of a sub-set of a complete process data set. This can be
    the life cycle stage that a data set covers (such as used in EPDs for modular LCI
    reporting, with the inventory split up into "resource extraction stage",
    "production stage", "use stage" and "end-of-life stage"). Or it can be e.g. the
    type of emission source from which the elementary flows of the Inputs and Outputs
    stems (e.g. "incineration-related", "transport-related", etc.). Together with the
    field "Complementing processes" this allows to split up a process data set into a
    number of clearly identified data sets, each carrying only a part of the inventory
    and that together represent the complete inventory. Care has to be taken when
    naming the reference flow, to avoid misinterpretation.."""

    synonyms = create_attribute_list_process_dataset("common:synonyms", str)
    """Synonyms / alternative names / brands of the good, service, or
    process. Separated by semicolon."""

    generalComments = create_attribute_list_process_dataset(
        "common:generalComment", str
    )
    """General information about the data set, including e.g. general
    (internal, not reviewed) quality statements as well as information sources used.
    (Note: Please also check the more specific fields e.g. on "Intended application",
    "Advice on data set use" and the fields in the "Modelling and validation" section
    to avoid overlapping entries.)"""

    @property
    def name(self) -> "Name":
        """General descriptive and specifying name of the process."""
        return get_element(self, "name")

    @property
    def complementingProcesses(self) -> "ComplementingProcesses":
        """Process data set(s)" that complement this partial / sub-set of a
        complete process data set, if any and available as separate data set(s). The
        identifying name of this sub-set should be stated in the field "Identifier of
        sub-data set"."""
        return get_element(self, "complementingProcesses")

    @property
    def classificationInformation(self) -> "FlowCategoryInformation":
        """Hierarchical classification of the good, service, or process.
        (Note: This entry is NOT required for the identification of a Process. It should
        nevertheless be avoided to use identical names for Processes in the same
        category."""
        return get_element(self, "classificationInformation")

    @property
    def referenceToExternalDocumentation(self) -> "GlobalReference":
        """ "Source data set(s)" of detailed LCA study on the process or
        product represented by this data set, as well as documents / files with
        overarching documentative information on technology, geographical and / or time
        aspects etc. (e.g. basic engineering studies, process simulation results,
        patents, plant documentation, model behind the parameterisation of the
        "Mathematical model" section, etc.) (Note: can indirectly reference to
        digital file.)"""
        return get_element(self, "referenceToExternalDocumentation")


class QuantitativeReference(etree.ElementBase):
    """This section names the quantitative reference used for this data
    set, i.e. the reference to which the inputs and outputs quantiatively relate."""

    referenceToReferenceFlow = create_attribute_list_process_dataset(
        "referenceToReferenceFlow", int
    )
    """One or more of the Inputs or Outputs in case "Type of quantitative
    reference" is of type "Reference flow(s)". (Data set internal reference.)"""

    functionalUnitOrOther = create_attribute_list_process_dataset(
        "functionalUnitOrOther", str
    )
    """Quantity, name, property/quality, and measurement unit of the
    Functional unit, Production period, or Other parameter, in case "Type of
    quantitative reference" is of one of these types. [Note: One or more functional
    units can also be given in addition to a reference flow.]"""

    type = create_attribute_process_dataset("type", str)
    """Type of quantitative reference of this data set."""


class Time(etree.ElementBase):
    """Provides information about the time representativeness of the dataset."""

    referenceYear = create_element_text_process_dataset("referenceYear", int)
    """Start year of the time period for which the data set is valid (until year
    of "Data set valid until:"). For data sets that combine data from different
    years, the most representative year is given regarding the overall environmental
    impact. In that case, the reference year is derived by expert judgement."""

    dataSetValidUntil = create_element_text_process_dataset("dataSetValidUntil", int)
    """End year of the time period for which the data set is still valid /
    sufficiently representative. This date also determines when a data set revision /
    remodelling is required or recommended due to expected relevant changes in
    environmentally or technically relevant inventory values, including in the
    background system."""

    timeRepresentativenessDescription = create_attribute_list_process_dataset(
        "timeRepresentativenessDescription", str
    )
    """Description of the valid time span of the data set including information on
    limited usability within sub-time spans (e.g. summer/winter)."""


class Geography(etree.ElementBase):
    """Provides information about the geographical representativeness of the dataset."""

    @property
    def locationOfOperationSupplyOrProduction(
        self,
    ) -> "LocationOfOperationSupplyOrProduction":
        """Location, country or region the data set represents. [Note 1: This
        field does not refer to e.g. the country in which a specific site is located
        that is represented by this data set but to the actually represented country,
        region, or site. Note 2: Entry can be of type "two-letter ISO 3166 country
        code" for countries, "seven-letter regional codes" for regions or continents,
        or "market areas and market organisations", as predefined for the ILCD. Also
        a name for e.g. a specific plant etc. can be given here (e.g. "FR, Lyon, XY
        Company, Z Site"; user defined). Note 3: The fact whether the entry refers to
        production or to consumption / supply has to be stated in the name-field "Mix
        and location types" e.g. as "Production mix".]"""
        return get_element(self, "locationOfOperationSupplyOrProduction")

    @property
    def subLocationOfOperationSupplyOrProduction(
        self,
    ) -> List["SubLocationOfOperationSupplyOrProduction"]:
        """One or more geographical sub-unit(s) of the stated "Location". Such
        sub-units can be e.g. the sampling sites of a company-average data set, the
        countries of a region-average data set, or specific sites in a country-average
        data set. [Note: For single site data sets this field is empty and the site is
        named in the "Location" field.]"""
        return get_element_list(self, "subLocationOfOperationSupplyOrProduction")


class Technology(etree.ElementBase):
    """Provides information about the technological representativeness of the
    dataset."""

    technologyDescriptionAndIncludedProcesses = create_attribute_list_process_dataset(
        "technologyDescriptionAndIncludedProcesses", str
    )
    """Description of the technological characteristics including
    operating conditions of the process or product system. For the latter this
    includes the relevant upstream and downstream processes included in the data set.
    Professional terminology should be used."""

    technologicalApplicability = create_attribute_list_process_dataset(
        "technologicalApplicability", str
    )
    """Description of the intended / possible applications of the good,
    service, or process. E.g. for which type of products the material, represented by
    this data set, is used. Examples: "This high purity chemical is used for
    analytical laboratories only." or "This technical quality bulk chemical is used
    for large scale synthesis in chemical industry.". Or: "This truck is used only for
    long-distance transport of liquid bulk chemicals"."""

    @property
    def referenceToIncludedProcesses(self) -> List["GlobalReference"]:
        """ "Process data set(s)" included in this data set, if any and
        available as separate data set(s)."""
        return get_element_list(self, "referenceToIncludedProcesses")

    @property
    def referenceToTechnologyPictogramme(self) -> "GlobalReference":
        """ "Source data set" of the pictogramme of the good, service,
        technogy, plant etc. represented by this data set. For use in graphical user
        interfaces of LCA software."""
        return get_element(self, "referenceToTechnologyPictogramme")

    @property
    def referenceToTechnologyFlowDiagrammOrPicture(self) -> List["GlobalReference"]:
        """ "Source data set" of the flow diagramm(s) and/or photo(s) of the
        good, service, technology, plant etc represented by this data set. For clearer
        illustration and documentation of data set."""
        return get_element_list(self, "referenceToTechnologyFlowDiagrammOrPicture")


class MathematicalRelations(etree.ElementBase):
    """A set of formulas that allows to model the amount of single
    exchanges in the input and output list in dependency of each other and/or
    in dependency of parameters. Used to provide a process model ("parameterized
    process") for calculation of inventories in dependency of user settings of e.g.
    yield, efficiency of abatement measures, processing of different educts, etc."""

    modelDescription = create_attribute_list_process_dataset("modelDescription", str)
    """Description of the model(s) represented in this section of
    mathematical relations. Can cover information on restrictions, model strenghts
    and weaknesses, etc. (Note: Also see information provided on the level of the
    individual formula in field "Comment" and in the general process description in
    the fields in section "Technology".)"""

    @property
    def variableParameter(self) -> List["VariableParameter"]:
        """Name of variable or parameter used as scaling factors for the "Mean
        amount" of individual inputs or outputs of the data set."""
        return get_element_list(self, "variableParameter")


class LCIMethodAndAllocation(etree.ElementBase):
    """LCI methodological modelling aspects including allocation /
    substitution information."""

    typeOfDataSet = create_element_text_process_dataset("typeOfDataSet", str)
    """Type of the data set regarding systematic inclusion/exclusion of
    upstream or downstream processes, transparency and internal (hidden)
    multi-functionality, and the completeness of modelling."""

    LCIMethodPrinciple = create_element_text_process_dataset("LCIMethodPrinciple", str)
    """LCI method principle followed in the product system modelling, i.e.
    regarding using average data (= attributional = non-marginal) or modelling effects
    in a change-oriented way (= consequential = marginal)."""

    deviationsFromLCIMethodPrinciple = create_attribute_list_process_dataset(
        "deviationsFromLCIMethodPrinciple", str
    )
    """Short description of any deviations from the general "LCI method
    principles" and additional explanations. Refers especially to specific
    processes/cases where the stated "attributional" or "consequential" approach was
    not applied. Or where deviations were made from any specific rules for applying
    the "Consequential with attributional components" approach. A reference to the
    "Intended application" of the data collection can be made here, too. Allocated
    co-products may be reported here as well. In case of no (quantitatively relevant)
    deviations from the LCI method principle, "none" should be stated."""

    LCIMethodApproaches = create_attribute_list_process_dataset(
        "LCIMethodApproaches", str
    )
    """Names briefly the specific approach(es) used in LCI modeling, e.g.
    allocation, substitution etc. In case of LCI results and Partly terminated system
    data sets this also covers those applied in the included background system."""

    deviationsFromLCIMethodApproaches = create_attribute_list_process_dataset(
        "deviationsFromLCIMethodApproaches", str
    )
    """Description of relevant deviations from the applied approaches as
    well as of the relevant specific approaches that were applied, including in an
    possibly included background system. Further explanations and details of the
    allocation, substitution and other consequential approaches applied for relevant
    processes, e.g. how the marginal substitute was identified, year and region of
    which market prices were used in market allocation, i.e. method, procedure,
    data/information details. In case of no (result relevant) deviations from the
    before stated LCI method approaches, and in case of no need for further
    explanations, "none" is entered."""

    modellingConstants = create_attribute_list_process_dataset(
        "modellingConstants", str
    )
    """Short identification and description of constants applied in LCI
    modelling other than allocation / substitution, e.g. systematic setting of
    recycling quota, use of gross or net calorific value, etc."""

    deviationsFromModellingConstants = create_attribute_list_process_dataset(
        "deviationsFromModellingConstants", str
    )
    """Short description of data set specific deviations from the
    "Modelling constants" if any, including in the possibly included background
    system."""

    @property
    def referenceToLCAMethodDetails(self) -> List["GlobalReference"]:
        """ "Source data set"(s) where the generally used LCA methods including
        the LCI method principles and specific approaches, the modelling constants
        details, as well as any other applied methodological conventions are
        described."""
        return get_element_list(self, "referenceToLCAMethodDetails")


class DataSourcesTreatmentAndRepresentativeness(etree.ElementBase):
    """Data selection, completeness, and treatment principles and
    procedures, data sources and market coverage information."""

    dataCutOffAndCompletenessPrinciples = create_attribute_list_process_dataset(
        "dataCutOffAndCompletenessPrinciples", str
    )
    """Principles applied in data collection regarding completeness of
    (also intermediate) product and waste flows and of elementary flows.
    Examples are: cut-off rules, systematic exclusion of infrastructure,
    services or auxiliaries, etc. systematic exclusion of air in incineration
    processes, coling water, etc."""

    deviationsFromCutOffAndCompletenessPrinciples = (
        create_attribute_list_process_dataset(
            "deviationsFromCutOffAndCompletenessPrinciples", str
        )
    )
    """Short description of any deviations from the "Data completeness
    principles". In case of no (result relevant) deviations, "none" is entered."""

    dataSelectionAndCombinationPrinciples = create_attribute_list_process_dataset(
        "dataSelectionAndCombinationPrinciples", str
    )
    """Principles applied in data selection and in combination of data
    from different sources. Includes brief discussion of consistency of data sources
    regarding data itself, modelling, appropriateness. In case of averaging:
    Principles and data selection applied in horizontal and / or vertical averaging."""

    deviationsFromSelectionAndCombinationPrinciples = (
        create_attribute_list_process_dataset(
            "deviationsFromSelectionAndCombinationPrinciples", str
        )
    )
    """Short description of any deviations from the "Data selection and
    combination principles". In case of no (result relevant) deviations, "none" is
    entered."""

    dataTreatmentAndExtrapolationsPrinciples = create_attribute_list_process_dataset(
        "dataTreatmentAndExtrapolationsPrinciples", str
    )
    """Principles applied regarding methods, sources, and assumptions done
    in data adjustment including extrapolations of data from another time period,
    another geographical area, or another technology."""

    deviationsFromTreatmentAndExtrapolationPrinciples = (
        create_attribute_list_process_dataset(
            "deviationsFromTreatmentAndExtrapolationPrinciples", str
        )
    )
    """Short description of any deviations from the " Data treatment and
    extrapolations principles". In case of no (result relevant) deviations, "none" is
    entered. (Note: If data representative for one "Location" is used for another
    "Location", its original representativity can be indicated here; see field
    "Percentage supply or production covered".)"""

    percentageSupplyOrProductionCovered = create_element_text_process_dataset(
        "percentageSupplyOrProductionCovered", float
    )
    """Percentage of the overall supply, consumption, or production of the
    specific good, service, or technology represented by this data set, in the
    region/market of the stated "Location". For multi-functional processes the market
    share of the specific technology is stated. If data that is representative for a
    process operated in one "Location" is used for another "Location", the entry is
    '0'. The representativity for the original "Location" is documented in the field
    "Deviation from data treatment and extrapolation principles, explanations"."""

    annualSupplyOrProductionVolume = create_attribute_list_process_dataset(
        "annualSupplyOrProductionVolume", str
    )
    """Supply / consumption or production volume of the specific good,
    service, or technology in the region/market of the stated "Location". The market
    volume is given in absolute numbers per year, in common units, for the stated
    "Reference year". For multi-fucntional processes the data should be given for all
    co-functions (good and services)."""

    samplingProcedure = create_attribute_list_process_dataset("samplingProcedure", str)
    """Sampling procedure used for quantifying the amounts of Inputs and
    Outputs. Possible problems in combining different sampling procedures should be
    mentioned."""

    dataCollectionPeriod = create_attribute_list_process_dataset(
        "dataCollectionPeriod", str
    )
    """Date(s) or time period(s) when the data was collected. Note that
    this does NOT refer to e.g. the publication dates of papers or books from which
    the data may stem, but to the original data collection period."""

    uncertaintyAdjustments = create_attribute_list_process_dataset(
        "uncertaintyAdjustments", str
    )
    """Description of methods, sources, and assumptions made in
    uncertainty adjustment. [Note: For data sets where the additional uncertainty due
    to lacking representativeness has been included in the quantified uncertainty
    values, this field also reports the original representativeness, the additional
    uncertainty, and the procedure by which the overall uncertainty was assessed or
    calculated.]"""

    useAdviceForDataSet = create_attribute_list_process_dataset(
        "useAdviceForDataSet", str
    )
    """Specific methodological advice for data set users that requires
    attention. E.g. on inclusion/exclusion of recycling e.g. in material data sets,
    specific use phase behavior to be modelled, and other methodological advices. See
    also field "Technological applicability"."""

    @property
    def referenceToDataHandlingPrinciples(self) -> List["GlobalReference"]:
        """ "Source data set"(s) of the source(s) in which the data
        completeness, selection, combination, treatment, and
        extrapolations principles' details are described"""
        return get_element_list(self, "referenceToDataHandlingPrinciples")

    @property
    def referenceToDataSource(self) -> List["GlobalReference"]:
        """ "Source data set"(s) of the source(s) used for deriving/compiling
        the inventory of this data set e.g. questionnaires, monographies,
        plant operation protocols, etc. For LCI results and Partly
        terminated systems the sources for relevant background system
        data are to be given, too. For parameterised data sets the sources
        used for the parameterisation / mathematical relations in the section
        "Mathematical model" are referenced here as well. [Note: If the data
        set stems from another database or data set publication and is only
        re-published: identify the origin of a converted data set in
        "Converted original data set from:" field in section "Data entry by"
        and its unchanged re-publication in "Unchanged re-publication of:"
        in the section "Publication and ownership". The data sources used
        to model a converted or re-published data set are nevertheless to
        be given here in this field, for transparency reasons.]"""
        return get_element_list(self, "referenceToDataSource")


class Completeness(etree.ElementBase):
    """Data completeness aspects for this specific data set."""

    completenessProductModel = create_element_text_process_dataset(
        "completenessProductModel", str
    )
    """Completeness of coverage of relevant product, waste and elementary
    flows. [Notes: For LCI results and Partly terminated systems this means throughout
    the underlying product system model. "Relevant" refers to the overall
    environmental relevance, i.e. for unit processes including the upstream and
    downstream burdens of product and waste flows.]"""

    completenessOtherProblemField = create_attribute_list_process_dataset(
        "completenessOtherProblemField", str
    )
    """Completeness of coverage of elementary flows that contribute to
    other problem fields that are named here as free text, preferably
    using the same terminology as for the specified environmental problems."""

    @property
    def completenessElementaryFlows(self) -> List["CompletenessElementaryFlows"]:
        """ "Completeness of the elementary flows in the Inputs and Outputs
        section of this data set from impact perspective, regarding addressing the
        individual mid-point problem field / impact category given. The completeness
        refers to the state-of-the-art of scientific knowledge whether or not an
        individual elementary flow contributes to the respective mid-point topic in a
        relevant way, which is e.g. the basis for the ILCD reference elementary flows.
        [Note: The "Completeness" statement does not automatically mean that related
        LCIA methods exist or reference the elementary flows of this data set. Hence
        for direct applicability of existing LCIA methods, check the field "Supported
        LCIA method data sets".]"""
        return get_element_list(self, "completenessElementaryFlows")

    @property
    def referenceToSupportedImpactAssessmentMethods(self) -> "GlobalReference":
        """ "LCIA methods data sets" that can be applied to the elementary
        flows in the Inputs and Outputs section, i.e. ALL these flows are referenced by
        the respective LCIA method data set (if they are of environmental relevance and
        a characterisation factor is defined for the respective flow). [Note:
        Applicability is not given if the inventoty contains some elementary flows with
        the same meaning as referenced in the LCIA method data set but in a different
        nomenclature (and hence carry no characterisation factor), or if the flows are
        sum indicators or flow groups that are addressed differently in the LCIA method
        data set.]"""
        return get_element(self, "referenceToSupportedImpactAssessmentMethods")


class Validation(etree.ElementBase):
    """Review / validation information on data set."""

    @property
    def reviews(self) -> List["Review"]:
        """Review information on data set."""
        return get_element_list(self, "review")


class ComplianceDeclarations(etree.ElementBase):
    """Statements on compliance of several data set aspects with
    compliance requirements as defined by the referenced compliance system (e.g. an
    EPD scheme, handbook of a national or international data network such as the ILCD,
    etc.)."""

    @property
    def compliances(self) -> List["Compliance"]:
        """One compliance declaration"""
        return get_element_list(self, "compliance")


class DataGenerator(etree.ElementBase):
    """Expert(s), that compiled and modelled the data set as well as
    internal administrative information linked to the data generation activity."""

    @property
    def referenceToPersonOrEntityGeneratingTheDataSet(self) -> List["GlobalReference"]:
        """ "Contact data set" of the person(s), working group(s),
        organisation(s) or database network, that generated the
        data set, i.e. being responsible for its correctness regarding
        methods, inventory, and documentative information."""
        return get_element_list(
            self, "common:referenceToPersonOrEntityGeneratingTheDataSet"
        )


class DataEntryBy(DataEntryByGroup1, DataEntryByGroup2):
    """Staff or entity, that documented the generated data set, entering
    the information into the database; plus administrative information linked to the
    data entry activity."""

    @property
    def referenceToConvertedOriginalDataSetFrom(self) -> "GlobalReference":
        """ "Source data set" of the database or data set publication from
        which this data set has been obtained by conversion. This can cover e.g.
        conversion to a different format, applying a different nomenclature, mapping of
        flow names, conversion of units, etc. This may however not have changed or
        re-modeled the Inputs and Outputs, i.e. obtaining the same LCIA results. This
        entry is required for converted data sets stemming originally from other LCA
        databases (e.g. when re-publishing data from IISI, ILCD etc. databases). [Note:
        Identically re-published data sets are identied in the field "Unchanged
        re-publication of:" in the section "Publication and Ownership".]"""
        return get_element(self, "common:referenceToConvertedOriginalDataSetFrom")

    @property
    def referenceToDataSetUseApproval(self) -> List["GlobalReference"]:
        """ "Source data set": Names exclusively the producer or operator of
        the good, service or technology represented by this data set, which officially
        has approved this data set in all its parts. In case of nationally or
        internationally averaged data sets, this will be the respective business
        association. If no official approval has been given, the entry "No official
        approval by producer or operator" is to be entered and the reference will
        point to an empty "Contact data set". [Notes: The producer or operator may only
        be named here, if a written approval of this data set was given. A recognition
        of this data set by any other organisation then the producer/operator of the
        good, service, or process is not to be stated here, but as a "review" in the
        validation section.]"""
        return get_element_list(self, "common:referenceToDataSetUseApproval")


class PublicationAndOwnership(
    PublicationAndOwnershipGroup1,
    PublicationAndOwnershipGroup2,
    PublicationAndOwnershipGroup3,
):
    """Information related to publication and version management of the
    data set including copyright and access restrictions."""

    registrationNumber = create_element_text_process_dataset(
        "common:registrationNumber", str
    )
    """A unique identifying number for this data set issued by the
    registration authority."""

    @property
    def referenceToRegistrationAuthority(self) -> "GlobalReference":
        """ "Contact data set" of the authority that has registered this
        data set."""
        return get_element(self, "common:referenceToRegistrationAuthority")

    @property
    def referenceToOwnershipOfDataSet(self) -> "GlobalReference":
        """ ""Contact data set" of the person or entity who owns this data set.
        (Note: this is not necessarily the publisher of the data set.)"""
        return get_element(self, "common:referenceToOwnershipOfDataSet")


class Exchange(etree.ElementBase):
    """Input/Output list of exchanges with the quantitative inventory data
    as well as pre-calculated LCIA results."""

    dataSetInternalID = create_attribute_process_dataset("dataSetInternalID", int)
    """Automated entry: internal ID, used in the "Quantitative reference"
    section to identify the "Reference flow(s)" in case the quantitative
    reference of this Process data set is of this type."""

    location = create_element_text_process_dataset("location", str)
    """Location where exchange of elementary flow occurs. Used only for
    those LCIA methods, that make use of this information. This information refers to
    the entry within the same field in the "Inputs and Outpts" section of the "Process
    or LCI result data set"."""

    functionType = create_element_text_process_dataset("functionType", str)
    """"""

    exchangeDirection = create_element_text_process_dataset("exchangeDirection", str)
    """Direction of Input or Output flow."""

    referenceToVariable = create_element_text_process_dataset(
        "referenceToVariable", str
    )
    """Data set internal reference to a variable or parameter name as
    defined in the section "Mathematical model". The value of this variable or
    parameter acts as linear multiplier to the value given in the field "Mean amount"
    to yield the "Resulting amount", which is the final value in the inventory."""

    meanAmount = create_element_text_process_dataset("meanAmount", float)
    """Mean amount of the Input or Output. Only significant digits of the
    amount should be stated."""

    resultingAmount = create_element_text_process_dataset("resultingAmount", float)
    """Final value to be used for calculation of the LCI results and in
    the product system: It is calculated as the product of the "Mean amount" value
    times the value of the "Variable". In case that no "Variable" entry is given, the
    "Resulting amount" is identical to the "Mean amount", i.e. a factor "1" is
    applied."""

    minimumAmount = create_element_text_process_dataset("minimumAmount", float)
    """Minimum amount of the Input or Output in case the uncertainty
    distribution is uniform or triangular. In case of calculated LCI results and for
    the aggregated flows in Partly terminated system data sets, the lower end of the
    95% likelihood range, i.e. the "2.5% value" can be reported in this field."""

    maximumAmount = create_element_text_process_dataset("maximumAmount", float)
    """Maximum amount of the Input or Output in case the uncertainty
    distribution is uniform or triangular. In case of calculated LCI results and for
    the aggregated flows in Partly terminated system data sets, the upper end of the
    95% likelihood range, i.e. the "97.5% value" can be reported in this field."""

    uncertaintyDistributionType = create_element_text_process_dataset(
        "uncertaintyDistributionType", str
    )
    """Defines the kind of uncertainty distribution that is valid for this
    particular object or parameter."""

    relativeStandardDeviation95In = create_element_text_process_dataset(
        "relativeStandardDeviation95In", float
    )
    """The resulting overall uncertainty of the calculated variable value
    considering uncertainty of measurements, modelling, appropriateness etc. [Notes:
    For log-normal distribution the square of the geometric standard deviation (SDg^2)
    is stated. Mean value times SDg^2 equals the 97.5% value (= Maximum value), Mean
    value divided by SDg^2 equals the 2.5% value (= Minimum value). For normal
    distribution the doubled standard deviation value (2*SD) is entered. Mean value
    plus 2*SD equals 97.5% value (= Maximum value), Mean value minus 2*SD equals 2.5%
    value (= Minimum value). This data field remains empty when uniform or triangular
    uncertainty distribution is applied.]"""

    dataSourceType = create_element_text_process_dataset("dataSourceType", str)
    """Identifies the data source type of each single Input or Output as
    being "Primary", "Secondary", or "Mixed primary/secondary"."""

    dataDerivationTypeStatus = create_element_text_process_dataset(
        "dataDerivationTypeStatus", str
    )
    """Identifies the way by which the individual Input / Output amount
    was derived (e.g. measured, estimated etc.), respectively the status and relevancy
    of missing data."""

    generalComment = create_attribute_list_process_dataset("generalComment", str)
    """General comment on this specific Input or Output, e.g. commenting
    on the data sources used and their specific representatuveness etc., on the status
    of "finalisation" of an entry as workflow information, etc."""

    @property
    def referenceToFlowDataSet(self) -> "GlobalReference":
        """ "Flow data set" of this Input or Output."""
        return get_element(self, "referenceToFlowDataSet")

    @property
    def allocations(self) -> "Allocations":
        """ "Container tag for the specification of allocations if process has
        more than one reference product. Use only for multifunctional processes."""
        return get_element(self, "allocations")

    @property
    def referencesToDataSource(self) -> "ReferencesToDataSource":
        """ "Source data set" of data source(s) used for the value of this
        specific Input or Output, especially if differing from the general data source
        used for this data set."""
        return get_element(self, "referencesToDataSource")


class LCIAResult(etree.ElementBase):
    """Single LCIA result"""

    meanAmount = create_element_text_process_dataset("meanAmount", float)
    """Mean amount of the LCIA result of the inventory, calculated for
    this LCIA method. Only significant digits should be stated."""

    uncertaintyDistributionType = create_element_text_process_dataset(
        "uncertaintyDistributionType", str
    )
    """Defines the kind of uncertainty distribution that is valid for this
    LCIA result."""

    relativeStandardDeviation95In = create_element_text_process_dataset(
        "relativeStandardDeviation95In", float
    )
    """The resulting overall uncertainty of the calculated variable value
    considering uncertainty of measurements, modelling, appropriateness etc. [Notes:
    For log-normal distribution the square of the geometric standard deviation (SDg^2)
    is stated. Mean value times SDg^2 equals the 97.5% value (= Maximum value), Mean
    value divided by SDg^2 equals the 2.5% value (= Minimum value). For normal
    distribution the doubled standard deviation value (2*SD) is entered. Mean value
    plus 2*SD equals 97.5% value (= Maximum value), Mean value minus 2*SD equals 2.5%
    value (= Minimum value). This data field remains empty when uniform or triangular
    uncertainty distribution is applied.]"""

    commonGeneralComment = create_attribute_list_process_dataset(
        "common:generalComment", str
    )
    """General comment on this specific LCIA result, e.g. commenting on
    the correspondence of the inputs and outputs with the applied LCIA method etc."""

    @property
    def referenceToLCIAMethodDataSets(self) -> "GlobalReference":
        """ "LCIA method data set" applied to calculate the LCIA results."""
        return get_element(self, "referenceToLCIAMethodDataSet")


class Name(etree.ElementBase):
    """General descriptive and specifying name of the process."""

    baseName = create_attribute_list_process_dataset("baseName", str)
    """General descriptive name of the process and/or its main good(s) or
    service(s) and/or it's level of processing."""

    treatmentStandardsRoutes = create_attribute_list_process_dataset(
        "treatmentStandardsRoutes", str
    )
    """Specifying information on the good, service, or process in
    technical term(s): treatment received, standard fulfilled, product quality, use
    information, production route name, educt name, primary / secondary etc. Separated
    by commata."""

    mixAndLocationTypes = create_attribute_list_process_dataset(
        "mixAndLocationTypes", str
    )
    """Specifying information on the good, service, or process whether
    being a production mix or consumption mix, location type of availability (such as
    e.g. "to consumer" or "at plant"). Separated by commata."""

    functionalUnitFlowProperties = create_attribute_list_process_dataset(
        "functionalUnitFlowProperties", str
    )
    """Further, quantitative specifying information on the good, service
    or process in technical term(s): qualifying constituent(s)-content and / or
    energy-content per unit etc. as appropriate. Separated by commata. (Note:
    non-qualifying flow properties, CAS No, Synonyms, Chemical formulas etc. are
    documented exclusively in the "Flow data set".)"""


class ComplementingProcesses(etree.ElementBase):
    """Process data set(s)" that complement this partial / sub-set of a
    complete process data set, if any and available as separate data set(s). The
    identifying name of this sub-set should be stated in the field "Identifier of
    sub-data set"."""

    @property
    def referenceToComplementingProcesses(self) -> List["GlobalReference"]:
        """Reference to one complementing process"""
        return get_element_list(self, "referenceToComplementingProcess")


class LocationOfOperationSupplyOrProduction(etree.ElementBase):
    """Location, country or region the data set represents. [Note 1: This
    field does not refer to e.g. the country in which a specific site is located that
    is represented by this data set but to the actually represented country, region,
    or site. Note 2: Entry can be of type "two-letter ISO 3166 country code" for
    countries, "seven-letter regional codes" for regions or continents, or "market
    areas and market organisations", as predefined for the ILCD. Also a name for e.g.
    a specific plant etc. can be given here (e.g. "FR, Lyon, XY Company, Z Site"; user
    defined). Note 3: The fact whether the entry refers to production or to
    consumption / supply has to be stated in the name-field "Mix and location types"
    e.g. as "Production mix".]"""

    descriptionOfRestrictions = create_attribute_list_process_dataset(
        "descriptionOfRestrictions", str
    )
    """Further explanations about additional aspects of the location: e.g.
    a company and/or site description and address, whether for certain sub-areas
    within the "Location" the data set is not valid, whether data is only valid for
    certain regions within the location indicated, or whether certain elementary flows
    or intermediate product flows are extrapolated from another geographical area."""

    location = create_attribute_process_dataset("location", str)
    """Location, country or region the data set represents. [Note 1: This
    field does not refer to e.g. the country in which a specific site is located that is
    represented by this data set but to the actually represented country, region, or
    site. Note 2: Entry can be of type "two-letter ISO 3166 country code" for countries,
    "seven-letter regional codes" for regions or continents, or "market areas and market
    organisations", as predefined for the ILCD. Also a name for e.g. a specific plant
    etc. can be given here (e.g. "FR, Lyon, XY Company, Z Site"; user defined). Note 3:
    The fact whether the entry refers to production or to consumption / supply has to be
    stated in the name-field "Mix and location types" e.g. as "Production mix".]"""

    latitudeAndLongitude = create_attribute_process_dataset("latitudeAndLongitude", str)
    """Geographical latitude and longitude reference of "Location" /
    "Sub-location". For area-type locations (e.g. countries, continents) the field is
    empty."""


class SubLocationOfOperationSupplyOrProduction(etree.ElementBase):
    """One or more geographical sub-unit(s) of the stated "Location". Such
    sub-units can be e.g. the sampling sites of a company-average data set, the
    countries of a region-average data set, or specific sites in a country-average
    data set. [Note: For single site data sets this field is empty and the site is
    named in the "Location" field.]"""

    descriptionOfRestrictions = create_attribute_list_process_dataset(
        "descriptionOfRestrictions", str
    )
    """Further explanations about additional aspects of the location: e.g.
    a company and/or site description and address, whether for certain sub-areas
    within the "Location" the data set is not valid, whether data is only valid for
    certain regions within the location indicated, or whether certain elementary flows
    or intermediate product flows are extrapolated from another geographical area."""

    subLocation = create_attribute_process_dataset("subLocation", str)
    """One or more geographical sub-unit(s) of the stated "Location". Such
    sub-units can be e.g. the sampling sites of a company-average data set, the
    countries of a region-average data set, or specific sites in a country-average
    data set. [Note: For single site data sets this field is empty and the site
    is named in the "Location" field.]"""

    latitudeAndLongitude = create_attribute_process_dataset("latitudeAndLongitude", str)
    """Geographical latitude and longitude reference of "Location" /
    "Sub-location". For area-type locations (e.g. countries, continents) the field is
    empty."""


class VariableParameter(etree.ElementBase):
    """Name of variable or parameter used as scaling factors for the "Mean
    amount" of individual inputs or outputs of the data set."""

    formula = create_element_text_process_dataset("formula", str)
    """Mathematical expression that determines the value of a variable.
    [Note: A parameter is defined by entering the value manually into the field "Mean
    value" and this field can be left empty.]"""

    meanValue = create_element_text_process_dataset("meanValue", float)
    """Parameter value entered by user OR in case a formula is given in
    the "Formula" field, the result of the formula for the variable is
    displayed here."""

    minimumValue = create_element_text_process_dataset("minimumValue", float)
    """Minimum value permissible for this parameter. For variables this
    field is empty"""

    maximumValue = create_element_text_process_dataset("maximumValue", float)
    """Maximum value permissible for this parameter. For variables this
    field is empty."""

    uncertaintyDistributionType = create_element_text_process_dataset(
        "uncertaintyDistributionType", str
    )
    """Defines the kind of uncertainty distribution that is valid for this
    particular object or parameter."""

    relativeStandardDeviation95In = create_element_text_process_dataset(
        "relativeStandardDeviation95In", float
    )
    """The resulting overall uncertainty of the calculated variable value
    considering uncertainty of measurements, modelling, appropriateness etc. [Notes:
    For log-normal distribution the square of the geometric standard deviation (SDg^2)
    is stated. Mean value times SDg^2 equals the 97.5% value (= Maximum value), Mean
    value divided by SDg^2 equals the 2.5% value (= Minimum value). For normal
    distribution the doubled standard deviation value (2*SD) is entered. Mean value
    plus 2*SD equals 97.5% value (= Maximum value), Mean value minus 2*SD equals 2.5%
    value (= Minimum value). This data field remains empty when uniform or triangular
    uncertainty distribution is applied.]"""

    comment = create_attribute_list_process_dataset("comment", str)
    """Comment or description of variable or parameter. Typically
    including its unit and default values, e.g. in the pattern &lt;[unit] description;
    defaults; comments&gt;."""

    name = create_attribute_process_dataset("name", str)
    """Name of variable or parameter used as scaling factors for the "Mean
    amount" of individual inputs or outputs of the data set."""


class CompletenessElementaryFlows(etree.ElementBase):
    """Completeness of the elementary flows in the Inputs and Outputs
    section of this data set from impact perspective, regarding addressing the
    individual mid-point problem field / impact category given. The completeness
    refers to the state-of-the-art of scientific knowledge whether or not an
    individual elementary flow contributes to the respective mid-point topic in a
    relevant way, which is e.g. the basis for the ILCD reference elementary flows.
    [Note: The "Completeness" statement does not automatically mean that related LCIA
    methods exist or reference the elementary flows of this data set. Hence for direct
    applicability of existing LCIA methods, check the field "Supported LCIA method
    data sets".]"""

    type = create_attribute_process_dataset("type", str)
    """Impact category for which the completeness information is stated."""

    value = create_attribute_process_dataset("value", str)
    """Completeness value for the given impact category."""


class Review(ValidationGroup1, ValidationGroup3):
    """Review information on data set."""

    type = create_attribute_process_dataset("type", str)
    """Type of review that has been performed regarding independency and type
    of review process."""


class Compliance(ComplianceGroup):
    """One compliance declaration"""

    nomenclatureCompliance = create_element_text_process_dataset(
        "common:nomenclatureCompliance", str
    )
    """Nomenclature compliance of this data set with the respective
    requirements set by the "compliance system" refered to."""

    methodologicalCompliance = create_element_text_process_dataset(
        "common:methodologicalCompliance", str
    )
    """Methodological compliance of this data set with the respective
    requirements set by the "compliance system" refered to."""

    reviewCompliance = create_element_text_process_dataset(
        "common:reviewCompliance", str
    )
    """Review/Verification compliance of this data set with the respective
    requirements set by the "compliance system" refered to."""

    documentationCompliance = create_element_text_process_dataset(
        "common:documentationCompliance", str
    )
    """Documentation/Reporting compliance of this data set with the
    respective requirements set by the "compliance system" refered to."""

    qualityCompliance = create_element_text_process_dataset(
        "common:qualityCompliance", str
    )
    """Quality compliance of this data set with the respective
    requirements set by the "compliance system" refered to."""


class Allocations(etree.ElementBase):
    """Container tag for the specification of allocations if process has
    more than one reference product. Use only for multifunctional processes."""

    @property
    def allocations(self) -> List["Allocation"]:
        """Specifies one allocation of this exchange (see the attributes of
        this tag below)"""
        return get_element_list(self, "allocation")


class Allocation(etree.ElementBase):
    """Specifies one allocation of this exchange (see the attributes of
    this tag below)"""

    internalReferenceToCoProduct = create_attribute_process_dataset(
        "internalReferenceToCoProduct", int
    )
    """Reference to one of the co-products. The applied allocation
    approach(es), details and and explanations are documented in the fields "LCI method
    approaches" and "Deviations from LCI method approaches / explanations". [Notes:
    Applicable only to multifunctional processes. The documented allocated fractions are
    only applicable when using the data set for attributional modelling and are to be
    ignored for consequential modeling.]"""

    allocatedFraction = create_attribute_process_dataset("allocatedFraction", float)
    """Fraction (expressed in %) of this Input or Output flow that is
    foreseen to be allocated to this co-product (recommended allocation). The numbers
    across the co-products should sum up to 100%."""


class ReferencesToDataSource(etree.ElementBase):
    """ "Source data set" of data source(s) used for the value of this
    specific Input or Output, especially if differing from the general data source
    used for this data set."""

    @property
    def referenceToDataSources(self) -> List["GlobalReference"]:
        """ ""Source data set" of data source(s) used for the value of this
        specific Input or Output, especially if differing from the general data source
        used for this data set."""
        return get_element_list(self, "referenceToDataSource")
