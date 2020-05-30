#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse) on 2020-02-10.
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
class CoverageEligibilityResponseInsuranceItemBenefit(BackboneElement):
    """ Benefit Summary.

    Benefits used to date.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityResponseInsuranceItemBenefit"

    type: CodeableConcept = None
    allowedUnsignedInt: Optional[int] = field(default=None, metadata=dict(one_of_many='allowed',))
    allowedString: Optional[str] = field(default=None, metadata=dict(one_of_many='allowed',))
    allowedMoney: Optional[Money] = field(default=None, metadata=dict(one_of_many='allowed',))
    usedUnsignedInt: Optional[int] = field(default=None, metadata=dict(one_of_many='used',))
    usedString: Optional[str] = field(default=None, metadata=dict(one_of_many='used',))
    usedMoney: Optional[Money] = field(default=None, metadata=dict(one_of_many='used',))


@dataclass
class CoverageEligibilityResponseInsuranceItem(BackboneElement):
    """ Benefits and authorization details.

    Benefits and optionally current balances, and authorization details by
    category or service.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityResponseInsuranceItem"

    category: Optional[CodeableConcept] = None
    productOrService: Optional[CodeableConcept] = None
    modifier: Optional[List[CodeableConcept]] = None
    provider: Optional[FHIRReference] = None
    excluded: Optional[bool] = None
    name: Optional[str] = None
    description: Optional[str] = None
    network: Optional[CodeableConcept] = None
    unit: Optional[CodeableConcept] = None
    term: Optional[CodeableConcept] = None
    benefit: Optional[List[CoverageEligibilityResponseInsuranceItemBenefit]] = None
    authorizationRequired: Optional[bool] = None
    authorizationSupporting: Optional[List[CodeableConcept]] = None
    authorizationUrl: Optional[str] = None


@dataclass
class CoverageEligibilityResponseInsurance(BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityResponseInsurance"

    coverage: FHIRReference = None
    inforce: Optional[bool] = None
    benefitPeriod: Optional[Period] = None
    item: Optional[List[CoverageEligibilityResponseInsuranceItem]] = None


@dataclass
class CoverageEligibilityResponseError(BackboneElement):
    """ Processing errors.

    Errors encountered during the processing of the request.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityResponseError"

    code: CodeableConcept = None


@dataclass
class CoverageEligibilityResponse(DomainResource):
    """ CoverageEligibilityResponse resource.

    This resource provides eligibility and plan details from the processing of
    an CoverageEligibilityRequest resource.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityResponse"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    purpose: List[str] = field(default_factory=list)
    patient: FHIRReference = None
    servicedDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='serviced',))
    servicedPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='serviced',))
    created: FHIRDate = None
    requestor: Optional[FHIRReference] = None
    request: FHIRReference = None
    outcome: str = None
    disposition: Optional[str] = None
    insurer: FHIRReference = None
    insurance: Optional[List[CoverageEligibilityResponseInsurance]] = None
    preAuthRef: Optional[str] = None
    form: Optional[CodeableConcept] = None
    error: Optional[List[CoverageEligibilityResponseError]] = None