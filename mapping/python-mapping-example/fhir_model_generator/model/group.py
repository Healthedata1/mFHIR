#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Group) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range


@dataclass
class GroupCharacteristic(BackboneElement):
    """ Include / Exclude group members by Trait.

    Identifies traits whose presence r absence is shared by members of the
    group.
    """
    resource_type: ClassVar[str] = "GroupCharacteristic"

    code: CodeableConcept = None
    valueCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='value',))
    valueBoolean: bool = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Quantity = field(default=None, metadata=dict(one_of_many='value',))
    valueRange: Range = field(default=None, metadata=dict(one_of_many='value',))
    valueReference: FHIRReference = field(default=None, metadata=dict(one_of_many='value',))
    exclude: bool = None
    period: Optional[Period] = None


@dataclass
class GroupMember(BackboneElement):
    """ Who or what is in group.

    Identifies the resource instances that are members of the group.
    """
    resource_type: ClassVar[str] = "GroupMember"

    entity: FHIRReference = None
    period: Optional[Period] = None
    inactive: Optional[bool] = None


@dataclass
class Group(DomainResource):
    """ Group of multiple entities.

    Represents a defined collection of entities that may be discussed or acted
    upon collectively but which are not expected to act collectively, and are
    not formally or legally recognized; i.e. a collection of entities that
    isn't an Organization.
    """
    resource_type: ClassVar[str] = "Group"

    identifier: Optional[List[Identifier]] = None
    active: Optional[bool] = None
    type: str = None
    actual: bool = None
    code: Optional[CodeableConcept] = None
    name: Optional[str] = None
    quantity: Optional[int] = None
    managingEntity: Optional[FHIRReference] = None
    characteristic: Optional[List[GroupCharacteristic]] = None
    member: Optional[List[GroupMember]] = None