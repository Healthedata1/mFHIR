#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/AllergyIntolerance) on 2020-02-10.
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
class AllergyIntoleranceReaction(BackboneElement):
    """ Adverse Reaction Events linked to exposure to substance.

    Details about each adverse reaction event linked to exposure to the
    identified substance.
    """
    resource_type: ClassVar[str] = "AllergyIntoleranceReaction"

    substance: Optional[CodeableConcept] = None
    manifestation: List[CodeableConcept] = field(default_factory=list)
    description: Optional[str] = None
    onset: Optional[FHIRDate] = None
    severity: Optional[str] = None
    exposureRoute: Optional[CodeableConcept] = None
    note: Optional[List[Annotation]] = None


@dataclass
class AllergyIntolerance(DomainResource):
    """ Allergy or Intolerance (generally: Risk of adverse reaction to a substance).

    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """
    resource_type: ClassVar[str] = "AllergyIntolerance"

    identifier: Optional[List[Identifier]] = None
    clinicalStatus: Optional[CodeableConcept] = None
    verificationStatus: Optional[CodeableConcept] = None
    type: Optional[str] = None
    category: Optional[List[str]] = None
    criticality: Optional[str] = None
    code: Optional[CodeableConcept] = None
    patient: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    onsetDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='onset',))
    onsetAge: Optional[Age] = field(default=None, metadata=dict(one_of_many='onset',))
    onsetPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='onset',))
    onsetRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='onset',))
    onsetString: Optional[str] = field(default=None, metadata=dict(one_of_many='onset',))
    recordedDate: Optional[FHIRDate] = None
    recorder: Optional[FHIRReference] = None
    asserter: Optional[FHIRReference] = None
    lastOccurrence: Optional[FHIRDate] = None
    note: Optional[List[Annotation]] = None
    reaction: Optional[List[AllergyIntoleranceReaction]] = None