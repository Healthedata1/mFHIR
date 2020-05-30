#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Composition) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .narrative import Narrative
from .period import Period


@dataclass
class CompositionAttester(BackboneElement):
    """ Attests to accuracy of composition.

    A participant who has attested to the accuracy of the composition/document.
    """
    resource_type: ClassVar[str] = "CompositionAttester"

    mode: str = None
    time: Optional[FHIRDate] = None
    party: Optional[FHIRReference] = None


@dataclass
class CompositionRelatesTo(BackboneElement):
    """ Relationships to other compositions/documents.

    Relationships that this composition has with other compositions or
    documents that already exist.
    """
    resource_type: ClassVar[str] = "CompositionRelatesTo"

    code: str = None
    targetIdentifier: Identifier = field(default=None, metadata=dict(one_of_many='target',))
    targetReference: FHIRReference = field(default=None, metadata=dict(one_of_many='target',))


@dataclass
class CompositionEvent(BackboneElement):
    """ The clinical service(s) being documented.

    The clinical service, such as a colonoscopy or an appendectomy, being
    documented.
    """
    resource_type: ClassVar[str] = "CompositionEvent"

    code: Optional[List[CodeableConcept]] = None
    period: Optional[Period] = None
    detail: Optional[List[FHIRReference]] = None


@dataclass
class CompositionSection(BackboneElement):
    """ Composition is broken into sections.

    The root of the sections that make up the composition.
    """
    resource_type: ClassVar[str] = "CompositionSection"

    title: Optional[str] = None
    code: Optional[CodeableConcept] = None
    author: Optional[List[FHIRReference]] = None
    focus: Optional[FHIRReference] = None
    text: Optional[Narrative] = None
    mode: Optional[str] = None
    orderedBy: Optional[CodeableConcept] = None
    entry: Optional[List[FHIRReference]] = None
    emptyReason: Optional[CodeableConcept] = None
    section: Optional[List["CompositionSection"]] = None


@dataclass
class Composition(DomainResource):
    """ A set of resources composed into a single coherent clinical statement with
    clinical attestation.

    A set of healthcare-related information that is assembled together into a
    single logical package that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation with
    regard to who is making the statement. A Composition defines the structure
    and narrative content necessary for a document. However, a Composition
    alone does not constitute a document. Rather, the Composition must be the
    first entry in a Bundle where Bundle.type=document, and any other resources
    referenced from Composition must be included as subsequent entries in the
    Bundle (for example Patient, Practitioner, Encounter, etc.).
    """
    resource_type: ClassVar[str] = "Composition"

    identifier: Optional[Identifier] = None
    status: str = None
    type: CodeableConcept = None
    category: Optional[List[CodeableConcept]] = None
    subject: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    date: FHIRDate = None
    author: List[FHIRReference] = field(default_factory=list)
    title: str = None
    confidentiality: Optional[str] = None
    attester: Optional[List[CompositionAttester]] = None
    custodian: Optional[FHIRReference] = None
    relatesTo: Optional[List[CompositionRelatesTo]] = None
    event: Optional[List[CompositionEvent]] = None
    section: Optional[List[CompositionSection]] = None