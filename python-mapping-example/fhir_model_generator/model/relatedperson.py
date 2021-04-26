#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/RelatedPerson) on 2020-02-10.
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
class RelatedPersonCommunication(BackboneElement):
    """ A language which may be used to communicate with about the patient's health.
    """
    resource_type: ClassVar[str] = "RelatedPersonCommunication"

    language: CodeableConcept = None
    preferred: Optional[bool] = None


@dataclass
class RelatedPerson(DomainResource):
    """ A person that is related to a patient, but who is not a direct target of
    care.

    Information about a person that is involved in the care for a patient, but
    who is not the target of healthcare, nor has a formal responsibility in the
    care process.
    """
    resource_type: ClassVar[str] = "RelatedPerson"

    identifier: Optional[List[Identifier]] = None
    active: Optional[bool] = None
    patient: FHIRReference = None
    relationship: Optional[List[CodeableConcept]] = None
    name: Optional[List[HumanName]] = None
    telecom: Optional[List[ContactPoint]] = None
    gender: Optional[str] = None
    birthDate: Optional[FHIRDate] = None
    address: Optional[List[Address]] = None
    photo: Optional[List[Attachment]] = None
    period: Optional[Period] = None
    communication: Optional[List[RelatedPersonCommunication]] = None