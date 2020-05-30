#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/NutritionOrder) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .ratio import Ratio
from .timing import Timing


@dataclass
class NutritionOrderEnteralFormulaAdministration(BackboneElement):
    """ Formula feeding instruction as structured data.

    Formula administration instructions as structured data.  This repeating
    structure allows for changing the administration rate or volume over time
    for both bolus and continuous feeding.  An example of this would be an
    instruction to increase the rate of continuous feeding every 2 hours.
    """
    resource_type: ClassVar[str] = "NutritionOrderEnteralFormulaAdministration"

    schedule: Optional[Timing] = None
    quantity: Optional[Quantity] = None
    rateQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='rate',))
    rateRatio: Optional[Ratio] = field(default=None, metadata=dict(one_of_many='rate',))


@dataclass
class NutritionOrderOralDietNutrient(BackboneElement):
    """ Required  nutrient modifications.

    Class that defines the quantity and type of nutrient modifications (for
    example carbohydrate, fiber or sodium) required for the oral diet.
    """
    resource_type: ClassVar[str] = "NutritionOrderOralDietNutrient"

    modifier: Optional[CodeableConcept] = None
    amount: Optional[Quantity] = None


@dataclass
class NutritionOrderOralDietTexture(BackboneElement):
    """ Required  texture modifications.

    Class that describes any texture modifications required for the patient to
    safely consume various types of solid foods.
    """
    resource_type: ClassVar[str] = "NutritionOrderOralDietTexture"

    modifier: Optional[CodeableConcept] = None
    foodType: Optional[CodeableConcept] = None


@dataclass
class NutritionOrderOralDiet(BackboneElement):
    """ Oral diet components.

    Diet given orally in contrast to enteral (tube) feeding.
    """
    resource_type: ClassVar[str] = "NutritionOrderOralDiet"

    type: Optional[List[CodeableConcept]] = None
    schedule: Optional[List[Timing]] = None
    nutrient: Optional[List[NutritionOrderOralDietNutrient]] = None
    texture: Optional[List[NutritionOrderOralDietTexture]] = None
    fluidConsistencyType: Optional[List[CodeableConcept]] = None
    instruction: Optional[str] = None


@dataclass
class NutritionOrderSupplement(BackboneElement):
    """ Supplement components.

    Oral nutritional products given in order to add further nutritional value
    to the patient's diet.
    """
    resource_type: ClassVar[str] = "NutritionOrderSupplement"

    type: Optional[CodeableConcept] = None
    productName: Optional[str] = None
    schedule: Optional[List[Timing]] = None
    quantity: Optional[Quantity] = None
    instruction: Optional[str] = None


@dataclass
class NutritionOrderEnteralFormula(BackboneElement):
    """ Enteral formula components.

    Feeding provided through the gastrointestinal tract via a tube, catheter,
    or stoma that delivers nutrition distal to the oral cavity.
    """
    resource_type: ClassVar[str] = "NutritionOrderEnteralFormula"

    baseFormulaType: Optional[CodeableConcept] = None
    baseFormulaProductName: Optional[str] = None
    additiveType: Optional[CodeableConcept] = None
    additiveProductName: Optional[str] = None
    caloricDensity: Optional[Quantity] = None
    routeofAdministration: Optional[CodeableConcept] = None
    administration: Optional[List[NutritionOrderEnteralFormulaAdministration]] = None
    maxVolumeToDeliver: Optional[Quantity] = None
    administrationInstruction: Optional[str] = None


@dataclass
class NutritionOrder(DomainResource):
    """ Diet, formula or nutritional supplement request.

    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """
    resource_type: ClassVar[str] = "NutritionOrder"

    identifier: Optional[List[Identifier]] = None
    instantiatesCanonical: Optional[List[str]] = None
    instantiatesUri: Optional[List[str]] = None
    instantiates: Optional[List[str]] = None
    status: str = None
    intent: str = None
    patient: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    dateTime: FHIRDate = None
    orderer: Optional[FHIRReference] = None
    allergyIntolerance: Optional[List[FHIRReference]] = None
    foodPreferenceModifier: Optional[List[CodeableConcept]] = None
    excludeFoodModifier: Optional[List[CodeableConcept]] = None
    oralDiet: Optional[NutritionOrderOralDiet] = None
    supplement: Optional[List[NutritionOrderSupplement]] = None
    enteralFormula: Optional[NutritionOrderEnteralFormula] = None
    note: Optional[List[Annotation]] = None