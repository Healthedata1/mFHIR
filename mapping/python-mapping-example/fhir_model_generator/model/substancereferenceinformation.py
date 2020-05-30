#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SubstanceReferenceInformation) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .range import Range


@dataclass
class SubstanceReferenceInformationGene(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstanceReferenceInformationGene"

    geneSequenceOrigin: Optional[CodeableConcept] = None
    gene: Optional[CodeableConcept] = None
    source: Optional[List[FHIRReference]] = None


@dataclass
class SubstanceReferenceInformationGeneElement(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstanceReferenceInformationGeneElement"

    type: Optional[CodeableConcept] = None
    element: Optional[Identifier] = None
    source: Optional[List[FHIRReference]] = None


@dataclass
class SubstanceReferenceInformationClassification(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstanceReferenceInformationClassification"

    domain: Optional[CodeableConcept] = None
    classification: Optional[CodeableConcept] = None
    subtype: Optional[List[CodeableConcept]] = None
    source: Optional[List[FHIRReference]] = None


@dataclass
class SubstanceReferenceInformationTarget(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstanceReferenceInformationTarget"

    target: Optional[Identifier] = None
    type: Optional[CodeableConcept] = None
    interaction: Optional[CodeableConcept] = None
    organism: Optional[CodeableConcept] = None
    organismType: Optional[CodeableConcept] = None
    amountQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='amount',))
    amountRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='amount',))
    amountString: Optional[str] = field(default=None, metadata=dict(one_of_many='amount',))
    amountType: Optional[CodeableConcept] = None
    source: Optional[List[FHIRReference]] = None


@dataclass
class SubstanceReferenceInformation(DomainResource):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstanceReferenceInformation"

    comment: Optional[str] = None
    gene: Optional[List[SubstanceReferenceInformationGene]] = None
    geneElement: Optional[List[SubstanceReferenceInformationGeneElement]] = None
    classification: Optional[List[SubstanceReferenceInformationClassification]] = None
    target: Optional[List[SubstanceReferenceInformationTarget]] = None