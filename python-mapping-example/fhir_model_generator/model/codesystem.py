#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CodeSystem) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .identifier import Identifier
from .usagecontext import UsageContext


@dataclass
class CodeSystemConceptDesignation(BackboneElement):
    """ Additional representations for the concept.

    Additional representations for the concept - other languages, aliases,
    specialized purposes, used for particular purposes, etc.
    """
    resource_type: ClassVar[str] = "CodeSystemConceptDesignation"

    language: Optional[str] = None
    use: Optional[Coding] = None
    value: str = None


@dataclass
class CodeSystemConceptProperty(BackboneElement):
    """ Property value for the concept.

    A property value for this concept.
    """
    resource_type: ClassVar[str] = "CodeSystemConceptProperty"

    code: str = None
    valueCode: str = field(default=None, metadata=dict(one_of_many='value',))
    valueCoding: Coding = field(default=None, metadata=dict(one_of_many='value',))
    valueString: str = field(default=None, metadata=dict(one_of_many='value',))
    valueInteger: int = field(default=None, metadata=dict(one_of_many='value',))
    valueBoolean: bool = field(default=None, metadata=dict(one_of_many='value',))
    valueDateTime: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueDecimal: float = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class CodeSystemFilter(BackboneElement):
    """ Filter that can be used in a value set.

    A filter that can be used in a value set compose statement when selecting
    concepts using a filter.
    """
    resource_type: ClassVar[str] = "CodeSystemFilter"

    code: str = None
    description: Optional[str] = None
    operator: List[str] = field(default_factory=list)
    value: str = None


@dataclass
class CodeSystemProperty(BackboneElement):
    """ Additional information supplied about each concept.

    A property defines an additional slot through which additional information
    can be provided about a concept.
    """
    resource_type: ClassVar[str] = "CodeSystemProperty"

    code: str = None
    uri: Optional[str] = None
    description: Optional[str] = None
    type: str = None


@dataclass
class CodeSystemConcept(BackboneElement):
    """ Concepts in the code system.

    Concepts that are in the code system. The concept definitions are
    inherently hierarchical, but the definitions must be consulted to determine
    what the meanings of the hierarchical relationships are.
    """
    resource_type: ClassVar[str] = "CodeSystemConcept"

    code: str = None
    display: Optional[str] = None
    definition: Optional[str] = None
    designation: Optional[List[CodeSystemConceptDesignation]] = None
    property: Optional[List[CodeSystemConceptProperty]] = None
    concept: Optional[List["CodeSystemConcept"]] = None


@dataclass
class CodeSystem(DomainResource):
    """ Declares the existence of and describes a code system or code system
    supplement.

    The CodeSystem resource is used to declare the existence of and describe a
    code system or code system supplement and its key properties, and
    optionally define a part or all of its content.
    """
    resource_type: ClassVar[str] = "CodeSystem"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
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
    caseSensitive: Optional[bool] = None
    valueSet: Optional[str] = None
    hierarchyMeaning: Optional[str] = None
    compositional: Optional[bool] = None
    versionNeeded: Optional[bool] = None
    content: str = None
    supplements: Optional[str] = None
    count: Optional[int] = None
    filter: Optional[List[CodeSystemFilter]] = None
    property: Optional[List[CodeSystemProperty]] = None
    concept: Optional[List[CodeSystemConcept]] = None