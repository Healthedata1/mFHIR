#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Endpoint) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class Endpoint(DomainResource):
    """ The technical details of an endpoint that can be used for electronic
    services.

    The technical details of an endpoint that can be used for electronic
    services, such as for web services providing XDS.b or a REST endpoint for
    another FHIR server. This may include any security context information.
    """
    resource_type: ClassVar[str] = "Endpoint"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    connectionType: Coding = None
    name: Optional[str] = None
    managingOrganization: Optional[FHIRReference] = None
    contact: Optional[List[ContactPoint]] = None
    period: Optional[Period] = None
    payloadType: List[CodeableConcept] = field(default_factory=list)
    payloadMimeType: Optional[List[str]] = None
    address: str = None
    header: Optional[List[str]] = None