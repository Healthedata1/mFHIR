#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Address) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element
from .period import Period


@dataclass
class Address(Element):
    """ An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).

    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).  This data type may be used to convey
    addresses for use in delivering mail as well as for visiting locations
    which might not be valid for mail delivery.  There are a variety of postal
    address formats defined around the world.
    """
    resource_type: ClassVar[str] = "Address"

    use: Optional[str] = None
    type: Optional[str] = None
    text: Optional[str] = None
    line: Optional[List[str]] = None
    city: Optional[str] = None
    district: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    country: Optional[str] = None
    period: Optional[Period] = None