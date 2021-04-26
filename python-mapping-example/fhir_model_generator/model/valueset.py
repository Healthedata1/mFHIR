#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ValueSet) on 2020-02-10.
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
class ValueSetExpansionParameter(BackboneElement):
    """ Parameter that controlled the expansion process.

    A parameter that controlled the expansion process. These parameters may be
    used by users of expanded value sets to check whether the expansion is
    suitable for a particular purpose, or to pick the correct expansion.
    """
    resource_type: ClassVar[str] = "ValueSetExpansionParameter"

    name: str = None
    valueString: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='value',))
    valueInteger: Optional[int] = field(default=None, metadata=dict(one_of_many='value',))
    valueDecimal: Optional[float] = field(default=None, metadata=dict(one_of_many='value',))
    valueUri: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueCode: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class ValueSetExpansionContains(BackboneElement):
    """ Codes in the value set.

    The codes that are contained in the value set expansion.
    """
    resource_type: ClassVar[str] = "ValueSetExpansionContains"

    system: Optional[str] = None
    abstract: Optional[bool] = None
    inactive: Optional[bool] = None
    version: Optional[str] = None
    code: Optional[str] = None
    display: Optional[str] = None
    designation: Optional[List["ValueSetComposeIncludeConceptDesignation"]] = None
    contains: Optional[List["ValueSetExpansionContains"]] = None


@dataclass
class ValueSetComposeIncludeConceptDesignation(BackboneElement):
    """ Additional representations for this concept.

    Additional representations for this concept when used in this value set -
    other languages, aliases, specialized purposes, used for particular
    purposes, etc.
    """
    resource_type: ClassVar[str] = "ValueSetComposeIncludeConceptDesignation"

    language: Optional[str] = None
    use: Optional[Coding] = None
    value: str = None


@dataclass
class ValueSetComposeIncludeConcept(BackboneElement):
    """ A concept defined in the system.

    Specifies a concept to be included or excluded.
    """
    resource_type: ClassVar[str] = "ValueSetComposeIncludeConcept"

    code: str = None
    display: Optional[str] = None
    designation: Optional[List[ValueSetComposeIncludeConceptDesignation]] = None


@dataclass
class ValueSetComposeIncludeFilter(BackboneElement):
    """ Select codes/concepts by their properties (including relationships).

    Select concepts by specify a matching criterion based on the properties
    (including relationships) defined by the system, or on filters defined by
    the system. If multiple filters are specified, they SHALL all be true.
    """
    resource_type: ClassVar[str] = "ValueSetComposeIncludeFilter"

    property: str = None
    op: str = None
    value: str = None


@dataclass
class ValueSetComposeInclude(BackboneElement):
    """ Include one or more codes from a code system or other value set(s).
    """
    resource_type: ClassVar[str] = "ValueSetComposeInclude"

    system: Optional[str] = None
    version: Optional[str] = None
    concept: Optional[List[ValueSetComposeIncludeConcept]] = None
    filter: Optional[List[ValueSetComposeIncludeFilter]] = None
    valueSet: Optional[List[str]] = None


@dataclass
class ValueSetCompose(BackboneElement):
    """ Content logical definition of the value set (CLD).

    A set of criteria that define the contents of the value set by including or
    excluding codes selected from the specified code system(s) that the value
    set draws from. This is also known as the Content Logical Definition (CLD).
    """
    resource_type: ClassVar[str] = "ValueSetCompose"

    lockedDate: Optional[FHIRDate] = None
    inactive: Optional[bool] = None
    include: List[ValueSetComposeInclude] = field(default_factory=list)
    exclude: Optional[List[ValueSetComposeInclude]] = None


@dataclass
class ValueSetExpansion(BackboneElement):
    """ Used when the value set is "expanded".

    A value set can also be "expanded", where the value set is turned into a
    simple collection of enumerated codes. This element holds the expansion, if
    it has been performed.
    """
    resource_type: ClassVar[str] = "ValueSetExpansion"

    identifier: Optional[str] = None
    timestamp: FHIRDate = None
    total: Optional[int] = None
    offset: Optional[int] = None
    parameter: Optional[List[ValueSetExpansionParameter]] = None
    contains: Optional[List[ValueSetExpansionContains]] = None


@dataclass
class ValueSet(DomainResource):
    """ A set of codes drawn from one or more code systems.

    A ValueSet resource instance specifies a set of codes drawn from one or
    more code systems, intended for use in a particular context. Value sets
    link between [CodeSystem](codesystem.html) definitions and their use in
    [coded elements](terminologies.html).
    """
    resource_type: ClassVar[str] = "ValueSet"

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
    immutable: Optional[bool] = None
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    compose: Optional[ValueSetCompose] = None
    expansion: Optional[ValueSetExpansion] = None