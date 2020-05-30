#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CarePlan) on 2020-02-10.
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
from .quantity import Quantity
from .timing import Timing


@dataclass
class CarePlanActivityDetail(BackboneElement):
    """ In-line definition of activity.

    A simple summary of a planned activity suitable for a general care plan
    system (e.g. form driven) that doesn't know about specific resources such
    as procedure etc.
    """
    resource_type: ClassVar[str] = "CarePlanActivityDetail"

    kind: Optional[str] = None
    instantiatesCanonical: Optional[List[str]] = None
    instantiatesUri: Optional[List[str]] = None
    code: Optional[CodeableConcept] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    goal: Optional[List[FHIRReference]] = None
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    doNotPerform: Optional[bool] = None
    scheduledTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='scheduled',))
    scheduledPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='scheduled',))
    scheduledString: Optional[str] = field(default=None, metadata=dict(one_of_many='scheduled',))
    location: Optional[FHIRReference] = None
    performer: Optional[List[FHIRReference]] = None
    productCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='product',))
    productReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='product',))
    dailyAmount: Optional[Quantity] = None
    quantity: Optional[Quantity] = None
    description: Optional[str] = None


@dataclass
class CarePlanActivity(BackboneElement):
    """ Action to occur as part of plan.

    Identifies a planned action to occur as part of the plan.  For example, a
    medication to be used, lab tests to perform, self-monitoring, education,
    etc.
    """
    resource_type: ClassVar[str] = "CarePlanActivity"

    outcomeCodeableConcept: Optional[List[CodeableConcept]] = None
    outcomeReference: Optional[List[FHIRReference]] = None
    progress: Optional[List[Annotation]] = None
    reference: Optional[FHIRReference] = None
    detail: Optional[CarePlanActivityDetail] = None


@dataclass
class CarePlan(DomainResource):
    """ Healthcare plan for patient or group.

    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient, group or community for a period of time,
    possibly limited to care for a specific condition or set of conditions.
    """
    resource_type: ClassVar[str] = "CarePlan"

    identifier: Optional[List[Identifier]] = None
    instantiatesCanonical: Optional[List[str]] = None
    instantiatesUri: Optional[List[str]] = None
    basedOn: Optional[List[FHIRReference]] = None
    replaces: Optional[List[FHIRReference]] = None
    partOf: Optional[List[FHIRReference]] = None
    status: str = None
    intent: str = None
    category: Optional[List[CodeableConcept]] = None
    title: Optional[str] = None
    description: Optional[str] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    period: Optional[Period] = None
    created: Optional[FHIRDate] = None
    author: Optional[FHIRReference] = None
    contributor: Optional[List[FHIRReference]] = None
    careTeam: Optional[List[FHIRReference]] = None
    addresses: Optional[List[FHIRReference]] = None
    supportingInfo: Optional[List[FHIRReference]] = None
    goal: Optional[List[FHIRReference]] = None
    activity: Optional[List[CarePlanActivity]] = None
    note: Optional[List[Annotation]] = None