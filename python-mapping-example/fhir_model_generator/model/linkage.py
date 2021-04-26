#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Linkage) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .domainresource import DomainResource
from .fhirreference import FHIRReference


@dataclass
class LinkageItem(BackboneElement):
    """ Item to be linked.

    Identifies which record considered as the reference to the same real-world
    occurrence as well as how the items should be evaluated within the
    collection of linked items.
    """
    resource_type: ClassVar[str] = "LinkageItem"

    type: str = None
    resource: FHIRReference = None


@dataclass
class Linkage(DomainResource):
    """ Links records for 'same' item.

    Identifies two or more records (resource instances) that refer to the same
    real-world "occurrence".
    """
    resource_type: ClassVar[str] = "Linkage"

    active: Optional[bool] = None
    author: Optional[FHIRReference] = None
    item: List[LinkageItem] = field(default_factory=list)