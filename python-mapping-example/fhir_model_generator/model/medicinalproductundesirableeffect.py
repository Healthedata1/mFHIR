#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductUndesirableEffect) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .population import Population


@dataclass
class MedicinalProductUndesirableEffect(DomainResource):
    """ MedicinalProductUndesirableEffect.

    Describe the undesirable effects of the medicinal product.
    """
    resource_type: ClassVar[str] = "MedicinalProductUndesirableEffect"

    subject: Optional[List[FHIRReference]] = None
    symptomConditionEffect: Optional[CodeableConcept] = None
    classification: Optional[CodeableConcept] = None
    frequencyOfOccurrence: Optional[CodeableConcept] = None
    population: Optional[List[Population]] = None