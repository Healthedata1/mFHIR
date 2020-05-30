#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Appointment) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class AppointmentParticipant(BackboneElement):
    """ Participants involved in appointment.

    List of participants involved in the appointment.
    """
    resource_type: ClassVar[str] = "AppointmentParticipant"

    type: Optional[List[CodeableConcept]] = None
    actor: Optional[FHIRReference] = None
    required: Optional[str] = None
    status: str = None
    period: Optional[Period] = None


@dataclass
class Appointment(DomainResource):
    """ A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one
    or more Encounter(s).
    """
    resource_type: ClassVar[str] = "Appointment"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    cancelationReason: Optional[CodeableConcept] = None
    serviceCategory: Optional[List[CodeableConcept]] = None
    serviceType: Optional[List[CodeableConcept]] = None
    specialty: Optional[List[CodeableConcept]] = None
    appointmentType: Optional[CodeableConcept] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    priority: Optional[int] = None
    description: Optional[str] = None
    supportingInformation: Optional[List[FHIRReference]] = None
    start: Optional[FHIRDate] = None
    end: Optional[FHIRDate] = None
    minutesDuration: Optional[int] = None
    slot: Optional[List[FHIRReference]] = None
    created: Optional[FHIRDate] = None
    comment: Optional[str] = None
    patientInstruction: Optional[str] = None
    basedOn: Optional[List[FHIRReference]] = None
    participant: List[AppointmentParticipant] = field(default_factory=list)
    requestedPeriod: Optional[List[Period]] = None