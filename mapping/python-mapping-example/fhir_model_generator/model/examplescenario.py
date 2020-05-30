#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ExampleScenario) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .identifier import Identifier
from .usagecontext import UsageContext


@dataclass
class ExampleScenarioProcessStepOperation(BackboneElement):
    """ Each interaction or action.
    """
    resource_type: ClassVar[str] = "ExampleScenarioProcessStepOperation"

    number: str = None
    type: Optional[str] = None
    name: Optional[str] = None
    initiator: Optional[str] = None
    receiver: Optional[str] = None
    description: Optional[str] = None
    initiatorActive: Optional[bool] = None
    receiverActive: Optional[bool] = None
    request: Optional["ExampleScenarioInstanceContainedInstance"] = None
    response: Optional["ExampleScenarioInstanceContainedInstance"] = None


@dataclass
class ExampleScenarioProcessStepAlternative(BackboneElement):
    """ Alternate non-typical step action.

    Indicates an alternative step that can be taken instead of the operations
    on the base step in exceptional/atypical circumstances.
    """
    resource_type: ClassVar[str] = "ExampleScenarioProcessStepAlternative"

    title: str = None
    description: Optional[str] = None
    step: Optional[List["ExampleScenarioProcessStep"]] = None


@dataclass
class ExampleScenarioProcessStep(BackboneElement):
    """ Each step of the process.
    """
    resource_type: ClassVar[str] = "ExampleScenarioProcessStep"

    process: Optional[List["ExampleScenarioProcess"]] = None
    pause: Optional[bool] = None
    operation: Optional[ExampleScenarioProcessStepOperation] = None
    alternative: Optional[List[ExampleScenarioProcessStepAlternative]] = None


@dataclass
class ExampleScenarioInstanceVersion(BackboneElement):
    """ A specific version of the resource.
    """
    resource_type: ClassVar[str] = "ExampleScenarioInstanceVersion"

    versionId: str = None
    description: str = None


@dataclass
class ExampleScenarioInstanceContainedInstance(BackboneElement):
    """ Resources contained in the instance.

    Resources contained in the instance (e.g. the observations contained in a
    bundle).
    """
    resource_type: ClassVar[str] = "ExampleScenarioInstanceContainedInstance"

    resourceId: str = None
    versionId: Optional[str] = None


@dataclass
class ExampleScenarioActor(BackboneElement):
    """ Actor participating in the resource.
    """
    resource_type: ClassVar[str] = "ExampleScenarioActor"

    actorId: str = None
    type: str = None
    name: Optional[str] = None
    description: Optional[str] = None


@dataclass
class ExampleScenarioInstance(BackboneElement):
    """ Each resource and each version that is present in the workflow.
    """
    resource_type: ClassVar[str] = "ExampleScenarioInstance"

    resourceId: str = None
    resourceType: str = None
    name: Optional[str] = None
    description: Optional[str] = None
    version: Optional[List[ExampleScenarioInstanceVersion]] = None
    containedInstance: Optional[List[ExampleScenarioInstanceContainedInstance]] = None


@dataclass
class ExampleScenarioProcess(BackboneElement):
    """ Each major process - a group of operations.
    """
    resource_type: ClassVar[str] = "ExampleScenarioProcess"

    title: str = None
    description: Optional[str] = None
    preConditions: Optional[str] = None
    postConditions: Optional[str] = None
    step: Optional[List[ExampleScenarioProcessStep]] = None


@dataclass
class ExampleScenario(DomainResource):
    """ Example of workflow instance.
    """
    resource_type: ClassVar[str] = "ExampleScenario"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    copyright: Optional[str] = None
    purpose: Optional[str] = None
    actor: Optional[List[ExampleScenarioActor]] = None
    instance: Optional[List[ExampleScenarioInstance]] = None
    process: Optional[List[ExampleScenarioProcess]] = None
    workflow: Optional[List[str]] = None