#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/OperationOutcome) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource


@dataclass
class OperationOutcomeIssue(BackboneElement):
    """ A single issue associated with the action.

    An error, warning, or information message that results from a system
    action.
    """
    resource_type: ClassVar[str] = "OperationOutcomeIssue"

    severity: str = None
    code: str = None
    details: Optional[CodeableConcept] = None
    diagnostics: Optional[str] = None
    location: Optional[List[str]] = None
    expression: Optional[List[str]] = None


@dataclass
class OperationOutcome(DomainResource):
    """ Information about the success/failure of an action.

    A collection of error, warning, or information messages that result from a
    system action.
    """
    resource_type: ClassVar[str] = "OperationOutcome"

    issue: List[OperationOutcomeIssue] = field(default_factory=list)