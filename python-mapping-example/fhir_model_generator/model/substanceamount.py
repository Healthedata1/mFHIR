#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SubstanceAmount) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .element import Element
from .quantity import Quantity
from .range import Range


@dataclass
class SubstanceAmountReferenceRange(Element):
    """ Reference range of possible or expected values.
    """
    resource_type: ClassVar[str] = "SubstanceAmountReferenceRange"

    lowLimit: Optional[Quantity] = None
    highLimit: Optional[Quantity] = None


@dataclass
class SubstanceAmount(BackboneElement):
    """ Chemical substances are a single substance type whose primary defining
    element is the molecular structure. Chemical substances shall be defined on
    the basis of their complete covalent molecular structure; the presence of a
    salt (counter-ion) and/or solvates (water, alcohols) is also captured.
    Purity, grade, physical form or particle size are not taken into account in
    the definition of a chemical substance or in the assignment of a Substance
    ID.
    """
    resource_type: ClassVar[str] = "SubstanceAmount"

    amountQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='amount',))
    amountRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='amount',))
    amountString: Optional[str] = field(default=None, metadata=dict(one_of_many='amount',))
    amountType: Optional[CodeableConcept] = None
    amountText: Optional[str] = None
    referenceRange: Optional[SubstanceAmountReferenceRange] = None