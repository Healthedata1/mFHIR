#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/EpisodeOfCare) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class EpisodeOfCareStatusHistory(BackboneElement):
    """ Past list of status codes (the current status may be included to cover the
    start date of the status).

    The history of statuses that the EpisodeOfCare has been through (without
    requiring processing the history of the resource).
    """
    resource_type: ClassVar[str] = "EpisodeOfCareStatusHistory"

    status: str = None
    period: Period = None


@dataclass
class EpisodeOfCareDiagnosis(BackboneElement):
    """ The list of diagnosis relevant to this episode of care.
    """
    resource_type: ClassVar[str] = "EpisodeOfCareDiagnosis"

    condition: FHIRReference = None
    role: Optional[CodeableConcept] = None
    rank: Optional[int] = None


@dataclass
class EpisodeOfCare(DomainResource):
    """ An association of a Patient with an Organization and  Healthcare
    Provider(s) for a period of time that the Organization assumes some level
    of responsibility.

    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during this
    time.
    """
    resource_type: ClassVar[str] = "EpisodeOfCare"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    statusHistory: Optional[List[EpisodeOfCareStatusHistory]] = None
    type: Optional[List[CodeableConcept]] = None
    diagnosis: Optional[List[EpisodeOfCareDiagnosis]] = None
    patient: FHIRReference = None
    managingOrganization: Optional[FHIRReference] = None
    period: Optional[Period] = None
    referralRequest: Optional[List[FHIRReference]] = None
    careManager: Optional[FHIRReference] = None
    team: Optional[List[FHIRReference]] = None
    account: Optional[List[FHIRReference]] = None