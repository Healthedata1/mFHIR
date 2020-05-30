#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Signature) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .coding import Coding
from .element import Element
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference


@dataclass
class Signature(Element):
    """ A Signature - XML DigSig, JWS, Graphical image of signature, etc..

    A signature along with supporting context. The signature may be a digital
    signature that is cryptographic in nature, or some other signature
    acceptable to the domain. This other signature may be as simple as a
    graphical image representing a hand-written signature, or a signature
    ceremony Different signature approaches have different utilities.
    """
    resource_type: ClassVar[str] = "Signature"

    type: List[Coding] = field(default_factory=list)
    when: FHIRDate = None
    who: FHIRReference = None
    onBehalfOf: Optional[FHIRReference] = None
    targetFormat: Optional[str] = None
    sigFormat: Optional[str] = None
    data: Optional[str] = None