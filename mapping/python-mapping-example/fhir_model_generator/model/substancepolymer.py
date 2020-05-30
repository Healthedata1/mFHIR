#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SubstancePolymer) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .substanceamount import SubstanceAmount


@dataclass
class SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation"

    degree: Optional[CodeableConcept] = None
    amount: Optional[SubstanceAmount] = None


@dataclass
class SubstancePolymerRepeatRepeatUnitStructuralRepresentation(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeatRepeatUnitStructuralRepresentation"

    type: Optional[CodeableConcept] = None
    representation: Optional[str] = None
    attachment: Optional[Attachment] = None


@dataclass
class SubstancePolymerRepeatRepeatUnit(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeatRepeatUnit"

    orientationOfPolymerisation: Optional[CodeableConcept] = None
    repeatUnit: Optional[str] = None
    amount: Optional[SubstanceAmount] = None
    degreeOfPolymerisation: Optional[List[SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation]] = None
    structuralRepresentation: Optional[List[SubstancePolymerRepeatRepeatUnitStructuralRepresentation]] = None


@dataclass
class SubstancePolymerMonomerSetStartingMaterial(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerMonomerSetStartingMaterial"

    material: Optional[CodeableConcept] = None
    type: Optional[CodeableConcept] = None
    isDefining: Optional[bool] = None
    amount: Optional[SubstanceAmount] = None


@dataclass
class SubstancePolymerMonomerSet(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerMonomerSet"

    ratioType: Optional[CodeableConcept] = None
    startingMaterial: Optional[List[SubstancePolymerMonomerSetStartingMaterial]] = None


@dataclass
class SubstancePolymerRepeat(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeat"

    numberOfUnits: Optional[int] = None
    averageMolecularFormula: Optional[str] = None
    repeatUnitAmountType: Optional[CodeableConcept] = None
    repeatUnit: Optional[List[SubstancePolymerRepeatRepeatUnit]] = None


@dataclass
class SubstancePolymer(DomainResource):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymer"

    class_fhir: Optional[CodeableConcept] = field(default=None, metadata=dict(orig_name='class'))
    geometry: Optional[CodeableConcept] = None
    copolymerConnectivity: Optional[List[CodeableConcept]] = None
    modification: Optional[List[str]] = None
    monomerSet: Optional[List[SubstancePolymerMonomerSet]] = None
    repeat: Optional[List[SubstancePolymerRepeat]] = None