#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicationAdministration) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class MedicationAdministrationPerformer(BackboneElement):
    """ Who performed the medication administration and what they did.

    Indicates who or what performed the medication administration and how they
    were involved.
    """
    resource_type: ClassVar[str] = "MedicationAdministrationPerformer"

    function: Optional[CodeableConcept] = None
    actor: FHIRReference = None


@dataclass
class MedicationAdministrationDosage(BackboneElement):
    """ Details of how medication was taken.

    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """
    resource_type: ClassVar[str] = "MedicationAdministrationDosage"

    text: Optional[str] = None
    site: Optional[CodeableConcept] = None
    route: Optional[CodeableConcept] = None
    method: Optional[CodeableConcept] = None
    dose: Optional[Quantity] = None
    rateRatio: Optional[Ratio] = field(default=None, metadata=dict(one_of_many='rate',))
    rateQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='rate',))


@dataclass
class MedicationAdministration(DomainResource):
    """ Administration of medication to a patient.

    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """
    resource_type: ClassVar[str] = "MedicationAdministration"

    identifier: Optional[List[Identifier]] = None
    instantiates: Optional[List[str]] = None
    partOf: Optional[List[FHIRReference]] = None
    status: str = None
    statusReason: Optional[List[CodeableConcept]] = None
    category: Optional[CodeableConcept] = None
    medicationCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='medication',))
    medicationReference: FHIRReference = field(default=None, metadata=dict(one_of_many='medication',))
    subject: FHIRReference = None
    context: Optional[FHIRReference] = None
    supportingInformation: Optional[List[FHIRReference]] = None
    effectiveDateTime: FHIRDate = field(default=None, metadata=dict(one_of_many='effective',))
    effectivePeriod: Period = field(default=None, metadata=dict(one_of_many='effective',))
    performer: Optional[List[MedicationAdministrationPerformer]] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    request: Optional[FHIRReference] = None
    device: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None
    dosage: Optional[MedicationAdministrationDosage] = None
    eventHistory: Optional[List[FHIRReference]] = None