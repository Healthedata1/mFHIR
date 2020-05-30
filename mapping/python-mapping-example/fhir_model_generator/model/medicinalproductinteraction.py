#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductInteraction) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference


@dataclass
class MedicinalProductInteractionInteractant(BackboneElement):
    """ The specific medication, food or laboratory test that interacts.
    """
    resource_type: ClassVar[str] = "MedicinalProductInteractionInteractant"

    itemReference: FHIRReference = field(default=None, metadata=dict(one_of_many='item',))
    itemCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='item',))


@dataclass
class MedicinalProductInteraction(DomainResource):
    """ MedicinalProductInteraction.

    The interactions of the medicinal product with other medicinal products, or
    other forms of interactions.
    """
    resource_type: ClassVar[str] = "MedicinalProductInteraction"

    subject: Optional[List[FHIRReference]] = None
    description: Optional[str] = None
    interactant: Optional[List[MedicinalProductInteractionInteractant]] = None
    type: Optional[CodeableConcept] = None
    effect: Optional[CodeableConcept] = None
    incidence: Optional[CodeableConcept] = None
    management: Optional[CodeableConcept] = None