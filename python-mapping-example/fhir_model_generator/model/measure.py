#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Measure) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .relatedartifact import RelatedArtifact
from .usagecontext import UsageContext


@dataclass
class MeasureGroupStratifierComponent(BackboneElement):
    """ Stratifier criteria component for the measure.

    A component of the stratifier criteria for the measure report, specified as
    either the name of a valid CQL expression defined within a referenced
    library or a valid FHIR Resource Path.
    """
    resource_type: ClassVar[str] = "MeasureGroupStratifierComponent"

    code: Optional[CodeableConcept] = None
    description: Optional[str] = None
    criteria: Expression = None


@dataclass
class MeasureGroupPopulation(BackboneElement):
    """ Population criteria.

    A population criteria for the measure.
    """
    resource_type: ClassVar[str] = "MeasureGroupPopulation"

    code: Optional[CodeableConcept] = None
    description: Optional[str] = None
    criteria: Expression = None


@dataclass
class MeasureGroupStratifier(BackboneElement):
    """ Stratifier criteria for the measure.

    The stratifier criteria for the measure report, specified as either the
    name of a valid CQL expression defined within a referenced library or a
    valid FHIR Resource Path.
    """
    resource_type: ClassVar[str] = "MeasureGroupStratifier"

    code: Optional[CodeableConcept] = None
    description: Optional[str] = None
    criteria: Optional[Expression] = None
    component: Optional[List[MeasureGroupStratifierComponent]] = None


@dataclass
class MeasureGroup(BackboneElement):
    """ Population criteria group.

    A group of population criteria for the measure.
    """
    resource_type: ClassVar[str] = "MeasureGroup"

    code: Optional[CodeableConcept] = None
    description: Optional[str] = None
    population: Optional[List[MeasureGroupPopulation]] = None
    stratifier: Optional[List[MeasureGroupStratifier]] = None


@dataclass
class MeasureSupplementalData(BackboneElement):
    """ What other data should be reported with the measure.

    The supplemental data criteria for the measure report, specified as either
    the name of a valid CQL expression within a referenced library, or a valid
    FHIR Resource Path.
    """
    resource_type: ClassVar[str] = "MeasureSupplementalData"

    code: Optional[CodeableConcept] = None
    usage: Optional[List[CodeableConcept]] = None
    description: Optional[str] = None
    criteria: Expression = None


@dataclass
class Measure(DomainResource):
    """ A quality measure definition.

    The Measure resource provides the definition of a quality measure.
    """
    resource_type: ClassVar[str] = "Measure"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
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
    disclaimer: Optional[str] = None
    scoring: Optional[CodeableConcept] = None
    compositeScoring: Optional[CodeableConcept] = None
    type: Optional[List[CodeableConcept]] = None
    riskAdjustment: Optional[str] = None
    rateAggregation: Optional[str] = None
    rationale: Optional[str] = None
    clinicalRecommendationStatement: Optional[str] = None
    improvementNotation: Optional[CodeableConcept] = None
    definition: Optional[List[str]] = None
    guidance: Optional[str] = None
    group: Optional[List[MeasureGroup]] = None
    supplementalData: Optional[List[MeasureSupplementalData]] = None