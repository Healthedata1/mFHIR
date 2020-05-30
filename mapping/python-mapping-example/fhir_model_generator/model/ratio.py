#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Ratio) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element
from .quantity import Quantity


@dataclass
class Ratio(Element):
    """ A ratio of two Quantity values - a numerator and a denominator.

    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """
    resource_type: ClassVar[str] = "Ratio"

    numerator: Optional[Quantity] = None
    denominator: Optional[Quantity] = None