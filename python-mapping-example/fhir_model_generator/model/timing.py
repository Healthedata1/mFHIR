#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Timing) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .duration import Duration
from .element import Element
from .fhirdate import FHIRDate
from .period import Period
from .range import Range


@dataclass
class TimingRepeat(Element):
    """ When the event is to occur.

    A set of rules that describe when the event is scheduled.
    """
    resource_type: ClassVar[str] = "TimingRepeat"

    boundsDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='bounds',))
    boundsRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='bounds',))
    boundsPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='bounds',))
    count: Optional[int] = None
    countMax: Optional[int] = None
    duration: Optional[float] = None
    durationMax: Optional[float] = None
    durationUnit: Optional[str] = None
    frequency: Optional[int] = None
    frequencyMax: Optional[int] = None
    period: Optional[float] = None
    periodMax: Optional[float] = None
    periodUnit: Optional[str] = None
    dayOfWeek: Optional[List[str]] = None
    timeOfDay: Optional[List[FHIRDate]] = None
    when: Optional[List[str]] = None
    offset: Optional[int] = None


@dataclass
class Timing(BackboneElement):
    """ A timing schedule that specifies an event that may occur multiple times.

    Specifies an event that may occur multiple times. Timing schedules are used
    to record when things are planned, expected or requested to occur. The most
    common usage is in dosage instructions for medications. They are also used
    when planning care of various kinds, and may be used for reporting the
    schedule to which past regular activities were carried out.
    """
    resource_type: ClassVar[str] = "Timing"

    event: Optional[List[FHIRDate]] = None
    repeat: Optional[TimingRepeat] = None
    code: Optional[CodeableConcept] = None