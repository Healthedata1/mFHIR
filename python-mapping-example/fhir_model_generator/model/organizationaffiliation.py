#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/OrganizationAffiliation) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class OrganizationAffiliation(DomainResource):
    """ Defines an affiliation/assotiation/relationship between 2 distinct
    oganizations, that is not a part-of relationship/sub-division relationship.
    """
    resource_type: ClassVar[str] = "OrganizationAffiliation"

    identifier: Optional[List[Identifier]] = None
    active: Optional[bool] = None
    period: Optional[Period] = None
    organization: Optional[FHIRReference] = None
    participatingOrganization: Optional[FHIRReference] = None
    network: Optional[List[FHIRReference]] = None
    code: Optional[List[CodeableConcept]] = None
    specialty: Optional[List[CodeableConcept]] = None
    location: Optional[List[FHIRReference]] = None
    healthcareService: Optional[List[FHIRReference]] = None
    telecom: Optional[List[ContactPoint]] = None
    endpoint: Optional[List[FHIRReference]] = None