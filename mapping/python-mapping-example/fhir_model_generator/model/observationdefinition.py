#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ObservationDefinition) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .range import Range


@dataclass
class ObservationDefinitionQuantitativeDetails(BackboneElement):
    """ Characteristics of quantitative results.

    Characteristics for quantitative results of this observation.
    """
    resource_type: ClassVar[str] = "ObservationDefinitionQuantitativeDetails"

    customaryUnit: Optional[CodeableConcept] = None
    unit: Optional[CodeableConcept] = None
    conversionFactor: Optional[float] = None
    decimalPrecision: Optional[int] = None


@dataclass
class ObservationDefinitionQualifiedInterval(BackboneElement):
    """ Qualified range for continuous and ordinal observation results.

    Multiple  ranges of results qualified by different contexts for ordinal or
    continuous observations conforming to this ObservationDefinition.
    """
    resource_type: ClassVar[str] = "ObservationDefinitionQualifiedInterval"

    category: Optional[str] = None
    range: Optional[Range] = None
    context: Optional[CodeableConcept] = None
    appliesTo: Optional[List[CodeableConcept]] = None
    gender: Optional[str] = None
    age: Optional[Range] = None
    gestationalAge: Optional[Range] = None
    condition: Optional[str] = None


@dataclass
class ObservationDefinition(DomainResource):
    """ Definition of an observation.

    Set of definitional characteristics for a kind of observation or
    measurement produced or consumed by an orderable health care service.
    """
    resource_type: ClassVar[str] = "ObservationDefinition"

    category: Optional[List[CodeableConcept]] = None
    code: CodeableConcept = None
    identifier: Optional[List[Identifier]] = None
    permittedDataType: Optional[List[str]] = None
    multipleResultsAllowed: Optional[bool] = None
    method: Optional[CodeableConcept] = None
    preferredReportName: Optional[str] = None
    quantitativeDetails: Optional[ObservationDefinitionQuantitativeDetails] = None
    qualifiedInterval: Optional[List[ObservationDefinitionQualifiedInterval]] = None
    validCodedValueSet: Optional[FHIRReference] = None
    normalCodedValueSet: Optional[FHIRReference] = None
    abnormalCodedValueSet: Optional[FHIRReference] = None
    criticalCodedValueSet: Optional[FHIRReference] = None