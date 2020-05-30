#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CodeableConcept) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .coding import Coding
from .element import Element


@dataclass
class CodeableConcept(Element):
    """ Concept - reference to a terminology or just  text.

    A concept that may be defined by a formal reference to a terminology or
    ontology or may be provided by text.
    """
    resource_type: ClassVar[str] = "CodeableConcept"

    coding: Optional[List[Coding]] = None
    text: Optional[str] = None