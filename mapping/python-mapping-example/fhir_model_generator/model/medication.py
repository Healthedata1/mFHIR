#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Medication) on 2020-02-10.
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
from .ratio import Ratio


@dataclass
class MedicationIngredient(BackboneElement):
    """ Active or inactive ingredient.

    Identifies a particular constituent of interest in the product.
    """
    resource_type: ClassVar[str] = "MedicationIngredient"

    itemCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='item',))
    itemReference: FHIRReference = field(default=None, metadata=dict(one_of_many='item',))
    isActive: Optional[bool] = None
    strength: Optional[Ratio] = None


@dataclass
class MedicationBatch(BackboneElement):
    """ Details about packaged medications.

    Information that only applies to packages (not products).
    """
    resource_type: ClassVar[str] = "MedicationBatch"

    lotNumber: Optional[str] = None
    expirationDate: Optional[FHIRDate] = None


@dataclass
class Medication(DomainResource):
    """ Definition of a Medication.

    This resource is primarily used for the identification and definition of a
    medication for the purposes of prescribing, dispensing, and administering a
    medication as well as for making statements about medication use.
    """
    resource_type: ClassVar[str] = "Medication"

    identifier: Optional[List[Identifier]] = None
    code: Optional[CodeableConcept] = None
    status: Optional[str] = None
    manufacturer: Optional[FHIRReference] = None
    form: Optional[CodeableConcept] = None
    amount: Optional[Ratio] = None
    ingredient: Optional[List[MedicationIngredient]] = None
    batch: Optional[MedicationBatch] = None