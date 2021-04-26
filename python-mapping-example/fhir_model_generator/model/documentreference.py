#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DocumentReference) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class DocumentReferenceRelatesTo(BackboneElement):
    """ Relationships to other documents.

    Relationships that this document has with other document references that
    already exist.
    """
    resource_type: ClassVar[str] = "DocumentReferenceRelatesTo"

    code: str = None
    target: FHIRReference = None


@dataclass
class DocumentReferenceContent(BackboneElement):
    """ Document referenced.

    The document and format referenced. There may be multiple content element
    repetitions, each with a different format.
    """
    resource_type: ClassVar[str] = "DocumentReferenceContent"

    attachment: Attachment = None
    format: Optional[Coding] = None


@dataclass
class DocumentReferenceContext(BackboneElement):
    """ Clinical context of document.

    The clinical context in which the document was prepared.
    """
    resource_type: ClassVar[str] = "DocumentReferenceContext"

    encounter: Optional[List[FHIRReference]] = None
    event: Optional[List[CodeableConcept]] = None
    period: Optional[Period] = None
    facilityType: Optional[CodeableConcept] = None
    practiceSetting: Optional[CodeableConcept] = None
    sourcePatientInfo: Optional[FHIRReference] = None
    related: Optional[List[FHIRReference]] = None


@dataclass
class DocumentReference(DomainResource):
    """ A reference to a document.

    A reference to a document of any kind for any purpose. Provides metadata
    about the document so that the document can be discovered and managed. The
    scope of a document is any seralized object with a mime-type, so includes
    formal patient centric documents (CDA), cliical notes, scanned paper, and
    non-patient specific documents like policy text.
    """
    resource_type: ClassVar[str] = "DocumentReference"

    masterIdentifier: Optional[Identifier] = None
    identifier: Optional[List[Identifier]] = None
    status: str = None
    docStatus: Optional[str] = None
    type: Optional[CodeableConcept] = None
    category: Optional[List[CodeableConcept]] = None
    subject: Optional[FHIRReference] = None
    date: Optional[FHIRDate] = None
    author: Optional[List[FHIRReference]] = None
    authenticator: Optional[FHIRReference] = None
    custodian: Optional[FHIRReference] = None
    relatesTo: Optional[List[DocumentReferenceRelatesTo]] = None
    description: Optional[str] = None
    securityLabel: Optional[List[CodeableConcept]] = None
    content: List[DocumentReferenceContent] = field(default_factory=list)
    context: Optional[DocumentReferenceContext] = None