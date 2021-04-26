#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .address import Address
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period
from .quantity import Quantity


@dataclass
class ExplanationOfBenefitBenefitBalanceFinancial(BackboneElement):
    """ Benefit Summary.

    Benefits Used to date.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitBenefitBalanceFinancial"

    type: CodeableConcept = None
    allowedUnsignedInt: Optional[int] = field(default=None, metadata=dict(one_of_many='allowed',))
    allowedString: Optional[str] = field(default=None, metadata=dict(one_of_many='allowed',))
    allowedMoney: Optional[Money] = field(default=None, metadata=dict(one_of_many='allowed',))
    usedUnsignedInt: Optional[int] = field(default=None, metadata=dict(one_of_many='used',))
    usedMoney: Optional[Money] = field(default=None, metadata=dict(one_of_many='used',))


@dataclass
class ExplanationOfBenefitAddItemDetailSubDetail(BackboneElement):
    """ Insurer added line items.

    The third-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAddItemDetailSubDetail"

    productOrService: CodeableConcept = None
    modifier: Optional[List[CodeableConcept]] = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List["ExplanationOfBenefitItemAdjudication"]] = None


@dataclass
class ExplanationOfBenefitAddItemDetail(BackboneElement):
    """ Insurer added line items.

    The second-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAddItemDetail"

    productOrService: CodeableConcept = None
    modifier: Optional[List[CodeableConcept]] = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List["ExplanationOfBenefitItemAdjudication"]] = None
    subDetail: Optional[List[ExplanationOfBenefitAddItemDetailSubDetail]] = None


@dataclass
class ExplanationOfBenefitItemDetailSubDetail(BackboneElement):
    """ Additional items.

    Third-tier of goods and services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItemDetailSubDetail"

    sequence: int = None
    revenue: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    productOrService: CodeableConcept = None
    modifier: Optional[List[CodeableConcept]] = None
    programCode: Optional[List[CodeableConcept]] = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    udi: Optional[List[FHIRReference]] = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List["ExplanationOfBenefitItemAdjudication"]] = None


@dataclass
class ExplanationOfBenefitItemAdjudication(BackboneElement):
    """ Adjudication details.

    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItemAdjudication"

    category: CodeableConcept = None
    reason: Optional[CodeableConcept] = None
    amount: Optional[Money] = None
    value: Optional[float] = None


@dataclass
class ExplanationOfBenefitItemDetail(BackboneElement):
    """ Additional items.

    Second-tier of goods and services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItemDetail"

    sequence: int = None
    revenue: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    productOrService: CodeableConcept = None
    modifier: Optional[List[CodeableConcept]] = None
    programCode: Optional[List[CodeableConcept]] = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    net: Optional[Money] = None
    udi: Optional[List[FHIRReference]] = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = None
    subDetail: Optional[List[ExplanationOfBenefitItemDetailSubDetail]] = None


@dataclass
class ExplanationOfBenefitRelated(BackboneElement):
    """ Prior or corollary claims.

    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitRelated"

    claim: Optional[FHIRReference] = None
    relationship: Optional[CodeableConcept] = None
    reference: Optional[Identifier] = None


@dataclass
class ExplanationOfBenefitPayee(BackboneElement):
    """ Recipient of benefits payable.

    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitPayee"

    type: Optional[CodeableConcept] = None
    party: Optional[FHIRReference] = None


@dataclass
class ExplanationOfBenefitCareTeam(BackboneElement):
    """ Care Team members.

    The members of the team who provided the products and services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitCareTeam"

    sequence: int = None
    provider: FHIRReference = None
    responsible: Optional[bool] = None
    role: Optional[CodeableConcept] = None
    qualification: Optional[CodeableConcept] = None


@dataclass
class ExplanationOfBenefitSupportingInfo(BackboneElement):
    """ Supporting information.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitSupportingInfo"

    sequence: int = None
    category: CodeableConcept = None
    code: Optional[CodeableConcept] = None
    timingDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='timing',))
    timingPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='timing',))
    valueBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='value',))
    valueString: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='value',))
    valueAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='value',))
    valueReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='value',))
    reason: Optional[Coding] = None


@dataclass
class ExplanationOfBenefitDiagnosis(BackboneElement):
    """ Pertinent diagnosis information.

    Information about diagnoses relevant to the claim items.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitDiagnosis"

    sequence: int = None
    diagnosisCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='diagnosis',))
    diagnosisReference: FHIRReference = field(default=None, metadata=dict(one_of_many='diagnosis',))
    type: Optional[List[CodeableConcept]] = None
    onAdmission: Optional[CodeableConcept] = None
    packageCode: Optional[CodeableConcept] = None


@dataclass
class ExplanationOfBenefitProcedure(BackboneElement):
    """ Clinical procedures performed.

    Procedures performed on the patient relevant to the billing items with the
    claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitProcedure"

    sequence: int = None
    type: Optional[List[CodeableConcept]] = None
    date: Optional[FHIRDate] = None
    procedureCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='procedure',))
    procedureReference: FHIRReference = field(default=None, metadata=dict(one_of_many='procedure',))
    udi: Optional[List[FHIRReference]] = None


