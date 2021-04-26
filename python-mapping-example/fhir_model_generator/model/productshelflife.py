#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ProductShelfLife) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .identifier import Identifier
from .quantity import Quantity


@dataclass
class ProductShelfLife(BackboneElement):
    """ The shelf-life and storage information for a medicinal product item or
    container can be described using this class.
    """
    resource_type: ClassVar[str] = "ProductShelfLife"

    identifier: Optional[Identifier] = None
    type: CodeableConcept = None
    period: Quantity = None
    specialPrecautionsForStorage: Optional[List[CodeableConcept]] = None