#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/TestScript) on 2020-02-10.
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
from .identifier import Identifier
from .usagecontext import UsageContext


@dataclass
class TestScriptTeardownAction(BackboneElement):
    """ One or more teardown operations to perform.

    The teardown action will only contain an operation.
    """
    resource_type: ClassVar[str] = "TestScriptTeardownAction"

    operation: "TestScriptSetupActionOperation" = None


@dataclass
class TestScriptTestAction(BackboneElement):
    """ A test operation or assert to perform.

    Action would contain either an operation or an assertion.
    """
    resource_type: ClassVar[str] = "TestScriptTestAction"

    operation: Optional["TestScriptSetupActionOperation"] = None
    assert_fhir: Optional["TestScriptSetupActionAssert"] = field(default=None, metadata=dict(orig_name='assert'))


@dataclass
class TestScriptSetupActionOperationRequestHeader(BackboneElement):
    """ Each operation can have one or more header elements.

    Header elements would be used to set HTTP headers.
    """
    resource_type: ClassVar[str] = "TestScriptSetupActionOperationRequestHeader"

    field: str = None
    value: str = None


@dataclass
class TestScriptSetupActionOperation(BackboneElement):
    """ The setup operation to perform.

    The operation to perform.
    """
    resource_type: ClassVar[str] = "TestScriptSetupActionOperation"

    type: Optional[Coding] = None
    resource: Optional[str] = None
    label: Optional[str] = None
    description: Optional[str] = None
    accept: Optional[str] = None
    contentType: Optional[str] = None
    destination: Optional[int] = None
    encodeRequestUrl: bool = None
    method: Optional[str] = None
    origin: Optional[int] = None
    params: Optional[str] = None
    requestHeader: Optional[List[TestScriptSetupActionOperationRequestHeader]] = None
    requestId: Optional[str] = None
    responseId: Optional[str] = None
    sourceId: Optional[str] = None
    targetId: Optional[str] = None
    url: Optional[str] = None


@dataclass
class TestScriptSetupActionAssert(BackboneElement):
    """ The assertion to perform.

    Evaluates the results of previous operations to determine if the server
    under test behaves appropriately.
    """
    resource_type: ClassVar[str] = "TestScriptSetupActionAssert"

    label: Optional[str] = None
    description: Optional[str] = None
    direction: Optional[str] = None
    compareToSourceId: Optional[str] = None
    compareToSourceExpression: Optional[str] = None
    compareToSourcePath: Optional[str] = None
    contentType: Optional[str] = None
    expression: Optional[str] = None
    headerField: Optional[str] = None
    minimumId: Optional[str] = None
    navigationLinks: Optional[bool] = None
    operator: Optional[str] = None
    path: Optional[str] = None
    requestMethod: Optional[str] = None
    requestURL: Optional[str] = None
    resource: Optional[str] = None
    response: Optional[str] = None
    responseCode: Optional[str] = None
    sourceId: Optional[str] = None
    validateProfileId: Optional[str] = None
    value: Optional[str] = None
    warningOnly: bool = None


@dataclass
class TestScriptSetupAction(BackboneElement):
    """ A setup operation or assert to perform.

    Action would contain either an operation or an assertion.
    """
    resource_type: ClassVar[str] = "TestScriptSetupAction"

    operation: Optional[TestScriptSetupActionOperation] = None
    assert_fhir: Optional[TestScriptSetupActionAssert] = field(default=None, metadata=dict(orig_name='assert'))


@dataclass
class TestScriptMetadataLink(BackboneElement):
    """ Links to the FHIR specification.

    A link to the FHIR specification that this test is covering.
    """
    resource_type: ClassVar[str] = "TestScriptMetadataLink"

    url: str = None
    description: Optional[str] = None


