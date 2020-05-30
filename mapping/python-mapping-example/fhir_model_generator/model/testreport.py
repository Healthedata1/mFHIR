#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/TestReport) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class TestReportTeardownAction(BackboneElement):
    """ One or more teardown operations performed.

    The teardown action will only contain an operation.
    """
    resource_type: ClassVar[str] = "TestReportTeardownAction"

    operation: "TestReportSetupActionOperation" = None


@dataclass
class TestReportTestAction(BackboneElement):
    """ A test operation or assert that was performed.

    Action would contain either an operation or an assertion.
    """
    resource_type: ClassVar[str] = "TestReportTestAction"

    operation: Optional["TestReportSetupActionOperation"] = None
    assert_fhir: Optional["TestReportSetupActionAssert"] = field(default=None, metadata=dict(orig_name='assert'))


@dataclass
class TestReportSetupActionOperation(BackboneElement):
    """ The operation to perform.

    The operation performed.
    """
    resource_type: ClassVar[str] = "TestReportSetupActionOperation"

    result: str = None
    message: Optional[str] = None
    detail: Optional[str] = None


@dataclass
class TestReportSetupActionAssert(BackboneElement):
    """ The assertion to perform.

    The results of the assertion performed on the previous operations.
    """
    resource_type: ClassVar[str] = "TestReportSetupActionAssert"

    result: str = None
    message: Optional[str] = None
    detail: Optional[str] = None


@dataclass
class TestReportSetupAction(BackboneElement):
    """ A setup operation or assert that was executed.

    Action would contain either an operation or an assertion.
    """
    resource_type: ClassVar[str] = "TestReportSetupAction"

    operation: Optional[TestReportSetupActionOperation] = None
    assert_fhir: Optional[TestReportSetupActionAssert] = field(default=None, metadata=dict(orig_name='assert'))


@dataclass
class TestReportParticipant(BackboneElement):
    """ A participant in the test execution, either the execution engine, a client,
    or a server.
    """
    resource_type: ClassVar[str] = "TestReportParticipant"

    type: str = None
    uri: str = None
    display: Optional[str] = None


@dataclass
class TestReportSetup(BackboneElement):
    """ The results of the series of required setup operations before the tests
    were executed.
    """
    resource_type: ClassVar[str] = "TestReportSetup"

    action: List[TestReportSetupAction] = field(default_factory=list)


@dataclass
class TestReportTest(BackboneElement):
    """ A test executed from the test script.
    """
    resource_type: ClassVar[str] = "TestReportTest"

    name: Optional[str] = None
    description: Optional[str] = None
    action: List[TestReportTestAction] = field(default_factory=list)


@dataclass
class TestReportTeardown(BackboneElement):
    """ The results of running the series of required clean up steps.

    The results of the series of operations required to clean up after all the
    tests were executed (successfully or otherwise).
    """
    resource_type: ClassVar[str] = "TestReportTeardown"

    action: List[TestReportTeardownAction] = field(default_factory=list)


@dataclass
class TestReport(DomainResource):
    """ Describes the results of a TestScript execution.

    A summary of information based on the results of executing a TestScript.
    """
    resource_type: ClassVar[str] = "TestReport"

    identifier: Optional[Identifier] = None
    name: Optional[str] = None
    status: str = None
    testScript: FHIRReference = None
    result: str = None
    score: Optional[float] = None
    tester: Optional[str] = None
    issued: Optional[FHIRDate] = None
    participant: Optional[List[TestReportParticipant]] = None
    setup: Optional[TestReportSetup] = None
    test: Optional[List[TestReportTest]] = None
    teardown: Optional[TestReportTeardown] = None