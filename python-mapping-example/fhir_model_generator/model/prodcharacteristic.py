#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ProdCharacteristic) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .quantity import Quantity


@dataclass
class ProdCharacteristic(BackboneElement):
    """ The marketing status describes the date when a medicinal product is
    actually put on the market or the date as of which it is no longer
    available.
    """
    resource_type: ClassVar[str] = "ProdCharacteristic"

    height: Optional[Quantity] = None
    width: Optional[Quantity] = None
    depth: Optional[Quantity] = None
    weight: Optional[Quantity] = None
    nominalVolume: Optional[Quantity] = None
    externalDiameter: Optional[Quantity] = None
    shape: Optional[str] = None
    color: Optional[List[str]] = None
    imprint: Optional[List[str]] = None
    image: Optional[List[Attachment]] = None
    scoring: Optional[CodeableConcept] = None