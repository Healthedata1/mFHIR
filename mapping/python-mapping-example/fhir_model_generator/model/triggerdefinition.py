#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/TriggerDefinition) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .datarequirement import DataRequirement
from .element import Element
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .timing import Timing


@dataclass
class TriggerDefinition(Element):
    """ Defines an expected trigger for a module.

    A description of a triggering event. Triggering events can be named events,
    data events, or periodic, as determined by the type element.
    """
    resource_type: ClassVar[str] = "TriggerDefinition"

    type: str = None
    name: Optional[str] = None
    timingTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='timing',))
    timingReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='timing',))
    timingDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='timing',))
    timingDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='timing',))
    data: Optional[List[DataRequirement]] = None
    condition: Optional[Expression] = None