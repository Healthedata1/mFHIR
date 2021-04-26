#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity


@dataclass
class QuestionnaireResponseItemAnswer(BackboneElement):
    """ The response(s) to the question.

    The respondent's answer(s) to the question.
    """
    resource_type: ClassVar[str] = "QuestionnaireResponseItemAnswer"

    valueBoolean: Optional[bool] = field(default=None, metadata=dict(one_of_many='value',))
    valueDecimal: Optional[float] = field(default=None, metadata=dict(one_of_many='value',))
    valueInteger: Optional[int] = field(default=None, metadata=dict(one_of_many='value',))
    valueDate: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valueDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valueTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='value',))
    valueString: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueUri: Optional[str] = field(default=None, metadata=dict(one_of_many='value',))
    valueAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='value',))
    valueCoding: Optional[Coding] = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='value',))
    valueReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='value',))
    item: Optional[List["QuestionnaireResponseItem"]] = None


@dataclass
class QuestionnaireResponseItem(BackboneElement):
    """ Groups and questions.

    A group or question item from the original questionnaire for which answers
    are provided.
    """
    resource_type: ClassVar[str] = "QuestionnaireResponseItem"

    linkId: str = None
    definition: Optional[str] = None
    text: Optional[str] = None
    answer: Optional[List[QuestionnaireResponseItemAnswer]] = None
    item: Optional[List["QuestionnaireResponseItem"]] = None


@dataclass
class QuestionnaireResponse(DomainResource):
    """ A structured set of questions and their answers.

    A structured set of questions and their answers. The questions are ordered
    and grouped into coherent subsets, corresponding to the structure of the
    grouping of the questionnaire being responded to.
    """
    resource_type: ClassVar[str] = "QuestionnaireResponse"

    identifier: Optional[Identifier] = None
    basedOn: Optional[List[FHIRReference]] = None
    partOf: Optional[List[FHIRReference]] = None
    questionnaire: Optional[str] = None
    status: str = None
    subject: Optional[FHIRReference] = None
    encounter: Optional[FHIRReference] = None
    authored: Optional[FHIRDate] = None
    author: Optional[FHIRReference] = None
    source: Optional[FHIRReference] = None
    item: Optional[List[QuestionnaireResponseItem]] = None