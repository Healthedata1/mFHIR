#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Practitioner) on 2020-02-10.
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
class PractitionerQualification(BackboneElement):
    """ Certification, licenses, or training pertaining to the provision of care.

    The official certifications, training, and licenses that authorize or
    otherwise pertain to the provision of care by the practitioner.  For
    example, a medical license issued by a medical board authorizing the
    practitioner to practice medicine within a certian locality.
    """
    resource_type: ClassVar[str] = "PractitionerQualification"

    identifier: Optional[List[Identifier]] = None
    code: CodeableConcept = None
    period: Optional[Period] = None
    issuer: Optional[FHIRReference] = None


@dataclass
class Practitioner(DomainResource):
    """ A person with a  formal responsibility in the provisioning of healthcare or
    related services.

    A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """
    resource_type: ClassVar[str] = "Practitioner"

    identifier: Optional[List[Identifier]] = None
    active: Optional[bool] = None
    name: Optional[List[HumanName]] = None
    telecom: Optional[List[ContactPoint]] = None
    address: Optional[List[Address]] = None
    gender: Optional[str] = None
    birthDate: Optional[FHIRDate] = None
    photo: Optional[List[Attachment]] = None
    qualification: Optional[List[PractitionerQualification]] = None
    communication: Optional[List[CodeableConcept]] = None