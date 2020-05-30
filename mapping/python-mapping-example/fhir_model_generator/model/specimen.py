#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Specimen) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .duration import Duration
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity


@dataclass
class SpecimenCollection(BackboneElement):
    """ Collection details.

    Details concerning the specimen collection.
    """
    resource_type: ClassVar[str] = "SpecimenCollection"

    collector: Optional[FHIRReference] = None
    collectedDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='collected',))
    collectedPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='collected',))
    duration: Optional[Duration] = None
    quantity: Optional[Quantity] = None
    method: Optional[CodeableConcept] = None
    bodySite: Optional[CodeableConcept] = None
    fastingStatusCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='fastingStatus',))
    fastingStatusDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='fastingStatus',))


@dataclass
class SpecimenProcessing(BackboneElement):
    """ Processing and processing step details.

    Details concerning processing and processing steps for the specimen.
    """
    resource_type: ClassVar[str] = "SpecimenProcessing"

    description: Optional[str] = None
    procedure: Optional[CodeableConcept] = None
    additive: Optional[List[FHIRReference]] = None
    timeDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='time',))
    timePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='time',))


@dataclass
class SpecimenContainer(BackboneElement):
    """ Direct container of specimen (tube/slide, etc.).

    The container holding the specimen.  The recursive nature of containers;
    i.e. blood in tube in tray in rack is not addressed here.
    """
    resource_type: ClassVar[str] = "SpecimenContainer"

    identifier: Optional[List[Identifier]] = None
    description: Optional[str] = None
    type: Optional[CodeableConcept] = None
    capacity: Optional[Quantity] = None
    specimenQuantity: Optional[Quantity] = None
    additiveCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='additive',))
    additiveReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='additive',))


@dataclass
class Specimen(DomainResource):
    """ Sample for analysis.

    A sample to be used for analysis.
    """
    resource_type: ClassVar[str] = "Specimen"

    identifier: Optional[List[Identifier]] = None
    accessionIdentifier: Optional[Identifier] = None
    status: Optional[str] = None
    type: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    receivedTime: Optional[FHIRDate] = None
    parent: Optional[List[FHIRReference]] = None
    request: Optional[List[FHIRReference]] = None
    collection: Optional[SpecimenCollection] = None
    processing: Optional[List[SpecimenProcessing]] = None
    container: Optional[List[SpecimenContainer]] = None
    condition: Optional[List[CodeableConcept]] = None
    note: Optional[List[Annotation]] = None