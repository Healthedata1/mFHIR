#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Schedule) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class Schedule(DomainResource):
    """ A container for slots of time that may be available for booking
    appointments.
    """
    resource_type: ClassVar[str] = "Schedule"

    identifier: Optional[List[Identifier]] = None
    active: Optional[bool] = None
    serviceCategory: Optional[List[CodeableConcept]] = None
    serviceType: Optional[List[CodeableConcept]] = None
    specialty: Optional[List[CodeableConcept]] = None
    actor: List[FHIRReference] = field(default_factory=list)
    planningHorizon: Optional[Period] = None
    comment: Optional[str] = None