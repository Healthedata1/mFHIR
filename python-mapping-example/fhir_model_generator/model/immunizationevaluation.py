#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation) on 2020-02-10.
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
class ImmunizationEvaluation(DomainResource):
    """ Immunization evaluation information.

    Describes a comparison of an immunization event against published
    recommendations to determine if the administration is "valid" in relation
    to those  recommendations.
    """
    resource_type: ClassVar[str] = "ImmunizationEvaluation"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    patient: FHIRReference = None
    date: Optional[FHIRDate] = None
    authority: Optional[FHIRReference] = None
    targetDisease: CodeableConcept = None
    immunizationEvent: FHIRReference = None
    doseStatus: CodeableConcept = None
    doseStatusReason: Optional[List[CodeableConcept]] = None
    description: Optional[str] = None
    series: Optional[str] = None
    doseNumberPositiveInt: Optional[int] = field(default=None, metadata=dict(one_of_many='doseNumber',))
    doseNumberString: Optional[str] = field(default=None, metadata=dict(one_of_many='doseNumber',))
    seriesDosesPositiveInt: Optional[int] = field(default=None, metadata=dict(one_of_many='seriesDoses',))
    seriesDosesString: Optional[str] = field(default=None, metadata=dict(one_of_many='seriesDoses',))