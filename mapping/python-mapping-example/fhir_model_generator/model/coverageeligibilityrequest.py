#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityRequest) on 2020-02-10.
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
from .quantity import Quantity


@dataclass
class CoverageEligibilityRequestItemDiagnosis(BackboneElement):
    """ Applicable diagnosis.

    Patient diagnosis for which care is sought.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestItemDiagnosis"

    diagnosisCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='diagnosis',))
    diagnosisReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='diagnosis',))


@dataclass
class CoverageEligibilityRequestSupportingInfo(BackboneElement):
    """ Supporting information.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestSupportingInfo"

    sequence: int = None
    information: FHIRReference = None
    appliesToAll: Optional[bool] = None


@dataclass
class CoverageEligibilityRequestInsurance(BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestInsurance"

    focal: Optional[bool] = None
    coverage: FHIRReference = None
    businessArrangement: Optional[str] = None


@dataclass
class CoverageEligibilityRequestItem(BackboneElement):
    """ Item to be evaluated for eligibiity.

    Service categories or billable services for which benefit details and/or an
    authorization prior to service delivery may be required by the payor.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestItem"

    supportingInfoSequence: Optional[List[int]] = None
    category: Optional[CodeableConcept] = None
    productOrService: Optional[CodeableConcept] = None
    modifier: Optional[List[CodeableConcept]] = None
    provider: Optional[FHIRReference] = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    facility: Optional[FHIRReference] = None
    diagnosis: Optional[List[CoverageEligibilityRequestItemDiagnosis]] = None
    detail: Optional[List[FHIRReference]] = None


@dataclass
class CoverageEligibilityRequest(DomainResource):
    """ CoverageEligibilityRequest resource.

    The CoverageEligibilityRequest provides patient and insurance coverage
    information to an insurer for them to respond, in the form of an
    CoverageEligibilityResponse, with information regarding whether the stated
    coverage is valid and in-force and optionally to provide the insurance
    details of the policy.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequest"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    priority: Optional[CodeableConcept] = None
    purpose: List[str] = field(default_factory=list)
    patient: FHIRReference = None
    servicedDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='serviced',))
    servicedPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='serviced',))
    created: FHIRDate = None
    enterer: Optional[FHIRReference] = None
    provider: Optional[FHIRReference] = None
    insurer: FHIRReference = None
    facility: Optional[FHIRReference] = None
    supportingInfo: Optional[List[CoverageEligibilityRequestSupportingInfo]] = None
    insurance: Optional[List[CoverageEligibilityRequestInsurance]] = None
    item: Optional[List[CoverageEligibilityRequestItem]] = None