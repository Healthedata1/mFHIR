#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Parameters) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .address import Address
from .age import Age
from .annotation import Annotation
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .contactpoint import ContactPoint
from .contributor import Contributor
from .count import Count
from .datarequirement import DataRequirement
from .distance import Distance
from .dosage import Dosage
from .duration import Duration
from .expression import Expression
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .humanname import HumanName
from .identifier import Identifier
from .meta import Meta
from .money import Money
from .parameterdefinition import ParameterDefinition
from .period import Period
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .relatedartifact import RelatedArtifact
from .resource import Resource
from .sampleddata import SampledData
from .signature import Signature
from .timing import Timing
from .triggerdefinition import TriggerDefinition
from .usagecontext import UsageContext


@dataclass
class ParametersParameter(BackboneElement):
    """ Operation Parameter.

    A parameter passed to or received from the operation.
    """
    resource_type: ClassVar[str] = "ParametersParameter"

    name: str = None
    valueBase64Binary: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='value',))
    valueCanonical: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueCode: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valueDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valueDecimal: Optional[float] = field(default=None, metadata=dict(one_of_many='value',))
    valueId: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueInstant: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valueInteger: Optional[int] = field(default=None, metadata=dict(one_of_many='value',))
    valueMarkdown: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueOid: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valuePositiveInt: Optional[int] = field(default=None, metadata=dict(one_of_many='value',))
    valueString: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valueUnsignedInt: Optional[int] = field(default=None, metadata=dict(one_of_many='value',))
    valueUri: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueUrl: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueUuid: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueAddress: Optional[Address] = field(default=None, metadata=dict(one_of_many='value',))
    valueAge: Optional[Age] = field(default=None, metadata=dict(one_of_many='value',))
    valueAnnotation: Optional[Annotation] = field(default=None, metadata=dict(one_of_many='value',))
    valueAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='value',))
    valueCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='value',))
    valueCoding: Optional[Coding] = field(default=None, metadata=dict(one_of_many='value',))
    valueContactPoint: Optional[ContactPoint] = field(default=None, metadata=dict(one_of_many='value',))
    valueCount: Optional[Count] = field(default=None, metadata=dict(one_of_many='value',))
    valueDistance: Optional[Distance] = field(default=None, metadata=dict(one_of_many='value',))
    valueDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='value',))
    valueHumanName: Optional[HumanName] = field(default=None, metadata=dict(one_of_many='value',))
    valueIdentifier: Optional[Identifier] = field(default=None, metadata=dict(one_of_many='value',))
    valueMoney: Optional[Money] = field(default=None, metadata=dict(one_of_many='value',))
    valuePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='value',))
    valueRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='value',))
    valueRatio: Optional[Ratio] = field(default=None, metadata=dict(one_of_many='value',))
    valueReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='value',))
    valueSampledData: Optional[SampledData] = field(default=None, metadata=dict(one_of_many='value',))
    valueSignature: Optional[Signature] = field(default=None, metadata=dict(one_of_many='value',))
    valueTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='value',))
    valueContactDetail: Optional[ContactDetail] = field(default=None, metadata=dict(one_of_many='value',))
    valueContributor: Optional[Contributor] = field(default=None, metadata=dict(one_of_many='value',))
    valueDataRequirement: Optional[DataRequirement] = field(default=None, metadata=dict(one_of_many='value',))
    valueExpression: Optional[Expression] = field(default=None, metadata=dict(one_of_many='value',))
    valueParameterDefinition: Optional[ParameterDefinition] = field(default=None, metadata=dict(one_of_many='value',))
    valueRelatedArtifact: Optional[RelatedArtifact] = field(default=None, metadata=dict(one_of_many='value',))
    valueTriggerDefinition: Optional[TriggerDefinition] = field(default=None, metadata=dict(one_of_many='value',))
    valueUsageContext: Optional[UsageContext] = field(default=None, metadata=dict(one_of_many='value',))
    valueDosage: Optional[Dosage] = field(default=None, metadata=dict(one_of_many='value',))
    valueMeta: Optional[Meta] = field(default=None, metadata=dict(one_of_many='value',))
    resource: Optional[Resource] = None
    part: Optional[List["ParametersParameter"]] = None


@dataclass
class Parameters(Resource):
    """ Operation Request or Response.

    This resource is a non-persisted resource used to pass information into and
    back from an [operation](operations.html). It has no other use, and there
    is no RESTful endpoint associated with it.
    """
    resource_type: ClassVar[str] = "Parameters"

    parameter: Optional[List[ParametersParameter]] = None