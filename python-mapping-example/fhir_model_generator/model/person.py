#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Person) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .address import Address
from .attachment import Attachment
from .backboneelement import BackboneElement
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier


@dataclass
class PersonLink(BackboneElement):
    """ Link to a resource that concerns the same actual person.
    """
    resource_type: ClassVar[str] = "PersonLink"

    target: FHIRReference = None
    assurance: Optional[str] = None


@dataclass
class Person(DomainResource):
    """ A generic person record.

    Demographics and administrative information about a person independent of a
    specific health-related context.
    """
    resource_type: ClassVar[str] = "Person"

    identifier: Optional[List[Identifier]] = None
    name: Optional[List[HumanName]] = None
    telecom: Optional[List[ContactPoint]] = None
    gender: Optional[str] = None
    birthDate: Optional[FHIRDate] = None
    address: Optional[List[Address]] = None
    photo: Optional[Attachment] = None
    managingOrganization: Optional[FHIRReference] = None
    active: Optional[bool] = None
    link: Optional[List[PersonLink]] = None