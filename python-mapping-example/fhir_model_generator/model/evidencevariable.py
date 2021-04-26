#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/EvidenceVariable) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
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
from .relatedartifact import RelatedArtifact
from .timing import Timing
from .triggerdefinition import TriggerDefinition
from .usagecontext import UsageContext


@dataclass
class EvidenceVariableCharacteristic(BackboneElement):
    """ What defines the members of the evidence element.

    A characteristic that defines the members of the evidence element. Multiple
    characteristics are applied with "and" semantics.
    """
    resource_type: ClassVar[str] = "EvidenceVariableCharacteristic"

    description: Optional[str] = None
    definitionReference: FHIRReference = field(default=None, metadata=dict(one_of_many='definition',))
    definitionCanonical: str = field(default=None, metadata=dict(one_of_many='definition',))
    definitionCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='definition',))
    definitionExpression: Expression = field(default=None, metadata=dict(one_of_many='definition',))
    definitionDataRequirement: DataRequirement = field(default=None, metadata=dict(one_of_many='definition',))
    definitionTriggerDefinition: TriggerDefinition = field(default=None, metadata=dict(one_of_many='definition',))
    usageContext: Optional[List[UsageContext]] = None
    exclude: Optional[bool] = None
    participantEffectiveDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='participantEffective',))
    participantEffectivePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='participantEffective',))
    participantEffectiveDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='participantEffective',))
    participantEffectiveTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='participantEffective',))
    timeFromStart: Optional[Duration] = None
    groupMeasure: Optional[str] = None


@dataclass
class EvidenceVariable(DomainResource):
    """ A population, intervention, or exposure definition.

    The EvidenceVariable resource describes a "PICO" element that knowledge
    (evidence, assertion, recommendation) is about.
    """
    resource_type: ClassVar[str] = "EvidenceVariable"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    shortTitle: Optional[str] = None
    subtitle: Optional[str] = None
    status: str = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    note: Optional[List[Annotation]] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
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
    type: Optional[str] = None
    characteristic: List[EvidenceVariableCharacteristic] = field(default_factory=list)