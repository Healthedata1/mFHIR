#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProduct) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .marketingstatus import MarketingStatus


@dataclass
class MedicinalProductNameNamePart(BackboneElement):
    """ Coding words or phrases of the name.
    """
    resource_type: ClassVar[str] = "MedicinalProductNameNamePart"

    part: str = None
    type: Coding = None


@dataclass
class MedicinalProductNameCountryLanguage(BackboneElement):
    """ Country where the name applies.
    """
    resource_type: ClassVar[str] = "MedicinalProductNameCountryLanguage"

    country: CodeableConcept = None
    jurisdiction: Optional[CodeableConcept] = None
    language: CodeableConcept = None


@dataclass
class MedicinalProductName(BackboneElement):
    """ The product's name, including full name and possibly coded parts.
    """
    resource_type: ClassVar[str] = "MedicinalProductName"

    productName: str = None
    namePart: Optional[List[MedicinalProductNameNamePart]] = None
    countryLanguage: Optional[List[MedicinalProductNameCountryLanguage]] = None


@dataclass
class MedicinalProductManufacturingBusinessOperation(BackboneElement):
    """ An operation applied to the product, for manufacturing or adminsitrative
    purpose.
    """
    resource_type: ClassVar[str] = "MedicinalProductManufacturingBusinessOperation"

    operationType: Optional[CodeableConcept] = None
    authorisationReferenceNumber: Optional[Identifier] = None
    effectiveDate: Optional[FHIRDate] = None
    confidentialityIndicator: Optional[CodeableConcept] = None
    manufacturer: Optional[List[FHIRReference]] = None
    regulator: Optional[FHIRReference] = None


@dataclass
class MedicinalProductSpecialDesignation(BackboneElement):
    """ Indicates if the medicinal product has an orphan designation for the
    treatment of a rare disease.
    """
    resource_type: ClassVar[str] = "MedicinalProductSpecialDesignation"

    identifier: Optional[List[Identifier]] = None
    type: Optional[CodeableConcept] = None
    intendedUse: Optional[CodeableConcept] = None
    indicationCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='indication',))
    indicationReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='indication',))
    status: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    species: Optional[CodeableConcept] = None


@dataclass
class MedicinalProduct(DomainResource):
    """ Detailed definition of a medicinal product, typically for uses other than
    direct patient care (e.g. regulatory use).
    """
    resource_type: ClassVar[str] = "MedicinalProduct"

    identifier: Optional[List[Identifier]] = None
    type: Optional[CodeableConcept] = None
    domain: Optional[Coding] = None
    combinedPharmaceuticalDoseForm: Optional[CodeableConcept] = None
    legalStatusOfSupply: Optional[CodeableConcept] = None
    additionalMonitoringIndicator: Optional[CodeableConcept] = None
    specialMeasures: Optional[List[str]] = None
    paediatricUseIndicator: Optional[CodeableConcept] = None
    productClassification: Optional[List[CodeableConcept]] = None
    marketingStatus: Optional[List[MarketingStatus]] = None
    pharmaceuticalProduct: Optional[List[FHIRReference]] = None
    packagedMedicinalProduct: Optional[List[FHIRReference]] = None
    attachedDocument: Optional[List[FHIRReference]] = None
    masterFile: Optional[List[FHIRReference]] = None
    contact: Optional[List[FHIRReference]] = None
    clinicalTrial: Optional[List[FHIRReference]] = None
    name: List[MedicinalProductName] = field(default_factory=list)
    crossReference: Optional[List[Identifier]] = None
    manufacturingBusinessOperation: Optional[List[MedicinalProductManufacturingBusinessOperation]] = None
    specialDesignation: Optional[List[MedicinalProductSpecialDesignation]] = None