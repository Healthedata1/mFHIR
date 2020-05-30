#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period
from .usagecontext import UsageContext


@dataclass
class ChargeItemDefinitionPropertyGroupPriceComponent(BackboneElement):
    """ Components of total line item price.

    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice of how the prices have been calculated.
    """
    resource_type: ClassVar[str] = "ChargeItemDefinitionPropertyGroupPriceComponent"

    type: str = None
    code: Optional[CodeableConcept] = None
    factor: Optional[float] = None
    amount: Optional[Money] = None


@dataclass
class ChargeItemDefinitionApplicability(BackboneElement):
    """ Whether or not the billing code is applicable.

    Expressions that describe applicability criteria for the billing code.
    """
    resource_type: ClassVar[str] = "ChargeItemDefinitionApplicability"

    description: Optional[str] = None
    language: Optional[str] = None
    expression: Optional[str] = None


@dataclass
class ChargeItemDefinitionPropertyGroup(BackboneElement):
    """ Group of properties which are applicable under the same conditions.

    Group of properties which are applicable under the same conditions. If no
    applicability rules are established for the group, then all properties
    always apply.
    """
    resource_type: ClassVar[str] = "ChargeItemDefinitionPropertyGroup"

    applicability: Optional[List[ChargeItemDefinitionApplicability]] = None
    priceComponent: Optional[List[ChargeItemDefinitionPropertyGroupPriceComponent]] = None


@dataclass
class ChargeItemDefinition(DomainResource):
    """ Definition of properties and rules about how the price and the
    applicability of a ChargeItem can be determined.

    The ChargeItemDefinition resource provides the properties that apply to the
    (billing) codes necessary to calculate costs and prices. The properties may
    differ largely depending on type and realm, therefore this resource gives
    only a rough structure and requires profiling for each type of billing code
    system.
    """
    resource_type: ClassVar[str] = "ChargeItemDefinition"

    url: str = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    title: Optional[str] = None
    derivedFromUri: Optional[List[str]] = None
    partOf: Optional[List[str]] = None
    replaces: Optional[List[str]] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    copyright: Optional[str] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    code: Optional[CodeableConcept] = None
    instance: Optional[List[FHIRReference]] = None
    applicability: Optional[List[ChargeItemDefinitionApplicability]] = None
    propertyGroup: Optional[List[ChargeItemDefinitionPropertyGroup]] = None