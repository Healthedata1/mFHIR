#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/EffectEvidenceSynthesis) on 2020-02-10.
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
class EffectEvidenceSynthesisCertaintyCertaintySubcomponent(BackboneElement):
    """ A component that contributes to the overall certainty.

    A description of a component of the overall certainty.
    """
    resource_type: ClassVar[str] = "EffectEvidenceSynthesisCertaintyCertaintySubcomponent"

    type: Optional[CodeableConcept] = None
    rating: Optional[List[CodeableConcept]] = None
    note: Optional[List[Annotation]] = None


@dataclass
class EffectEvidenceSynthesisEffectEstimatePrecisionEstimate(BackboneElement):
    """ How precise the estimate is.

    A description of the precision of the estimate for the effect.
    """
    resource_type: ClassVar[str] = "EffectEvidenceSynthesisEffectEstimatePrecisionEstimate"

    type: Optional[CodeableConcept] = None
    level: Optional[float] = None
    from_fhir: Optional[float] = field(default=None, metadata=dict(orig_name='from'))
    to: Optional[float] = None


@dataclass
class EffectEvidenceSynthesisSampleSize(BackboneElement):
    """ What sample size was involved?.

    A description of the size of the sample involved in the synthesis.
    """
    resource_type: ClassVar[str] = "EffectEvidenceSynthesisSampleSize"

    description: Optional[str] = None
    numberOfStudies: Optional[int] = None
    numberOfParticipants: Optional[int] = None


@dataclass
class EffectEvidenceSynthesisResultsByExposure(BackboneElement):
    """ What was the result per exposure?.

    A description of the results for each exposure considered in the effect
    estimate.
    """
    resource_type: ClassVar[str] = "EffectEvidenceSynthesisResultsByExposure"

    description: Optional[str] = None
    exposureState: Optional[str] = None
    variantState: Optional[CodeableConcept] = None
    riskEvidenceSynthesis: FHIRReference = None


@dataclass
class EffectEvidenceSynthesisEffectEstimate(BackboneElement):
    """ What was the estimated effect.

    The estimated effect of the exposure variant.
    """
    resource_type: ClassVar[str] = "EffectEvidenceSynthesisEffectEstimate"

    description: Optional[str] = None
    type: Optional[CodeableConcept] = None
    variantState: Optional[CodeableConcept] = None
    value: Optional[float] = None
    unitOfMeasure: Optional[CodeableConcept] = None
    precisionEstimate: Optional[List[EffectEvidenceSynthesisEffectEstimatePrecisionEstimate]] = None


@dataclass
class EffectEvidenceSynthesisCertainty(BackboneElement):
    """ How certain is the effect.

    A description of the certainty of the effect estimate.
    """
    resource_type: ClassVar[str] = "EffectEvidenceSynthesisCertainty"

    rating: Optional[List[CodeableConcept]] = None
    note: Optional[List[Annotation]] = None
    certaintySubcomponent: Optional[List[EffectEvidenceSynthesisCertaintyCertaintySubcomponent]] = None


@dataclass
class EffectEvidenceSynthesis(DomainResource):
    """ A quantified estimate of effect based on a body of evidence.

    The EffectEvidenceSynthesis resource describes the difference in an outcome
    between exposures states in a population where the effect estimate is
    derived from a combination of research studies.
    """
    resource_type: ClassVar[str] = "EffectEvidenceSynthesis"

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
    exposure: FHIRReference = None
    exposureAlternative: FHIRReference = None
    outcome: FHIRReference = None
    sampleSize: Optional[EffectEvidenceSynthesisSampleSize] = None
    resultsByExposure: Optional[List[EffectEvidenceSynthesisResultsByExposure]] = None
    effectEstimate: Optional[List[EffectEvidenceSynthesisEffectEstimate]] = None
    certainty: Optional[List[EffectEvidenceSynthesisCertainty]] = None