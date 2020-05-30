#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicationDispense) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .dosage import Dosage
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity


@dataclass
class MedicationDispensePerformer(BackboneElement):
    """ Who performed event.

    Indicates who or what performed the event.
    """
    resource_type: ClassVar[str] = "MedicationDispensePerformer"

    function: Optional[CodeableConcept] = None
    actor: FHIRReference = None


@dataclass
class MedicationDispenseSubstitution(BackboneElement):
    """ Whether a substitution was performed on the dispense.

    Indicates whether or not substitution was made as part of the dispense.  In
    some cases, substitution will be expected but does not happen, in other
    cases substitution is not expected but does happen.  This block explains
    what substitution did or did not happen and why.  If nothing is specified,
    substitution was not done.
    """
    resource_type: ClassVar[str] = "MedicationDispenseSubstitution"

    wasSubstituted: bool = None
    type: Optional[CodeableConcept] = None
    reason: Optional[List[CodeableConcept]] = None
    responsibleParty: Optional[List[FHIRReference]] = None


@dataclass
class MedicationDispense(DomainResource):
    """ Dispensing a medication to a named patient.

    Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """
    resource_type: ClassVar[str] = "MedicationDispense"

    identifier: Optional[List[Identifier]] = None
    partOf: Optional[List[FHIRReference]] = None
    status: str = None
    statusReasonCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='statusReason',))
    statusReasonReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='statusReason',))
    category: Optional[CodeableConcept] = None
    medicationCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='medication',))
    medicationReference: FHIRReference = field(default=None, metadata=dict(one_of_many='medication',))
    subject: Optional[FHIRReference] = None
    context: Optional[FHIRReference] = None
    supportingInformation: Optional[List[FHIRReference]] = None
    performer: Optional[List[MedicationDispensePerformer]] = None
    location: Optional[FHIRReference] = None
    authorizingPrescription: Optional[List[FHIRReference]] = None
    type: Optional[CodeableConcept] = None
    quantity: Optional[Quantity] = None
    daysSupply: Optional[Quantity] = None
    whenPrepared: Optional[FHIRDate] = None
    whenHandedOver: Optional[FHIRDate] = None
    destination: Optional[FHIRReference] = None
    receiver: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None
    dosageInstruction: Optional[List[Dosage]] = None
    substitution: Optional[MedicationDispenseSubstitution] = None
    detectedIssue: Optional[List[FHIRReference]] = None
    eventHistory: Optional[List[FHIRReference]] = None