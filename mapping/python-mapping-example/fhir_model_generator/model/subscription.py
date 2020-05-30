#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Subscription) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate


@dataclass
class SubscriptionChannel(BackboneElement):
    """ The channel on which to report matches to the criteria.

    Details where to send notifications when resources are received that meet
    the criteria.
    """
    resource_type: ClassVar[str] = "SubscriptionChannel"

    type: str = None
    endpoint: Optional[str] = None
    payload: Optional[str] = None
    header: Optional[List[str]] = None


@dataclass
class Subscription(DomainResource):
    """ Server push subscription criteria.

    The subscription resource is used to define a push-based subscription from
    a server to another system. Once a subscription is registered with the
    server, the server checks every resource that is created or updated, and if
    the resource matches the given criteria, it sends a message on the defined
    "channel" so that another system can take an appropriate action.
    """
    resource_type: ClassVar[str] = "Subscription"

    status: str = None
    contact: Optional[List[ContactPoint]] = None
    end: Optional[FHIRDate] = None
    reason: str = None
    criteria: str = None
    error: Optional[str] = None
    channel: SubscriptionChannel = None