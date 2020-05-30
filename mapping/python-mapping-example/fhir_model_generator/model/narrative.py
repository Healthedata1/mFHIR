#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Narrative) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element


@dataclass
class Narrative(Element):
    """ Human-readable summary of the resource (essential clinical and business
    information).

    A human-readable summary of the resource conveying the essential clinical
    and business information for the resource.
    """
    resource_type: ClassVar[str] = "Narrative"

    status: str = None
    div: str = None