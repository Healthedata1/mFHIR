#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/InsurancePlan) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .address import Address
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier
from .money import Money
from .period import Period
from .quantity import Quantity


@dataclass
class InsurancePlanPlanSpecificCostBenefitCost(BackboneElement):
    """ List of the costs.

    List of the costs associated with a specific benefit.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanSpecificCostBenefitCost"

    type: CodeableConcept = None
    applicability: Optional[CodeableConcept] = None
    qualifiers: Optional[List[CodeableConcept]] = None
    value: Optional[Quantity] = None


@dataclass
class InsurancePlanPlanSpecificCostBenefit(BackboneElement):
    """ Benefits list.

    List of the specific benefits under this category of benefit.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanSpecificCostBenefit"

    type: CodeableConcept = None
    cost: Optional[List[InsurancePlanPlanSpecificCostBenefitCost]] = None


@dataclass
class InsurancePlanPlanGeneralCost(BackboneElement):
    """ Overall costs.

    Overall costs associated with the plan.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanGeneralCost"

    type: Optional[CodeableConcept] = None
    groupSize: Optional[int] = None
    cost: Optional[Money] = None
    comment: Optional[str] = None


@dataclass
class InsurancePlanPlanSpecificCost(BackboneElement):
    """ Specific costs.

    Costs associated with the coverage provided by the product.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlanSpecificCost"

    category: CodeableConcept = None
    benefit: Optional[List[InsurancePlanPlanSpecificCostBenefit]] = None


@dataclass
class InsurancePlanCoverageBenefitLimit(BackboneElement):
    """ Benefit limits.

    The specific limits on the benefit.
    """
    resource_type: ClassVar[str] = "InsurancePlanCoverageBenefitLimit"

    value: Optional[Quantity] = None
    code: Optional[CodeableConcept] = None


@dataclass
class InsurancePlanCoverageBenefit(BackboneElement):
    """ List of benefits.

    Specific benefits under this type of coverage.
    """
    resource_type: ClassVar[str] = "InsurancePlanCoverageBenefit"

    type: CodeableConcept = None
    requirement: Optional[str] = None
    limit: Optional[List[InsurancePlanCoverageBenefitLimit]] = None


@dataclass
class InsurancePlanContact(BackboneElement):
    """ Contact for the product.

    The contact for the health insurance product for a certain purpose.
    """
    resource_type: ClassVar[str] = "InsurancePlanContact"

    purpose: Optional[CodeableConcept] = None
    name: Optional[HumanName] = None
    telecom: Optional[List[ContactPoint]] = None
    address: Optional[Address] = None


@dataclass
class InsurancePlanCoverage(BackboneElement):
    """ Coverage details.

    Details about the coverage offered by the insurance product.
    """
    resource_type: ClassVar[str] = "InsurancePlanCoverage"

    type: CodeableConcept = None
    network: Optional[List[FHIRReference]] = None
    benefit: List[InsurancePlanCoverageBenefit] = field(default_factory=list)


@dataclass
class InsurancePlanPlan(BackboneElement):
    """ Plan details.

    Details about an insurance plan.
    """
    resource_type: ClassVar[str] = "InsurancePlanPlan"

    identifier: Optional[List[Identifier]] = None
    type: Optional[CodeableConcept] = None
    coverageArea: Optional[List[FHIRReference]] = None
    network: Optional[List[FHIRReference]] = None
    generalCost: Optional[List[InsurancePlanPlanGeneralCost]] = None
    specificCost: Optional[List[InsurancePlanPlanSpecificCost]] = None


@dataclass
class InsurancePlan(DomainResource):
    """ Details of a Health Insurance product/plan provided by an organization.
    """
    resource_type: ClassVar[str] = "InsurancePlan"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    type: Optional[List[CodeableConcept]] = None
    name: Optional[str] = None
    alias: Optional[List[str]] = None
    period: Optional[Period] = None
    ownedBy: Optional[FHIRReference] = None
    administeredBy: Optional[FHIRReference] = None
    coverageArea: Optional[List[FHIRReference]] = None
    contact: Optional[List[InsurancePlanContact]] = None
    endpoint: Optional[List[FHIRReference]] = None
    network: Optional[List[FHIRReference]] = None
    coverage: Optional[List[InsurancePlanCoverage]] = None
    plan: Optional[List[InsurancePlanPlan]] = None