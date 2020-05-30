#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Element) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .fhirabstractbase import FHIRAbstractBase



@dataclass
class Element(FHIRAbstractBase):
    """ Base for all elements.

    Base definition for all elements in a resource.
    """
    resource_type: ClassVar[str] = "Element"

    id: Optional["str"] = None
    extension: Optional[List["Extension"]] = None