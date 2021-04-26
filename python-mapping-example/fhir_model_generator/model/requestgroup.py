#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/RequestGroup) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .age import Age
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .duration import Duration
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .range import Range
from .relatedartifact import RelatedArtifact
from .timing import Timing


@dataclass
class RequestGroupActionCondition(BackboneElement):
    """ Whether or not the action is applicable.

    An expression that describes applicability criteria, or start/stop
    conditions for the action.
    """
    resource_type: ClassVar[str] = "RequestGroupActionCondition"

    kind: str = None
    expression: Optional[Expression] = None


@dataclass
class RequestGroupActionRelatedAction(BackboneElement):
    """ Relationship to another action.

    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    resource_type: ClassVar[str] = "RequestGroupActionRelatedAction"

    actionId: str = None
    relationship: str = None
    offsetDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='offset',))
    offsetRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='offset',))


@dataclass
class RequestGroupAction(BackboneElement):
    """ Proposed actions, if any.

    The actions, if any, produced by the evaluation of the artifact.
    """
    resource_type: ClassVar[str] = "RequestGroupAction"

    prefix: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    textEquivalent: Optional[str] = None
    priority: Optional[str] = None
    code: Optional[List[CodeableConcept]] = None
    documentation: Optional[List[RelatedArtifact]] = None
    condition: Optional[List[RequestGroupActionCondition]] = None
    relatedAction: Optional[List[RequestGroupActionRelatedAction]] = None
    timingDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='timing',))
    timingAge: Optional[Age] = field(default=None, metadata=dict(one_of_many='timing',))
    timingPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='timing',))
    timingDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='timing',))
    timingRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='timing',))
    timingTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='timing',))
    participant: Optional[List[FHIRReference]] = None
    type: Optional[CodeableConcept] = None
    groupingBehavior: Optional[str] = None
    selectionBehavior: Optional[str] = None
    requiredBehavior: Optional[str] = None
    precheckBehavior: Optional[str] = None
    cardinalityBehavior: Optional[str] = None
    resource: Optional[FHIRReference] = None
    action: Optional[List["RequestGroupAction"]] = None


@dataclass
class RequestGroup(DomainResource):
    """ A group of related requests.

    A group of related requests that can be used to capture intended activities
    that have inter-dependencies such as "give this medication after that one".
    """
    resource_type: ClassVar[str] = "RequestGroup"

    identifier: Optional[List[Identifier]] = None
    instantiatesCanonical: Optional[List[str]] = None
    instantiatesUri: Optional[List[str]] = None
    basedOn: Optional[List[FHIRReference]] = None
    replaces: Optional[List[FHIRReference]] = None
    groupIdentifier: Optional[Identifier] = None
    status: str = None
    intent: str = None
    priority: Optional[str] = None
    code: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    authoredOn: Optional[FHIRDate] = None
    author: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None
    action: Optional[List[RequestGroupAction]] = None