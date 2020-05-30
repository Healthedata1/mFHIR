#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/StructureMap) on 2020-02-10.
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
class StructureMapGroupRuleTargetParameter(BackboneElement):
    """ Parameters to the transform.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleTargetParameter"

    valueId: str = field(default=None, metadata=dict(one_of_many='value',))
    valueString: str = field(default=None, metadata=dict(one_of_many='value',))
    valueBoolean: bool = field(default=None, metadata=dict(one_of_many='value',))
    valueInteger: int = field(default=None, metadata=dict(one_of_many='value',))
    valueDecimal: float = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class StructureMapGroupRuleSource(BackboneElement):
    """ Source inputs to the mapping.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleSource"

    context: str = None
    min: Optional[int] = None
    max: Optional[str] = None
    type: Optional[str] = None
    defaultValueBase64Binary: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueCanonical: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueCode: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueDecimal: Optional[float] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueId: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueInstant: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueInteger: Optional[int] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueMarkdown: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueOid: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValuePositiveInt: Optional[int] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueString: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueUnsignedInt: Optional[int] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueUri: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueUrl: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueUuid: Optional[str] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueAddress: Optional[Address] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueAge: Optional[Age] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueAnnotation: Optional[Annotation] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueCoding: Optional[Coding] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueContactPoint: Optional[ContactPoint] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueCount: Optional[Count] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueDistance: Optional[Distance] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueDuration: Optional[Duration] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueHumanName: Optional[HumanName] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueIdentifier: Optional[Identifier] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueMoney: Optional[Money] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValuePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueRange: Optional[Range] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueRatio: Optional[Ratio] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueSampledData: Optional[SampledData] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueSignature: Optional[Signature] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueContactDetail: Optional[ContactDetail] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueContributor: Optional[Contributor] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueDataRequirement: Optional[DataRequirement] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueExpression: Optional[Expression] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueParameterDefinition: Optional[ParameterDefinition] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueRelatedArtifact: Optional[RelatedArtifact] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueTriggerDefinition: Optional[TriggerDefinition] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueUsageContext: Optional[UsageContext] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueDosage: Optional[Dosage] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    defaultValueMeta: Optional[Meta] = field(default=None, metadata=dict(one_of_many='defaultValue',))
    element: Optional[str] = None
    listMode: Optional[str] = None
    variable: Optional[str] = None
    condition: Optional[str] = None
    check: Optional[str] = None
    logMessage: Optional[str] = None


@dataclass
class StructureMapGroupRuleTarget(BackboneElement):
    """ Content to create because of this mapping rule.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleTarget"

    context: Optional[str] = None
    contextType: Optional[str] = None
    element: Optional[str] = None
    variable: Optional[str] = None
    listMode: Optional[List[str]] = None
    listRuleId: Optional[str] = None
    transform: Optional[str] = None
    parameter: Optional[List[StructureMapGroupRuleTargetParameter]] = None


@dataclass
class StructureMapGroupRuleDependent(BackboneElement):
    """ Which other rules to apply in the context of this rule.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleDependent"

    name: str = None
    variable: List[str] = field(default_factory=list)


@dataclass
class StructureMapGroupInput(BackboneElement):
    """ Named instance provided when invoking the map.

    A name assigned to an instance of data. The instance must be provided when
    the mapping is invoked.
    """
    resource_type: ClassVar[str] = "StructureMapGroupInput"

    name: str = None
    type: Optional[str] = None
    mode: str = None
    documentation: Optional[str] = None


@dataclass
class StructureMapGroupRule(BackboneElement):
    """ Transform Rule from source to target.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRule"

    name: str = None
    source: List[StructureMapGroupRuleSource] = field(default_factory=list)
    target: Optional[List[StructureMapGroupRuleTarget]] = None
    rule: Optional[List["StructureMapGroupRule"]] = None
    dependent: Optional[List[StructureMapGroupRuleDependent]] = None
    documentation: Optional[str] = None


@dataclass
class StructureMapStructure(BackboneElement):
    """ Structure Definition used by this map.

    A structure definition used by this map. The structure definition may
    describe instances that are converted, or the instances that are produced.
    """
    resource_type: ClassVar[str] = "StructureMapStructure"

    url: str = None
    mode: str = None
    alias: Optional[str] = None
    documentation: Optional[str] = None


@dataclass
class StructureMapGroup(BackboneElement):
    """ Named sections for reader convenience.

    Organizes the mapping into manageable chunks for human review/ease of
    maintenance.
    """
    resource_type: ClassVar[str] = "StructureMapGroup"

    name: str = None
    extends: Optional[str] = None
    typeMode: str = None
    documentation: Optional[str] = None
    input: List[StructureMapGroupInput] = field(default_factory=list)
    rule: List[StructureMapGroupRule] = field(default_factory=list)


@dataclass
class StructureMap(DomainResource):
    """ A Map of relationships between 2 structures that can be used to transform
    data.
    """
    resource_type: ClassVar[str] = "StructureMap"

    url: str = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: str = None
    title: Optional[str] = None
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    structure: Optional[List[StructureMapStructure]] = None
    import_fhir: Optional[List[str]] = field(default_factory=list, metadata=dict(orig_name='import'))
    group: List[StructureMapGroup] = field(default_factory=list)