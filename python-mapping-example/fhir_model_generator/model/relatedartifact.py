#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/RelatedArtifact) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .element import Element


@dataclass
class RelatedArtifact(Element):
    """ Related artifacts for a knowledge resource.

    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """
    resource_type: ClassVar[str] = "RelatedArtifact"

    type: str = None
    label: Optional[str] = None
    display: Optional[str] = None
    citation: Optional[str] = None
    url: Optional[str] = None
    document: Optional[Attachment] = None
    resource: Optional[str] = None