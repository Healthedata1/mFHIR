#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/BodyStructure) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class BodyStructure(DomainResource):
    """ Specific and identified anatomical structure.

    Record details about an anatomical structure.  This resource may be used
    when a coded concept does not provide the necessary detail needed for the
    use case.
    """
    resource_type: ClassVar[str] = "BodyStructure"

    identifier: Optional[List[Identifier]] = None
    active: Optional[bool] = None
    morphology: Optional[CodeableConcept] = None
    location: Optional[CodeableConcept] = None
    locationQualifier: Optional[List[CodeableConcept]] = None
    description: Optional[str] = None
    image: Optional[List[Attachment]] = None
    patient: FHIRReference = None