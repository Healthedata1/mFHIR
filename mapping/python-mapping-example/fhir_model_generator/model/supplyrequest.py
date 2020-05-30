#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SupplyRequest) on 2020-02-10.
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
from .range import Range
from .timing import Timing


@dataclass
class SupplyRequestParameter(BackboneElement):
    """ Ordered item details.

    Specific parameters for the ordered item.  For example, the size of the
    indicated item.
    """
    resource_type: ClassVar[str] = "SupplyRequestParameter"

    code: Optional[CodeableConcept] = None
    valueCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='value',))
    valueRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='value',))
    valueBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class SupplyRequest(DomainResource):
    """ Request for a medication, substance or device.

    A record of a request for a medication, substance or device used in the
    healthcare setting.
    """
    resource_type: ClassVar[str] = "SupplyRequest"

    identifier: Optional[List[Identifier]] = None
    status: Optional[str] = None
    category: Optional[CodeableConcept] = None
    priority: Optional[str] = None
    itemCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='item',))
    itemReference: FHIRReference = field(default=None, metadata=dict(one_of_many='item',))
    quantity: Quantity = None
    parameter: Optional[List[SupplyRequestParameter]] = None
    occurrenceDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrencePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrenceTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='occurrence',))
    authoredOn: Optional[FHIRDate] = None
    requester: Optional[FHIRReference] = None
    supplier: Optional[List[FHIRReference]] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    deliverFrom: Optional[FHIRReference] = None
    deliverTo: Optional[FHIRReference] = None