#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MessageDefinition) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .identifier import Identifier
from .usagecontext import UsageContext


@dataclass
class MessageDefinitionFocus(BackboneElement):
    """ Resource(s) that are the subject of the event.

    Identifies the resource (or resources) that are being addressed by the
    event.  For example, the Encounter for an admit message or two Account
    records for a merge.
    """
    resource_type: ClassVar[str] = "MessageDefinitionFocus"

    code: str = None
    profile: Optional[str] = None
    min: int = None
    max: Optional[str] = None


@dataclass
class MessageDefinitionAllowedResponse(BackboneElement):
    """ Responses to this message.

    Indicates what types of messages may be sent as an application-level
    response to this message.
    """
    resource_type: ClassVar[str] = "MessageDefinitionAllowedResponse"

    message: str = None
    situation: Optional[str] = None


@dataclass
class MessageDefinition(DomainResource):
    """ A resource that defines a type of message that can be exchanged between
    systems.

    Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.
    """
    resource_type: ClassVar[str] = "MessageDefinition"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    replaces: Optional[List[str]] = None
    status: str = None
    experimental: Optional[bool] = None
    date: FHIRDate = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    base: Optional[str] = None
    parent: Optional[List[str]] = None
    eventCoding: Coding = field(default=None, metadata=dict(one_of_many='event',))
    eventUri: str = field(default=None, metadata=dict(one_of_many='event',))
    category: Optional[str] = None
    focus: Optional[List[MessageDefinitionFocus]] = None
    responseRequired: Optional[str] = None
    allowedResponse: Optional[List[MessageDefinitionAllowedResponse]] = None
    graph: Optional[List[str]] = None