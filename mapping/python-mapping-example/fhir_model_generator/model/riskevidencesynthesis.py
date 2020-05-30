#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/RiskEvidenceSynthesis) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .relatedartifact import RelatedArtifact
from .usagecontext import UsageContext


@dataclass
class RiskEvidenceSynthesisCertaintyCertaintySubcomponent(BackboneElement):
    """ A component that contributes to the overall certainty.

    A description of a component of the overall certainty.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesisCertaintyCertaintySubcomponent"

    type: Optional[CodeableConcept] = None
    rating: Optional[List[CodeableConcept]] = None
    note: Optional[List[Annotation]] = None


@dataclass
class RiskEvidenceSynthesisRiskEstimatePrecisionEstimate(BackboneElement):
    """ How precise the estimate is.

    A description of the precision of the estimate for the effect.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesisRiskEstimatePrecisionEstimate"

    type: Optional[CodeableConcept] = None
    level: Optional[float] = None
    from_fhir: Optional[float] = field(default=None, metadata=dict(orig_name='from'))
    to: Optional[float] = None


@dataclass
class RiskEvidenceSynthesisSampleSize(BackboneElement):
    """ What sample size was involved?.

    A description of the size of the sample involved in the synthesis.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesisSampleSize"

    description: Optional[str] = None
    numberOfStudies: Optional[int] = None
    numberOfParticipants: Optional[int] = None


@dataclass
class RiskEvidenceSynthesisRiskEstimate(BackboneElement):
    """ What was the estimated risk.

    The estimated risk of the outcome.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesisRiskEstimate"

    description: Optional[str] = None
    type: Optional[CodeableConcept] = None
    value: Optional[float] = None
    unitOfMeasure: Optional[CodeableConcept] = None
    denominatorCount: Optional[int] = None
    numeratorCount: Optional[int] = None
    precisionEstimate: Optional[List[RiskEvidenceSynthesisRiskEstimatePrecisionEstimate]] = None


@dataclass
class RiskEvidenceSynthesisCertainty(BackboneElement):
    """ How certain is the risk.

    A description of the certainty of the risk estimate.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesisCertainty"

    rating: Optional[List[CodeableConcept]] = None
    note: Optional[List[Annotation]] = None
    certaintySubcomponent: Optional[List[RiskEvidenceSynthesisCertaintyCertaintySubcomponent]] = None


@dataclass
class RiskEvidenceSynthesis(DomainResource):
    """ A quantified estimate of risk based on a body of evidence.

    The RiskEvidenceSynthesis resource describes the likelihood of an outcome
    in a population plus exposure state where the risk estimate is derived from
    a combination of research studies.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesis"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
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
    synthesisType: Optional[CodeableConcept] = None
    studyType: Optional[CodeableConcept] = None
    population: FHIRReference = None
    exposure: Optional[FHIRReference] = None
    outcome: FHIRReference = None
    sampleSize: Optional[RiskEvidenceSynthesisSampleSize] = None
    riskEstimate: Optional[RiskEvidenceSynthesisRiskEstimate] = None
    certainty: Optional[List[RiskEvidenceSynthesisCertainty]] = None