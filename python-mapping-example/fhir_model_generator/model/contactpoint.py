#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ContactPoint) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element
from .period import Period


@dataclass
class ContactPoint(Element):
    """ Details of a Technology mediated contact point (phone, fax, email, etc.).

    Details for all kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """
    resource_type: ClassVar[str] = "ContactPoint"

    system: Optional[str] = None
    value: Optional[str] = None
    use: Optional[str] = None
    rank: Optional[int] = None
    period: Optional[Period] = None