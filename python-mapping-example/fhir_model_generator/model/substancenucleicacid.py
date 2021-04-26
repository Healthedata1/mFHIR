#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SubstanceNucleicAcid) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .identifier import Identifier


@dataclass
class SubstanceNucleicAcidSubunitLinkage(BackboneElement):
    """ The linkages between sugar residues will also be captured.
    """
    resource_type: ClassVar[str] = "SubstanceNucleicAcidSubunitLinkage"

    connectivity: Optional[str] = None
    identifier: Optional[Identifier] = None
    name: Optional[str] = None
    residueSite: Optional[str] = None


@dataclass
class SubstanceNucleicAcidSubunitSugar(BackboneElement):
    """ 5.3.6.8.1 Sugar ID (Mandatory).
    """
    resource_type: ClassVar[str] = "SubstanceNucleicAcidSubunitSugar"

    identifier: Optional[Identifier] = None
    name: Optional[str] = None
    residueSite: Optional[str] = None


@dataclass
class SubstanceNucleicAcidSubunit(BackboneElement):
    """ Subunits are listed in order of decreasing length; sequences of the same
    length will be ordered by molecular weight; subunits that have identical
    sequences will be repeated multiple times.
    """
    resource_type: ClassVar[str] = "SubstanceNucleicAcidSubunit"

    subunit: Optional[int] = None
    sequence: Optional[str] = None
    length: Optional[int] = None
    sequenceAttachment: Optional[Attachment] = None
    fivePrime: Optional[CodeableConcept] = None
    threePrime: Optional[CodeableConcept] = None
    linkage: Optional[List[SubstanceNucleicAcidSubunitLinkage]] = None
    sugar: Optional[List[SubstanceNucleicAcidSubunitSugar]] = None


@dataclass
class SubstanceNucleicAcid(DomainResource):
    """ Nucleic acids are defined by three distinct elements: the base, sugar and
    linkage. Individual substance/moiety IDs will be created for each of these
    elements. The nucleotide sequence will be always entered in the 5’-3’
    direction.
    """
    resource_type: ClassVar[str] = "SubstanceNucleicAcid"

    sequenceType: Optional[CodeableConcept] = None
    numberOfSubunits: Optional[int] = None
    areaOfHybridisation: Optional[str] = None
    oligoNucleotideType: Optional[CodeableConcept] = None
    subunit: Optional[List[SubstanceNucleicAcidSubunit]] = None