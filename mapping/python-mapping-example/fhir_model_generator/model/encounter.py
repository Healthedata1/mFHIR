#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Encounter) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .duration import Duration
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class EncounterStatusHistory(BackboneElement):
    """ List of past encounter statuses.

    The status history permits the encounter resource to contain the status
    history without needing to read through the historical versions of the
    resource, or even have the server store them.
    """
    resource_type: ClassVar[str] = "EncounterStatusHistory"

    status: str = None
    period: Period = None


@dataclass
class EncounterClassHistory(BackboneElement):
    """ List of past encounter classes.

    The class history permits the tracking of the encounters transitions
    without needing to go  through the resource history.  This would be used
    for a case where an admission starts of as an emergency encounter, then
    transitions into an inpatient scenario. Doing this and not restarting a new
    encounter ensures that any lab/diagnostic results can more easily follow
    the patient and not require re-processing and not get lost or cancelled
    during a kind of discharge from emergency to inpatient.
    """
    resource_type: ClassVar[str] = "EncounterClassHistory"

    class_fhir: Coding = field(default=None, metadata=dict(orig_name='class'))
    period: Period = None


@dataclass
class EncounterParticipant(BackboneElement):
    """ List of participants involved in the encounter.

    The list of people responsible for providing the service.
    """
    resource_type: ClassVar[str] = "EncounterParticipant"

    type: Optional[List[CodeableConcept]] = None
    period: Optional[Period] = None
    individual: Optional[FHIRReference] = None


@dataclass
class EncounterDiagnosis(BackboneElement):
    """ The list of diagnosis relevant to this encounter.
    """
    resource_type: ClassVar[str] = "EncounterDiagnosis"

    condition: FHIRReference = None
    use: Optional[CodeableConcept] = None
    rank: Optional[int] = None


@dataclass
class EncounterHospitalization(BackboneElement):
    """ Details about the admission to a healthcare service.
    """
    resource_type: ClassVar[str] = "EncounterHospitalization"

    preAdmissionIdentifier: Optional[Identifier] = None
    origin: Optional[FHIRReference] = None
    admitSource: Optional[CodeableConcept] = None
    reAdmission: Optional[CodeableConcept] = None
    dietPreference: Optional[List[CodeableConcept]] = None
    specialCourtesy: Optional[List[CodeableConcept]] = None
    specialArrangement: Optional[List[CodeableConcept]] = None
    destination: Optional[FHIRReference] = None
    dischargeDisposition: Optional[CodeableConcept] = None


@dataclass
class EncounterLocation(BackboneElement):
    """ List of locations where the patient has been.

    List of locations where  the patient has been during this encounter.
    """
    resource_type: ClassVar[str] = "EncounterLocation"

    location: FHIRReference = None
    status: Optional[str] = None
    physicalType: Optional[CodeableConcept] = None
    period: Optional[Period] = None


@dataclass
class Encounter(DomainResource):
    """ An interaction during which services are provided to the patient.

    An interaction between a patient and healthcare provider(s) for the purpose
    of providing healthcare service(s) or assessing the health status of a
    patient.
    """
    resource_type: ClassVar[str] = "Encounter"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    statusHistory: Optional[List[EncounterStatusHistory]] = None
    class_fhir: Coding = field(default=None, metadata=dict(orig_name='class'))
    classHistory: Optional[List[EncounterClassHistory]] = None
    type: Optional[List[CodeableConcept]] = None
    serviceType: Optional[CodeableConcept] = None
    priority: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    episodeOfCare: Optional[List[FHIRReference]] = None
    basedOn: Optional[List[FHIRReference]] = None
    participant: Optional[List[EncounterParticipant]] = None
    appointment: Optional[List[FHIRReference]] = None
    period: Optional[Period] = None
    length: Optional[Duration] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    diagnosis: Optional[List[EncounterDiagnosis]] = None
    account: Optional[List[FHIRReference]] = None
    hospitalization: Optional[EncounterHospitalization] = None
    location: Optional[List[EncounterLocation]] = None
    serviceProvider: Optional[FHIRReference] = None
    partOf: Optional[FHIRReference] = None