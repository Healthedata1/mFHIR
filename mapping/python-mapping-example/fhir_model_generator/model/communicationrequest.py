#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CommunicationRequest) on 2020-02-10.
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
from .period import Period


@dataclass
class CommunicationRequestPayload(BackboneElement):
    """ Message payload.

    Text, attachment(s), or resource(s) to be communicated to the recipient.
    """
    resource_type: ClassVar[str] = "CommunicationRequestPayload"

    contentString: str = field(default=None, metadata=dict(one_of_many='content',))
    contentAttachment: Attachment = field(default=None, metadata=dict(one_of_many='content',))
    contentReference: FHIRReference = field(default=None, metadata=dict(one_of_many='content',))


@dataclass
class CommunicationRequest(DomainResource):
    """ A request for information to be sent to a receiver.

    A request to convey information; e.g. the CDS system proposes that an alert
    be sent to a responsible provider, the CDS system proposes that the public
    health agency be notified about a reportable condition.
    """
    resource_type: ClassVar[str] = "CommunicationRequest"

    identifier: Optional[List[Identifier]] = None
    basedOn: Optional[List[FHIRReference]] = None
    replaces: Optional[List[FHIRReference]] = None
    groupIdentifier: Optional[Identifier] = None
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    category: Optional[List[CodeableConcept]] = None
    priority: Optional[str] = None
    doNotPerform: Optional[bool] = None
    medium: Optional[List[CodeableConcept]] = None
    subject: Optional[FHIRReference] = None
    about: Optional[List[FHIRReference]] = None
    encounter: Optional[FHIRReference] = None
    payload: Optional[List[CommunicationRequestPayload]] = None
    occurrenceDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrencePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='occurrence',))
    authoredOn: Optional[FHIRDate] = None
    requester: Optional[FHIRReference] = None
    recipient: Optional[List[FHIRReference]] = None
    sender: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None