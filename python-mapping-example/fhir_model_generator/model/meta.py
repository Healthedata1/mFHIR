#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Meta) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .coding import Coding
from .element import Element
from .fhirdate import FHIRDate


@dataclass
class Meta(Element):
    """ Metadata about a resource.

    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content might not always
    be associated with version changes to the resource.
    """
    resource_type: ClassVar[str] = "Meta"

    versionId: Optional[str] = None
    lastUpdated: Optional[FHIRDate] = None
    source: Optional[str] = None
    profile: Optional[List[str]] = None
    security: Optional[List[Coding]] = None
    tag: Optional[List[Coding]] = None