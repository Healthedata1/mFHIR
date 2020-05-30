#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Period) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element
from .fhirdate import FHIRDate


@dataclass
class Period(Element):
    """ Time range defined by start and end date/time.

    A time period defined by a start and end date and optionally time.
    """
    resource_type: ClassVar[str] = "Period"

    start: Optional[FHIRDate] = None
    end: Optional[FHIRDate] = None