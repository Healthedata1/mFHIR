#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SubstanceSpecification) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .range import Range
from .ratio import Ratio


@dataclass
class SubstanceSpecificationNameOfficial(BackboneElement):
    """ Details of the official nature of this name.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationNameOfficial"

    authority: Optional[CodeableConcept] = None
    status: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None


@dataclass
class SubstanceSpecificationStructureIsotopeMolecularWeight(BackboneElement):
    """ The molecular weight or weight range (for proteins, polymers or nucleic
    acids).
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationStructureIsotopeMolecularWeight"

    method: Optional[CodeableConcept] = None
    type: Optional[CodeableConcept] = None
    amount: Optional[Quantity] = None


@dataclass
class SubstanceSpecificationStructureIsotope(BackboneElement):
    """ Applicable for single substances that contain a radionuclide or a non-
    natural isotopic ratio.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationStructureIsotope"

    identifier: Optional[Identifier] = None
    name: Optional[CodeableConcept] = None
    substitution: Optional[CodeableConcept] = None
    halfLife: Optional[Quantity] = None
    molecularWeight: Optional[SubstanceSpecificationStructureIsotopeMolecularWeight] = None


@dataclass
class SubstanceSpecificationStructureRepresentation(BackboneElement):
    """ Molecular structural representation.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationStructureRepresentation"

    type: Optional[CodeableConcept] = None
    representation: Optional[str] = None
    attachment: Optional[Attachment] = None


@dataclass
class SubstanceSpecificationMoiety(BackboneElement):
    """ Moiety, for structural modifications.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationMoiety"

    role: Optional[CodeableConcept] = None
    identifier: Optional[Identifier] = None
    name: Optional[str] = None
    stereochemistry: Optional[CodeableConcept] = None
    opticalActivity: Optional[CodeableConcept] = None
    molecularFormula: Optional[str] = None
    amountQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='amount',))
    amountString: Optional[str] = field(default=None, metadata=dict(one_of_many='amount',))


@dataclass
class SubstanceSpecificationProperty(BackboneElement):
    """ General specifications for this substance, including how it is related to
    other substances.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationProperty"

    category: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    parameters: Optional[str] = None
    definingSubstanceReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='definingSubstance',))
    definingSubstanceCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='definingSubstance',))
    amountQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='amount',))
    amountString: Optional[str] = field(default=None, metadata=dict(one_of_many='amount',))


@dataclass
class SubstanceSpecificationStructure(BackboneElement):
    """ Structural information.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationStructure"

    stereochemistry: Optional[CodeableConcept] = None
    opticalActivity: Optional[CodeableConcept] = None
    molecularFormula: Optional[str] = None
    molecularFormulaByMoiety: Optional[str] = None
    isotope: Optional[List[SubstanceSpecificationStructureIsotope]] = None
    molecularWeight: Optional[SubstanceSpecificationStructureIsotopeMolecularWeight] = None
    source: Optional[List[FHIRReference]] = None
    representation: Optional[List[SubstanceSpecificationStructureRepresentation]] = None


@dataclass
class SubstanceSpecificationstr(BackboneElement):
    """ Codes associated with the substance.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationstr"

    code: Optional[CodeableConcept] = None
    status: Optional[CodeableConcept] = None
    statusDate: Optional[FHIRDate] = None
    comment: Optional[str] = None
    source: Optional[List[FHIRReference]] = None


@dataclass
class SubstanceSpecificationName(BackboneElement):
    """ Names applicable to this substance.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationName"

    name: str = None
    type: Optional[CodeableConcept] = None
    status: Optional[CodeableConcept] = None
    preferred: Optional[bool] = None
    language: Optional[List[CodeableConcept]] = None
    domain: Optional[List[CodeableConcept]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    synonym: Optional[List["SubstanceSpecificationName"]] = None
    translation: Optional[List["SubstanceSpecificationName"]] = None
    official: Optional[List[SubstanceSpecificationNameOfficial]] = None
    source: Optional[List[FHIRReference]] = None


@dataclass
class SubstanceSpecificationRelationship(BackboneElement):
    """ A link between this substance and another, with details of the relationship.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationRelationship"

    substanceReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='substance',))
    substanceCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='substance',))
    relationship: Optional[CodeableConcept] = None
    isDefining: Optional[bool] = None
    amountQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='amount',))
    amountRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='amount',))
    amountRatio: Optional[Ratio] = field(default=None, metadata=dict(one_of_many='amount',))
    amountString: Optional[str] = field(default=None, metadata=dict(one_of_many='amount',))
    amountRatioLowLimit: Optional[Ratio] = None
    amountType: Optional[CodeableConcept] = None
    source: Optional[List[FHIRReference]] = None


@dataclass
class SubstanceSpecification(DomainResource):
    """ The detailed description of a substance, typically at a level beyond what
    is used for prescribing.
    """
    resource_type: ClassVar[str] = "SubstanceSpecification"

    identifier: Optional[Identifier] = None
    type: Optional[CodeableConcept] = None
    status: Optional[CodeableConcept] = None
    domain: Optional[CodeableConcept] = None
    description: Optional[str] = None
    source: Optional[List[FHIRReference]] = None
    comment: Optional[str] = None
    moiety: Optional[List[SubstanceSpecificationMoiety]] = None
    property: Optional[List[SubstanceSpecificationProperty]] = None
    referenceInformation: Optional[FHIRReference] = None
    structure: Optional[SubstanceSpecificationStructure] = None
    code: Optional[List[SubstanceSpecificationstr]] = None
    name: Optional[List[SubstanceSpecificationName]] = None
    molecularWeight: Optional[List[SubstanceSpecificationStructureIsotopeMolecularWeight]] = None
    relationship: Optional[List[SubstanceSpecificationRelationship]] = None
    nucleicAcid: Optional[FHIRReference] = None
    polymer: Optional[FHIRReference] = None
    protein: Optional[FHIRReference] = None
    sourceMaterial: Optional[FHIRReference] = None