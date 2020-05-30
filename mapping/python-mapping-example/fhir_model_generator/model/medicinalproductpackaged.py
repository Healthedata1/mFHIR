#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductPackaged) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .marketingstatus import MarketingStatus
from .prodcharacteristic import ProdCharacteristic
from .productshelflife import ProductShelfLife
from .quantity import Quantity


@dataclass
class MedicinalProductPackagedBatchIdentifier(BackboneElement):
    """ Batch numbering.
    """
    resource_type: ClassVar[str] = "MedicinalProductPackagedBatchIdentifier"

    outerPackaging: Identifier = None
    immediatePackaging: Optional[Identifier] = None


@dataclass
class MedicinalProductPackagedPackageItem(BackboneElement):
    """ A packaging item, as a contained for medicine, possibly with other
    packaging items within.
    """
    resource_type: ClassVar[str] = "MedicinalProductPackagedPackageItem"

    identifier: Optional[List[Identifier]] = None
    type: CodeableConcept = None
    quantity: Quantity = None
    material: Optional[List[CodeableConcept]] = None
    alternateMaterial: Optional[List[CodeableConcept]] = None
    device: Optional[List[FHIRReference]] = None
    manufacturedItem: Optional[List[FHIRReference]] = None
    packageItem: Optional[List["MedicinalProductPackagedPackageItem"]] = None
    physicalCharacteristics: Optional[ProdCharacteristic] = None
    otherCharacteristics: Optional[List[CodeableConcept]] = None
    shelfLifeStorage: Optional[List[ProductShelfLife]] = None
    manufacturer: Optional[List[FHIRReference]] = None


@dataclass
class MedicinalProductPackaged(DomainResource):
    """ A medicinal product in a container or package.
    """
    resource_type: ClassVar[str] = "MedicinalProductPackaged"

    identifier: Optional[List[Identifier]] = None
    subject: Optional[List[FHIRReference]] = None
    description: Optional[str] = None
    legalStatusOfSupply: Optional[CodeableConcept] = None
    marketingStatus: Optional[List[MarketingStatus]] = None
    marketingAuthorization: Optional[FHIRReference] = None
    manufacturer: Optional[List[FHIRReference]] = None
    batchIdentifier: Optional[List[MedicinalProductPackagedBatchIdentifier]] = None
    packageItem: List[MedicinalProductPackagedPackageItem] = field(default_factory=list)