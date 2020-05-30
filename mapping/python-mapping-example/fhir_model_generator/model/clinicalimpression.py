#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ClinicalImpression) on 2020-02-10.
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


@dataclass
class ClinicalImpressionInvestigation(BackboneElement):
    """ One or more sets of investigations (signs, symptoms, etc.).

    One or more sets of investigations (signs, symptoms, etc.). The actual
    grouping of investigations varies greatly depending on the type and context
    of the assessment. These investigations may include data generated during
    the assessment process, or data previously generated and recorded that is
    pertinent to the outcomes.
    """
    resource_type: ClassVar[str] = "ClinicalImpressionInvestigation"

    code: CodeableConcept = None
    item: Optional[List[FHIRReference]] = None


@dataclass
class ClinicalImpressionFinding(BackboneElement):
    """ Possible or likely findings and diagnoses.

    Specific findings or diagnoses that were considered likely or relevant to
    ongoing treatment.
    """
    resource_type: ClassVar[str] = "ClinicalImpressionFinding"

    itemCodeableConcept: Optional[CodeableConcept] = None
    itemReference: Optional[FHIRReference] = None
    basis: Optional[str] = None


@dataclass
class ClinicalImpression(DomainResource):
    """ A clinical assessment performed when planning treatments and management
    strategies for a patient.

    A record of a clinical assessment performed to determine what problem(s)
    may affect the patient and before planning the treatments or management
    strategies that are best to manage a patient's condition. Assessments are
    often 1:1 with a clinical consultation / encounter,  but this varies
    greatly depending on the clinical workflow. This resource is called
    "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion
    with the recording of assessment tools such as Apgar score.
    """
    resource_type: ClassVar[str] = "ClinicalImpression"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    description: Optional[str] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    effectiveDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='effective',))
    effectivePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='effective',))
    date: Optional[FHIRDate] = None
    assessor: Optional[FHIRReference] = None
    previous: Optional[FHIRReference] = None
    problem: Optional[List[FHIRReference]] = None
    investigation: Optional[List[ClinicalImpressionInvestigation]] = None
    protocol: Optional[List[str]] = None
    summary: Optional[str] = None
    finding: Optional[List[ClinicalImpressionFinding]] = None
    prognosisCodeableConcept: Optional[List[CodeableConcept]] = None
    prognosisReference: Optional[List[FHIRReference]] = None
    supportingInfo: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None