#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DiagnosticReport) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class DiagnosticReportMedia(BackboneElement):
    """ Key images associated with this report.

    A list of key images associated with this report. The images are generally
    created during the diagnostic process, and may be directly of the patient,
    or of treated specimens (i.e. slides of interest).
    """
    resource_type: ClassVar[str] = "DiagnosticReportMedia"

    comment: Optional[str] = None
    link: FHIRReference = None


@dataclass
class DiagnosticReport(DomainResource):
    """ A Diagnostic report - a combination of request information, atomic results,
    images, interpretation, as well as formatted reports.

    The findings and interpretation of diagnostic  tests performed on patients,
    groups of patients, devices, and locations, and/or specimens derived from
    these. The report includes clinical context such as requesting and provider
    information, and some mix of atomic results, images, textual and coded
    interpretations, and formatted representation of diagnostic reports.
    """
    resource_type: ClassVar[str] = "DiagnosticReport"

    identifier: Optional[List[Identifier]] = None
    basedOn: Optional[List[FHIRReference]] = None
    status: str = None
    category: Optional[List[CodeableConcept]] = None
    code: CodeableConcept = None
    subject: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    effectiveDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='effective',))
    effectivePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='effective',))
    issued: Optional[FHIRDate] = None
    performer: Optional[List[FHIRReference]] = None
    resultsInterpreter: Optional[List[FHIRReference]] = None
    specimen: Optional[List[FHIRReference]] = None
    result: Optional[List[FHIRReference]] = None
    imagingStudy: Optional[List[FHIRReference]] = None
    media: Optional[List[DiagnosticReportMedia]] = None
    conclusion: Optional[str] = None
    conclusionCode: Optional[List[CodeableConcept]] = None
    presentedForm: Optional[List[Attachment]] = None