#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Patient) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .address import Address
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier
from .period import Period


@dataclass
class PatientContact(BackboneElement):
    """ A contact party (e.g. guardian, partner, friend) for the patient.
    """
    resource_type: ClassVar[str] = "PatientContact"

    relationship: Optional[List[CodeableConcept]] = None
    name: Optional[HumanName] = None
    telecom: Optional[List[ContactPoint]] = None
    address: Optional[Address] = None
    gender: Optional[str] = None
    organization: Optional[FHIRReference] = None
    period: Optional[Period] = None


@dataclass
class PatientCommunication(BackboneElement):
    """ A language which may be used to communicate with the patient about his or
    her health.
    """
    resource_type: ClassVar[str] = "PatientCommunication"

    language: CodeableConcept = None
    preferred: Optional[bool] = None


@dataclass
class PatientLink(BackboneElement):
    """ Link to another patient resource that concerns the same actual person.

    Link to another patient resource that concerns the same actual patient.
    """
    resource_type: ClassVar[str] = "PatientLink"

    other: FHIRReference = None
    type: str = None


@dataclass
class Patient(DomainResource):
    """ Information about an individual or animal receiving health care services.

    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """
    resource_type: ClassVar[str] = "Patient"

    identifier: Optional[List[Identifier]] = None
    active: Optional[bool] = None
    name: Optional[List[HumanName]] = None
    telecom: Optional[List[ContactPoint]] = None
    gender: Optional[str] = None
    birthDate: Optional[FHIRDate] = None
    deceasedBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='deceased',))
    deceasedDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='deceased',))
    address: Optional[List[Address]] = None
    maritalStatus: Optional[CodeableConcept] = None
    multipleBirthBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='multipleBirth',))
    multipleBirthInteger: Optional[int] = field(default=None, metadata=dict(one_of_many='multipleBirth',))
    photo: Optional[List[Attachment]] = None
    contact: Optional[List[PatientContact]] = None
    communication: Optional[List[PatientCommunication]] = None
    generalPractitioner: Optional[List[FHIRReference]] = None
    managingOrganization: Optional[FHIRReference] = None
    link: Optional[List[PatientLink]] = None