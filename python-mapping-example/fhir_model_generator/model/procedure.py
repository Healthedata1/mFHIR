#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Procedure) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .age import Age
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .range import Range


@dataclass
class ProcedurePerformer(BackboneElement):
    """ The people who performed the procedure.

    Limited to "real" people rather than equipment.
    """
    resource_type: ClassVar[str] = "ProcedurePerformer"

    function: Optional[CodeableConcept] = None
    actor: FHIRReference = None
    onBehalfOf: Optional[FHIRReference] = None


@dataclass
class ProcedureFocalDevice(BackboneElement):
    """ Manipulated, implanted, or removed device.

    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """
    resource_type: ClassVar[str] = "ProcedureFocalDevice"

    action: Optional[CodeableConcept] = None
    manipulated: FHIRReference = None


@dataclass
class Procedure(DomainResource):
    """ An action that is being or was performed on a patient.

    An action that is or was performed on or for a patient. This can be a
    physical intervention like an operation, or less invasive like long term
    services, counseling, or hypnotherapy.
    """
    resource_type: ClassVar[str] = "Procedure"

    identifier: Optional[List[Identifier]] = None
    instantiatesCanonical: Optional[List[str]] = None
    instantiatesUri: Optional[List[str]] = None
    basedOn: Optional[List[FHIRReference]] = None
    partOf: Optional[List[FHIRReference]] = None
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    category: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    performedDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='performed',))
    performedPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='performed',))
    performedString: Optional[str] = field(default=None, metadata=dict(one_of_many='performed',))
    performedAge: Optional[Age] = field(default=None, metadata=dict(one_of_many='performed',))
    performedRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='performed',))
    recorder: Optional[FHIRReference] = None
    asserter: Optional[FHIRReference] = None
    performer: Optional[List[ProcedurePerformer]] = None
    location: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    bodySite: Optional[List[CodeableConcept]] = None
    outcome: Optional[CodeableConcept] = None
    report: Optional[List[FHIRReference]] = None
    complication: Optional[List[CodeableConcept]] = None
    complicationDetail: Optional[List[FHIRReference]] = None
    followUp: Optional[List[CodeableConcept]] = None
    note: Optional[List[Annotation]] = None
    focalDevice: Optional[List[ProcedureFocalDevice]] = None
    usedReference: Optional[List[FHIRReference]] = None
    usedCode: Optional[List[CodeableConcept]] = None