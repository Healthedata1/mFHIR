#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/StructureDefinition) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .elementdefinition import ElementDefinition
from .fhirdate import FHIRDate
from .identifier import Identifier
from .usagecontext import UsageContext


@dataclass
class StructureDefinitionMapping(BackboneElement):
    """ External specification that the content is mapped to.

    An external specification that the content is mapped to.
    """
    resource_type: ClassVar[str] = "StructureDefinitionMapping"

    identity: str = None
    uri: Optional[str] = None
    name: Optional[str] = None
    comment: Optional[str] = None


@dataclass
class StructureDefinitionContext(BackboneElement):
    """ If an extension, where it can be used in instances.

    Identifies the types of resource or data type elements to which the
    extension can be applied.
    """
    resource_type: ClassVar[str] = "StructureDefinitionContext"

    type: str = None
    expression: str = None


@dataclass
class StructureDefinitionSnapshot(BackboneElement):
    """ Snapshot view of the structure.

    A snapshot view is expressed in a standalone form that can be used and
    interpreted without considering the base StructureDefinition.
    """
    resource_type: ClassVar[str] = "StructureDefinitionSnapshot"

    element: List[ElementDefinition] = field(default_factory=list)


@dataclass
class StructureDefinitionDifferential(BackboneElement):
    """ Differential view of the structure.

    A differential view is expressed relative to the base StructureDefinition -
    a statement of differences that it applies.
    """
    resource_type: ClassVar[str] = "StructureDefinitionDifferential"

    element: List[ElementDefinition] = field(default_factory=list)


@dataclass
class StructureDefinition(DomainResource):
    """ Structural Definition.

    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions and constraints on resources and data types.
    """
    resource_type: ClassVar[str] = "StructureDefinition"

    url: str = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: str = None
    title: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    keyword: Optional[List[Coding]] = None
    fhirVersion: Optional[str] = None
    mapping: Optional[List[StructureDefinitionMapping]] = None
    kind: str = None
    abstract: bool = None
    context: Optional[List[StructureDefinitionContext]] = None
    contextInvariant: Optional[List[str]] = None
    type: str = None
    baseDefinition: Optional[str] = None
    derivation: Optional[str] = None
    snapshot: Optional[StructureDefinitionSnapshot] = None
    differential: Optional[StructureDefinitionDifferential] = None