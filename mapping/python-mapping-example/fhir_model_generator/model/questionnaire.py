#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Questionnaire) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .usagecontext import UsageContext


@dataclass
class QuestionnaireItemEnableWhen(BackboneElement):
    """ Only allow data when.

    A constraint indicating that this item should only be enabled
    (displayed/allow answers to be captured) when the specified condition is
    true.
    """
    resource_type: ClassVar[str] = "QuestionnaireItemEnableWhen"

    question: str = None
    operator: str = None
    answerBoolean: bool = field(default=None, metadata=dict(one_of_many='answer',))
    answerDecimal: float = field(default=None, metadata=dict(one_of_many='answer',))
    answerInteger: int = field(default=None, metadata=dict(one_of_many='answer',))
    answerDate: FHIRDate = field(default=None, metadata=dict(one_of_many='answer',))
    answerDateTime: FHIRDate = field(default=None, metadata=dict(one_of_many='answer',))
    answerTime: FHIRDate = field(default=None, metadata=dict(one_of_many='answer',))
    answerString: str = field(default=None, metadata=dict(one_of_many='answer',))
    answerCoding: Coding = field(default=None, metadata=dict(one_of_many='answer',))
    answerQuantity: Quantity = field(default=None, metadata=dict(one_of_many='answer',))
    answerReference: FHIRReference = field(default=None, metadata=dict(one_of_many='answer',))


@dataclass
class QuestionnaireItemAnswerOption(BackboneElement):
    """ Permitted answer.

    One of the permitted answers for a "choice" or "open-choice" question.
    """
    resource_type: ClassVar[str] = "QuestionnaireItemAnswerOption"

    valueInteger: int = field(default=None, metadata=dict(one_of_many='value',))
    valueDate: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueTime: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueString: str = field(default=None, metadata=dict(one_of_many='value',))
    valueCoding: Coding = field(default=None, metadata=dict(one_of_many='value',))
    valueReference: FHIRReference = field(default=None, metadata=dict(one_of_many='value',))
    initialSelected: Optional[bool] = None


@dataclass
class QuestionnaireItemInitial(BackboneElement):
    """ Initial value(s) when item is first rendered.

    One or more values that should be pre-populated in the answer when
    initially rendering the questionnaire for user input.
    """
    resource_type: ClassVar[str] = "QuestionnaireItemInitial"

    valueBoolean: bool = field(default=None, metadata=dict(one_of_many='value',))
    valueDecimal: float = field(default=None, metadata=dict(one_of_many='value',))
    valueInteger: int = field(default=None, metadata=dict(one_of_many='value',))
    valueDate: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueDateTime: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueTime: FHIRDate = field(default=None, metadata=dict(one_of_many='value',))
    valueString: str = field(default=None, metadata=dict(one_of_many='value',))
    valueUri: str = field(default=None, metadata=dict(one_of_many='value',))
    valueAttachment: Attachment = field(default=None, metadata=dict(one_of_many='value',))
    valueCoding: Coding = field(default=None, metadata=dict(one_of_many='value',))
    valueQuantity: Quantity = field(default=None, metadata=dict(one_of_many='value',))
    valueReference: FHIRReference = field(default=None, metadata=dict(one_of_many='value',))


@dataclass
class QuestionnaireItem(BackboneElement):
    """ Questions and sections within the Questionnaire.

    A particular question, question grouping or display text that is part of
    the questionnaire.
    """
    resource_type: ClassVar[str] = "QuestionnaireItem"

    linkId: str = None
    definition: Optional[str] = None
    code: Optional[List[Coding]] = None
    prefix: Optional[str] = None
    text: Optional[str] = None
    type: str = None
    enableWhen: Optional[List[QuestionnaireItemEnableWhen]] = None
    enableBehavior: Optional[str] = None
    required: Optional[bool] = None
    repeats: Optional[bool] = None
    readOnly: Optional[bool] = None
    maxLength: Optional[int] = None
    answerValueSet: Optional[str] = None
    answerOption: Optional[List[QuestionnaireItemAnswerOption]] = None
    initial: Optional[List[QuestionnaireItemInitial]] = None
    item: Optional[List["QuestionnaireItem"]] = None


@dataclass
class Questionnaire(DomainResource):
    """ A structured set of questions.

    A structured set of questions intended to guide the collection of answers
    from end-users. Questionnaires provide detailed control over order,
    presentation, phraseology and grouping to allow coherent, consistent data
    collection.
    """
    resource_type: ClassVar[str] = "Questionnaire"

    url: Optional[str] = None
    identifier: Optional[List[Identifier]] = None
    version: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    derivedFrom: Optional[List[str]] = None
    status: str = None
    experimental: Optional[bool] = None
    subjectType: Optional[List[str]] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = None
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = None
    jurisdiction: Optional[List[CodeableConcept]] = None
    purpose: Optional[str] = None
    copyright: Optional[str] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    code: Optional[List[Coding]] = None
    item: Optional[List[QuestionnaireItem]] = None