"""Custom ILCD Python classes for UnitGroupDataSet of ILCD schema."""

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
    create_attribute_list_unit_group_dataset,
    create_attribute_unit_group_dataset,
    create_element_text_unit_group_dataset,
)


class UnitGroupDataSet(etree.ElementBase):
    """Unit Group Dataset."""

    version = create_attribute_unit_group_dataset("version", str)
    """Indicates, which version of the ILCD format is used."""

    @property
    def unitGroupInformation(self) -> "UnitGroupInformation":
        """Unit group information."""
        return get_element(self, "unitGroupInformation")

    @property
    def modellingAndValidation(self) -> "ModellingAndValidation":
        """Sections used to a very limited degree; covers the five sub-sections
        1) LCI method and allocation (not used for unit groups), 2) Data sources,
        treatment and representativeness (not used for unit groups), 3) Completeness
        (not used for unit groups), 4) Validation (not used for unit groups), and 5)
        Compliance."""
        return get_element(self, "modellingAndValidation")

    @property
    def administrativeInformation(self) -> "AdministrativeInformation":
        """Information on data set management and administration."""
        return get_element(self, "administrativeInformation")

    @property
    def units(self) -> "Units":
        """List of units that belong to this Unit group and are interconvertible
        among each other with a fixed factor, such as this can be done e.g. for
        kg, g, ounces, pounds etc. of the Unit group "Units of mass"."""
        return get_element(self, "units")


class UnitGroupInformation(etree.ElementBase):
    """Unit group information."""

    @property
    def dataSetInformation(self) -> "DataSetInformation":
        """General data set information."""
        return get_element(self, "dataSetInformation")

    @property
    def quantitativeReference(self) -> "QuantitativeReference":
        """This section identifies the quantitative reference of this
        data set, i.e. the "reference unit" in which the data set is
        expressed. It is the basis for the conversion to other units
        in the data set (e.g. for mass-related units "kg" as basis for
        conversion to and among "g", "ounces", "short tons", etc.)."""
        return get_element(self, "quantitativeReference")


class ModellingAndValidation(etree.ElementBase):
    """Sections used to a very limited degree; covers the five sub-sections
    1) LCI method and allocation (not used for unit groups), 2) Data sources,
    treatment and representativeness (not used for unit groups), 3) Completeness
    (not used for unit groups), 4) Validation (not used for unit groups), and 5)
    Compliance."""

    @property
    def complianceDeclarations(self) -> "ComplianceDeclarations":
        """Statements on compliance of several data set aspects with compliance
        requirements as defined by the referenced compliance system (e.g. an EPD
        scheme, handbook of a national or international data network such as the
        ILCD, etc.)."""
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


class Units(etree.ElementBase):
    """Unit group information."""

    @property
    def units(self) -> List["Unit"]:
        """One unit."""
        return get_element_list(self, "unit")


class DataSetInformation(etree.ElementBase):
    """General data set information."""

    commonUUID = create_attribute_unit_group_dataset("common:UUID", str)
    """Automatically generated Universally Unique Identifier of this data
    set. Together with the "Data set version", the UUID uniquely identifies each data
    set."""

    names = create_attribute_list_unit_group_dataset("common:name", str)
    """Name of the unit group, typically indicating for which flow property or group
    of flow properties it is used. The individual units are named in the "Units"
    section of the "Unit group data set"."""

    synonyms = create_attribute_list_unit_group_dataset("common:synonyms", str)
    """Synonyms / alternative names / brands of the good, service, or
    process. Separated by semicolon."""

    generalComments = create_attribute_list_unit_group_dataset(
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
    """This section identifies the quantitative reference of this
    data set, i.e. the "reference unit" in which the data set is
    expressed. It is the basis for the conversion to other units
    in the data set (e.g. for mass-related units "kg" as basis for
    conversion to and among "g", "ounces", "short tons", etc.)."""

    referenceToReferenceUnit = create_attribute_unit_group_dataset(
        "referenceToReferenceUnit", int
    )
    """The Unit group's unit in which the data set is expressed
    (data set internal reference)."""


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


class Unit(etree.ElementBase):
    """One unit."""

    dataSetInternalID = create_attribute_unit_group_dataset("dataSetInternalID", int)
    """Automated entry: internal ID, used in the "Quantitative reference"
    section to identify the reference unit."""

    meanValue = create_element_text_unit_group_dataset("meanValue", float)
    """Mean value of this unit in relationship to the reference unit of
    this Unit group (see field "Reference unit" in the "Quantitative
    reference" section). [Notes and Examples: This vale is i.e. the
    linear conversion factor for this unit. E.g., if the Unit group
    would be "Units of mass" and the selected reference unit "kg",
    then the value stated here for an additional unit "g" would be
    0.001, as 1 g is 0.001 times 1 kg. It is recommended to report
    only significant digits of the value.]"""

    generalComment = create_attribute_list_unit_group_dataset("name", str)
    """General comment on each single unit, typically giving the
    long name and unit system from which this unit stems, and
    (if necessary) referring to specifc data sources used, or for
    workflow purposes about status of "finalisation" of an entry etc."""
