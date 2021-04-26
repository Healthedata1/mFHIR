#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductContraindication) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .population import Population


@dataclass
class MedicinalProductContraindicationOtherTherapy(BackboneElement):
    """ Information about the use of the medicinal product in relation to other
    therapies described as part of the indication.
    """
    resource_type: ClassVar[str] = "MedicinalProductContraindicationOtherTherapy"

    therapyRelationshipType: CodeableConcept = None
    medicationCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='medication',))
    medicationReference: FHIRReference = field(default=None, metadata=dict(one_of_many='medication',))


@dataclass
class MedicinalProductContraindication(DomainResource):
    """ MedicinalProductContraindication.

    The clinical particulars - indications, contraindications etc. of a
    medicinal product, including for regulatory purposes.
    """
    resource_type: ClassVar[str] = "MedicinalProductContraindication"

    subject: Optional[List[FHIRReference]] = None
    disease: Optional[CodeableConcept] = None
    diseaseStatus: Optional[CodeableConcept] = None
    comorbidity: Optional[List[CodeableConcept]] = None
    therapeuticIndication: Optional[List[FHIRReference]] = None
    otherTherapy: Optional[List[MedicinalProductContraindicationOtherTherapy]] = None
    population: Optional[List[Population]] = None