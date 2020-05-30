#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ResearchElementDefinition) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
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
from .usagecontext import UsageContext


@dataclass
class ResearchElementDefinitionCharacteristic(BackboneElement):
    """ What defines the members of the research element.

    A characteristic that defines the members of the research element. Multiple
    characteristics are applied with "and" semantics.
    """
    resource_type: ClassVar[str] = "ResearchElementDefinitionCharacteristic"

    definitionCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='definition',))
    definitionCanonical: str = field(default=None, metadata=dict(one_of_many='definition',))
    definitionExpression: Expression = field(default=None, metadata=dict(one_of_many='definition',))
    definitionDataRequirement: DataRequirement = field(default=None, metadata=dict(one_of_many='definition',))
    usageContext: Optional[List[UsageContext]] = None
    exclude: Optional[bool] = None
    unitOfMeasure: Optional[CodeableConcept] = None
    studyEffectiveDescription: Optional[str] = None
    studyEffectiveDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='studyEffective',))
    studyEffectivePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='studyEffective',))
    studyEffectiveDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='studyEffective',))
    studyEffectiveTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='studyEffective',))
    studyEffectiveTimeFromStart: Optional[Duration] = None
    studyEffectiveGroupMeasure: Optional[str] = None
    participantEffectiveDescription: Optional[str] = None
    participantEffectiveDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='participantEffective',))
    participantEffectivePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='participantEffective',))
    participantEffectiveDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='participantEffective',))
    participantEffectiveTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='participantEffective',))
    participantEffectiveTimeFromStart: Optional[Duration] = None
    participantEffectiveGroupMeasure: Optional[str] = None


@dataclass
class ResearchElementDefinition(DomainResource):
    """ A population, intervention, or exposure definition.

    The ResearchElementDefinition resource describes a "PICO" element that
    knowledge (evidence, assertion, recommendation) is about.
    """
    resource_type: ClassVar[str] = "ResearchElementDefinition"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    shortTitle: Optional[str] = None
    subtitle: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    subjectCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='subject',))
    subjectReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='subject',))
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    comment: Optional[List[str]] = None
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
    type: str = None
    variableType: Optional[str] = None
    characteristic: List[ResearchElementDefinitionCharacteristic] = field(default_factory=list)