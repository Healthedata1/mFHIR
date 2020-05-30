#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Condition) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .age import Age
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
class ConditionStage(BackboneElement):
    """ Stage/grade, usually assessed formally.

    Clinical stage or grade of a condition. May include formal severity
    assessments.
    """
    resource_type: ClassVar[str] = "ConditionStage"

    summary: Optional[CodeableConcept] = None
    assessment: Optional[List[FHIRReference]] = None
    type: Optional[CodeableConcept] = None


@dataclass
class ConditionEvidence(BackboneElement):
    """ Supporting evidence.

    Supporting evidence / manifestations that are the basis of the Condition's
    verification status, such as evidence that confirmed or refuted the
    condition.
    """
    resource_type: ClassVar[str] = "ConditionEvidence"

    code: Optional[List[CodeableConcept]] = None
    detail: Optional[List[FHIRReference]] = None


@dataclass
class Condition(DomainResource):
    """ Detailed information about conditions, problems or diagnoses.

    A clinical condition, problem, diagnosis, or other event, situation, issue,
    or clinical concept that has risen to a level of concern.
    """
    resource_type: ClassVar[str] = "Condition"

    identifier: Optional[List[Identifier]] = None
    clinicalStatus: Optional[CodeableConcept] = None
    verificationStatus: Optional[CodeableConcept] = None
    category: Optional[List[CodeableConcept]] = None
    severity: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    bodySite: Optional[List[CodeableConcept]] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    onsetDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='onset',))
    onsetAge: Optional[Age] = field(default=None, metadata=dict(one_of_many='onset',))
    onsetPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='onset',))
    onsetRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='onset',))
    onsetString: Optional[str] = field(default=None, metadata=dict(one_of_many='onset',))
    abatementDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='abatement',))
    abatementAge: Optional[Age] = field(default=None, metadata=dict(one_of_many='abatement',))
    abatementPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='abatement',))
    abatementRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='abatement',))
    abatementString: Optional[str] = field(default=None, metadata=dict(one_of_many='abatement',))
    recordedDate: Optional[FHIRDate] = None
    recorder: Optional[FHIRReference] = None
    asserter: Optional[FHIRReference] = None
    stage: Optional[List[ConditionStage]] = None
    evidence: Optional[List[ConditionEvidence]] = None
    note: Optional[List[Annotation]] = None