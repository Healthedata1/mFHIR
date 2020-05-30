#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ClaimResponse) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .address import Address
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period
from .quantity import Quantity


@dataclass
class ClaimResponseAddItemDetailSubDetail(BackboneElement):
    """ Insurer added line items.

    The third-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ClaimResponseAddItemDetailSubDetail"

    productOrService: CodeableConcept = None
    modifier: Optional[List[CodeableConcept]] = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = None
    adjudication: List["ClaimResponseItemAdjudication"] = field(default_factory=list)


@dataclass
class ClaimResponseAddItemDetail(BackboneElement):
    """ Insurer added line details.

    The second-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ClaimResponseAddItemDetail"

    productOrService: CodeableConcept = None
    modifier: Optional[List[CodeableConcept]] = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = None
    adjudication: List["ClaimResponseItemAdjudication"] = field(default_factory=list)
    subDetail: Optional[List[ClaimResponseAddItemDetailSubDetail]] = None


@dataclass
class ClaimResponseItemDetailSubDetail(BackboneElement):
    """ Adjudication for claim sub-details.

    A sub-detail adjudication of a simple product or service.
    """
    resource_type: ClassVar[str] = "ClaimResponseItemDetailSubDetail"

    subDetailSequence: int = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List["ClaimResponseItemAdjudication"]] = None


@dataclass
class ClaimResponseItemAdjudication(BackboneElement):
    """ Adjudication details.

    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
    """
    resource_type: ClassVar[str] = "ClaimResponseItemAdjudication"

    category: CodeableConcept = None
    reason: Optional[CodeableConcept] = None
    amount: Optional[Money] = None
    value: Optional[float] = None


@dataclass
class ClaimResponseItemDetail(BackboneElement):
    """ Adjudication for claim details.

    A claim detail. Either a simple (a product or service) or a 'group' of sub-
    details which are simple items.
    """
    resource_type: ClassVar[str] = "ClaimResponseItemDetail"

    detailSequence: int = None
    noteNumber: Optional[List[int]] = None
    adjudication: List[ClaimResponseItemAdjudication] = field(default_factory=list)
    subDetail: Optional[List[ClaimResponseItemDetailSubDetail]] = None


@dataclass
class ClaimResponseItem(BackboneElement):
    """ Adjudication for claim line items.

    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
    """
    resource_type: ClassVar[str] = "ClaimResponseItem"

    itemSequence: int = None
    noteNumber: Optional[List[int]] = None
    adjudication: List[ClaimResponseItemAdjudication] = field(default_factory=list)
    detail: Optional[List[ClaimResponseItemDetail]] = None


@dataclass
class ClaimResponseAddItem(BackboneElement):
    """ Insurer added line items.

    The first-tier service adjudications for payor added product or service
    lines.
    """
    resource_type: ClassVar[str] = "ClaimResponseAddItem"

    itemSequence: Optional[List[int]] = None
    detailSequence: Optional[List[int]] = None
    subdetailSequence: Optional[List[int]] = None
    provider: Optional[List[FHIRReference]] = None
    productOrService: CodeableConcept = None
    modifier: Optional[List[CodeableConcept]] = None
    programCode: Optional[List[CodeableConcept]] = None
    servicedDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='serviced',))
    servicedPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='serviced',))
    locationCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='location',))
    locationAddress: Optional[Address] = field(default=None, metadata=dict(one_of_many='location',))
    locationReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='location',))
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    bodySite: Optional[CodeableConcept] = None
    subSite: Optional[List[CodeableConcept]] = None
    noteNumber: Optional[List[int]] = None
    adjudication: List[ClaimResponseItemAdjudication] = field(default_factory=list)
    detail: Optional[List[ClaimResponseAddItemDetail]] = None


@dataclass
class ClaimResponseTotal(BackboneElement):
    """ Adjudication totals.

    Categorized monetary totals for the adjudication.
    """
    resource_type: ClassVar[str] = "ClaimResponseTotal"

    category: CodeableConcept = None
    amount: Money = None


@dataclass
class ClaimResponsePayment(BackboneElement):
    """ Payment Details.

    Payment details for the adjudication of the claim.
    """
    resource_type: ClassVar[str] = "ClaimResponsePayment"

    type: CodeableConcept = None
    adjustment: Optional[Money] = None
    adjustmentReason: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    amount: Money = None
    identifier: Optional[Identifier] = None


@dataclass
class ClaimResponseProcessNote(BackboneElement):
    """ Note concerning adjudication.

    A note that describes or explains adjudication results in a human readable
    form.
    """
    resource_type: ClassVar[str] = "ClaimResponseProcessNote"

    number: Optional[int] = None
    type: Optional[str] = None
    text: str = None
    language: Optional[CodeableConcept] = None


@dataclass
class ClaimResponseInsurance(BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    resource_type: ClassVar[str] = "ClaimResponseInsurance"

    sequence: int = None
    focal: bool = None
    coverage: FHIRReference = None
    businessArrangement: Optional[str] = None
    claimResponse: Optional[FHIRReference] = None


@dataclass
class ClaimResponseError(BackboneElement):
    """ Processing errors.

    Errors encountered during the processing of the adjudication.
    """
    resource_type: ClassVar[str] = "ClaimResponseError"

    itemSequence: Optional[int] = None
    detailSequence: Optional[int] = None
    subDetailSequence: Optional[int] = None
    code: CodeableConcept = None


@dataclass
class ClaimResponse(DomainResource):
    """ Response to a claim predetermination or preauthorization.

    This resource provides the adjudication details from the processing of a
    Claim resource.
    """
    resource_type: ClassVar[str] = "ClaimResponse"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    type: CodeableConcept = None
    subType: Optional[CodeableConcept] = None
    use: str = None
    patient: FHIRReference = None
    created: FHIRDate = None
    insurer: FHIRReference = None
    requestor: Optional[FHIRReference] = None
    request: Optional[FHIRReference] = None
    outcome: str = None
    disposition: Optional[str] = None
    preAuthRef: Optional[str] = None
    preAuthPeriod: Optional[Period] = None
    payeeType: Optional[CodeableConcept] = None
    item: Optional[List[ClaimResponseItem]] = None
    addItem: Optional[List[ClaimResponseAddItem]] = None
    adjudication: Optional[List[ClaimResponseItemAdjudication]] = None
    total: Optional[List[ClaimResponseTotal]] = None
    payment: Optional[ClaimResponsePayment] = None
    fundsReserve: Optional[CodeableConcept] = None
    formCode: Optional[CodeableConcept] = None
    form: Optional[Attachment] = None
    processNote: Optional[List[ClaimResponseProcessNote]] = None
    communicationRequest: Optional[List[FHIRReference]] = None
    insurance: Optional[List[ClaimResponseInsurance]] = None
    error: Optional[List[ClaimResponseError]] = None