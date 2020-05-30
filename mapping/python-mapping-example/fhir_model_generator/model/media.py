#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Media) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .attachment import Attachment
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class Media(DomainResource):
    """ A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """
    resource_type: ClassVar[str] = "Media"

    identifier: Optional[List[Identifier]] = None
    basedOn: Optional[List[FHIRReference]] = None
    partOf: Optional[List[FHIRReference]] = None
    status: str = None
    type: Optional[CodeableConcept] = None
    modality: Optional[CodeableConcept] = None
    view: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    createdDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='created',))
    createdPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='created',))
    issued: Optional[FHIRDate] = None
    operator: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    bodySite: Optional[CodeableConcept] = None
    deviceName: Optional[str] = None
    device: Optional[FHIRReference] = None
    height: Optional[int] = None
    width: Optional[int] = None
    frames: Optional[int] = None
    duration: Optional[float] = None
    content: Attachment = None
    note: Optional[List[Annotation]] = None