#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/List) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class ListEntry(BackboneElement):
    """ Entries in the list.

    Entries in this list.
    """
    resource_type: ClassVar[str] = "ListEntry"

    flag: Optional[CodeableConcept] = None
    deleted: Optional[bool] = None
    date: Optional[FHIRDate] = None
    item: FHIRReference = None


@dataclass
class List(DomainResource):
    """ A list is a curated collection of resources.
    """
    resource_type: ClassVar[str] = "List"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    mode: str = None
    title: Optional[str] = None
    code: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    source: Optional[FHIRReference] = None
    orderedBy: Optional[CodeableConcept] = None
    note: Optional[List[Annotation]] = None
    entry: Optional[List[ListEntry]] = None
    emptyReason: Optional[CodeableConcept] = None