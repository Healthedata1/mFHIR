#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SubstanceProtein) on 2020-02-10.
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
class SubstanceProteinSubunit(BackboneElement):
    """ This subclause refers to the description of each subunit constituting the
    SubstanceProtein. A subunit is a linear sequence of amino acids linked
    through peptide bonds. The Subunit information shall be provided when the
    finished SubstanceProtein is a complex of multiple sequences; subunits are
    not used to delineate domains within a single sequence. Subunits are listed
    in order of decreasing length; sequences of the same length will be ordered
    by decreasing molecular weight; subunits that have identical sequences will
    be repeated multiple times.
    """
    resource_type: ClassVar[str] = "SubstanceProteinSubunit"

    subunit: Optional[int] = None
    sequence: Optional[str] = None
    length: Optional[int] = None
    sequenceAttachment: Optional[Attachment] = None
    nTerminalModificationId: Optional[Identifier] = None
    nTerminalModification: Optional[str] = None
    cTerminalModificationId: Optional[Identifier] = None
    cTerminalModification: Optional[str] = None


@dataclass
class SubstanceProtein(DomainResource):
    """ A SubstanceProtein is defined as a single unit of a linear amino acid
    sequence, or a combination of subunits that are either covalently linked or
    have a defined invariant stoichiometric relationship. This includes all
    synthetic, recombinant and purified SubstanceProteins of defined sequence,
    whether the use is therapeutic or prophylactic. This set of elements will
    be used to describe albumins, coagulation factors, cytokines, growth
    factors, peptide/SubstanceProtein hormones, enzymes, toxins, toxoids,
    recombinant vaccines, and immunomodulators.
    """
    resource_type: ClassVar[str] = "SubstanceProtein"

    sequenceType: Optional[CodeableConcept] = None
    numberOfSubunits: Optional[int] = None
    disulfideLinkage: Optional[List[str]] = None
    subunit: Optional[List[SubstanceProteinSubunit]] = None