#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Task) on 2020-02-10.
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
from .domainresource import DomainResource
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
from .sampleddata import SampledData
from .signature import Signature
from .timing import Timing
from .triggerdefinition import TriggerDefinition
from .usagecontext import UsageContext


@dataclass
class TaskRestriction(BackboneElement):
    """ Constraints on fulfillment tasks.

    If the Task.focus is a request resource and the task is seeking fulfillment
    (i.e. is asking for the request to be actioned), this element identifies
    any limitations on what parts of the referenced request should be actioned.
    """
    resource_type: ClassVar[str] = "TaskRestriction"

    repetitions: Optional[int] = None
    period: Optional[Period] = None
    recipient: Optional[List[FHIRReference]] = None


@dataclass
class TaskInput(BackboneElement):
    """ Information used to perform task.

    Additional information that may be needed in the execution of the task.
    """
    resource_type: ClassVar[str] = "TaskInput"

    type: CodeableConcept = None
    valueBase64Binary: str = field(default=None, metadata=dict(one_of_many='value',))
    valueBoolean: bool = field(default=None, metadata=dict(one_of_many='value',))
    valueCanonical: str = field(default=None, metadata=dict(one_of_many='value',))
    valueCode: str = field(default=None, metadata=dict(one_of_many='value',))
    valueDate: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueDateTime: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueDecimal: float = field(default=None, metadata=dict(one_of_many='value',))
    valueId: str = field(default=None, metadata=dict(one_of_many='value',))
    valueInstant: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueInteger: int = field(default=None, metadata=dict(one_of_many='value',))
    valueMarkdown: str = field(default=None, metadata=dict(one_of_many='value',))
    valueOid: str = field(default=None, metadata=dict(one_of_many='value',))
    valuePositiveInt: int = field(default=None, metadata=dict(one_of_many='value',))
    valueString: str = field(default=None, metadata=dict(one_of_many='value',))
    valueTime: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueUnsignedInt: int = field(default=None, metadata=dict(one_of_many='value',))
    valueUri: str = field(default=None, metadata=dict(one_of_many='value',))
    valueUrl: str = field(default=None, metadata=dict(one_of_many='value',))
    valueUuid: str = field(default=None, metadata=dict(one_of_many='value',))
    valueAddress: Address = field(default=None, metadata=dict(one_of_many='value',))
    valueAge: Age = field(default=None, metadata=dict(one_of_many='value',))
    valueAnnotation: Annotation = field(default=None, metadata=dict(one_of_many='value',))
    valueAttachment: Attachment = field(default=None, metadata=dict(one_of_many='value',))
    valueCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='value',))
    valueCoding: Coding = field(default=None, metadata=dict(one_of_many='value',))
    valueContactPoint: ContactPoint = field(default=None, metadata=dict(one_of_many='value',))
    valueCount: Count = field(default=None, metadata=dict(one_of_many='value',))
    valueDistance: Distance = field(default=None, metadata=dict(one_of_many='value',))
    valueDuration: Duration = field(default=None, metadata=dict(one_of_many='value',))
    valueHumanName: HumanName = field(default=None, metadata=dict(one_of_many='value',))
    valueIdentifier: Identifier = field(default=None, metadata=dict(one_of_many='value',))
    valueMoney: Money = field(default=None, metadata=dict(one_of_many='value',))
    valuePeriod: Period = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Quantity = field(default=None, metadata=dict(one_of_many='value',))
    valueRange: Range = field(default=None, metadata=dict(one_of_many='value',))
    valueRatio: Ratio = field(default=None, metadata=dict(one_of_many='value',))
    valueReference: FHIRReference = field(default=None, metadata=dict(one_of_many='value',))
    valueSampledData: SampledData = field(default=None, metadata=dict(one_of_many='value',))
    valueSignature: Signature = field(default=None, metadata=dict(one_of_many='value',))
    valueTiming: Timing = field(default=None, metadata=dict(one_of_many='value',))
    valueContactDetail: ContactDetail = field(default=None, metadata=dict(one_of_many='value',))
    valueContributor: Contributor = field(default=None, metadata=dict(one_of_many='value',))
    valueDataRequirement: DataRequirement = field(default=None, metadata=dict(one_of_many='value',))
    valueExpression: Expression = field(default=None, metadata=dict(one_of_many='value',))
    valueParameterDefinition: ParameterDefinition = field(default=None, metadata=dict(one_of_many='value',))
    valueRelatedArtifact: RelatedArtifact = field(default=None, metadata=dict(one_of_many='value',))
    valueTriggerDefinition: TriggerDefinition = field(default=None, metadata=dict(one_of_many='value',))
    valueUsageContext: UsageContext = field(default=None, metadata=dict(one_of_many='value',))
    valueDosage: Dosage = field(default=None, metadata=dict(one_of_many='value',))
    valueMeta: Meta = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class TaskOutput(BackboneElement):
    """ Information produced as part of task.

    Outputs produced by the Task.
    """
    resource_type: ClassVar[str] = "TaskOutput"

    type: CodeableConcept = None
    valueBase64Binary: str = field(default=None, metadata=dict(one_of_many='value',))
    valueBoolean: bool = field(default=None, metadata=dict(one_of_many='value',))
    valueCanonical: str = field(default=None, metadata=dict(one_of_many='value',))
    valueCode: str = field(default=None, metadata=dict(one_of_many='value',))
    valueDate: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueDateTime: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueDecimal: float = field(default=None, metadata=dict(one_of_many='value',))
    valueId: str = field(default=None, metadata=dict(one_of_many='value',))
    valueInstant: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueInteger: int = field(default=None, metadata=dict(one_of_many='value',))
    valueMarkdown: str = field(default=None, metadata=dict(one_of_many='value',))
    valueOid: str = field(default=None, metadata=dict(one_of_many='value',))
    valuePositiveInt: int = field(default=None, metadata=dict(one_of_many='value',))
    valueString: str = field(default=None, metadata=dict(one_of_many='value',))
    valueTime: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueUnsignedInt: int = field(default=None, metadata=dict(one_of_many='value',))
    valueUri: str = field(default=None, metadata=dict(one_of_many='value',))
    valueUrl: str = field(default=None, metadata=dict(one_of_many='value',))
    valueUuid: str = field(default=None, metadata=dict(one_of_many='value',))
    valueAddress: Address = field(default=None, metadata=dict(one_of_many='value',))
    valueAge: Age = field(default=None, metadata=dict(one_of_many='value',))
    valueAnnotation: Annotation = field(default=None, metadata=dict(one_of_many='value',))
    valueAttachment: Attachment = field(default=None, metadata=dict(one_of_many='value',))
    valueCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='value',))
    valueCoding: Coding = field(default=None, metadata=dict(one_of_many='value',))
    valueContactPoint: ContactPoint = field(default=None, metadata=dict(one_of_many='value',))
    valueCount: Count = field(default=None, metadata=dict(one_of_many='value',))
    valueDistance: Distance = field(default=None, metadata=dict(one_of_many='value',))
    valueDuration: Duration = field(default=None, metadata=dict(one_of_many='value',))
    valueHumanName: HumanName = field(default=None, metadata=dict(one_of_many='value',))
    valueIdentifier: Identifier = field(default=None, metadata=dict(one_of_many='value',))
    valueMoney: Money = field(default=None, metadata=dict(one_of_many='value',))
    valuePeriod: Period = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Quantity = field(default=None, metadata=dict(one_of_many='value',))
    valueRange: Range = field(default=None, metadata=dict(one_of_many='value',))
    valueRatio: Ratio = field(default=None, metadata=dict(one_of_many='value',))
    valueReference: FHIRReference = field(default=None, metadata=dict(one_of_many='value',))
    valueSampledData: SampledData = field(default=None, metadata=dict(one_of_many='value',))
    valueSignature: Signature = field(default=None, metadata=dict(one_of_many='value',))
    valueTiming: Timing = field(default=None, metadata=dict(one_of_many='value',))
    valueContactDetail: ContactDetail = field(default=None, metadata=dict(one_of_many='value',))
    valueContributor: Contributor = field(default=None, metadata=dict(one_of_many='value',))
    valueDataRequirement: DataRequirement = field(default=None, metadata=dict(one_of_many='value',))
    valueExpression: Expression = field(default=None, metadata=dict(one_of_many='value',))
    valueParameterDefinition: ParameterDefinition = field(default=None, metadata=dict(one_of_many='value',))
    valueRelatedArtifact: RelatedArtifact = field(default=None, metadata=dict(one_of_many='value',))
    valueTriggerDefinition: TriggerDefinition = field(default=None, metadata=dict(one_of_many='value',))
    valueUsageContext: UsageContext = field(default=None, metadata=dict(one_of_many='value',))
    valueDosage: Dosage = field(default=None, metadata=dict(one_of_many='value',))
    valueMeta: Meta = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class Task(DomainResource):
    """ A task to be performed.
    """
    resource_type: ClassVar[str] = "Task"

    identifier: Optional[List[Identifier]] = None
    instantiatesCanonical: Optional[str] = None
    instantiatesUri: Optional[str] = None
    basedOn: Optional[List[FHIRReference]] = None
    groupIdentifier: Optional[Identifier] = None
    partOf: Optional[List[FHIRReference]] = None
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    businessStatus: Optional[CodeableConcept] = None
    intent: str = None
    priority: Optional[str] = None
    code: Optional[CodeableConcept] = None
    description: Optional[str] = None
    focus: Optional[FHIRReference] = None
    for_fhir: Optional[FHIRReference] = field(default=None, metadata=dict(orig_name='for'))
    encounter: Optional[FHIRReference] = None
    executionPeriod: Optional[Period] = None
    authoredOn: Optional[FHIRDate] = None
    lastModified: Optional[FHIRDate] = None
    requester: Optional[FHIRReference] = None
    performerType: Optional[List[CodeableConcept]] = None
    owner: Optional[FHIRReference] = None
    location: Optional[FHIRReference] = None
    reasonCode: Optional[CodeableConcept] = None
    reasonReference: Optional[FHIRReference] = None
    insurance: Optional[List[FHIRReference]] = None
    note: Optional[List[Annotation]] = None
    relevantHistory: Optional[List[FHIRReference]] = None
    restriction: Optional[TaskRestriction] = None
    input: Optional[List[TaskInput]] = None
    output: Optional[List[TaskOutput]] = None