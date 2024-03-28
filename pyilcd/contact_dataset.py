"""Custom ILCD Python classes for ContactDataSet of ILCD schema."""

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
    create_attribute_contact_dataset,
    create_attribute_list_contact_dataset,
    create_element_text_contact_dataset,
)


class ContactDataSet(etree.ElementBase):
    """Contact Dataset."""

    version = create_attribute_contact_dataset("version", str)
    """Indicates, which version of the ILCD format is used."""

    @property
    def contactInformation(self) -> "ContactInformation":
        """Contact information,"""
        return get_element(self, "contactInformation")

    @property
    def administrativeInformation(self) -> "AdministrativeInformation":
        """Information on data set management and administration."""
        return get_element(self, "administrativeInformation")


class ContactInformation(etree.ElementBase):
    """Contact information."""

    @property
    def dataSetInformation(self) -> "DataSetInformation":
        """Data set information."""
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

    UUID = create_element_text_contact_dataset("common:UUID", str)
    """Automatically generated Universally Unique Identifier of this data
    set. Together with the "Data set version", the UUID uniquely identifies each data
    set."""

    shortNames = create_attribute_list_contact_dataset("common:shortName", str)
    """Short name for the contact, that is used for display e.g. of links to this
    data set (especially in case the full name of the contact is rather long, e.g.
    "FAO" for "Food and Agriculture Organization")."""

    names = create_attribute_list_contact_dataset("common:name", str)
    """Name of the person, working group, organisation, or database network, which
    is represented by this contact data set."""

    contactAddresses = create_attribute_list_contact_dataset("contactAddress", str)
    """Mail address of the contact; specific for the person, working group, or
    department. [Note: A general contact point to the organisation is to be given
    in "General contact point".]"""

    telephone = create_attribute_contact_dataset("telephone", str)
    """Contact's phone number(s) including country and regional codes."""

    telefax = create_attribute_contact_dataset("telefax", str)
    """Contact's fax number(s) including country and regional codes."""

    email = create_attribute_contact_dataset("email", str)
    """Contact's e-mail address."""

    wwwAddress = create_attribute_contact_dataset("WWWAddress", str)
    """Web-address of the person, working group, organisation or database network."""

    centralContactPoints = create_attribute_list_contact_dataset(
        "centralContactPoint", str
    )
    """Alternative address / contact details for the contact. Provides contact
    information in case e.g. the person or group represented by this contact
    has left the organisation or changed office/telephone. This alternative
    contact point can hence contain also a central telephone number, e-mail,
    www-address etc. of the organisation."""

    contactDescriptionOrComments = create_attribute_list_contact_dataset(
        "contactDescriptionOrComment", str
    )
    """Free text for additional description of the organisation or person of
    the contact, such as organisational profile, person responsibilities, etc."""

    @property
    def classificationInformation(self) -> "ClassificationInformation":
        """Hierachical classification of the contact foreseen to be used to
        structure the contact content of the database. (Note: This entry is
        NOT required for the identification of the contact data set. It should
        nevertheless be avoided to use identical names for contacts in the same
        class."""
        return get_element(self, "classificationInformation")

    @property
    def referenceToContact(self) -> List["GlobalReference"]:
        """ "Contact data set"s of working groups, organisations or database
        networks to which EITHER this person or entity OR this database, data set
        format, or compliance system belongs. [Note: This does not necessarily
        imply a legally binding relationship, but may also be a voluntary
        membership.]"""
        return get_element_list(self, "referenceToContact")

    @property
    def referenceToLogo(self) -> "GlobalReference":
        """ "Source data set" of the logo of the organisation or source to
        be used in reports etc."""
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
        """ "Contact data set" of the person or entity who owns this data
        set. (Note: this is not necessarily the publisher of the data set.)"""
        return get_element(self, "common:referenceToOwnershipOfDataSet")
