#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DocumentManifest) on 2020-02-10.
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


@dataclass
class DocumentManifestRelated(BackboneElement):
    """ Related things.

    Related identifiers or resources associated with the DocumentManifest.
    """
    resource_type: ClassVar[str] = "DocumentManifestRelated"

    identifier: Optional[Identifier] = None
    ref: Optional[FHIRReference] = None


@dataclass
class DocumentManifest(DomainResource):
    """ A list that defines a set of documents.

    A collection of documents compiled for a purpose together with metadata
    that applies to the collection.
    """
    resource_type: ClassVar[str] = "DocumentManifest"

    masterIdentifier: Optional[Identifier] = None
    identifier: Optional[List[Identifier]] = None
    status: str = None
    type: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None
    created: Optional[FHIRDate] = None
    author: Optional[List[FHIRReference]] = None
    recipient: Optional[List[FHIRReference]] = None
    source: Optional[str] = None
    description: Optional[str] = None
    content: List[FHIRReference] = field(default_factory=list)
    related: Optional[List[DocumentManifestRelated]] = None