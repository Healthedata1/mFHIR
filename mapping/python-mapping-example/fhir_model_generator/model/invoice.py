#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Invoice) on 2020-02-10.
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


@dataclass
class InvoiceLineItemPriceComponent(BackboneElement):
    """ Components of total line item price.

    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice as to how the prices have been calculated.
    """
    resource_type: ClassVar[str] = "InvoiceLineItemPriceComponent"

    type: str = None
    code: Optional[CodeableConcept] = None
    factor: Optional[float] = None
    amount: Optional[Money] = None


@dataclass
class InvoiceParticipant(BackboneElement):
    """ Participant in creation of this Invoice.

    Indicates who or what performed or participated in the charged service.
    """
    resource_type: ClassVar[str] = "InvoiceParticipant"

    role: Optional[CodeableConcept] = None
    actor: FHIRReference = None


@dataclass
class InvoiceLineItem(BackboneElement):
    """ Line items of this Invoice.

    Each line item represents one charge for goods and services rendered.
    Details such as date, code and amount are found in the referenced
    ChargeItem resource.
    """
    resource_type: ClassVar[str] = "InvoiceLineItem"

    sequence: Optional[int] = None
    chargeItemReference: FHIRReference = field(default=None, metadata=dict(one_of_many='chargeItem',))
    chargeItemCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='chargeItem',))
    priceComponent: Optional[List[InvoiceLineItemPriceComponent]] = None


@dataclass
class Invoice(DomainResource):
    """ Invoice containing ChargeItems from an Account.

    Invoice containing collected ChargeItems from an Account with calculated
    individual and total price for Billing purpose.
    """
    resource_type: ClassVar[str] = "Invoice"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    cancelledReason: Optional[str] = None
    type: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    recipient: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    participant: Optional[List[InvoiceParticipant]] = None
    issuer: Optional[FHIRReference] = None
    account: Optional[FHIRReference] = None
    lineItem: Optional[List[InvoiceLineItem]] = None
    totalPriceComponent: Optional[List[InvoiceLineItemPriceComponent]] = None
    totalNet: Optional[Money] = None
    totalGross: Optional[Money] = None
    paymentTerms: Optional[str] = None
    note: Optional[List[Annotation]] = None