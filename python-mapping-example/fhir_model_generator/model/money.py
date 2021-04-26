#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Money) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element


@dataclass
class Money(Element):
    """ An amount of economic utility in some recognized currency.
    """
    resource_type: ClassVar[str] = "Money"

    value: Optional[float] = None
    currency: Optional[str] = None