@dataclass
class TestScriptMetadataCapability(BackboneElement):
    """ Capabilities  that are assumed to function correctly on the FHIR server
    being tested.

    Capabilities that must exist and are assumed to function correctly on the
    FHIR server being tested.
    """
    resource_type: ClassVar[str] = "TestScriptMetadataCapability"

    required: bool = None
    validated: bool = None
    description: Optional[str] = None
    origin: Optional[List[int]] = None
    destination: Optional[int] = None
    link: Optional[List[str]] = None
    capabilities: str = None


@dataclass
class TestScriptOrigin(BackboneElement):
    """ An abstract server representing a client or sender in a message exchange.

    An abstract server used in operations within this test script in the origin
    element.
    """
    resource_type: ClassVar[str] = "TestScriptOrigin"

    index: int = None
    profile: Coding = None


@dataclass
class TestScriptDestination(BackboneElement):
    """ An abstract server representing a destination or receiver in a message
    exchange.

    An abstract server used in operations within this test script in the
    destination element.
    """
    resource_type: ClassVar[str] = "TestScriptDestination"

    index: int = None
    profile: Coding = None


@dataclass
class TestScriptMetadata(BackboneElement):
    """ Required capability that is assumed to function correctly on the FHIR
    server being tested.

    The required capability must exist and are assumed to function correctly on
    the FHIR server being tested.
    """
    resource_type: ClassVar[str] = "TestScriptMetadata"

    link: Optional[List[TestScriptMetadataLink]] = None
    capability: List[TestScriptMetadataCapability] = field(default_factory=list)


@dataclass
class TestScriptFixture(BackboneElement):
    """ Fixture in the test script - by reference (uri).

    Fixture in the test script - by reference (uri). All fixtures are required
    for the test script to execute.
    """
    resource_type: ClassVar[str] = "TestScriptFixture"

    autocreate: bool = None
    autodelete: bool = None
    resource: Optional[FHIRReference] = None


@dataclass
class TestScriptVariable(BackboneElement):
    """ Placeholder for evaluated elements.

    Variable is set based either on element value in response body or on header
    field value in the response headers.
    """
    resource_type: ClassVar[str] = "TestScriptVariable"

    name: str = None
    defaultValue: Optional[str] = None
    description: Optional[str] = None
    expression: Optional[str] = None
    headerField: Optional[str] = None
    hint: Optional[str] = None
    path: Optional[str] = None
    sourceId: Optional[str] = None


@dataclass
class TestScriptSetup(BackboneElement):
    """ A series of required setup operations before tests are executed.
    """
    resource_type: ClassVar[str] = "TestScriptSetup"

    action: List[TestScriptSetupAction] = field(default_factory=list)


@dataclass
class TestScriptTest(BackboneElement):
    """ A test in this script.
    """
    resource_type: ClassVar[str] = "TestScriptTest"

    name: Optional[str] = None
    description: Optional[str] = None
    action: List[TestScriptTestAction] = field(default_factory=list)


@dataclass
class TestScriptTeardown(BackboneElement):
    """ A series of required clean up steps.

    A series of operations required to clean up after all the tests are
    executed (successfully or otherwise).
    """
    resource_type: ClassVar[str] = "TestScriptTeardown"

    action: List[TestScriptTeardownAction] = field(default_factory=list)


@dataclass
class TestScript(DomainResource):
    """ Describes a set of tests.

    A structured set of tests against a FHIR server or client implementation to
    determine compliance against the FHIR specification.
    """
    resource_type: ClassVar[str] = "TestScript"

    url: str = None
    identifier: Optional[Identifier] = None
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
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    origin: Optional[List[TestScriptOrigin]] = None
    destination: Optional[List[TestScriptDestination]] = None
    metadata: Optional[TestScriptMetadata] = None
    fixture: Optional[List[TestScriptFixture]] = None
    profile: Optional[List[FHIRReference]] = None
    variable: Optional[List[TestScriptVariable]] = None
    setup: Optional[TestScriptSetup] = None
    test: Optional[List[TestScriptTest]] = None
    teardown: Optional[TestScriptTeardown] = None