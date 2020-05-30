#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DeviceRequest) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .timing import Timing


@dataclass
class DeviceRequestParameter(BackboneElement):
    """ Device details.

    Specific parameters for the ordered item.  For example, the prism value for
    lenses.
    """
    resource_type: ClassVar[str] = "DeviceRequestParameter"

    code: Optional[CodeableConcept] = None
    valueCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='value',))
    valueRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='value',))
    valueBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class DeviceRequest(DomainResource):
    """ Medical device request.

    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """
    resource_type: ClassVar[str] = "DeviceRequest"

    identifier: Optional[List[Identifier]] = None
    instantiatesCanonical: Optional[List[str]] = None
    instantiatesUri: Optional[List[str]] = None
    basedOn: Optional[List[FHIRReference]] = None
    priorRequest: Optional[List[FHIRReference]] = None
    groupIdentifier: Optional[Identifier] = None
    status: Optional[str] = None
    intent: str = None
    priority: Optional[str] = None
    codeReference: FHIRReference = field(default=None, metadata=dict(one_of_many='code',))
    codeCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='code',))
    parameter: Optional[List[DeviceRequestParameter]] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrencePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrenceTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='occurrence',))
    authoredOn: Optional[FHIRDate] = None
    requester: Optional[FHIRReference] = None
    performerType: Optional[CodeableConcept] = None
    performer: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    insurance: Optional[List[FHIRReference]] = None
    supportingInfo: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None
    relevantHistory: Optional[List[FHIRReference]] = None