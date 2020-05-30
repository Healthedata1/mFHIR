#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Goal) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .duration import Duration
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .range import Range
from .ratio import Ratio


@dataclass
class GoalTarget(BackboneElement):
    """ Target outcome for the goal.

    Indicates what should be done by when.
    """
    resource_type: ClassVar[str] = "GoalTarget"

    measure: Optional[CodeableConcept] = None
    detailQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='detail',))
    detailRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='detail',))
    detailCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='detail',))
    detailString: Optional[str] = field(default=None, metadata=dict(one_of_many='detail',))
    detailBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='detail',))
    detailInteger: Optional[int] = field(default=None, metadata=dict(one_of_many='detail',))
    detailRatio: Optional[Ratio] = field(default=None, metadata=dict(one_of_many='detail',))
    dueDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='due',))
    dueDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='due',))


@dataclass
class Goal(DomainResource):
    """ Describes the intended objective(s) for a patient, group or organization.

    Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """
    resource_type: ClassVar[str] = "Goal"

    identifier: Optional[List[Identifier]] = None
    lifecycleStatus: str = None
    achievementStatus: Optional[CodeableConcept] = None
    category: Optional[List[CodeableConcept]] = None
    priority: Optional[CodeableConcept] = None
    description: CodeableConcept = None
    subject: FHIRReference = None
    startDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='start',))
    startCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='start',))
    target: Optional[List[GoalTarget]] = None
    statusDate: Optional[FHIRDate] = None
    statusReason: Optional[str] = None
    expressedBy: Optional[FHIRReference] = None
    addresses: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None
    outcomeCode: Optional[List[CodeableConcept]] = None
    outcomeReference: Optional[List[FHIRReference]] = None