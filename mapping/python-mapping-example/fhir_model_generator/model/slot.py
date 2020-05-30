#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Slot) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class Slot(DomainResource):
    """ A slot of time on a schedule that may be available for booking appointments.
    """
    resource_type: ClassVar[str] = "Slot"

    identifier: Optional[List[Identifier]] = None
    serviceCategory: Optional[List[CodeableConcept]] = None
    serviceType: Optional[List[CodeableConcept]] = None
    specialty: Optional[List[CodeableConcept]] = None
    appointmentType: Optional[CodeableConcept] = None
    schedule: FHIRReference = None
    status: str = None
    start: FHIRDate = None
    end: FHIRDate = None
    overbooked: Optional[bool] = None
    comment: Optional[str] = None