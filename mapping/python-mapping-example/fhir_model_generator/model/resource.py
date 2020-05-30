#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Resource) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .fhirabstractresource import FHIRAbstractResource
from .meta import Meta


@dataclass
class Resource(FHIRAbstractResource):
    """ Base Resource.

    This is the base resource type for everything.
    """
    resource_type: ClassVar[str] = "Resource"

    id: Optional[str] = None
    meta: Optional[Meta] = None
    implicitRules: Optional[str] = None
    language: Optional[str] = None