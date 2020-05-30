#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ImagingStudy) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class ImagingStudySeriesPerformer(BackboneElement):
    """ Who performed the series.

    Indicates who or what performed the series and how they were involved.
    """
    resource_type: ClassVar[str] = "ImagingStudySeriesPerformer"

    function: Optional[CodeableConcept] = None
    actor: FHIRReference = None


@dataclass
class ImagingStudySeriesInstance(BackboneElement):
    """ A single SOP instance from the series.

    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """
    resource_type: ClassVar[str] = "ImagingStudySeriesInstance"

    uid: str = None
    sopClass: Coding = None
    number: Optional[int] = None
    title: Optional[str] = None


@dataclass
class ImagingStudySeries(BackboneElement):
    """ Each study has one or more series of instances.

    Each study has one or more series of images or other content.
    """
    resource_type: ClassVar[str] = "ImagingStudySeries"

    uid: str = None
    number: Optional[int] = None
    modality: Coding = None
    description: Optional[str] = None
    numberOfInstances: Optional[int] = None
    endpoint: Optional[List[FHIRReference]] = None
    bodySite: Optional[Coding] = None
    laterality: Optional[Coding] = None
    specimen: Optional[List[FHIRReference]] = None
    started: Optional[FHIRDate] = None
    performer: Optional[List[ImagingStudySeriesPerformer]] = None
    instance: Optional[List[ImagingStudySeriesInstance]] = None


@dataclass
class ImagingStudy(DomainResource):
    """ A set of images produced in single study (one or more series of references
    images).

    Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-Object
    Pair Instances (SOP Instances - images or other data) acquired or produced
    in a common context.  A series is of only one modality (e.g. X-ray, CT, MR,
    ultrasound), but a study may have multiple series of different modalities.
    """
    resource_type: ClassVar[str] = "ImagingStudy"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    modality: Optional[List[Coding]] = None
    subject: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    started: Optional[FHIRDate] = None
    basedOn: Optional[List[FHIRReference]] = None
    referrer: Optional[FHIRReference] = None
    interpreter: Optional[List[FHIRReference]] = None
    endpoint: Optional[List[FHIRReference]] = None
    numberOfSeries: Optional[int] = None
    numberOfInstances: Optional[int] = None
    procedureReference: Optional[FHIRReference] = None
    procedureCode: Optional[List[CodeableConcept]] = None
    location: Optional[FHIRReference] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None
    description: Optional[str] = None
    series: Optional[List[ImagingStudySeries]] = None