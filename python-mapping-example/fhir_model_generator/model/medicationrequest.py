#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicationRequest) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .dosage import Dosage
from .duration import Duration
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity


@dataclass
class MedicationRequestDispenseRequestInitialFill(BackboneElement):
    """ First fill details.

    Indicates the quantity or duration for the first dispense of the
    medication.
    """
    resource_type: ClassVar[str] = "MedicationRequestDispenseRequestInitialFill"

    quantity: Optional[Quantity] = None
    duration: Optional[Duration] = None


@dataclass
class MedicationRequestDispenseRequest(BackboneElement):
    """ Medication supply authorization.

    Indicates the specific details for the dispense or medication supply part
    of a medication request (also known as a Medication Prescription or
    Medication Order).  Note that this information is not always sent with the
    order.  There may be in some settings (e.g. hospitals) institutional or
    system support for completing the dispense details in the pharmacy
    department.
    """
    resource_type: ClassVar[str] = "MedicationRequestDispenseRequest"

    initialFill: Optional[MedicationRequestDispenseRequestInitialFill] = None
    dispenseInterval: Optional[Duration] = None
    validityPeriod: Optional[Period] = None
    numberOfRepeatsAllowed: Optional[int] = None
    quantity: Optional[Quantity] = None
    expectedSupplyDuration: Optional[Duration] = None
    performer: Optional[FHIRReference] = None


@dataclass
class MedicationRequestSubstitution(BackboneElement):
    """ Any restrictions on medication substitution.

    Indicates whether or not substitution can or should be part of the
    dispense. In some cases, substitution must happen, in other cases
    substitution must not happen. This block explains the prescriber's intent.
    If nothing is specified substitution may be done.
    """
    resource_type: ClassVar[str] = "MedicationRequestSubstitution"

    allowedBoolean: bool = field(default=None, metadata=dict(one_of_many='allowed',))
    allowedCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='allowed',))
    reason: Optional[CodeableConcept] = None


@dataclass
class MedicationRequest(DomainResource):
    """ Ordering of medication for patient or group.

    An order or request for both supply of the medication and the instructions
    for administration of the medication to a patient. The resource is called
    "MedicationRequest" rather than "MedicationPrescription" or
    "MedicationOrder" to generalize the use across inpatient and outpatient
    settings, including care plans, etc., and to harmonize with workflow
    patterns.
    """
    resource_type: ClassVar[str] = "MedicationRequest"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    intent: str = None
    category: Optional[List[CodeableConcept]] = None
    priority: Optional[str] = None
    doNotPerform: Optional[bool] = None
    reportedBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='reported',))
    reportedReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='reported',))
    medicationCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='medication',))
    medicationReference: FHIRReference = field(default=None, metadata=dict(one_of_many='medication',))
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    supportingInformation: Optional[List[FHIRReference]] = None
    authoredOn: Optional[FHIRDate] = None
    requester: Optional[FHIRReference] = None
    performer: Optional[FHIRReference] = None
    performerType: Optional[CodeableConcept] = None
    recorder: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    instantiatesCanonical: Optional[List[str]] = None
    instantiatesUri: Optional[List[str]] = None
    basedOn: Optional[List[FHIRReference]] = None
    groupIdentifier: Optional[Identifier] = None
    courseOfTherapyType: Optional[CodeableConcept] = None
    insurance: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None
    dosageInstruction: Optional[List[Dosage]] = None
    dispenseRequest: Optional[MedicationRequestDispenseRequest] = None
    substitution: Optional[MedicationRequestSubstitution] = None
    priorPrescription: Optional[FHIRReference] = None
    detectedIssue: Optional[List[FHIRReference]] = None
    eventHistory: Optional[List[FHIRReference]] = None