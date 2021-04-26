#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period


@dataclass
class PaymentReconciliationDetail(BackboneElement):
    """ Settlement particulars.

    Distribution of the payment amount for a previously acknowledged payable.
    """
    resource_type: ClassVar[str] = "PaymentReconciliationDetail"

    identifier: Optional[Identifier] = None
    predecessor: Optional[Identifier] = None
    type: CodeableConcept = None
    request: Optional[FHIRReference] = None
    submitter: Optional[FHIRReference] = None
    response: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    responsible: Optional[FHIRReference] = None
    payee: Optional[FHIRReference] = None
    amount: Optional[Money] = None


@dataclass
class PaymentReconciliationProcessNote(BackboneElement):
    """ Note concerning processing.

    A note that describes or explains the processing in a human readable form.
    """
    resource_type: ClassVar[str] = "PaymentReconciliationProcessNote"

    type: Optional[str] = None
    text: Optional[str] = None


@dataclass
class PaymentReconciliation(DomainResource):
    """ PaymentReconciliation resource.

    This resource provides the details including amount of a payment and
    allocates the payment items being paid.
    """
    resource_type: ClassVar[str] = "PaymentReconciliation"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    period: Optional[Period] = None
    created: FHIRDate = None
    paymentIssuer: Optional[FHIRReference] = None
    request: Optional[FHIRReference] = None
    requestor: Optional[FHIRReference] = None
    outcome: Optional[str] = None
    disposition: Optional[str] = None
    paymentDate: FHIRDate = None
    paymentAmount: Money = None
    paymentIdentifier: Optional[Identifier] = None
    detail: Optional[List[PaymentReconciliationDetail]] = None
    formCode: Optional[CodeableConcept] = None
    processNote: Optional[List[PaymentReconciliationProcessNote]] = None