#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductIngredient) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .ratio import Ratio


@dataclass
class MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength(BackboneElement):
    """ Strength expressed in terms of a reference substance.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength"

    substance: Optional[CodeableConcept] = None
    strength: Ratio = None
    strengthLowLimit: Optional[Ratio] = None
    measurementPoint: Optional[str] = None
    country: Optional[List[CodeableConcept]] = None


@dataclass
class MedicinalProductIngredientSpecifiedSubstanceStrength(BackboneElement):
    """ Quantity of the substance or specified substance present in the
    manufactured item or pharmaceutical product.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSpecifiedSubstanceStrength"

    presentation: Ratio = None
    presentationLowLimit: Optional[Ratio] = None
    concentration: Optional[Ratio] = None
    concentrationLowLimit: Optional[Ratio] = None
    measurementPoint: Optional[str] = None
    country: Optional[List[CodeableConcept]] = None
    referenceStrength: Optional[List[MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength]] = None


@dataclass
class MedicinalProductIngredientSpecifiedSubstance(BackboneElement):
    """ A specified substance that comprises this ingredient.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSpecifiedSubstance"

    code: CodeableConcept = None
    group: CodeableConcept = None
    confidentiality: Optional[CodeableConcept] = None
    strength: Optional[List[MedicinalProductIngredientSpecifiedSubstanceStrength]] = None


@dataclass
class MedicinalProductIngredientSubstance(BackboneElement):
    """ The ingredient substance.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSubstance"

    code: CodeableConcept = None
    strength: Optional[List[MedicinalProductIngredientSpecifiedSubstanceStrength]] = None


@dataclass
class MedicinalProductIngredient(DomainResource):
    """ An ingredient of a manufactured item or pharmaceutical product.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredient"

    identifier: Optional[Identifier] = None
    role: CodeableConcept = None
    allergenicIndicator: Optional[bool] = None
    manufacturer: Optional[List[FHIRReference]] = None
    specifiedSubstance: Optional[List[MedicinalProductIngredientSpecifiedSubstance]] = None
    substance: Optional[MedicinalProductIngredientSubstance] = None