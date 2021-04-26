#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/AdverseEvent) on 2020-02-10.
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


@dataclass
class AdverseEventSuspectEntityCausality(BackboneElement):
    """ Information on the possible cause of the event.
    """
    resource_type: ClassVar[str] = "AdverseEventSuspectEntityCausality"

    assessment: Optional[CodeableConcept] = None
    productRelatedness: Optional[str] = None
    author: Optional[FHIRReference] = None
    method: Optional[CodeableConcept] = None


@dataclass
class AdverseEventSuspectEntity(BackboneElement):
    """ The suspected agent causing the adverse event.

    Describes the entity that is suspected to have caused the adverse event.
    """
    resource_type: ClassVar[str] = "AdverseEventSuspectEntity"

    instance: FHIRReference = None
    causality: Optional[List[AdverseEventSuspectEntityCausality]] = None


@dataclass
class AdverseEvent(DomainResource):
    """ Medical care, research study or other healthcare event causing physical
    injury.

    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or other
    healthcare setting factors that requires additional monitoring, treatment,
    or hospitalization, or that results in death.
    """
    resource_type: ClassVar[str] = "AdverseEvent"

    identifier: Optional[Identifier] = None
    actuality: str = None
    category: Optional[List[CodeableConcept]] = None
    event: Optional[CodeableConcept] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    detected: Optional[FHIRDate] = None
    recordedDate: Optional[FHIRDate] = None
    resultingCondition: Optional[List[FHIRReference]] = None
    location: Optional[FHIRReference] = None
    seriousness: Optional[CodeableConcept] = None
    severity: Optional[CodeableConcept] = None
    outcome: Optional[CodeableConcept] = None
    recorder: Optional[FHIRReference] = None
    contributor: Optional[List[FHIRReference]] = None
    suspectEntity: Optional[List[AdverseEventSuspectEntity]] = None
    subjectMedicalHistory: Optional[List[FHIRReference]] = None
    referenceDocument: Optional[List[FHIRReference]] = None
    study: Optional[List[FHIRReference]] = None