"""Custom ILCD Python classes for FlowDataSet of ILCD schema."""

from typing import List

from lxml import etree
from lxmlh import get_element, get_element_list

from .common import (
    ClassificationInformation,
    ComplianceDeclarations,
    DataEntryByGroup1,
    GlobalReference,
    PublicationAndOwnershipGroup1,
)
from .helpers import (
    create_attribute_flow_property_dataset,
    create_attribute_list_flow_property_dataset,
)


class FlowPropertyDataSet(etree.ElementBase):
    """Flow Property Dataset."""

    version = create_attribute_flow_property_dataset("version", str)
    """Indicates, which version of the ILCD format is used."""

    @property
    def flowPropertiesInformation(self) -> "FlowPropertiesInformation":
        """Flow property information."""
        return get_element(self, "flowPropertiesInformation")

    @property
    def modellingAndValidation(self) -> "ModellingAndValidation":
        """Covers the five sub-sections 1) LCI method (not used),
        2) Data sources, treatment and representativeness (only
        3 fields), 3) Completeness (not used), 4) Validation,
        and 5) Compliance."""
        return get_element(self, "modellingAndValidation")

    @property
    def administrativeInformation(self) -> "AdministrativeInformation":
        """Information on data set management and administration."""
        return get_element(self, "administrativeInformation")


class FlowPropertiesInformation(etree.ElementBase):
    """Flow property information."""

    @property
    def dataSetInformation(self) -> "DataSetInformation":
        """General data set information."""
        return get_element(self, "dataSetInformation")

    @property
    def quantitativeReference(self) -> "QuantitativeReference":
        """This section allows to refer to the Flow property's
        quantitative reference, which is always a unit (i.e. that
        unit, in which the property is measured, e.g. "MJ" for
        energy-related Flow properties)."""
        return get_element(self, "quantitativeReference")


class ModellingAndValidation(etree.ElementBase):
    """Covers the five sub-sections 1) LCI method (not used),
    2) Data sources, treatment and representativeness (only
    3 fields), 3) Completeness (not used), 4) Validation,
    and 5) Compliance."""

    @property
    def dataSourcesTreatmentAndRepresentativeness(
        self,
    ) -> "DataSourcesTreatmentAndRepresentativeness":
        """Data sources, treatment and representativeness."""
        return get_element(self, "dataSourcesTreatmentAndRepresentativeness")

    @property
    def complianceDeclarations(self) -> "ComplianceDeclarations":
        """Statements on compliance of several data set aspects with
        compliance requirements as defined by the referenced compliance
        system (e.g. an EPD scheme, handbook of a national or
        international data network such as the ILCD, etc.)."""
        return get_element(self, "complianceDeclarations")


class AdministrativeInformation(etree.ElementBase):
    """Information on data set management and administration."""

    @property
    def dataEntryBy(self) -> "DataEntryBy":
        """Staff or entity, that documented the generated data set,
        entering the information into the database; plus administrative
        information linked to the data entry activity."""
        return get_element(self, "dataEntryBy")

    @property
    def publicationAndOwnership(self) -> "PublicationAndOwnership":
        """Information related to publication and version management of
        the data set including copyright and access restrictions."""
        return get_element(self, "publicationAndOwnership")


class DataSetInformation(etree.ElementBase):
    """General data set information."""

    commonUUID = create_attribute_flow_property_dataset("common:UUID", str)
    """Automatically generated Universally Unique Identifier of this data
    set. Together with the "Data set version", the UUID uniquely identifies each data
    set."""

    names = create_attribute_list_flow_property_dataset("common:name", str)
    """Name of flow property."""

    synonyms = create_attribute_list_flow_property_dataset("common:synonyms", str)
    """Synonyms / alternative names / brands of the good, service, or
    process. Separated by semicolon."""

    generalComments = create_attribute_list_flow_property_dataset(
        "common:generalComment", str
    )
    """Free text for general information about the Flow data set. It may contain
    information about e.g. the use of the substance, good, service or process in
    a specific technology or industry-context, information sources used, data
    selection principles etc."""

    @property
    def classificationInformation(self) -> "ClassificationInformation":
        """Hierarchical classification of the good, service, or process.
        (Note: This entry is NOT required for the identification of a Process. It should
        nevertheless be avoided to use identical names for Processes in the same
        category."""
        return get_element(self, "classificationInformation")


class QuantitativeReference(etree.ElementBase):
    """This section allows to refer to the Flow property's
    quantitative reference, which is always a unit (i.e. that
    unit, in which the property is measured, e.g. "MJ" for
    energy-related Flow properties)."""

    @property
    def referenceToReferenceUnitGroup(self) -> "GlobalReference":
        """ "Unit group data set" and its reference unit, in which
        the Flow property is measured."""
        return get_element(self, "referenceToReferenceUnitGroup")


class DataSourcesTreatmentAndRepresentativeness(etree.ElementBase):
    """Data sources, treatment and representativeness."""

    @property
    def referenceToDataSources(self) -> List["GlobalReference"]:
        """ "Source data set" of data source(s) used for the data
        set e.g. a paper, a questionnaire, a monography etc. The
        main raw data sources should be named, too. [Note: relevant
        especially for market price data.]"""
        return get_element_list(self, "referenceToDataSource")


class DataEntryBy(DataEntryByGroup1):
    """Staff or entity, that documented the generated data set,
    entering the information into the database; plus administrative
    information linked to the data entry activity."""


class PublicationAndOwnership(PublicationAndOwnershipGroup1):
    """Information related to publication and version management of
    the data set including copyright and access restrictions."""

    @property
    def referenceToOwnershipOfDataSet(self) -> "GlobalReference":
        """ "Contact data set" of the person or entity who owns this
        ata set. (Note: this is not necessarily the publisher of the
        ata set.)"""
        return get_element(self, "common:referenceToOwnershipOfDataSet")
