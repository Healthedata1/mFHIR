#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Binary) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .fhirreference import FHIRReference
from .resource import Resource


@dataclass
class Binary(Resource):
    """ Pure binary content defined by a format other than FHIR.

    A resource that represents the data of a single raw artifact as digital
    content accessible in its native format.  A Binary resource can contain any
    content, whether text, image, pdf, zip archive, etc.
    """
    resource_type: ClassVar[str] = "Binary"

    contentType: str = None
    securityContext: Optional[FHIRReference] = None
    data: Optional[str] = None