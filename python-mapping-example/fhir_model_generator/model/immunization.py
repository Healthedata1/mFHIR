#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Immunization) on 2020-02-10.
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
from .quantity import Quantity


@dataclass
class ImmunizationPerformer(BackboneElement):
    """ Who performed event.

    Indicates who performed the immunization event.
    """
    resource_type: ClassVar[str] = "ImmunizationPerformer"

    function: Optional[CodeableConcept] = None
    actor: FHIRReference = None


@dataclass
class ImmunizationEducation(BackboneElement):
    """ Educational material presented to patient.

    Educational material presented to the patient (or guardian) at the time of
    vaccine administration.
    """
    resource_type: ClassVar[str] = "ImmunizationEducation"

    documentType: Optional[str] = None
    reference: Optional[str] = None
    publicationDate: Optional[FHIRDate] = None
    presentationDate: Optional[FHIRDate] = None


@dataclass
class ImmunizationReaction(BackboneElement):
    """ Details of a reaction that follows immunization.

    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """
    resource_type: ClassVar[str] = "ImmunizationReaction"

    date: Optional[FHIRDate] = None
    detail: Optional[FHIRReference] = None
    reported: Optional[bool] = None


@dataclass
class ImmunizationProtocolApplied(BackboneElement):
    """ Protocol followed by the provider.

    The protocol (set of recommendations) being followed by the provider who
    administered the dose.
    """
    resource_type: ClassVar[str] = "ImmunizationProtocolApplied"

    series: Optional[str] = None
    authority: Optional[FHIRReference] = None
    targetDisease: Optional[List[CodeableConcept]] = None
    doseNumberPositiveInt: int = field(default=None, metadata=dict(one_of_many='doseNumber',))
    doseNumberString: str = field(default=None, metadata=dict(one_of_many='doseNumber',))
    seriesDosesPositiveInt: Optional[int] = field(default=None, metadata=dict(one_of_many='seriesDoses',))
    seriesDosesString: Optional[str] = field(default=None, metadata=dict(one_of_many='seriesDoses',))


@dataclass
class Immunization(DomainResource):
    """ Immunization event information.

    Describes the event of a patient being administered a vaccine or a record
    of an immunization as reported by a patient, a clinician or another party.
    """
    resource_type: ClassVar[str] = "Immunization"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    vaccineCode: CodeableConcept = None
    patient: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    occurrenceDateTime: FHIRDate = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrenceString: str = field(default=None, metadata=dict(one_of_many='occurrence',))
    recorded: Optional[FHIRDate] = None
    primarySource: Optional[bool] = None
    reportOrigin: Optional[CodeableConcept] = None
    location: Optional[FHIRReference] = None
    manufacturer: Optional[FHIRReference] = None
    lotNumber: Optional[str] = None
    expirationDate: Optional[FHIRDate] = None
    site: Optional[CodeableConcept] = None
    route: Optional[CodeableConcept] = None
    doseQuantity: Optional[Quantity] = None
    performer: Optional[List[ImmunizationPerformer]] = None
    note: Optional[List[Annotation]] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    isSubpotent: Optional[bool] = None
    subpotentReason: Optional[List[CodeableConcept]] = None
    education: Optional[List[ImmunizationEducation]] = None
    programEligibility: Optional[List[CodeableConcept]] = None
    fundingSource: Optional[CodeableConcept] = None
    reaction: Optional[List[ImmunizationReaction]] = None
    protocolApplied: Optional[List[ImmunizationProtocolApplied]] = None