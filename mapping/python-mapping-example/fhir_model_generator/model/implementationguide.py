#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ImplementationGuide) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .usagecontext import UsageContext


@dataclass
class ImplementationGuideManifestResource(BackboneElement):
    """ Resource in the implementation guide.

    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    resource_type: ClassVar[str] = "ImplementationGuideManifestResource"

    reference: FHIRReference = None
    exampleBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='example',))
    exampleCanonical: Optional[str] = field(default=None, metadata=dict(one_of_many='example',))
    relativePath: Optional[str] = None


@dataclass
class ImplementationGuideManifestPage(BackboneElement):
    """ HTML page within the parent IG.

    Information about a page within the IG.
    """
    resource_type: ClassVar[str] = "ImplementationGuideManifestPage"

    name: str = None
    title: Optional[str] = None
    anchor: Optional[List[str]] = None


@dataclass
class ImplementationGuideDefinitionGrouping(BackboneElement):
    """ Grouping used to present related resources in the IG.

    A logical group of resources. Logical groups can be used when building
    pages.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinitionGrouping"

    name: str = None
    description: Optional[str] = None


@dataclass
class ImplementationGuideDefinitionResource(BackboneElement):
    """ Resource in the implementation guide.

    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinitionResource"

    reference: FHIRReference = None
    fhirVersion: Optional[List[str]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    exampleBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='example',))
    exampleCanonical: Optional[str] = field(default=None, metadata=dict(one_of_many='example',))
    groupingId: Optional[str] = None


@dataclass
class ImplementationGuideDefinitionPage(BackboneElement):
    """ Page/Section in the Guide.

    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinitionPage"

    nameUrl: str = field(default=None, metadata=dict(one_of_many='name',))
    nameReference: FHIRReference = field(default=None, metadata=dict(one_of_many='name',))
    title: str = None
    generation: str = None
    page: Optional[List["ImplementationGuideDefinitionPage"]] = None


@dataclass
class ImplementationGuideDefinitionParameter(BackboneElement):
    """ Defines how IG is built by tools.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinitionParameter"

    code: str = None
    value: str = None


@dataclass
class ImplementationGuideDefinitionTemplate(BackboneElement):
    """ A template for building resources.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinitionTemplate"

    code: str = None
    source: str = None
    scope: Optional[str] = None


@dataclass
class ImplementationGuideDependsOn(BackboneElement):
    """ Another Implementation guide this depends on.

    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDependsOn"

    uri: str = None
    packageId: Optional[str] = None
    version: Optional[str] = None


@dataclass
class ImplementationGuideGlobal(BackboneElement):
    """ Profiles that apply globally.

    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """
    resource_type: ClassVar[str] = "ImplementationGuideGlobal"

    type: str = None
    profile: str = None


@dataclass
class ImplementationGuideDefinition(BackboneElement):
    """ Information needed to build the IG.

    The information needed by an IG publisher tool to publish the whole
    implementation guide.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinition"

    grouping: Optional[List[ImplementationGuideDefinitionGrouping]] = None
    resource: List[ImplementationGuideDefinitionResource] = field(default_factory=list)
    page: Optional[ImplementationGuideDefinitionPage] = None
    parameter: Optional[List[ImplementationGuideDefinitionParameter]] = None
    template: Optional[List[ImplementationGuideDefinitionTemplate]] = None


@dataclass
class ImplementationGuideManifest(BackboneElement):
    """ Information about an assembled IG.

    Information about an assembled implementation guide, created by the
    publication tooling.
    """
    resource_type: ClassVar[str] = "ImplementationGuideManifest"

    rendering: Optional[str] = None
    resource: List[ImplementationGuideManifestResource] = field(default_factory=list)
    page: Optional[List[ImplementationGuideManifestPage]] = None
    image: Optional[List[str]] = None
    other: Optional[List[str]] = None


@dataclass
class ImplementationGuide(DomainResource):
    """ A set of rules about how FHIR is used.

    A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used
    to gather all the parts of an implementation guide into a logical whole and
    to publish a computable definition of all the parts.
    """
    resource_type: ClassVar[str] = "ImplementationGuide"

    url: str = None
    version: Optional[str] = None
    name: str = None
    title: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    copyright: Optional[str] = None
    packageId: str = None
    license: Optional[str] = None
    fhirVersion: List[str] = field(default_factory=list)
    dependsOn: Optional[List[ImplementationGuideDependsOn]] = None
    global_fhir: Optional[List[ImplementationGuideGlobal]] = field(default_factory=list, metadata=dict(orig_name='global'))
    definition: Optional[ImplementationGuideDefinition] = None
    manifest: Optional[ImplementationGuideManifest] = None