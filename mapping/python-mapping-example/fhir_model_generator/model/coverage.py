#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Coverage) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period
from .quantity import Quantity


@dataclass
class CoverageCostToBeneficiaryException(BackboneElement):
    """ Exceptions for patient payments.

    A suite of codes indicating exceptions or reductions to patient costs and
    their effective periods.
    """
    resource_type: ClassVar[str] = "CoverageCostToBeneficiaryException"

    type: CodeableConcept = None
    period: Optional[Period] = None


@dataclass
class CoverageClass(BackboneElement):
    """ Additional coverage classifications.

    A suite of underwriter specific classifiers.
    """
    resource_type: ClassVar[str] = "CoverageClass"

    type: CodeableConcept = None
    value: str = None
    name: Optional[str] = None


@dataclass
class CoverageCostToBeneficiary(BackboneElement):
    """ Patient payments for services/products.

    A suite of codes indicating the cost category and associated amount which
    have been detailed in the policy and may have been  included on the health
    card.
    """
    resource_type: ClassVar[str] = "CoverageCostToBeneficiary"

    type: Optional[CodeableConcept] = None
    valueQuantity: Quantity = field(default=None, metadata=dict(one_of_many='value',))
    valueMoney: Money = field(default=None, metadata=dict(one_of_many='value',))
    exception: Optional[List[CoverageCostToBeneficiaryException]] = None


@dataclass
class Coverage(DomainResource):
    """ Insurance or medical plan or a payment agreement.

    Financial instrument which may be used to reimburse or pay for health care
    products and services. Includes both insurance and self-payment.
    """
    resource_type: ClassVar[str] = "Coverage"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    type: Optional[CodeableConcept] = None
    policyHolder: Optional[FHIRReference] = None
    subscriber: Optional[FHIRReference] = None
    subscriberId: Optional[str] = None
    beneficiary: FHIRReference = None
    dependent: Optional[str] = None
    relationship: Optional[CodeableConcept] = None
    period: Optional[Period] = None
    payor: List[FHIRReference] = field(default_factory=list)
    class_fhir: Optional[List[CoverageClass]] = field(default_factory=list, metadata=dict(orig_name='class'))
    order: Optional[int] = None
    network: Optional[str] = None
    costToBeneficiary: Optional[List[CoverageCostToBeneficiary]] = None
    subrogation: Optional[bool] = None
    contract: Optional[List[FHIRReference]] = None