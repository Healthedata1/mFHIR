#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/TerminologyCapabilities) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .usagecontext import UsageContext


@dataclass
class TerminologyCapabilitiesExpansionParameter(BackboneElement):
    """ Supported expansion parameter.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesExpansionParameter"

    name: str = None
    documentation: Optional[str] = None


@dataclass
class TerminologyCapabilitiesCodeSystemVersionFilter(BackboneElement):
    """ Filter Properties supported.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesCodeSystemVersionFilter"

    code: str = None
    op: List[str] = field(default_factory=list)


@dataclass
class TerminologyCapabilitiesCodeSystemVersion(BackboneElement):
    """ Version of Code System supported.

    For the code system, a list of versions that are supported by the server.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesCodeSystemVersion"

    code: Optional[str] = None
    isDefault: Optional[bool] = None
    compositional: Optional[bool] = None
    language: Optional[List[str]] = None
    filter: Optional[List[TerminologyCapabilitiesCodeSystemVersionFilter]] = None
    property: Optional[List[str]] = None


@dataclass
class TerminologyCapabilitiesSoftware(BackboneElement):
    """ Software that is covered by this terminology capability statement.

    Software that is covered by this terminology capability statement.  It is
    used when the statement describes the capabilities of a particular software
    version, independent of an installation.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesSoftware"

    name: str = None
    version: Optional[str] = None


@dataclass
class TerminologyCapabilitiesImplementation(BackboneElement):
    """ If this describes a specific instance.

    Identifies a specific implementation instance that is described by the
    terminology capability statement - i.e. a particular installation, rather
    than the capabilities of a software program.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesImplementation"

    description: str = None
    url: Optional[str] = None


@dataclass
class TerminologyCapabilitiesCodeSystem(BackboneElement):
    """ A code system supported by the server.

    Identifies a code system that is supported by the server. If there is a no
    code system URL, then this declares the general assumptions a client can
    make about support for any CodeSystem resource.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesCodeSystem"

    uri: Optional[str] = None
    version: Optional[List[TerminologyCapabilitiesCodeSystemVersion]] = None
    subsumption: Optional[bool] = None


@dataclass
class TerminologyCapabilitiesExpansion(BackboneElement):
    """ Information about the [ValueSet/$expand](valueset-operation-expand.html)
    operation.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesExpansion"

    hierarchical: Optional[bool] = None
    paging: Optional[bool] = None
    incomplete: Optional[bool] = None
    parameter: Optional[List[TerminologyCapabilitiesExpansionParameter]] = None
    textFilter: Optional[str] = None


@dataclass
class TerminologyCapabilitiesValidateCode(BackboneElement):
    """ Information about the [ValueSet/$validate-code](valueset-operation-
    validate-code.html) operation.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesValidateCode"

    translations: bool = None


@dataclass
class TerminologyCapabilitiesTranslation(BackboneElement):
    """ Information about the [ConceptMap/$translate](conceptmap-operation-
    translate.html) operation.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesTranslation"

    needsMap: bool = None


@dataclass
class TerminologyCapabilitiesClosure(BackboneElement):
    """ Information about the [ConceptMap/$closure](conceptmap-operation-
    closure.html) operation.

    Whether the $closure operation is supported.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilitiesClosure"

    translation: Optional[bool] = None


@dataclass
class TerminologyCapabilities(DomainResource):
    """ A statement of system capabilities.

    A TerminologyCapabilities resource documents a set of capabilities
    (behaviors) of a FHIR Terminology Server that may be used as a statement of
    actual server functionality or a statement of required or desired server
    implementation.
    """
    resource_type: ClassVar[str] = "TerminologyCapabilities"

    url: Optional[str] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: FHIRDate = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    kind: str = None
    software: Optional[TerminologyCapabilitiesSoftware] = None
    implementation: Optional[TerminologyCapabilitiesImplementation] = None
    lockedDate: Optional[bool] = None
    codeSystem: Optional[List[TerminologyCapabilitiesCodeSystem]] = None
    expansion: Optional[TerminologyCapabilitiesExpansion] = None
    codeSearch: Optional[str] = None
    validateCode: Optional[TerminologyCapabilitiesValidateCode] = None
    translation: Optional[TerminologyCapabilitiesTranslation] = None
    closure: Optional[TerminologyCapabilitiesClosure] = None