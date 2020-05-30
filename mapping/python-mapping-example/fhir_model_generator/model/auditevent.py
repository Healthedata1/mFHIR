#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/AuditEvent) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .period import Period


@dataclass
class AuditEventEntityDetail(BackboneElement):
    """ Additional Information about the entity.

    Tagged value pairs for conveying additional information about the entity.
    """
    resource_type: ClassVar[str] = "AuditEventEntityDetail"

    type: str = None
    valueString: str = field(default=None, metadata=dict(one_of_many='value',))
    valueBase64Binary: str = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class AuditEventAgentNetwork(BackboneElement):
    """ Logical network location for application activity.

    Logical network location for application activity, if the activity has a
    network location.
    """
    resource_type: ClassVar[str] = "AuditEventAgentNetwork"

    address: Optional[str] = None
    type: Optional[str] = None


@dataclass
class AuditEventAgent(BackboneElement):
    """ Actor involved in the event.

    An actor taking an active role in the event or activity that is logged.
    """
    resource_type: ClassVar[str] = "AuditEventAgent"

    type: Optional[CodeableConcept] = None
    role: Optional[List[CodeableConcept]] = None
    who: Optional[FHIRReference] = None
    altId: Optional[str] = None
    name: Optional[str] = None
    requestor: bool = None
    location: Optional[FHIRReference] = None
    policy: Optional[List[str]] = None
    media: Optional[Coding] = None
    network: Optional[AuditEventAgentNetwork] = None
    purposeOfUse: Optional[List[CodeableConcept]] = None


@dataclass
class AuditEventSource(BackboneElement):
    """ Audit Event Reporter.

    The system that is reporting the event.
    """
    resource_type: ClassVar[str] = "AuditEventSource"

    site: Optional[str] = None
    observer: FHIRReference = None
    type: Optional[List[Coding]] = None


@dataclass
class AuditEventEntity(BackboneElement):
    """ Data or objects used.

    Specific instances of data or objects that have been accessed.
    """
    resource_type: ClassVar[str] = "AuditEventEntity"

    what: Optional[FHIRReference] = None
    type: Optional[Coding] = None
    role: Optional[Coding] = None
    lifecycle: Optional[Coding] = None
    securityLabel: Optional[List[Coding]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    query: Optional[str] = None
    detail: Optional[List[AuditEventEntityDetail]] = None


@dataclass
class AuditEvent(DomainResource):
    """ Event record kept for security purposes.

    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """
    resource_type: ClassVar[str] = "AuditEvent"

    type: Coding = None
    subtype: Optional[List[Coding]] = None
    action: Optional[str] = None
    period: Optional[Period] = None
    recorded: FHIRDate = None
    outcome: Optional[str] = None
    outcomeDesc: Optional[str] = None
    purposeOfEvent: Optional[List[CodeableConcept]] = None
    agent: List[AuditEventAgent] = field(default_factory=list)
    source: AuditEventSource = None
    entity: Optional[List[AuditEventEntity]] = None