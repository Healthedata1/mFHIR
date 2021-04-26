#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Claim) on 2020-02-10.
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
class ClaimItemDetailSubDetail(BackboneElement):
    """ Product or service provided.

    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """
    resource_type: ClassVar[str] = "ClaimItemDetailSubDetail"

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


@dataclass
class ClaimItemDetail(BackboneElement):
    """ Product or service provided.

    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """
    resource_type: ClassVar[str] = "ClaimItemDetail"

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
    subDetail: Optional[List[ClaimItemDetailSubDetail]] = None


@dataclass
class ClaimRelated(BackboneElement):
    """ Prior or corollary claims.

    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """
    resource_type: ClassVar[str] = "ClaimRelated"

    claim: Optional[FHIRReference] = None
    relationship: Optional[CodeableConcept] = None
    reference: Optional[Identifier] = None


@dataclass
class ClaimPayee(BackboneElement):
    """ Recipient of benefits payable.

    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """
    resource_type: ClassVar[str] = "ClaimPayee"

    type: CodeableConcept = None
    party: Optional[FHIRReference] = None


@dataclass
class ClaimCareTeam(BackboneElement):
    """ Members of the care team.

    The members of the team who provided the products and services.
    """
    resource_type: ClassVar[str] = "ClaimCareTeam"

    sequence: int = None
    provider: FHIRReference = None
    responsible: Optional[bool] = None
    role: Optional[CodeableConcept] = None
    qualification: Optional[CodeableConcept] = None


@dataclass
class ClaimSupportingInfo(BackboneElement):
    """ Supporting information.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    resource_type: ClassVar[str] = "ClaimSupportingInfo"

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
    reason: Optional[CodeableConcept] = None


@dataclass
class ClaimDiagnosis(BackboneElement):
    """ Pertinent diagnosis information.

    Information about diagnoses relevant to the claim items.
    """
    resource_type: ClassVar[str] = "ClaimDiagnosis"

    sequence: int = None
    diagnosisCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='diagnosis',))
    diagnosisReference: FHIRReference = field(default=None, metadata=dict(one_of_many='diagnosis',))
    type: Optional[List[CodeableConcept]] = None
    onAdmission: Optional[CodeableConcept] = None
    packageCode: Optional[CodeableConcept] = None


@dataclass
class ClaimProcedure(BackboneElement):
    """ Clinical procedures performed.

    Procedures performed on the patient relevant to the billing items with the
    claim.
    """
    resource_type: ClassVar[str] = "ClaimProcedure"

    sequence: int = None
    type: Optional[List[CodeableConcept]] = None
    date: Optional[FHIRDate] = None
    procedureCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='procedure',))
    procedureReference: FHIRReference = field(default=None, metadata=dict(one_of_many='procedure',))
    udi: Optional[List[FHIRReference]] = None


@dataclass
class ClaimInsurance(BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    resource_type: ClassVar[str] = "ClaimInsurance"

    sequence: int = None
    focal: bool = None
    identifier: Optional[Identifier] = None
    coverage: FHIRReference = None
    businessArrangement: Optional[str] = None
    preAuthRef: Optional[List[str]] = None
    claimResponse: Optional[FHIRReference] = None


@dataclass
class ClaimAccident(BackboneElement):
    """ Details of the event.

    Details of an accident which resulted in injuries which required the
    products and services listed in the claim.
    """
    resource_type: ClassVar[str] = "ClaimAccident"

    date: FHIRDate = None
    type: Optional[CodeableConcept] = None
    locationAddress: Optional[Address] = field(default=None, metadata=dict(one_of_many='location',))
    locationReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='location',))


@dataclass
class ClaimItem(BackboneElement):
    """ Product or service provided.

    A claim line. Either a simple  product or service or a 'group' of details
    which can each be a simple items or groups of sub-details.
    """
    resource_type: ClassVar[str] = "ClaimItem"

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
    detail: Optional[List[ClaimItemDetail]] = None


@dataclass
class Claim(DomainResource):
    """ Claim, Pre-determination or Pre-authorization.

    A provider issued list of professional services and products which have
    been provided, or are to be provided, to a patient which is sent to an
    insurer for reimbursement.
    """
    resource_type: ClassVar[str] = "Claim"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    type: CodeableConcept = None
    subType: Optional[CodeableConcept] = None
    use: str = None
    patient: FHIRReference = None
    billablePeriod: Optional[Period] = None
    created: FHIRDate = None
    enterer: Optional[FHIRReference] = None
    insurer: Optional[FHIRReference] = None
    provider: FHIRReference = None
    priority: CodeableConcept = None
    fundsReserve: Optional[CodeableConcept] = None
    related: Optional[List[ClaimRelated]] = None
    prescription: Optional[FHIRReference] = None
    originalPrescription: Optional[FHIRReference] = None
    payee: Optional[ClaimPayee] = None
    referral: Optional[FHIRReference] = None
    facility: Optional[FHIRReference] = None
    careTeam: Optional[List[ClaimCareTeam]] = None
    supportingInfo: Optional[List[ClaimSupportingInfo]] = None
    diagnosis: Optional[List[ClaimDiagnosis]] = None
    procedure: Optional[List[ClaimProcedure]] = None
    insurance: List[ClaimInsurance] = field(default_factory=list)
    accident: Optional[ClaimAccident] = None
    item: Optional[List[ClaimItem]] = None
    total: Optional[Money] = None