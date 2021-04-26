#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SubstanceSourceMaterial) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .identifier import Identifier


@dataclass
class SubstanceSourceMaterialOrganismAuthor(BackboneElement):
    """ 4.9.13.6.1 Author type (Conditional).
    """
    resource_type: ClassVar[str] = "SubstanceSourceMaterialOrganismAuthor"

    authorType: Optional[CodeableConcept] = None
    authorDescription: Optional[str] = None


@dataclass
class SubstanceSourceMaterialOrganismHybrid(BackboneElement):
    """ 4.9.13.8.1 Hybrid species maternal organism ID (Optional).
    """
    resource_type: ClassVar[str] = "SubstanceSourceMaterialOrganismHybrid"

    maternalOrganismId: Optional[str] = None
    maternalOrganismName: Optional[str] = None
    paternalOrganismId: Optional[str] = None
    paternalOrganismName: Optional[str] = None
    hybridType: Optional[CodeableConcept] = None


@dataclass
class SubstanceSourceMaterialOrganismOrganismGeneral(BackboneElement):
    """ 4.9.13.7.1 Kingdom (Conditional).
    """
    resource_type: ClassVar[str] = "SubstanceSourceMaterialOrganismOrganismGeneral"

    kingdom: Optional[CodeableConcept] = None
    phylum: Optional[CodeableConcept] = None
    class_fhir: Optional[CodeableConcept] = field(default=None, metadata=dict(orig_name='class'))
    order: Optional[CodeableConcept] = None


@dataclass
class SubstanceSourceMaterialFractionDescription(BackboneElement):
    """ Many complex materials are fractions of parts of plants, animals, or
    minerals. Fraction elements are often necessary to define both Substances
    and Specified Group 1 Substances. For substances derived from Plants,
    fraction information will be captured at the Substance information level (
    . Oils, Juices and Exudates). Additional information for Extracts, such as
    extraction solvent composition, will be captured at the Specified Substance
    Group 1 information level. For plasma-derived products fraction information
    will be captured at the Substance and the Specified Substance Group 1
    levels.
    """
    resource_type: ClassVar[str] = "SubstanceSourceMaterialFractionDescription"

    fraction: Optional[str] = None
    materialType: Optional[CodeableConcept] = None


@dataclass
class SubstanceSourceMaterialOrganism(BackboneElement):
    """ This subclause describes the organism which the substance is derived from.
    For vaccines, the parent organism shall be specified based on these
    subclause elements. As an example, full taxonomy will be described for the
    Substance Name: ., Leaf.
    """
    resource_type: ClassVar[str] = "SubstanceSourceMaterialOrganism"

    family: Optional[CodeableConcept] = None
    genus: Optional[CodeableConcept] = None
    species: Optional[CodeableConcept] = None
    intraspecificType: Optional[CodeableConcept] = None
    intraspecificDescription: Optional[str] = None
    author: Optional[List[SubstanceSourceMaterialOrganismAuthor]] = None
    hybrid: Optional[SubstanceSourceMaterialOrganismHybrid] = None
    organismGeneral: Optional[SubstanceSourceMaterialOrganismOrganismGeneral] = None


@dataclass
class SubstanceSourceMaterialPartDescription(BackboneElement):
    """ To do.
    """
    resource_type: ClassVar[str] = "SubstanceSourceMaterialPartDescription"

    part: Optional[CodeableConcept] = None
    partLocation: Optional[CodeableConcept] = None


@dataclass
class SubstanceSourceMaterial(DomainResource):
    """ Source material shall capture information on the taxonomic and anatomical
    origins as well as the fraction of a material that can result in or can be
    modified to form a substance. This set of data elements shall be used to
    define polymer substances isolated from biological matrices. Taxonomic and
    anatomical origins shall be described using a controlled vocabulary as
    required. This information is captured for naturally derived polymers ( .
    starch) and structurally diverse substances. For Organisms belonging to the
    Kingdom Plantae the Substance level defines the fresh material of a single
    species or infraspecies, the Herbal Drug and the Herbal preparation. For
    Herbal preparations, the fraction information will be captured at the
    Substance information level and additional information for herbal extracts
    will be captured at the Specified Substance Group 1 information level. See
    for further explanation the Substance Class: Structurally Diverse and the
    herbal annex.
    """
    resource_type: ClassVar[str] = "SubstanceSourceMaterial"

    sourceMaterialClass: Optional[CodeableConcept] = None
    sourceMaterialType: Optional[CodeableConcept] = None
    sourceMaterialState: Optional[CodeableConcept] = None
    organismId: Optional[Identifier] = None
    organismName: Optional[str] = None
    parentSubstanceId: Optional[List[Identifier]] = None
    parentSubstanceName: Optional[List[str]] = None
    countryOfOrigin: Optional[List[CodeableConcept]] = None
    geographicalLocation: Optional[List[str]] = None
    developmentStage: Optional[CodeableConcept] = None
    fractionDescription: Optional[List[SubstanceSourceMaterialFractionDescription]] = None
    organism: Optional[SubstanceSourceMaterialOrganism] = None
    partDescription: Optional[List[SubstanceSourceMaterialPartDescription]] = None