#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/EnrollmentRequest) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class EnrollmentRequest(DomainResource):
    """ Enroll in coverage.

    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """
    resource_type: ClassVar[str] = "EnrollmentRequest"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    created: Optional[FHIRDate] = None
    insurer: Optional[FHIRReference] = None
    provider: Optional[FHIRReference] = None
    candidate: Optional[FHIRReference] = None
    coverage: Optional[FHIRReference] = None