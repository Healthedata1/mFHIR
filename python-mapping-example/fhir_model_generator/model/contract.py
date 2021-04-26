#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Contract) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period
from .quantity import Quantity
from .signature import Signature
from .timing import Timing


@dataclass
class ContractTermActionSubject(BackboneElement):
    """ Entity of the action.
    """
    resource_type: ClassVar[str] = "ContractTermActionSubject"

    reference: List[FHIRReference] = field(default_factory=list)
    role: Optional[CodeableConcept] = None


@dataclass
class ContractTermAssetContext(BackboneElement):
    """ Circumstance of the asset.
    """
    resource_type: ClassVar[str] = "ContractTermAssetContext"

    reference: Optional[FHIRReference] = None
    code: Optional[List[CodeableConcept]] = None
    text: Optional[str] = None


@dataclass
class ContractTermAssetValuedItem(BackboneElement):
    """ Contract Valued Item List.
    """
    resource_type: ClassVar[str] = "ContractTermAssetValuedItem"

    entityCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='entity',))
    entityReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='entity',))
    identifier: Optional[Identifier] = None
    effectiveTime: Optional[FHIRDate] = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None
    factor: Optional[float] = None
    points: Optional[float] = None
    net: Optional[Money] = None
    payment: Optional[str] = None
    paymentDate: Optional[FHIRDate] = None
    responsible: Optional[FHIRReference] = None
    recipient: Optional[FHIRReference] = None
    linkId: Optional[List[str]] = None
    securityLabelNumber: Optional[List[int]] = None


@dataclass
class ContractTermOfferParty(BackboneElement):
    """ Offer Recipient.
    """
    resource_type: ClassVar[str] = "ContractTermOfferParty"

    reference: List[FHIRReference] = field(default_factory=list)
    role: CodeableConcept = None


@dataclass
class ContractTermOfferAnswer(BackboneElement):
    """ Response to offer text.
    """
    resource_type: ClassVar[str] = "ContractTermOfferAnswer"

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
class ContractTermSecurityLabel(BackboneElement):
    """ Protection for the Term.

    Security labels that protect the handling of information about the term and
    its elements, which may be specifically identified..
    """
    resource_type: ClassVar[str] = "ContractTermSecurityLabel"

    number: Optional[List[int]] = None
    classification: Coding = None
    category: Optional[List[Coding]] = None
    control: Optional[List[Coding]] = None


@dataclass
class ContractTermOffer(BackboneElement):
    """ Context of the Contract term.

    The matter of concern in the context of this provision of the agrement.
    """
    resource_type: ClassVar[str] = "ContractTermOffer"

    identifier: Optional[List[Identifier]] = None
    party: Optional[List[ContractTermOfferParty]] = None
    topic: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None
    decision: Optional[CodeableConcept] = None
    decisionMode: Optional[List[CodeableConcept]] = None
    answer: Optional[List[ContractTermOfferAnswer]] = None
    text: Optional[str] = None
    linkId: Optional[List[str]] = None
    securityLabelNumber: Optional[List[int]] = None


@dataclass
class ContractTermAsset(BackboneElement):
    """ Contract Term Asset List.
    """
    resource_type: ClassVar[str] = "ContractTermAsset"

    scope: Optional[CodeableConcept] = None
    type: Optional[List[CodeableConcept]] = None
    typeReference: Optional[List[FHIRReference]] = None
    subtype: Optional[List[CodeableConcept]] = None
    relationship: Optional[Coding] = None
    context: Optional[List[ContractTermAssetContext]] = None
    condition: Optional[str] = None
    periodType: Optional[List[CodeableConcept]] = None
    period: Optional[List[Period]] = None
    usePeriod: Optional[List[Period]] = None
    text: Optional[str] = None
    linkId: Optional[List[str]] = None
    answer: Optional[List[ContractTermOfferAnswer]] = None
    securityLabelNumber: Optional[List[int]] = None
    valuedItem: Optional[List[ContractTermAssetValuedItem]] = None


