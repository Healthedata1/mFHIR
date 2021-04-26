#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class ImmunizationRecommendationRecommendationDateCriterion(BackboneElement):
    """ Dates governing proposed immunization.

    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendationRecommendationDateCriterion"

    code: CodeableConcept = None
    value: FHIRDate = None


@dataclass
class ImmunizationRecommendationRecommendation(BackboneElement):
    """ Vaccine administration recommendations.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendationRecommendation"

    vaccineCode: Optional[List[CodeableConcept]] = None
    targetDisease: Optional[CodeableConcept] = None
    contraindicatedVaccineCode: Optional[List[CodeableConcept]] = None
    forecastStatus: CodeableConcept = None
    forecastReason: Optional[List[CodeableConcept]] = None
    dateCriterion: Optional[List[ImmunizationRecommendationRecommendationDateCriterion]] = None
    description: Optional[str] = None
    series: Optional[str] = None
    doseNumberPositiveInt: Optional[int] = field(default=None, metadata=dict(one_of_many='doseNumber',))
    doseNumberString: Optional[str] = field(default=None, metadata=dict(one_of_many='doseNumber',))
    seriesDosesPositiveInt: Optional[int] = field(default=None, metadata=dict(one_of_many='seriesDoses',))
    seriesDosesString: Optional[str] = field(default=None, metadata=dict(one_of_many='seriesDoses',))
    supportingImmunization: Optional[List[FHIRReference]] = None
    supportingPatientInformation: Optional[List[FHIRReference]] = None


@dataclass
class ImmunizationRecommendation(DomainResource):
    """ Guidance or advice relating to an immunization.

    A patient's point-in-time set of recommendations (i.e. forecasting)
    according to a published schedule with optional supporting justification.
    """
    resource_type: ClassVar[str] = "ImmunizationRecommendation"

    identifier: Optional[List[Identifier]] = None
    patient: FHIRReference = None
    date: FHIRDate = None
    authority: Optional[FHIRReference] = None
    recommendation: List[ImmunizationRecommendationRecommendation] = field(default_factory=list)