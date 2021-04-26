#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DetectedIssue) on 2020-02-10.
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
from .period import Period


@dataclass
class DetectedIssueEvidence(BackboneElement):
    """ Supporting evidence.

    Supporting evidence or manifestations that provide the basis for
    identifying the detected issue such as a GuidanceResponse or MeasureReport.
    """
    resource_type: ClassVar[str] = "DetectedIssueEvidence"

    code: Optional[List[CodeableConcept]] = None
    detail: Optional[List[FHIRReference]] = None


@dataclass
class DetectedIssueMitigation(BackboneElement):
    """ Step taken to address.

    Indicates an action that has been taken or is committed to reduce or
    eliminate the likelihood of the risk identified by the detected issue from
    manifesting.  Can also reflect an observation of known mitigating factors
    that may reduce/eliminate the need for any action.
    """
    resource_type: ClassVar[str] = "DetectedIssueMitigation"

    action: CodeableConcept = None
    date: Optional[FHIRDate] = None
    author: Optional[FHIRReference] = None


@dataclass
class DetectedIssue(DomainResource):
    """ Clinical issue with action.

    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """
    resource_type: ClassVar[str] = "DetectedIssue"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    code: Optional[CodeableConcept] = None
    severity: Optional[str] = None
    patient: Optional[FHIRReference] = None
    identifiedDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='identified',))
    identifiedPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='identified',))
    author: Optional[FHIRReference] = None
    implicated: Optional[List[FHIRReference]] = None
    evidence: Optional[List[DetectedIssueEvidence]] = None
    detail: Optional[str] = None
    reference: Optional[str] = None
    mitigation: Optional[List[DetectedIssueMitigation]] = None