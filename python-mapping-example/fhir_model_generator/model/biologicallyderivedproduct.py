#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct) on 2020-02-10.
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
from .period import Period


@dataclass
class BiologicallyDerivedProductCollection(BackboneElement):
    """ How this product was collected.
    """
    resource_type: ClassVar[str] = "BiologicallyDerivedProductCollection"

    collector: Optional[FHIRReference] = None
    source: Optional[FHIRReference] = None
    collectedDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='collected',))
    collectedPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='collected',))


@dataclass
class BiologicallyDerivedProductProcessing(BackboneElement):
    """ Any processing of the product during collection.

    Any processing of the product during collection that does not change the
    fundamental nature of the product. For example adding anti-coagulants
    during the collection of Peripheral Blood Stem Cells.
    """
    resource_type: ClassVar[str] = "BiologicallyDerivedProductProcessing"

    description: Optional[str] = None
    procedure: Optional[CodeableConcept] = None
    additive: Optional[FHIRReference] = None
    timeDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='time',))
    timePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='time',))


@dataclass
class BiologicallyDerivedProductManipulation(BackboneElement):
    """ Any manipulation of product post-collection.

    Any manipulation of product post-collection that is intended to alter the
    product.  For example a buffy-coat enrichment or CD8 reduction of
    Peripheral Blood Stem Cells to make it more suitable for infusion.
    """
    resource_type: ClassVar[str] = "BiologicallyDerivedProductManipulation"

    description: Optional[str] = None
    timeDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='time',))
    timePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='time',))


@dataclass
class BiologicallyDerivedProductStorage(BackboneElement):
    """ Product storage.
    """
    resource_type: ClassVar[str] = "BiologicallyDerivedProductStorage"

    description: Optional[str] = None
    temperature: Optional[float] = None
    scale: Optional[str] = None
    duration: Optional[Period] = None


@dataclass
class BiologicallyDerivedProduct(DomainResource):
    """ A material substance originating from a biological entity.

    A material substance originating from a biological entity intended to be
    transplanted or infused
    into another (possibly the same) biological entity.
    """
    resource_type: ClassVar[str] = "BiologicallyDerivedProduct"

    identifier: Optional[List[Identifier]] = None
    productCategory: Optional[str] = None
    productCode: Optional[CodeableConcept] = None
    status: Optional[str] = None
    request: Optional[List[FHIRReference]] = None
    quantity: Optional[int] = None
    parent: Optional[List[FHIRReference]] = None
    collection: Optional[BiologicallyDerivedProductCollection] = None
    processing: Optional[List[BiologicallyDerivedProductProcessing]] = None
    manipulation: Optional[BiologicallyDerivedProductManipulation] = None
    storage: Optional[List[BiologicallyDerivedProductStorage]] = None