#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DataRequirement) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .coding import Coding
from .duration import Duration
from .element import Element
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .period import Period


@dataclass
class DataRequirementCodeFilter(Element):
    """ What codes are expected.

    Code filters specify additional constraints on the data, specifying the
    value set of interest for a particular element of the data. Each code
    filter defines an additional constraint on the data, i.e. code filters are
    AND'ed, not OR'ed.
    """
    resource_type: ClassVar[str] = "DataRequirementCodeFilter"

    path: Optional[str] = None
    searchParam: Optional[str] = None
    valueSet: Optional[str] = None
    code: Optional[List[Coding]] = None


@dataclass
class DataRequirementDateFilter(Element):
    """ What dates/date ranges are expected.

    Date filters specify additional constraints on the data in terms of the
    applicable date range for specific elements. Each date filter specifies an
    additional constraint on the data, i.e. date filters are AND'ed, not OR'ed.
    """
    resource_type: ClassVar[str] = "DataRequirementDateFilter"

    path: Optional[str] = None
    searchParam: Optional[str] = None
    valueDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valuePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='value',))
    valueDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class DataRequirementSort(Element):
    """ Order of the results.

    Specifies the order of the results to be returned.
    """
    resource_type: ClassVar[str] = "DataRequirementSort"

    path: str = None
    direction: str = None


@dataclass
class DataRequirement(Element):
    """ Describes a required data item.

    Describes a required data item for evaluation in terms of the type of data,
    and optional code or date-based filters of the data.
    """
    resource_type: ClassVar[str] = "DataRequirement"

    type: str = None
    profile: Optional[List[str]] = None
    subjectCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='subject',))
    subjectReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='subject',))
    mustSupport: Optional[List[str]] = None
    codeFilter: Optional[List[DataRequirementCodeFilter]] = None
    dateFilter: Optional[List[DataRequirementDateFilter]] = None
    limit: Optional[int] = None
    sort: Optional[List[DataRequirementSort]] = None