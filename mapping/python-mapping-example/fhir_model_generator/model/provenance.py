#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Provenance) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .period import Period
from .signature import Signature


@dataclass
class ProvenanceAgent(BackboneElement):
    """ Actor involved.

    An actor taking a role in an activity  for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    resource_type: ClassVar[str] = "ProvenanceAgent"

    type: Optional[CodeableConcept] = None
    role: Optional[List[CodeableConcept]] = None
    who: FHIRReference = None
    onBehalfOf: Optional[FHIRReference] = None


@dataclass
class ProvenanceEntity(BackboneElement):
    """ An entity used in this activity.
    """
    resource_type: ClassVar[str] = "ProvenanceEntity"

    role: str = None
    what: FHIRReference = None
    agent: Optional[List[ProvenanceAgent]] = None


@dataclass
class Provenance(DomainResource):
    """ Who, What, When for a set of resources.

    Provenance of a resource is a record that describes entities and processes
    involved in producing and delivering or otherwise influencing that
    resource. Provenance provides a critical foundation for assessing
    authenticity, enabling trust, and allowing reproducibility. Provenance
    assertions are a form of contextual metadata and can themselves become
    important records with their own provenance. Provenance statement indicates
    clinical significance in terms of confidence in authenticity, reliability,
    and trustworthiness, integrity, and stage in lifecycle (e.g. Document
    Completion - has the artifact been legally authenticated), all of which may
    impact security, privacy, and trust policies.
    """
    resource_type: ClassVar[str] = "Provenance"

    target: List[FHIRReference] = field(default_factory=list)
    occurredPeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='occurred',))
    occurredDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='occurred',))
    recorded: FHIRDate = None
    policy: Optional[List[str]] = None
    location: Optional[FHIRReference] = None
    reason: Optional[List[CodeableConcept]] = None
    activity: Optional[CodeableConcept] = None
    agent: List[ProvenanceAgent] = field(default_factory=list)
    entity: Optional[List[ProvenanceEntity]] = None
    signature: Optional[List[Signature]] = None