#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/HealthcareService) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class HealthcareServiceEligibility(BackboneElement):
    """ Specific eligibility requirements required to use the service.

    Does this service have specific eligibility requirements that need to be
    met in order to use the service?
    """
    resource_type: ClassVar[str] = "HealthcareServiceEligibility"

    code: Optional[CodeableConcept] = None
    comment: Optional[str] = None


@dataclass
class HealthcareServiceAvailableTime(BackboneElement):
    """ Times the Service Site is available.

    A collection of times that the Service Site is available.
    """
    resource_type: ClassVar[str] = "HealthcareServiceAvailableTime"

    daysOfWeek: Optional[List[str]] = None
    allDay: Optional[bool] = None
    availableStartTime: Optional[FHIRDate] = None
    availableEndTime: Optional[FHIRDate] = None


@dataclass
class HealthcareServiceNotAvailable(BackboneElement):
    """ Not available during this time due to provided reason.

    The HealthcareService is not available during this period of time due to
    the provided reason.
    """
    resource_type: ClassVar[str] = "HealthcareServiceNotAvailable"

    description: str = None
    during: Optional[Period] = None


@dataclass
class HealthcareService(DomainResource):
    """ The details of a healthcare service available at a location.
    """
    resource_type: ClassVar[str] = "HealthcareService"

    identifier: Optional[List[Identifier]] = None
    active: Optional[bool] = None
    providedBy: Optional[FHIRReference] = None
    category: Optional[List[CodeableConcept]] = None
    type: Optional[List[CodeableConcept]] = None
    specialty: Optional[List[CodeableConcept]] = None
    location: Optional[List[FHIRReference]] = None
    name: Optional[str] = None
    comment: Optional[str] = None
    extraDetails: Optional[str] = None
    photo: Optional[Attachment] = None
    telecom: Optional[List[ContactPoint]] = None
    coverageArea: Optional[List[FHIRReference]] = None
    serviceProvisionCode: Optional[List[CodeableConcept]] = None
    eligibility: Optional[List[HealthcareServiceEligibility]] = None
    program: Optional[List[CodeableConcept]] = None
    characteristic: Optional[List[CodeableConcept]] = None
    communication: Optional[List[CodeableConcept]] = None
    referralMethod: Optional[List[CodeableConcept]] = None
    appointmentRequired: Optional[bool] = None
    availableTime: Optional[List[HealthcareServiceAvailableTime]] = None
    notAvailable: Optional[List[HealthcareServiceNotAvailable]] = None
    availabilityExceptions: Optional[str] = None
    endpoint: Optional[List[FHIRReference]] = None