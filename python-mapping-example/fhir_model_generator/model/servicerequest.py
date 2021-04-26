#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ServiceRequest) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .timing import Timing


@dataclass
class ServiceRequest(DomainResource):
    """ A request for a service to be performed.

    A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
    """
    resource_type: ClassVar[str] = "ServiceRequest"

    identifier: Optional[List[Identifier]] = None
    instantiatesCanonical: Optional[List[str]] = None
    instantiatesUri: Optional[List[str]] = None
    basedOn: Optional[List[FHIRReference]] = None
    replaces: Optional[List[FHIRReference]] = None
    requisition: Optional[Identifier] = None
    status: str = None
    intent: str = None
    category: Optional[List[CodeableConcept]] = None
    priority: Optional[str] = None
    doNotPerform: Optional[bool] = None
    code: Optional[CodeableConcept] = None
    orderDetail: Optional[List[CodeableConcept]] = None
    quantityQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='quantity',))
    quantityRatio: Optional[Ratio] = field(default=None, metadata=dict(one_of_many='quantity',))
    quantityRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='quantity',))
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    occurrenceDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrencePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrenceTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='occurrence',))
    asNeededBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='asNeeded',))
    asNeededCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='asNeeded',))
    authoredOn: Optional[FHIRDate] = None
    requester: Optional[FHIRReference] = None
    performerType: Optional[CodeableConcept] = None
    performer: Optional[List[FHIRReference]] = None
    locationCode: Optional[List[CodeableConcept]] = None
    locationReference: Optional[List[FHIRReference]] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    insurance: Optional[List[FHIRReference]] = None
    supportingInfo: Optional[List[FHIRReference]] = None
    specimen: Optional[List[FHIRReference]] = None
    bodySite: Optional[List[CodeableConcept]] = None
    note: Optional[List[Annotation]] = None
    patientInstruction: Optional[str] = None
    relevantHistory: Optional[List[FHIRReference]] = None