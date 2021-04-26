#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DeviceDefinition) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .prodcharacteristic import ProdCharacteristic
from .productshelflife import ProductShelfLife
from .quantity import Quantity


@dataclass
class DeviceDefinitionUdiDeviceIdentifier(BackboneElement):
    """ Unique Device Identifier (UDI) Barcode string.

    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionUdiDeviceIdentifier"

    deviceIdentifier: str = None
    issuer: str = None
    jurisdiction: str = None


@dataclass
class DeviceDefinitionDeviceName(BackboneElement):
    """ A name given to the device to identify it.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionDeviceName"

    name: str = None
    type: str = None


@dataclass
class DeviceDefinitionSpecialization(BackboneElement):
    """ The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionSpecialization"

    systemType: str = None
    version: Optional[str] = None


@dataclass
class DeviceDefinitionCapability(BackboneElement):
    """ Device capabilities.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionCapability"

    type: CodeableConcept = None
    description: Optional[List[CodeableConcept]] = None


@dataclass
class DeviceDefinitionProperty(BackboneElement):
    """ The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionProperty"

    type: CodeableConcept = None
    valueQuantity: Optional[List[Quantity]] = None
    valueCode: Optional[List[CodeableConcept]] = None


@dataclass
class DeviceDefinitionMaterial(BackboneElement):
    """ A substance used to create the material(s) of which the device is made.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionMaterial"

    substance: CodeableConcept = None
    alternate: Optional[bool] = None
    allergenicIndicator: Optional[bool] = None


@dataclass
class DeviceDefinition(DomainResource):
    """ An instance of a medical-related component of a medical device.

    The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """
    resource_type: ClassVar[str] = "DeviceDefinition"

    identifier: Optional[List[Identifier]] = None
    udiDeviceIdentifier: Optional[List[DeviceDefinitionUdiDeviceIdentifier]] = None
    manufacturerString: Optional[str] = field(default=None, metadata=dict(one_of_many='manufacturer',))
    manufacturerReference: Optional[FHIRReference] = field(default=None, metadata=dict(one_of_many='manufacturer',))
    deviceName: Optional[List[DeviceDefinitionDeviceName]] = None
    modelNumber: Optional[str] = None
    type: Optional[CodeableConcept] = None
    specialization: Optional[List[DeviceDefinitionSpecialization]] = None
    version: Optional[List[str]] = None
    safety: Optional[List[CodeableConcept]] = None
    shelfLifeStorage: Optional[List[ProductShelfLife]] = None
    physicalCharacteristics: Optional[ProdCharacteristic] = None
    languageCode: Optional[List[CodeableConcept]] = None
    capability: Optional[List[DeviceDefinitionCapability]] = None
    property: Optional[List[DeviceDefinitionProperty]] = None
    owner: Optional[FHIRReference] = None
    contact: Optional[List[ContactPoint]] = None
    url: Optional[str] = None
    onlineInformation: Optional[str] = None
    note: Optional[List[Annotation]] = None
    quantity: Optional[Quantity] = None
    parentDevice: Optional[FHIRReference] = None
    material: Optional[List[DeviceDefinitionMaterial]] = None