#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ResearchStudy) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .relatedartifact import RelatedArtifact


@dataclass
class ResearchStudyArm(BackboneElement):
    """ Defined path through the study for a subject.

    Describes an expected sequence of events for one of the participants of a
    study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
    follow-up.
    """
    resource_type: ClassVar[str] = "ResearchStudyArm"

    name: str = None
    type: Optional[CodeableConcept] = None
    description: Optional[str] = None


@dataclass
class ResearchStudyObjective(BackboneElement):
    """ A goal for the study.

    A goal that the study is aiming to achieve in terms of a scientific
    question to be answered by the analysis of data collected during the study.
    """
    resource_type: ClassVar[str] = "ResearchStudyObjective"

    name: Optional[str] = None
    type: Optional[CodeableConcept] = None


@dataclass
class ResearchStudy(DomainResource):
    """ Investigation to increase healthcare-related patient-independent knowledge.

    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices, therapies
    and other interventional and investigative techniques.  A ResearchStudy
    involves the gathering of information about human or animal subjects.
    """
    resource_type: ClassVar[str] = "ResearchStudy"

    identifier: Optional[List[Identifier]] = None
    title: Optional[str] = None
    protocol: Optional[List[FHIRReference]] = None
    partOf: Optional[List[FHIRReference]] = None
    status: str = None
    primaryPurposeType: Optional[CodeableConcept] = None
    phase: Optional[CodeableConcept] = None
    category: Optional[List[CodeableConcept]] = None
    focus: Optional[List[CodeableConcept]] = None
    condition: Optional[List[CodeableConcept]] = None
    contact: Optional[List[ContactDetail]] = None
    relatedArtifact: Optional[List[RelatedArtifact]] = None
    keyword: Optional[List[CodeableConcept]] = None
    location: Optional[List[CodeableConcept]] = None
    description: Optional[str] = None
    enrollment: Optional[List[FHIRReference]] = None
    period: Optional[Period] = None
    sponsor: Optional[FHIRReference] = None
    principalInvestigator: Optional[FHIRReference] = None
    site: Optional[List[FHIRReference]] = None
    reasonStopped: Optional[CodeableConcept] = None
    note: Optional[List[Annotation]] = None
    arm: Optional[List[ResearchStudyArm]] = None
    objective: Optional[List[ResearchStudyObjective]] = None