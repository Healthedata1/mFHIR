#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/VisionPrescription) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity


@dataclass
class VisionPrescriptionLensSpecificationPrism(BackboneElement):
    """ Eye alignment compensation.

    Allows for adjustment on two axis.
    """
    resource_type: ClassVar[str] = "VisionPrescriptionLensSpecificationPrism"

    amount: float = None
    base: str = None


@dataclass
class VisionPrescriptionLensSpecification(BackboneElement):
    """ Vision lens authorization.

    Contain the details of  the individual lens specifications and serves as
    the authorization for the fullfillment by certified professionals.
    """
    resource_type: ClassVar[str] = "VisionPrescriptionLensSpecification"

    product: CodeableConcept = None
    eye: str = None
    sphere: Optional[float] = None
    cylinder: Optional[float] = None
    axis: Optional[int] = None
    prism: Optional[List[VisionPrescriptionLensSpecificationPrism]] = None
    add: Optional[float] = None
    power: Optional[float] = None
    backCurve: Optional[float] = None
    diameter: Optional[float] = None
    duration: Optional[Quantity] = None
    color: Optional[str] = None
    brand: Optional[str] = None
    note: Optional[List[Annotation]] = None


@dataclass
class VisionPrescription(DomainResource):
    """ Prescription for vision correction products for a patient.

    An authorization for the provision of glasses and/or contact lenses to a
    patient.
    """
    resource_type: ClassVar[str] = "VisionPrescription"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    created: FHIRDate = None
    patient: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    dateWritten: FHIRDate = None
    prescriber: FHIRReference = None
    lensSpecification: List[VisionPrescriptionLensSpecification] = field(default_factory=list)