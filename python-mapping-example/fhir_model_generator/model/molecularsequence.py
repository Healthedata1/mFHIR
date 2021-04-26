#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MolecularSequence) on 2020-02-10.
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


@dataclass
class MolecularSequenceStructureVariantOuter(BackboneElement):
    """ Structural variant outer.
    """
    resource_type: ClassVar[str] = "MolecularSequenceStructureVariantOuter"

    start: Optional[int] = None
    end: Optional[int] = None


@dataclass
class MolecularSequenceStructureVariantInner(BackboneElement):
    """ Structural variant inner.
    """
    resource_type: ClassVar[str] = "MolecularSequenceStructureVariantInner"

    start: Optional[int] = None
    end: Optional[int] = None


@dataclass
class MolecularSequenceQualityRoc(BackboneElement):
    """ Receiver Operator Characteristic (ROC) Curve.

    Receiver Operator Characteristic (ROC) Curve  to give
    sensitivity/specificity tradeoff.
    """
    resource_type: ClassVar[str] = "MolecularSequenceQualityRoc"

    score: Optional[List[int]] = None
    numTP: Optional[List[int]] = None
    numFP: Optional[List[int]] = None
    numFN: Optional[List[int]] = None
    precision: Optional[List[float]] = None
    sensitivity: Optional[List[float]] = None
    fMeasure: Optional[List[float]] = None


@dataclass
class MolecularSequenceReferenceSeq(BackboneElement):
    """ A sequence used as reference.

    A sequence that is used as a reference to describe variants that are
    present in a sequence analyzed.
    """
    resource_type: ClassVar[str] = "MolecularSequenceReferenceSeq"

    chromosome: Optional[CodeableConcept] = None
    genomeBuild: Optional[str] = None
    orientation: Optional[str] = None
    referenceSeqId: Optional[CodeableConcept] = None
    referenceSeqPointer: Optional[FHIRReference] = None
    referenceSeqString: Optional[str] = None
    strand: Optional[str] = None
    windowStart: Optional[int] = None
    windowEnd: Optional[int] = None


@dataclass
class MolecularSequenceVariant(BackboneElement):
    """ Variant in sequence.

    The definition of variant here originates from Sequence ontology ([variant_
    of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)).
    This element can represent amino acid or nucleic sequence change(including
    insertion,deletion,SNP,etc.)  It can represent some complex mutation or
    segment variation with the assist of CIGAR string.
    """
    resource_type: ClassVar[str] = "MolecularSequenceVariant"

    start: Optional[int] = None
    end: Optional[int] = None
    observedAllele: Optional[str] = None
    referenceAllele: Optional[str] = None
    cigar: Optional[str] = None
    variantPointer: Optional[FHIRReference] = None


@dataclass
class MolecularSequenceQuality(BackboneElement):
    """ An set of value as quality of sequence.

    An experimental feature attribute that defines the quality of the feature
    in a quantitative way, such as a phred quality score ([SO:0001686](http://w
    ww.sequenceontology.org/browser/current_svn/term/SO:0001686)).
    """
    resource_type: ClassVar[str] = "MolecularSequenceQuality"

    type: str = None
    standardSequence: Optional[CodeableConcept] = None
    start: Optional[int] = None
    end: Optional[int] = None
    score: Optional[Quantity] = None
    method: Optional[CodeableConcept] = None
    truthTP: Optional[float] = None
    queryTP: Optional[float] = None
    truthFN: Optional[float] = None
    queryFP: Optional[float] = None
    gtFP: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    fScore: Optional[float] = None
    roc: Optional[MolecularSequenceQualityRoc] = None


@dataclass
class MolecularSequenceRepository(BackboneElement):
    """ External repository which contains detailed report related with observedSeq
    in this resource.

    Configurations of the external repository. The repository shall store
    target's observedSeq or records related with target's observedSeq.
    """
    resource_type: ClassVar[str] = "MolecularSequenceRepository"

    type: str = None
    url: Optional[str] = None
    name: Optional[str] = None
    datasetId: Optional[str] = None
    variantsetId: Optional[str] = None
    readsetId: Optional[str] = None


@dataclass
class MolecularSequenceStructureVariant(BackboneElement):
    """ Structural variant.

    Information about chromosome structure variation.
    """
    resource_type: ClassVar[str] = "MolecularSequenceStructureVariant"

    variantType: Optional[CodeableConcept] = None
    exact: Optional[bool] = None
    length: Optional[int] = None
    outer: Optional[MolecularSequenceStructureVariantOuter] = None
    inner: Optional[MolecularSequenceStructureVariantInner] = None


@dataclass
class MolecularSequence(DomainResource):
    """ Information about a biological sequence.

    Raw data describing a biological sequence.
    """
    resource_type: ClassVar[str] = "MolecularSequence"

    identifier: Optional[List[Identifier]] = None
    type: Optional[str] = None
    coordinateSystem: int = None
    patient: Optional[FHIRReference] = None
    specimen: Optional[FHIRReference] = None
    device: Optional[FHIRReference] = None
    performer: Optional[FHIRReference] = None
    quantity: Optional[Quantity] = None
    referenceSeq: Optional[MolecularSequenceReferenceSeq] = None
    variant: Optional[List[MolecularSequenceVariant]] = None
    observedSeq: Optional[str] = None
    quality: Optional[List[MolecularSequenceQuality]] = None
    readCoverage: Optional[int] = None
    repository: Optional[List[MolecularSequenceRepository]] = None
    pointer: Optional[List[FHIRReference]] = None
    structureVariant: Optional[List[MolecularSequenceStructureVariant]] = None