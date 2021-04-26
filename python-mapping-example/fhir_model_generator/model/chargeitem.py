#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ChargeItem) on 2020-02-10.
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
from .money import Money
from .period import Period
from .quantity import Quantity
from .timing import Timing


@dataclass
class ChargeItemPerformer(BackboneElement):
    """ Who performed charged service.

    Indicates who or what performed or participated in the charged service.
    """
    resource_type: ClassVar[str] = "ChargeItemPerformer"

    function: Optional[CodeableConcept] = None
    actor: FHIRReference = None


@dataclass
class ChargeItem(DomainResource):
    """ Item containing charge code(s) associated with the provision of healthcare
    provider products.

    The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the
    product, but containing in addition details of the provision, like date,
    time, amounts and participating organizations and persons. Main Usage of
    the ChargeItem is to enable the billing process and internal cost
    allocation.
    """
    resource_type: ClassVar[str] = "ChargeItem"

    identifier: Optional[List[Identifier]] = None
    definitionUri: Optional[List[str]] = None
    definitionCanonical: Optional[List[str]] = None
    status: str = None
    partOf: Optional[List[FHIRReference]] = None
    code: CodeableConcept = None
    subject: FHIRReference = None
    context: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrencePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrenceTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='occurrence',))
    performer: Optional[List[ChargeItemPerformer]] = None
    performingOrganization: Optional[FHIRReference] = None
    requestingOrganization: Optional[FHIRReference] = None
    costCenter: Optional[FHIRReference] = None
    quantity: Optional[Quantity] = None
    bodysite: Optional[List[CodeableConcept]] = None
    factorOverride: Optional[float] = None
    priceOverride: Optional[Money] = None
    overrideReason: Optional[str] = None
    enterer: Optional[FHIRReference] = None
    enteredDate: Optional[FHIRDate] = None
    reason: Optional[List[CodeableConcept]] = None
    service: Optional[List[FHIRReference]] = None
    productReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='product',))
    productCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='product',))
    account: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None
    supportingInformation: Optional[List[FHIRReference]] = None