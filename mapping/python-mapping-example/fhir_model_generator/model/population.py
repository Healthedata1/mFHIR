#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Population) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .range import Range


@dataclass
class Population(BackboneElement):
    """ A definition of a set of people that apply to some clinically related
    context, for example people contraindicated for a certain medication.

    A populatioof people with some set of grouping criteria.
    """
    resource_type: ClassVar[str] = "Population"

    ageRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='age',))
    ageCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='age',))
    gender: Optional[CodeableConcept] = None
    race: Optional[CodeableConcept] = None
    physiologicalCondition: Optional[CodeableConcept] = None