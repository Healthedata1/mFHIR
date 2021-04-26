#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SearchParameter) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .usagecontext import UsageContext


@dataclass
class SearchParameterComponent(BackboneElement):
    """ For Composite resources to define the parts.

    Used to define the parts of a composite search parameter.
    """
    resource_type: ClassVar[str] = "SearchParameterComponent"

    definition: str = None
    expression: str = None


@dataclass
class SearchParameter(DomainResource):
    """ Search parameter for a resource.

    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """
    resource_type: ClassVar[str] = "SearchParameter"

    url: str = None
    version: Optional[str] = None
    name: str = None
    derivedFrom: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: str = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    purpose: Optional[str] = None
    code: str = None
    base: List[str] = field(default_factory=list)
    type: str = None
    expression: Optional[str] = None
    xpath: Optional[str] = None
    xpathUsage: Optional[str] = None
    target: Optional[List[str]] = None
    multipleOr: Optional[bool] = None
    multipleAnd: Optional[bool] = None
    comparator: Optional[List[str]] = None
    modifier: Optional[List[str]] = None
    chain: Optional[List[str]] = None
    component: Optional[List[SearchParameterComponent]] = None