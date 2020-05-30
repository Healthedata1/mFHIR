#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Location) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .address import Address
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class LocationPosition(BackboneElement):
    """ The absolute geographic location.

    The absolute geographic location of the Location, expressed using the WGS84
    datum (This is the same co-ordinate system used in KML).
    """
    resource_type: ClassVar[str] = "LocationPosition"

    longitude: float = None
    latitude: float = None
    altitude: Optional[float] = None


@dataclass
class LocationHoursOfOperation(BackboneElement):
    """ What days/times during a week is this location usually open.
    """
    resource_type: ClassVar[str] = "LocationHoursOfOperation"

    daysOfWeek: Optional[List[str]] = None
    allDay: Optional[bool] = None
    openingTime: Optional[FHIRDate] = None
    closingTime: Optional[FHIRDate] = None


@dataclass
class Location(DomainResource):
    """ Details and position information for a physical place.

    Details and position information for a physical place where services are
    provided and resources and participants may be stored, found, contained, or
    accommodated.
    """
    resource_type: ClassVar[str] = "Location"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    operationalStatus: Optional[Coding] = None
    name: Optional[str] = None
    alias: Optional[List[str]] = None
    description: Optional[str] = None
    mode: Optional[str] = None
    type: Optional[List[CodeableConcept]] = None
    telecom: Optional[List[ContactPoint]] = None
    address: Optional[Address] = None
    physicalType: Optional[CodeableConcept] = None
    position: Optional[LocationPosition] = None
    managingOrganization: Optional[FHIRReference] = None
    partOf: Optional[FHIRReference] = None
    hoursOfOperation: Optional[List[LocationHoursOfOperation]] = None
    availabilityExceptions: Optional[str] = None
    endpoint: Optional[List[FHIRReference]] = None