#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/PlanDefinition) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .age import Age
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .datarequirement import DataRequirement
from .domainresource import DomainResource
from .duration import Duration
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .relatedartifact import RelatedArtifact
from .timing import Timing
from .triggerdefinition import TriggerDefinition
from .usagecontext import UsageContext


@dataclass
class PlanDefinitionActionCondition(BackboneElement):
    """ Whether or not the action is applicable.

    An expression that describes applicability criteria or start/stop
    conditions for the action.
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionCondition"

    kind: str = None
    expression: Optional[Expression] = None


@dataclass
class PlanDefinitionActionRelatedAction(BackboneElement):
    """ Relationship to another action.

    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionRelatedAction"

    actionId: str = None
    relationship: str = None
    offsetDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='offset',))
    offsetRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='offset',))


@dataclass
class PlanDefinitionActionParticipant(BackboneElement):
    """ Who should participate in the action.

    Indicates who should participate in performing the action described.
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionParticipant"

    type: str = None
    role: Optional[CodeableConcept] = None


@dataclass
class PlanDefinitionActionDynamicValue(BackboneElement):
    """ Dynamic aspects of the definition.

    Customizations that should be applied to the statically defined resource.
    For example, if the dosage of a medication must be computed based on the
    patient's weight, a customization would be used to specify an expression
    that calculated the weight, and the path on the resource that would contain
    the result.
    """
    resource_type: ClassVar[str] = "PlanDefinitionActionDynamicValue"

    path: Optional[str] = None
    expression: Optional[Expression] = None


@dataclass
class PlanDefinitionGoalTarget(BackboneElement):
    """ Target outcome for the goal.

    Indicates what should be done and within what timeframe.
    """
    resource_type: ClassVar[str] = "PlanDefinitionGoalTarget"

    measure: Optional[CodeableConcept] = None
    detailQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='detail',))
    detailRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='detail',))
    detailCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='detail',))
    due: Optional[Duration] = None


@dataclass
class PlanDefinitionGoal(BackboneElement):
    """ What the plan is trying to accomplish.

    Goals that describe what the activities within the plan are intended to
    achieve. For example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """
    resource_type: ClassVar[str] = "PlanDefinitionGoal"

    category: Optional[CodeableConcept] = None
    description: CodeableConcept = None
    priority: Optional[CodeableConcept] = None
    start: Optional[CodeableConcept] = None
    addresses: Optional[List[CodeableConcept]] = None
    documentation: Optional[List[RelatedArtifact]] = None
    target: Optional[List[PlanDefinitionGoalTarget]] = None


@dataclass
class PlanDefinitionAction(BackboneElement):
    """ Action defined by the plan.

    An action or group of actions to be taken as part of the plan.
    """
    resource_type: ClassVar[str] = "PlanDefinitionAction"

    prefix: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    textEquivalent: Optional[str] = None
    priority: Optional[str] = None
    code: Optional[List[CodeableConcept]] = None
    reason: Optional[List[CodeableConcept]] = None
    documentation: Optional[List[RelatedArtifact]] = None
    goalId: Optional[List[str]] = None
    subjectCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='subject',))
    subjectReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='subject',))
    trigger: Optional[List[TriggerDefinition]] = None
    condition: Optional[List[PlanDefinitionActionCondition]] = None
    input: Optional[List[DataRequirement]] = None
    output: Optional[List[DataRequirement]] = None
    relatedAction: Optional[List[PlanDefinitionActionRelatedAction]] = None
    timingDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='timing',))
    timingAge: Optional[Age] = field(default=None, metadata=dict(one_of_many='timing',))
    timingPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='timing',))
    timingDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='timing',))
    timingRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='timing',))
    timingTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='timing',))
    participant: Optional[List[PlanDefinitionActionParticipant]] = None
    type: Optional[CodeableConcept] = None
    groupingBehavior: Optional[str] = None
    selectionBehavior: Optional[str] = None
    requiredBehavior: Optional[str] = None
    precheckBehavior: Optional[str] = None
    cardinalityBehavior: Optional[str] = None
    definitionCanonical: Optional[str] = field(default=None, metadata=dict(one_of_many='definition',))
    definitionUri: Optional[str] = field(default=None, metadata=dict(one_of_many='definition',))
    transform: Optional[str] = None
    dynamicValue: Optional[List[PlanDefinitionActionDynamicValue]] = None
    action: Optional[List["PlanDefinitionAction"]] = None


@dataclass
class PlanDefinition(DomainResource):
    """ The definition of a plan for a series of actions, independent of any
    specific patient or context.

    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """
    resource_type: ClassVar[str] = "PlanDefinition"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
    type: Optional[CodeableConcept] = None
    status: str = None
    experimental: Optional[bool] = None
    subjectCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='subject',))
    subjectReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='subject',))
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    purpose: Optional[str] = None
    usage: Optional[str] = None
    copyright: Optional[str] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    topic: Optional[List[CodeableConcept]] = None
    author: Optional[List[ContactDetail]] = None
    editor: Optional[List[ContactDetail]] = None
    reviewer: Optional[List[ContactDetail]] = None
    endorser: Optional[List[ContactDetail]] = None
    relatedArtifact: Optional[List[RelatedArtifact]] = None
    library: Optional[List[str]] = None
    goal: Optional[List[PlanDefinitionGoal]] = None
    action: Optional[List[PlanDefinitionAction]] = None