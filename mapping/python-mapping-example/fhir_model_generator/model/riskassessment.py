#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/RiskAssessment) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .range import Range


@dataclass
class RiskAssessmentPrediction(BackboneElement):
    """ Outcome predicted.

    Describes the expected outcome for the subject.
    """
    resource_type: ClassVar[str] = "RiskAssessmentPrediction"

    outcome: Optional[CodeableConcept] = None
    probabilityDecimal: Optional[float] = field(default=None, metadata=dict(one_of_many='probability',))
    probabilityRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='probability',))
    qualitativeRisk: Optional[CodeableConcept] = None
    relativeRisk: Optional[float] = None
    whenPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='when',))
    whenRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='when',))
    rationale: Optional[str] = None


@dataclass
class RiskAssessment(DomainResource):
    """ Potential outcomes for a subject with likelihood.

    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """
    resource_type: ClassVar[str] = "RiskAssessment"

    identifier: Optional[List[Identifier]] = None
    basedOn: Optional[FHIRReference] = None
    parent: Optional[FHIRReference] = None
    status: str = None
    method: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrencePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='occurrence',))
    condition: Optional[FHIRReference] = None
    performer: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    basis: Optional[List[FHIRReference]] = None
    prediction: Optional[List[RiskAssessmentPrediction]] = None
    mitigation: Optional[str] = None
    note: Optional[List[Annotation]] = None