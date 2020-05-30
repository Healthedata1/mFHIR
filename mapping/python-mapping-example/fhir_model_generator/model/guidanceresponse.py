#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/GuidanceResponse) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .codeableconcept import CodeableConcept
from .datarequirement import DataRequirement
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class GuidanceResponse(DomainResource):
    """ The formal response to a guidance request.

    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """
    resource_type: ClassVar[str] = "GuidanceResponse"

    requestIdentifier: Optional[Identifier] = None
    identifier: Optional[List[Identifier]] = None
    moduleUri: str = field(default=None, metadata=dict(one_of_many='module',))
    moduleCanonical: str = field(default=None, metadata=dict(one_of_many='module',))
    moduleCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='module',))
    status: str = None
    subject: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = None
    performer: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None
    evaluationMessage: Optional[List[FHIRReference]] = None
    outputParameters: Optional[FHIRReference] = None
    result: Optional[FHIRReference] = None
    dataRequirement: Optional[List[DataRequirement]] = None