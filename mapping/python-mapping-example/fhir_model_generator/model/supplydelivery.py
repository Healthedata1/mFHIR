#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SupplyDelivery) on 2020-02-10.
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
from .quantity import Quantity
from .timing import Timing


@dataclass
class SupplyDeliverySuppliedItem(BackboneElement):
    """ The item that is delivered or supplied.

    The item that is being delivered or has been supplied.
    """
    resource_type: ClassVar[str] = "SupplyDeliverySuppliedItem"

    quantity: Optional[Quantity] = None
    itemCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='item',))
    itemReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='item',))


@dataclass
class SupplyDelivery(DomainResource):
    """ Delivery of bulk Supplies.

    Record of delivery of what is supplied.
    """
    resource_type: ClassVar[str] = "SupplyDelivery"

    identifier: Optional[List[Identifier]] = None
    basedOn: Optional[List[FHIRReference]] = None
    partOf: Optional[List[FHIRReference]] = None
    status: Optional[str] = None
    patient: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None
    suppliedItem: Optional[SupplyDeliverySuppliedItem] = None
    occurrenceDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrencePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrenceTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='occurrence',))
    supplier: Optional[FHIRReference] = None
    destination: Optional[FHIRReference] = None
    receiver: Optional[List[FHIRReference]] = None