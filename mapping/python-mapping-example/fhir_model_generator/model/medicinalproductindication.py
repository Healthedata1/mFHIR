#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductIndication) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .population import Population
from .quantity import Quantity


@dataclass
class MedicinalProductIndicationOtherTherapy(BackboneElement):
    """ Information about the use of the medicinal product in relation to other
    therapies described as part of the indication.
    """
    resource_type: ClassVar[str] = "MedicinalProductIndicationOtherTherapy"

    therapyRelationshipType: CodeableConcept = None
    medicationCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='medication',))
    medicationReference: FHIRReference = field(default=None, metadata=dict(one_of_many='medication',))


@dataclass
class MedicinalProductIndication(DomainResource):
    """ MedicinalProductIndication.

    Indication for the Medicinal Product.
    """
    resource_type: ClassVar[str] = "MedicinalProductIndication"

    subject: Optional[List[FHIRReference]] = None
    diseaseSymptomProcedure: Optional[CodeableConcept] = None
    diseaseStatus: Optional[CodeableConcept] = None
    comorbidity: Optional[List[CodeableConcept]] = None
    intendedEffect: Optional[CodeableConcept] = None
    duration: Optional[Quantity] = None
    otherTherapy: Optional[List[MedicinalProductIndicationOtherTherapy]] = None
    undesirableEffect: Optional[List[FHIRReference]] = None
    population: Optional[List[Population]] = None