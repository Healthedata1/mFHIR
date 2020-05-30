#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ParameterDefinition) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .element import Element


@dataclass
class ParameterDefinition(Element):
    """ Definition of a parameter to a module.

    The parameters to the module. This collection specifies both the input and
    output parameters. Input parameters are provided by the caller as part of
    the $evaluate operation. Output parameters are included in the
    GuidanceResponse.
    """
    resource_type: ClassVar[str] = "ParameterDefinition"

    name: Optional[str] = None
    use: str = None
    min: Optional[int] = None
    max: Optional[str] = None
    documentation: Optional[str] = None
    type: str = None
    profile: Optional[str] = None