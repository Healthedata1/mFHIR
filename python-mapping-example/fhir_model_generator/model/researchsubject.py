#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ResearchSubject) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class ResearchSubject(DomainResource):
    """ Physical entity which is the primary unit of interest in the study.

    A physical entity which is the primary unit of operational and/or
    administrative interest in a study.
    """
    resource_type: ClassVar[str] = "ResearchSubject"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    period: Optional[Period] = None
    study: FHIRReference = None
    individual: FHIRReference = None
    assignedArm: Optional[str] = None
    actualArm: Optional[str] = None
    consent: Optional[FHIRReference] = None