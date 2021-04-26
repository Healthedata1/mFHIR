#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ContactDetail) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .contactpoint import ContactPoint
from .element import Element


@dataclass
class ContactDetail(Element):
    """ Contact information.

    Specifies contact information for a person or organization.
    """
    resource_type: ClassVar[str] = "ContactDetail"

    name: Optional[str] = None
    telecom: Optional[List[ContactPoint]] = None