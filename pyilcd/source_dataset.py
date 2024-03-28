"""Custom ILCD Python classes for SourceDataSet of ILCD schema."""

from typing import List

from lxml import etree
from lxmlh import get_element, get_element_list

from .common import (
    ClassificationInformation,
    DataEntryByGroup1,
    GlobalReference,
    PublicationAndOwnershipGroup1,
)
from .helpers import (
    create_attribute_list_source_dataset,
    create_attribute_source_dataset,
)


class SourceDataSet(etree.ElementBase):
    """Data set for bibliographical references to sources used, but also for
    reference to data set formats, databases, conformity systems etc."""

    version = create_attribute_source_dataset("version", str)
    """Indicates, which version of the ILCD format is used."""

    @property
    def sourceInformation(self) -> "SourceInformation":
        """Source information."""
        return get_element(self, "sourceInformation")

    @property
    def administrativeInformation(self) -> "AdministrativeInformation":
        """Information on data set management and administration."""
        return get_element(self, "administrativeInformation")


class SourceInformation(etree.ElementBase):
    """Source information."""

    @property
    def dataSetInformation(self) -> "DataSetInformation":
        """General data set information."""
        return get_element(self, "dataSetInformation")


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
    """Data set information."""

    commonUUID = create_attribute_source_dataset("common:UUID", str)
    """Automatically generated Universally Unique Identifier of this data
    set. Together with the "Data set version", the UUID uniquely identifies each data
    set."""

    shortNames = create_attribute_list_source_dataset("common:shortName", str)
    """Short name for the "Source citation", i.e. for the bibliographical
    reference or reference to internal data sources used."""

    sourceCitation = create_attribute_source_dataset("sourceCitation", str)
    """Bibliographical reference or reference to internal data source.
    Also used in order to reference to databases and tools, data set formats,
    conformity systems, pictures etc.."""

    publicationType = create_attribute_source_dataset("publicationType", str)
    """Bibliographic publication type of the source."""

    sourceDescriptionOrComments = create_attribute_list_source_dataset(
        "sourceDescriptionOrComment", str
    )
    """Free text for additional description of the source. In case of use of
    published data it may contain a brief summary of the publication and the
    kind of medium used (e.g. CD-ROM, hard copy)."""

    @property
    def classificationInformation(self) -> "ClassificationInformation":
        """Hierachical classification of the Source foreseen to be used to
        structure the Source content of the database. (Note: This entry is
        NOT required for the identification of a Source. It should nevertheless
        be avoided to use identical names for Source in the same class."""
        return get_element(self, "classificationInformation")

    @property
    def referenceToDigitalFiles(self) -> List["ReferenceToDigitalFile"]:
        """Link to a digital file of the source (www-address or intranet-path;
        relative or absolue path). (Info: Allows direct access to e.g.
        complete reports of further documentation, which may also be digitally
        attached to this data set and exchanged jointly with the XML file.)"""
        return get_element_list(self, "referenceToDigitalFile")

    @property
    def referenceToContact(self) -> List["GlobalReference"]:
        """ "Contact data set"s of working groups, organisations or
        database networks to which EITHER this person or entity OR this
        database, data set format, or compliance system belongs.
        [Note: This does not necessarily imply a legally binding relationship,
        but may also be a voluntary membership.]"""
        return get_element_list(self, "referenceToContact")

    @property
    def referenceToLogo(self) -> "GlobalReference":
        """ "Source data set" of the logo of the organisation or source to be
        used in reports etc."""
        return get_element(self, "referenceToLogo")


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


class ReferenceToDigitalFile(etree.ElementBase):
    """Link to a digital file of the source (www-address or intranet-path;
    relative or absolue path). (Info: Allows direct access to e.g.
    complete reports of further documentation, which may also be digitally
    attached to this data set and exchanged jointly with the XML file.)"""

    uri = create_attribute_source_dataset("uri", str)
    """URI for digital file."""
