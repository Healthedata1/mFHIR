#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ConceptMap) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .identifier import Identifier
from .usagecontext import UsageContext


@dataclass
class ConceptMapGroupElementTargetDependsOn(BackboneElement):
    """ Other elements required for this mapping (from context).

    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """
    resource_type: ClassVar[str] = "ConceptMapGroupElementTargetDependsOn"

    property: str = None
    system: Optional[str] = None
    value: str = None
    display: Optional[str] = None


@dataclass
class ConceptMapGroupElementTarget(BackboneElement):
    """ Concept in target system for element.

    A concept from the target value set that this concept maps to.
    """
    resource_type: ClassVar[str] = "ConceptMapGroupElementTarget"

    code: Optional[str] = None
    display: Optional[str] = None
    equivalence: str = None
    comment: Optional[str] = None
    dependsOn: Optional[List[ConceptMapGroupElementTargetDependsOn]] = None
    product: Optional[List[ConceptMapGroupElementTargetDependsOn]] = None


@dataclass
class ConceptMapGroupElement(BackboneElement):
    """ Mappings for a concept from the source set.

    Mappings for an individual concept in the source to one or more concepts in
    the target.
    """
    resource_type: ClassVar[str] = "ConceptMapGroupElement"

    code: Optional[str] = None
    display: Optional[str] = None
    target: Optional[List[ConceptMapGroupElementTarget]] = None


@dataclass
class ConceptMapGroupUnmapped(BackboneElement):
    """ What to do when there is no mapping for the source concept.

    What to do when there is no mapping for the source concept. "Unmapped" does
    not include codes that are unmatched, and the unmapped element is ignored
    in a code is specified to have equivalence = unmatched.
    """
    resource_type: ClassVar[str] = "ConceptMapGroupUnmapped"

    mode: str = None
    code: Optional[str] = None
    display: Optional[str] = None
    url: Optional[str] = None


@dataclass
class ConceptMapGroup(BackboneElement):
    """ Same source and target systems.

    A group of mappings that all have the same source and target system.
    """
    resource_type: ClassVar[str] = "ConceptMapGroup"

    source: Optional[str] = None
    sourceVersion: Optional[str] = None
    target: Optional[str] = None
    targetVersion: Optional[str] = None
    element: List[ConceptMapGroupElement] = field(default_factory=list)
    unmapped: Optional[ConceptMapGroupUnmapped] = None


@dataclass
class ConceptMap(DomainResource):
    """ A map from one set of concepts to one or more other concepts.

    A statement of relationships from one set of concepts to one or more other
    concepts - either concepts in code systems, or data element/data element
    concepts, or classes in class models.
    """
    resource_type: ClassVar[str] = "ConceptMap"

    url: Optional[str] = None
    identifier: Optional[Identifier] = None
    version: Optional[str] = None
    name: Optional[str] = None
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
    sourceUri: Optional[str] = field(default=None, metadata=dict(one_of_many='source',))
    sourceCanonical: Optional[str] = field(default=None, metadata=dict(one_of_many='source',))
    targetUri: Optional[str] = field(default=None, metadata=dict(one_of_many='target',))
    targetCanonical: Optional[str] = field(default=None, metadata=dict(one_of_many='target',))
    group: Optional[List[ConceptMapGroup]] = None