#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/VerificationResult) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .signature import Signature
from .timing import Timing


@dataclass
class VerificationResultPrimarySource(BackboneElement):
    """ Information about the primary source(s) involved in validation.
    """
    resource_type: ClassVar[str] = "VerificationResultPrimarySource"

    who: Optional[FHIRReference] = None
    type: Optional[List[CodeableConcept]] = None
    communicationMethod: Optional[List[CodeableConcept]] = None
    validationStatus: Optional[CodeableConcept] = None
    validationDate: Optional[FHIRDate] = None
    canPushUpdates: Optional[CodeableConcept] = None
    pushTypeAvailable: Optional[List[CodeableConcept]] = None


@dataclass
class VerificationResultAttestation(BackboneElement):
    """ Information about the entity attesting to information.
    """
    resource_type: ClassVar[str] = "VerificationResultAttestation"

    who: Optional[FHIRReference] = None
    onBehalfOf: Optional[FHIRReference] = None
    communicationMethod: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    sourceIdentityCertificate: Optional[str] = None
    proxyIdentityCertificate: Optional[str] = None
    proxySignature: Optional[Signature] = None
    sourceSignature: Optional[Signature] = None


@dataclass
class VerificationResultValidator(BackboneElement):
    """ Information about the entity validating information.
    """
    resource_type: ClassVar[str] = "VerificationResultValidator"

    organization: FHIRReference = None
    identityCertificate: Optional[str] = None
    attestationSignature: Optional[Signature] = None


@dataclass
class VerificationResult(DomainResource):
    """ Describes validation requirements, source(s), status and dates for one or
    more elements.
    """
    resource_type: ClassVar[str] = "VerificationResult"

    target: Optional[List[FHIRReference]] = None
    targetLocation: Optional[List[str]] = None
    need: Optional[CodeableConcept] = None
    status: str = None
    statusDate: Optional[FHIRDate] = None
    validationType: Optional[CodeableConcept] = None
    validationProcess: Optional[List[CodeableConcept]] = None
    frequency: Optional[Timing] = None
    lastPerformed: Optional[FHIRDate] = None
    nextScheduled: Optional[FHIRDate] = None
    failureAction: Optional[CodeableConcept] = None
    primarySource: Optional[List[VerificationResultPrimarySource]] = None
    attestation: Optional[VerificationResultAttestation] = None
    validator: Optional[List[VerificationResultValidator]] = None