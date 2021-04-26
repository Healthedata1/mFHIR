#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MeasureReport) on 2020-02-10.
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
from .period import Period
from .quantity import Quantity


@dataclass
class MeasureReportGroupStratifierStratumComponent(BackboneElement):
    """ Stratifier component values.

    A stratifier component value.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifierStratumComponent"

    code: CodeableConcept = None
    value: CodeableConcept = None


@dataclass
class MeasureReportGroupStratifierStratumPopulation(BackboneElement):
    """ Population results in this stratum.

    The populations that make up the stratum, one for each type of population
    appropriate to the measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifierStratumPopulation"

    code: Optional[CodeableConcept] = None
    count: Optional[int] = None
    subjectResults: Optional[FHIRReference] = None


@dataclass
class MeasureReportGroupStratifierStratum(BackboneElement):
    """ Stratum results, one for each unique value, or set of values, in the
    stratifier, or stratifier components.

    This element contains the results for a single stratum within the
    stratifier. For example, when stratifying on administrative gender, there
    will be four strata, one for each possible gender value.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifierStratum"

    value: Optional[CodeableConcept] = None
    component: Optional[List[MeasureReportGroupStratifierStratumComponent]] = None
    population: Optional[List[MeasureReportGroupStratifierStratumPopulation]] = None
    measureScore: Optional[Quantity] = None


@dataclass
class MeasureReportGroupPopulation(BackboneElement):
    """ The populations in the group.

    The populations that make up the population group, one for each type of
    population appropriate for the measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupPopulation"

    code: Optional[CodeableConcept] = None
    count: Optional[int] = None
    subjectResults: Optional[FHIRReference] = None


@dataclass
class MeasureReportGroupStratifier(BackboneElement):
    """ Stratification results.

    When a measure includes multiple stratifiers, there will be a stratifier
    group for each stratifier defined by the measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifier"

    code: Optional[List[CodeableConcept]] = None
    stratum: Optional[List[MeasureReportGroupStratifierStratum]] = None


@dataclass
class MeasureReportGroup(BackboneElement):
    """ Measure results for each group.

    The results of the calculation, one for each population group in the
    measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroup"

    code: Optional[CodeableConcept] = None
    population: Optional[List[MeasureReportGroupPopulation]] = None
    measureScore: Optional[Quantity] = None
    stratifier: Optional[List[MeasureReportGroupStratifier]] = None


@dataclass
class MeasureReport(DomainResource):
    """ Results of a measure evaluation.

    The MeasureReport resource contains the results of the calculation of a
    measure; and optionally a reference to the resources involved in that
    calculation.
    """
    resource_type: ClassVar[str] = "MeasureReport"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    type: str = None
    measure: str = None
    subject: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    reporter: Optional[FHIRReference] = None
    period: Period = None
    improvementNotation: Optional[CodeableConcept] = None
    group: Optional[List[MeasureReportGroup]] = None
    evaluatedResource: Optional[List[FHIRReference]] = None