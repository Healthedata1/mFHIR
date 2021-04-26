#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Organization) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .address import Address
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier


@dataclass
class OrganizationContact(BackboneElement):
    """ Contact for the organization for a certain purpose.
    """
    resource_type: ClassVar[str] = "OrganizationContact"

    purpose: Optional[CodeableConcept] = None
    name: Optional[HumanName] = None
    telecom: Optional[List[ContactPoint]] = None
    address: Optional[Address] = None


@dataclass
class Organization(DomainResource):
    """ A grouping of people or organizations with a common purpose.

    A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, payer/insurer, etc.
    """
    resource_type: ClassVar[str] = "Organization"

    identifier: Optional[List[Identifier]] = None
    active: Optional[bool] = None
    type: Optional[List[CodeableConcept]] = None
    name: Optional[str] = None
    alias: Optional[List[str]] = None
    telecom: Optional[List[ContactPoint]] = None
    address: Optional[List[Address]] = None
    partOf: Optional[FHIRReference] = None
    contact: Optional[List[OrganizationContact]] = None
    endpoint: Optional[List[FHIRReference]] = None