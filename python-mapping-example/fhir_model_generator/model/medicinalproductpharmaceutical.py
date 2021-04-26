#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductPharmaceutical) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .duration import Duration
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod(BackboneElement):
    """ A species specific time during which consumption of animal product is not
    appropriate.
    """
    resource_type: ClassVar[str] = "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod"

    tissue: CodeableConcept = None
    value: Quantity = None
    supportingInformation: Optional[str] = None


@dataclass
class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies(BackboneElement):
    """ A species for which this route applies.
    """
    resource_type: ClassVar[str] = "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies"

    code: CodeableConcept = None
    withdrawalPeriod: Optional[List[MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod]] = None


@dataclass
class MedicinalProductPharmaceuticalCharacteristics(BackboneElement):
    """ Characteristics e.g. a products onset of action.
    """
    resource_type: ClassVar[str] = "MedicinalProductPharmaceuticalCharacteristics"

    code: CodeableConcept = None
    status: Optional[CodeableConcept] = None


@dataclass
class MedicinalProductPharmaceuticalRouteOfAdministration(BackboneElement):
    """ The path by which the pharmaceutical product is taken into or makes contact
    with the body.
    """
    resource_type: ClassVar[str] = "MedicinalProductPharmaceuticalRouteOfAdministration"

    code: CodeableConcept = None
    firstDose: Optional[Quantity] = None
    maxSingleDose: Optional[Quantity] = None
    maxDosePerDay: Optional[Quantity] = None
    maxDosePerTreatmentPeriod: Optional[Ratio] = None
    maxTreatmentPeriod: Optional[Duration] = None
    targetSpecies: Optional[List[MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies]] = None


@dataclass
class MedicinalProductPharmaceutical(DomainResource):
    """ A pharmaceutical product described in terms of its composition and dose
    form.
    """
    resource_type: ClassVar[str] = "MedicinalProductPharmaceutical"

    identifier: Optional[List[Identifier]] = None
    administrableDoseForm: CodeableConcept = None
    unitOfPresentation: Optional[CodeableConcept] = None
    ingredient: Optional[List[FHIRReference]] = None
    device: Optional[List[FHIRReference]] = None
    characteristics: Optional[List[MedicinalProductPharmaceuticalCharacteristics]] = None
    routeOfAdministration: List[MedicinalProductPharmaceuticalRouteOfAdministration] = field(default_factory=list)