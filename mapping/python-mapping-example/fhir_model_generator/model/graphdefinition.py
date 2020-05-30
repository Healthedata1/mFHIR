#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/GraphDefinition) on 2020-02-10.
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
class GraphDefinitionLinkTargetCompartment(BackboneElement):
    """ Compartment Consistency Rules.
    """
    resource_type: ClassVar[str] = "GraphDefinitionLinkTargetCompartment"

    use: str = None
    code: str = None
    rule: str = None
    expression: Optional[str] = None
    description: Optional[str] = None


@dataclass
class GraphDefinitionLinkTarget(BackboneElement):
    """ Potential target for the link.
    """
    resource_type: ClassVar[str] = "GraphDefinitionLinkTarget"

    type: str = None
    params: Optional[str] = None
    profile: Optional[str] = None
    compartment: Optional[List[GraphDefinitionLinkTargetCompartment]] = None
    link: Optional[List["GraphDefinitionLink"]] = None


@dataclass
class GraphDefinitionLink(BackboneElement):
    """ Links this graph makes rules about.
    """
    resource_type: ClassVar[str] = "GraphDefinitionLink"

    path: Optional[str] = None
    sliceName: Optional[str] = None
    min: Optional[int] = None
    max: Optional[str] = None
    description: Optional[str] = None
    target: Optional[List[GraphDefinitionLinkTarget]] = None


@dataclass
class GraphDefinition(DomainResource):
    """ Definition of a graph of resources.

    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references. The
    Graph Definition resource defines a set and makes rules about the set.
    """
    resource_type: ClassVar[str] = "GraphDefinition"

    url: Optional[str] = None
    version: Optional[str] = None
    name: str = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    purpose: Optional[str] = None
    start: str = None
    profile: Optional[str] = None
    link: Optional[List[GraphDefinitionLink]] = None