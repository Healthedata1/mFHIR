#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductManufactured) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .prodcharacteristic import ProdCharacteristic
from .quantity import Quantity


@dataclass
class MedicinalProductManufactured(DomainResource):
    """ The manufactured item as contained in the packaged medicinal product.
    """
    resource_type: ClassVar[str] = "MedicinalProductManufactured"

    manufacturedDoseForm: CodeableConcept = None
    unitOfPresentation: Optional[CodeableConcept] = None
    quantity: Quantity = None
    manufacturer: Optional[List[FHIRReference]] = None
    ingredient: Optional[List[FHIRReference]] = None
    physicalCharacteristics: Optional[ProdCharacteristic] = None
    otherCharacteristics: Optional[List[CodeableConcept]] = None