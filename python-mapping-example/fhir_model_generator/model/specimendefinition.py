#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SpecimenDefinition) on 2020-02-10.
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
from .range import Range


@dataclass
class SpecimenDefinitionTypeTestedContainerAdditive(BackboneElement):
    """ Additive associated with container.

    Substance introduced in the kind of container to preserve, maintain or
    enhance the specimen. Examples: Formalin, Citrate, EDTA.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTestedContainerAdditive"

    additiveCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='additive',))
    additiveReference: FHIRReference = field(default=None, metadata=dict(one_of_many='additive',))


@dataclass
class SpecimenDefinitionTypeTestedContainer(BackboneElement):
    """ The specimen's container.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTestedContainer"

    material: Optional[CodeableConcept] = None
    type: Optional[CodeableConcept] = None
    cap: Optional[CodeableConcept] = None
    description: Optional[str] = None
    capacity: Optional[Quantity] = None
    minimumVolumeQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='minimumVolume',))
    minimumVolumeString: Optional[str] = field(default=None, metadata=dict(one_of_many='minimumVolume',))
    additive: Optional[List[SpecimenDefinitionTypeTestedContainerAdditive]] = None
    preparation: Optional[str] = None


@dataclass
class SpecimenDefinitionTypeTestedHandling(BackboneElement):
    """ Specimen handling before testing.

    Set of instructions for preservation/transport of the specimen at a defined
    temperature interval, prior the testing process.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTestedHandling"

    temperatureQualifier: Optional[CodeableConcept] = None
    temperatureRange: Optional[Range] = None
    maxDuration: Optional[Duration] = None
    instruction: Optional[str] = None


@dataclass
class SpecimenDefinitionTypeTested(BackboneElement):
    """ Specimen in container intended for testing by lab.

    Specimen conditioned in a container as expected by the testing laboratory.
    """
    resource_type: ClassVar[str] = "SpecimenDefinitionTypeTested"

    isDerived: Optional[bool] = None
    type: Optional[CodeableConcept] = None
    preference: str = None
    container: Optional[SpecimenDefinitionTypeTestedContainer] = None
    requirement: Optional[str] = None
    retentionTime: Optional[Duration] = None
    rejectionCriterion: Optional[List[CodeableConcept]] = None
    handling: Optional[List[SpecimenDefinitionTypeTestedHandling]] = None


@dataclass
class SpecimenDefinition(DomainResource):
    """ Kind of specimen.

    A kind of specimen with associated set of requirements.
    """
    resource_type: ClassVar[str] = "SpecimenDefinition"

    identifier: Optional[Identifier] = None
    typeCollected: Optional[CodeableConcept] = None
    patientPreparation: Optional[List[CodeableConcept]] = None
    timeAspect: Optional[str] = None
    collection: Optional[List[CodeableConcept]] = None
    typeTested: Optional[List[SpecimenDefinitionTypeTested]] = None