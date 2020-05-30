#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Substance) on 2020-02-10.
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
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class SubstanceInstance(BackboneElement):
    """ If this describes a specific package/container of the substance.

    Substance may be used to describe a kind of substance, or a specific
    package/container of the substance: an instance.
    """
    resource_type: ClassVar[str] = "SubstanceInstance"

    identifier: Optional[Identifier] = None
    expiry: Optional[FHIRDate] = None
    quantity: Optional[Quantity] = None


@dataclass
class SubstanceIngredient(BackboneElement):
    """ Composition information about the substance.

    A substance can be composed of other substances.
    """
    resource_type: ClassVar[str] = "SubstanceIngredient"

    quantity: Optional[Ratio] = None
    substanceCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='substance',))
    substanceReference: FHIRReference = field(default=None, metadata=dict(one_of_many='substance',))


@dataclass
class Substance(DomainResource):
    """ A homogeneous material with a definite composition.
    """
    resource_type: ClassVar[str] = "Substance"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    category: Optional[List[CodeableConcept]] = None
    code: CodeableConcept = None
    description: Optional[str] = None
    instance: Optional[List[SubstanceInstance]] = None
    ingredient: Optional[List[SubstanceIngredient]] = None