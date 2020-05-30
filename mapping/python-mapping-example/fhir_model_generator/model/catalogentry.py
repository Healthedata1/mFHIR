#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CatalogEntry) on 2020-02-10.
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
class CatalogEntryRelatedEntry(BackboneElement):
    """ An item that this catalog entry is related to.

    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """
    resource_type: ClassVar[str] = "CatalogEntryRelatedEntry"

    relationtype: str = None
    item: FHIRReference = None


@dataclass
class CatalogEntry(DomainResource):
    """ An entry in a catalog.

    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """
    resource_type: ClassVar[str] = "CatalogEntry"

    identifier: Optional[List[Identifier]] = None
    type: Optional[CodeableConcept] = None
    orderable: bool = None
    referencedItem: FHIRReference = None
    additionalIdentifier: Optional[List[Identifier]] = None
    classification: Optional[List[CodeableConcept]] = None
    status: Optional[str] = None
    validityPeriod: Optional[Period] = None
    validTo: Optional[FHIRDate] = None
    lastUpdated: Optional[FHIRDate] = None
    additionalCharacteristic: Optional[List[CodeableConcept]] = None
    additionalClassification: Optional[List[CodeableConcept]] = None
    relatedEntry: Optional[List[CatalogEntryRelatedEntry]] = None