@dataclass
class ContractTermAction(BackboneElement):
    """ Entity being ascribed responsibility.

    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    resource_type: ClassVar[str] = "ContractTermAction"

    doNotPerform: Optional[bool] = None
    type: CodeableConcept = None
    subject: Optional[List[ContractTermActionSubject]] = None
    intent: CodeableConcept = None
    linkId: Optional[List[str]] = None
    status: CodeableConcept = None
    context: Optional[FHIRReference] = None
    contextLinkId: Optional[List[str]] = None
    occurrenceDateTime: Optional[FHIRDate] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrencePeriod: Optional[Period] = field(default=None, metadata=dict(one_of_many='occurrence',))
    occurrenceTiming: Optional[Timing] = field(default=None, metadata=dict(one_of_many='occurrence',))
    requester: Optional[List[FHIRReference]] = None
    requesterLinkId: Optional[List[str]] = None
    performerType: Optional[List[CodeableConcept]] = None
    performerRole: Optional[CodeableConcept] = None
    performer: Optional[FHIRReference] = None
    performerLinkId: Optional[List[str]] = None
    reasonCode: Optional[List[CodeableConcept]] = None
    reasonReference: Optional[List[FHIRReference]] = None
    reason: Optional[List[str]] = None
    reasonLinkId: Optional[List[str]] = None
    note: Optional[List[Annotation]] = None
    securityLabelNumber: Optional[List[int]] = None


@dataclass
class ContractContentDefinition(BackboneElement):
    """ Contract precursor content.

    Precusory content developed with a focus and intent of supporting the
    formation a Contract instance, which may be associated with and
    transformable into a Contract.
    """
    resource_type: ClassVar[str] = "ContractContentDefinition"

    type: CodeableConcept = None
    subType: Optional[CodeableConcept] = None
    publisher: Optional[FHIRReference] = None
    publicationDate: Optional[FHIRDate] = None
    publicationStatus: str = None
    copyright: Optional[str] = None


@dataclass
class ContractTerm(BackboneElement):
    """ Contract Term List.

    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """
    resource_type: ClassVar[str] = "ContractTerm"

    identifier: Optional[Identifier] = None
    issued: Optional[FHIRDate] = None
    applies: Optional[Period] = None
    topicCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='topic',))
    topicReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='topic',))
    type: Optional[CodeableConcept] = None
    subType: Optional[CodeableConcept] = None
    text: Optional[str] = None
    securityLabel: Optional[List[ContractTermSecurityLabel]] = None
    offer: ContractTermOffer = None
    asset: Optional[List[ContractTermAsset]] = None
    action: Optional[List[ContractTermAction]] = None
    group: Optional[List["ContractTerm"]] = None


@dataclass
class ContractSigner(BackboneElement):
    """ Contract Signatory.

    Parties with legal standing in the Contract, including the principal
    parties, the grantor(s) and grantee(s), which are any person or
    organization bound by the contract, and any ancillary parties, which
    facilitate the execution of the contract such as a notary or witness.
    """
    resource_type: ClassVar[str] = "ContractSigner"

    type: Coding = None
    party: FHIRReference = None
    signature: List[Signature] = field(default_factory=list)


@dataclass
class ContractFriendly(BackboneElement):
    """ Contract Friendly Language.

    The "patient friendly language" versionof the Contract in whole or in
    parts. "Patient friendly language" means the representation of the Contract
    and Contract Provisions in a manner that is readily accessible and
    understandable by a layperson in accordance with best practices for
    communication styles that ensure that those agreeing to or signing the
    Contract understand the roles, actions, obligations, responsibilities, and
    implication of the agreement.
    """
    resource_type: ClassVar[str] = "ContractFriendly"

    contentAttachment: Attachment = field(default=None, metadata=dict(one_of_many='content',))
    contentReference: FHIRReference = field(default=None, metadata=dict(one_of_many='content',))


@dataclass
class ContractLegal(BackboneElement):
    """ Contract Legal Language.

    List of Legal expressions or representations of this Contract.
    """
    resource_type: ClassVar[str] = "ContractLegal"

    contentAttachment: Attachment = field(default=None, metadata=dict(one_of_many='content',))
    contentReference: FHIRReference = field(default=None, metadata=dict(one_of_many='content',))


@dataclass
class ContractRule(BackboneElement):
    """ Computable Contract Language.

    List of Computable Policy Rule Language Representations of this Contract.
    """
    resource_type: ClassVar[str] = "ContractRule"

    contentAttachment: Attachment = field(default=None, metadata=dict(one_of_many='content',))
    contentReference: FHIRReference = field(default=None, metadata=dict(one_of_many='content',))


@dataclass
class Contract(DomainResource):
    """ Legal Agreement.

    Legally enforceable, formally recorded unilateral or bilateral directive
    i.e., a policy or agreement.
    """
    resource_type: ClassVar[str] = "Contract"

    identifier: Optional[List[Identifier]] = None
    url: Optional[str] = None
    version: Optional[str] = None
    status: Optional[str] = None
    legalState: Optional[CodeableConcept] = None
    instantiatesCanonical: Optional[FHIRReference] = None
    instantiatesUri: Optional[str] = None
    contentDerivative: Optional[CodeableConcept] = None
    issued: Optional[FHIRDate] = None
    applies: Optional[Period] = None
    expirationType: Optional[CodeableConcept] = None
    subject: Optional[List[FHIRReference]] = None
    authority: Optional[List[FHIRReference]] = None
    domain: Optional[List[FHIRReference]] = None
    site: Optional[List[FHIRReference]] = None
    name: Optional[str] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
    alias: Optional[List[str]] = None
    author: Optional[FHIRReference] = None
    scope: Optional[CodeableConcept] = None
    topicCodeableConcept: Optional[CodeableConcept] = field(default=None, metadata=dict(one_of_many='topic',))
    topicReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='topic',))
    type: Optional[CodeableConcept] = None
    subType: Optional[List[CodeableConcept]] = None
    contentDefinition: Optional[ContractContentDefinition] = None
    term: Optional[List[ContractTerm]] = None
    supportingInfo: Optional[List[FHIRReference]] = None
    relevantHistory: Optional[List[FHIRReference]] = None
    signer: Optional[List[ContractSigner]] = None
    friendly: Optional[List[ContractFriendly]] = None
    legal: Optional[List[ContractLegal]] = None
    rule: Optional[List[ContractRule]] = None
    legallyBindingAttachment: Optional[Attachment] = field(default=None, metadata=dict(one_of_many='legallyBinding',))
    legallyBindingReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='legallyBinding',))