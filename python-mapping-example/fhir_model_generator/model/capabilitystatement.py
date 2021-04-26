#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CapabilityStatement) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .usagecontext import UsageContext


@dataclass
class CapabilityStatementMessagingEndpoint(BackboneElement):
    """ Where messages should be sent.

    An endpoint (network accessible address) to which messages and/or replies
    are to be sent.
    """
    resource_type: ClassVar[str] = "CapabilityStatementMessagingEndpoint"

    protocol: Coding = None
    address: str = None


@dataclass
class CapabilityStatementMessagingSupportedMessage(BackboneElement):
    """ Messages supported by this system.

    References to message definitions for messages this system can send or
    receive.
    """
    resource_type: ClassVar[str] = "CapabilityStatementMessagingSupportedMessage"

    mode: str = None
    definition: str = None


@dataclass
class CapabilityStatementRestResourceInteraction(BackboneElement):
    """ What operations are supported?.

    Identifies a restful operation supported by the solution.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestResourceInteraction"

    code: str = None
    documentation: Optional[str] = None


@dataclass
class CapabilityStatementRestResourceSearchParam(BackboneElement):
    """ Search parameters supported by implementation.

    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestResourceSearchParam"

    name: str = None
    definition: Optional[str] = None
    type: str = None
    documentation: Optional[str] = None


@dataclass
class CapabilityStatementRestResourceOperation(BackboneElement):
    """ Definition of a resource operation.

    Definition of an operation or a named query together with its parameters
    and their meaning and type. Consult the definition of the operation for
    details about how to invoke the operation, and the parameters.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestResourceOperation"

    name: str = None
    definition: str = None
    documentation: Optional[str] = None


@dataclass
class CapabilityStatementRestSecurity(BackboneElement):
    """ Information about security of implementation.

    Information about security implementation from an interface perspective -
    what a client needs to know.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestSecurity"

    cors: Optional[bool] = None
    service: Optional[List[CodeableConcept]] = None
    description: Optional[str] = None


@dataclass
class CapabilityStatementRestResource(BackboneElement):
    """ Resource served on the REST interface.

    A specification of the restful capabilities of the solution for a specific
    resource type.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestResource"

    type: str = None
    profile: Optional[str] = None
    supportedProfile: Optional[List[str]] = None
    documentation: Optional[str] = None
    interaction: Optional[List[CapabilityStatementRestResourceInteraction]] = None
    versioning: Optional[str] = None
    readHistory: Optional[bool] = None
    updateCreate: Optional[bool] = None
    conditionalCreate: Optional[bool] = None
    conditionalRead: Optional[str] = None
    conditionalUpdate: Optional[bool] = None
    conditionalDelete: Optional[str] = None
    referencePolicy: Optional[List[str]] = None
    searchInclude: Optional[List[str]] = None
    searchRevInclude: Optional[List[str]] = None
    searchParam: Optional[List[CapabilityStatementRestResourceSearchParam]] = None
    operation: Optional[List[CapabilityStatementRestResourceOperation]] = None


@dataclass
class CapabilityStatementRestInteraction(BackboneElement):
    """ What operations are supported?.

    A specification of restful operations supported by the system.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRestInteraction"

    code: str = None
    documentation: Optional[str] = None


@dataclass
class CapabilityStatementSoftware(BackboneElement):
    """ Software that is covered by this capability statement.

    Software that is covered by this capability statement.  It is used when the
    capability statement describes the capabilities of a particular software
    version, independent of an installation.
    """
    resource_type: ClassVar[str] = "CapabilityStatementSoftware"

    name: str = None
    version: Optional[str] = None
    releaseDate: Optional[FHIRDate] = None


@dataclass
class CapabilityStatementImplementation(BackboneElement):
    """ If this describes a specific instance.

    Identifies a specific implementation instance that is described by the
    capability statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """
    resource_type: ClassVar[str] = "CapabilityStatementImplementation"

    description: str = None
    url: Optional[str] = None
    custodian: Optional[FHIRReference] = None


@dataclass
class CapabilityStatementRest(BackboneElement):
    """ If the endpoint is a RESTful one.

    A definition of the restful capabilities of the solution, if any.
    """
    resource_type: ClassVar[str] = "CapabilityStatementRest"

    mode: str = None
    documentation: Optional[str] = None
    security: Optional[CapabilityStatementRestSecurity] = None
    resource: Optional[List[CapabilityStatementRestResource]] = None
    interaction: Optional[List[CapabilityStatementRestInteraction]] = None
    searchParam: Optional[List[CapabilityStatementRestResourceSearchParam]] = None
    operation: Optional[List[CapabilityStatementRestResourceOperation]] = None
    compartment: Optional[List[str]] = None


@dataclass
class CapabilityStatementMessaging(BackboneElement):
    """ If messaging is supported.

    A description of the messaging capabilities of the solution.
    """
    resource_type: ClassVar[str] = "CapabilityStatementMessaging"

    endpoint: Optional[List[CapabilityStatementMessagingEndpoint]] = None
    reliableCache: Optional[int] = None
    documentation: Optional[str] = None
    supportedMessage: Optional[List[CapabilityStatementMessagingSupportedMessage]] = None


@dataclass
class CapabilityStatementDocument(BackboneElement):
    """ Document definition.

    A document definition.
    """
    resource_type: ClassVar[str] = "CapabilityStatementDocument"

    mode: str = None
    documentation: Optional[str] = None
    profile: str = None


@dataclass
class CapabilityStatement(DomainResource):
    """ A statement of system capabilities.

    A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server for a particular version of FHIR that may be used as a
    statement of actual server functionality or a statement of required or
    desired server implementation.
    """
    resource_type: ClassVar[str] = "CapabilityStatement"

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
    instantiates: Optional[List[str]] = None
    imports: Optional[List[str]] = None
    software: Optional[CapabilityStatementSoftware] = None
    implementation: Optional[CapabilityStatementImplementation] = None
    fhirVersion: str = None
    format: List[str] = field(default_factory=list)
    patchFormat: Optional[List[str]] = None
    implementationGuide: Optional[List[str]] = None
    rest: Optional[List[CapabilityStatementRest]] = None
    messaging: Optional[List[CapabilityStatementMessaging]] = None
    document: Optional[List[CapabilityStatementDocument]] = None