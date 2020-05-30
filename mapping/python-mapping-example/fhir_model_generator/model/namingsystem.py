#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/NamingSystem) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .period import Period
from .usagecontext import UsageContext


@dataclass
class NamingSystemUniqueId(BackboneElement):
    """ Unique identifiers used for system.

    Indicates how the system may be identified when referenced in electronic
    exchange.
    """
    resource_type: ClassVar[str] = "NamingSystemUniqueId"

    type: str = None
    value: str = None
    preferred: Optional[bool] = None
    comment: Optional[str] = None
    period: Optional[Period] = None


@dataclass
class NamingSystem(DomainResource):
    """ System of unique identification.

    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """
    resource_type: ClassVar[str] = "NamingSystem"

    name: str = None
    status: str = None
    kind: str = None
    date: FHIRDate = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    responsible: Optional[str] = None
    type: Optional[CodeableConcept] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    usage: Optional[str] = None
    uniqueId: List[NamingSystemUniqueId] = field(default_factory=list)