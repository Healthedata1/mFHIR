#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DeviceMetric) on 2020-02-10.
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
from .timing import Timing


@dataclass
class DeviceMetricCalibration(BackboneElement):
    """ Describes the calibrations that have been performed or that are required to
    be performed.
    """
    resource_type: ClassVar[str] = "DeviceMetricCalibration"

    type: Optional[str] = None
    state: Optional[str] = None
    time: Optional[FHIRDate] = None


@dataclass
class DeviceMetric(DomainResource):
    """ Measurement, calculation or setting capability of a medical device.

    Describes a measurement, calculation or setting capability of a medical
    device.
    """
    resource_type: ClassVar[str] = "DeviceMetric"

    identifier: Optional[List[Identifier]] = None
    type: CodeableConcept = None
    unit: Optional[CodeableConcept] = None
    source: Optional[FHIRReference] = None
    parent: Optional[FHIRReference] = None
    operationalStatus: Optional[str] = None
    color: Optional[str] = None
    category: str = None
    measurementPeriod: Optional[Timing] = None
    calibration: Optional[List[DeviceMetricCalibration]] = None