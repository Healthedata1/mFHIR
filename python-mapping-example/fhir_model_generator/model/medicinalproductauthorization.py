#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductAuthorization) on 2020-02-10.
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
from .period import Period


@dataclass
class MedicinalProductAuthorizationJurisdictionalAuthorization(BackboneElement):
    """ Authorization in areas within a country.
    """
    resource_type: ClassVar[str] = "MedicinalProductAuthorizationJurisdictionalAuthorization"

    identifier: Optional[List[Identifier]] = None
    country: Optional[CodeableConcept] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    legalStatusOfSupply: Optional[CodeableConcept] = None
    validityPeriod: Optional[Period] = None


@dataclass
class MedicinalProductAuthorizationProcedure(BackboneElement):
    """ The regulatory procedure for granting or amending a marketing authorization.
    """
    resource_type: ClassVar[str] = "MedicinalProductAuthorizationProcedure"

    identifier: Optional[Identifier] = None
    type: CodeableConcept = None
    datePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='date',))
    dateDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='date',))
    application: Optional[List["MedicinalProductAuthorizationProcedure"]] = None


@dataclass
class MedicinalProductAuthorization(DomainResource):
    """ The regulatory authorization of a medicinal product.
    """
    resource_type: ClassVar[str] = "MedicinalProductAuthorization"

    identifier: Optional[List[Identifier]] = None
    subject: Optional[FHIRReference] = None
    country: Optional[List[CodeableConcept]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    status: Optional[CodeableConcept] = None
    statusDate: Optional[FHIRDate] = None
    restoreDate: Optional[FHIRDate] = None
    validityPeriod: Optional[Period] = None
    dataExclusivityPeriod: Optional[Period] = None
    dateOfFirstAuthorization: Optional[FHIRDate] = None
    internationalBirthDate: Optional[FHIRDate] = None
    legalBasis: Optional[CodeableConcept] = None
    jurisdictionalAuthorization: Optional[List[MedicinalProductAuthorizationJurisdictionalAuthorization]] = None
    holder: Optional[FHIRReference] = None
    regulator: Optional[FHIRReference] = None
    procedure: Optional[MedicinalProductAuthorizationProcedure] = None