@dataclass
class ExplanationOfBenefitInsurance(BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitInsurance"

    focal: bool = None
    coverage: FHIRReference = None
    preAuthRef: Optional[List[str]] = None


@dataclass
class ExplanationOfBenefitAccident(BackboneElement):
    """ Details of the event.

    Details of a accident which resulted in injuries which required the
    products and services listed in the claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAccident"

    date: Optional[FHIRDate] = None
    type: Optional[CodeableConcept] = None
    locationAddress: Optional[Address] = field(default=None, metadata=dict(one_of_many='location',))
    locationReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='location',))


@dataclass
class ExplanationOfBenefitItem(BackboneElement):
    """ Product or service provided.

    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItem"

    sequence: int = None
    careTeamSequence: Optional[List[int]] = None
    diagnosisSequence: Optional[List[int]] = None
    procedureSequence: Optional[List[int]] = None
    informationSequence: Optional[List[int]] = None
    revenue: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
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
    udi: Optional[List[FHIRReference]] = None
    bodySite: Optional[CodeableConcept] = None
    subSite: Optional[List[CodeableConcept]] = None
    encounter: Optional[List[FHIRReference]] = None
    noteNumber: Optional[List[int]] = None
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = None
    detail: Optional[List[ExplanationOfBenefitItemDetail]] = None


@dataclass
class ExplanationOfBenefitAddItem(BackboneElement):
    """ Insurer added line items.

    The first-tier service adjudications for payor added product or service
    lines.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAddItem"

    itemSequence: Optional[List[int]] = None
    detailSequence: Optional[List[int]] = None
    subDetailSequence: Optional[List[int]] = None
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
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = None
    detail: Optional[List[ExplanationOfBenefitAddItemDetail]] = None


@dataclass
class ExplanationOfBenefitTotal(BackboneElement):
    """ Adjudication totals.

    Categorized monetary totals for the adjudication.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitTotal"

    category: CodeableConcept = None
    amount: Money = None


@dataclass
class ExplanationOfBenefitPayment(BackboneElement):
    """ Payment Details.

    Payment details for the adjudication of the claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitPayment"

    type: Optional[CodeableConcept] = None
    adjustment: Optional[Money] = None
    adjustmentReason: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    amount: Optional[Money] = None
    identifier: Optional[Identifier] = None


@dataclass
class ExplanationOfBenefitProcessNote(BackboneElement):
    """ Note concerning adjudication.

    A note that describes or explains adjudication results in a human readable
    form.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitProcessNote"

    number: Optional[int] = None
    type: Optional[str] = None
    text: Optional[str] = None
    language: Optional[CodeableConcept] = None


@dataclass
class ExplanationOfBenefitBenefitBalance(BackboneElement):
    """ Balance by Benefit Category.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitBenefitBalance"

    category: CodeableConcept = None
    excluded: Optional[bool] = None
    name: Optional[str] = None
    description: Optional[str] = None
    network: Optional[CodeableConcept] = None
    unit: Optional[CodeableConcept] = None
    term: Optional[CodeableConcept] = None
    financial: Optional[List[ExplanationOfBenefitBenefitBalanceFinancial]] = None


@dataclass
class ExplanationOfBenefit(DomainResource):
    """ Explanation of Benefit resource.

    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefit"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    type: CodeableConcept = None
    subType: Optional[CodeableConcept] = None
    use: str = None
    patient: FHIRReference = None
    billablePeriod: Optional[Period] = None
    created: FHIRDate = None
    enterer: Optional[FHIRReference] = None
    insurer: FHIRReference = None
    provider: FHIRReference = None
    priority: Optional[CodeableConcept] = None
    fundsReserveRequested: Optional[CodeableConcept] = None
    fundsReserve: Optional[CodeableConcept] = None
    related: Optional[List[ExplanationOfBenefitRelated]] = None
    prescription: Optional[FHIRReference] = None
    originalPrescription: Optional[FHIRReference] = None
    payee: Optional[ExplanationOfBenefitPayee] = None
    referral: Optional[FHIRReference] = None
    facility: Optional[FHIRReference] = None
    claim: Optional[FHIRReference] = None
    claimResponse: Optional[FHIRReference] = None
    outcome: str = None
    disposition: Optional[str] = None
    preAuthRef: Optional[List[str]] = None
    preAuthRefPeriod: Optional[List[Period]] = None
    careTeam: Optional[List[ExplanationOfBenefitCareTeam]] = None
    supportingInfo: Optional[List[ExplanationOfBenefitSupportingInfo]] = None
    diagnosis: Optional[List[ExplanationOfBenefitDiagnosis]] = None
    procedure: Optional[List[ExplanationOfBenefitProcedure]] = None
    precedence: Optional[int] = None
    insurance: List[ExplanationOfBenefitInsurance] = field(default_factory=list)
    accident: Optional[ExplanationOfBenefitAccident] = None
    item: Optional[List[ExplanationOfBenefitItem]] = None
    addItem: Optional[List[ExplanationOfBenefitAddItem]] = None
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = None
    total: Optional[List[ExplanationOfBenefitTotal]] = None
    payment: Optional[ExplanationOfBenefitPayment] = None
    formCode: Optional[CodeableConcept] = None
    form: Optional[Attachment] = None
    processNote: Optional[List[ExplanationOfBenefitProcessNote]] = None
    benefitPeriod: Optional[Period] = None
    benefitBalance: Optional[List[ExplanationOfBenefitBenefitBalance]] = None