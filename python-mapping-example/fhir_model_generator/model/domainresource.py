#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DomainResource) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .extension import Extension
from .narrative import Narrative
from .resource import Resource


@dataclass
class DomainResource(Resource):
    """ A resource with narrative, extensions, and contained resources.

    A resource that includes narrative, extensions, and contained resources.
    """
    resource_type: ClassVar[str] = "DomainResource"

    text: Optional[Narrative] = None
    contained: Optional[List[Resource]] = None
    extension: Optional[List[Extension]] = None
    modifierExtension: Optional[List[Extension]] = None