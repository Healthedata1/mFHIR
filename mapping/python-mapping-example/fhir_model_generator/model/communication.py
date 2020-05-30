#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Communication) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class CommunicationPayload(BackboneElement):
    """ Message payload.

    Text, attachment(s), or resource(s) that was communicated to the recipient.
    """
    resource_type: ClassVar[str] = "CommunicationPayload"

    contentString: str = field(default=None, metadata=dict(one_of_many='content',))
    contentAttachment: Attachment = field(default=None, metadata=dict(one_of_many='content',))
    contentReference: FHIRReference = field(default=None, metadata=dict(one_of_many='content',))


@dataclass
class Communication(DomainResource):
    """ A record of information transmitted from a sender to a receiver.

    An occurrence of information being transmitted; e.g. an alert that was sent
    to a responsible provider, a public health agency that was notified about a
    reportable condition.
    """
    resource_type: ClassVar[str] = "Communication"

    identifier: Optional[List[Identifier]] = None
    instantiatesCanonical: Optional[List[str]] = None
    instantiatesUri: Optional[List[str]] = None
    basedOn: Optional[List[FHIRReference]] = None
    partOf: Optional[List[FHIRReference]] = None
    inResponseTo: Optional[List[FHIRReference]] = None
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    category: Optional[List[CodeableConcept]] = None
    priority: Optional[str] = None
    medium: Optional[List[CodeableConcept]] = None
    subject: Optional[FHIRReference] = None
    topic: Optional[CodeableConcept] = None
    about: Optional[List[FHIRReference]] = None
    encounter: Optional[FHIRReference] = None
    sent: Optional[FHIRDate] = None
    received: Optional[FHIRDate] = None
    recipient: Optional[List[FHIRReference]] = None
    sender: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    payload: Optional[List[CommunicationPayload]] = None
    note: Optional[List[Annotation]] = None