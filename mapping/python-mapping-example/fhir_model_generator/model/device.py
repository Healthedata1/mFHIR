#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Device) on 2020-02-10.
#  2020, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity


@dataclass
class DeviceUdiCarrier(BackboneElement):
    """ Unique Device Identifier (UDI) Barcode string.

    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """
    resource_type: ClassVar[str] = "DeviceUdiCarrier"

    deviceIdentifier: Optional[str] = None
    issuer: Optional[str] = None
    jurisdiction: Optional[str] = None
    carrierAIDC: Optional[str] = None
    carrierHRF: Optional[str] = None
    entryType: Optional[str] = None


@dataclass
class DeviceDeviceName(BackboneElement):
    """ The name of the device as given by the manufacturer.

    This represents the manufacturer's name of the device as provided by the
    device, from a UDI label, or by a person describing the Device.  This
    typically would be used when a person provides the name(s) or when the
    device represents one of the names available from DeviceDefinition.
    """
    resource_type: ClassVar[str] = "DeviceDeviceName"

    name: str = None
    type: str = None


@dataclass
class DeviceSpecialization(BackboneElement):
    """ The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """
    resource_type: ClassVar[str] = "DeviceSpecialization"

    systemType: CodeableConcept = None
    version: Optional[str] = None


@dataclass
class DeviceVersion(BackboneElement):
    """ The actual design of the device or software version running on the device.
    """
    resource_type: ClassVar[str] = "DeviceVersion"

    type: Optional[CodeableConcept] = None
    component: Optional[Identifier] = None
    value: str = None


@dataclass
class DeviceProperty(BackboneElement):
    """ The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """
    resource_type: ClassVar[str] = "DeviceProperty"

    type: CodeableConcept = None
    valueQuantity: Optional[List[Quantity]] = None
    valueCode: Optional[List[CodeableConcept]] = None


@dataclass
class Device(DomainResource):
    """ Item used in healthcare.

    A type of a manufactured item that is used in the provision of healthcare
    without being substantially changed through that activity. The device may
    be a medical or non-medical device.
    """
    resource_type: ClassVar[str] = "Device"

    identifier: Optional[List[Identifier]] = None
    definition: Optional[FHIRReference] = None
    udiCarrier: Optional[List[DeviceUdiCarrier]] = None
    status: Optional[str] = None
    statusReason: Optional[List[CodeableConcept]] = None
    distinctIdentifier: Optional[str] = None
    manufacturer: Optional[str] = None
    manufactureDate: Optional[FHIRDate] = None
    expirationDate: Optional[FHIRDate] = None
    lotNumber: Optional[str] = None
    serialNumber: Optional[str] = None
    deviceName: Optional[List[DeviceDeviceName]] = None
    modelNumber: Optional[str] = None
    partNumber: Optional[str] = None
    type: Optional[CodeableConcept] = None
    specialization: Optional[List[DeviceSpecialization]] = None
    version: Optional[List[DeviceVersion]] = None
    property: Optional[List[DeviceProperty]] = None
    patient: Optional[FHIRReference] = None
    owner: Optional[FHIRReference] = None
    contact: Optional[List[ContactPoint]] = None
    location: Optional[FHIRReference] = None
    url: Optional[str] = None
    note: Optional[List[Annotation]] = None
    safety: Optional[List[CodeableConcept]] = None
    parent: Optional[FHIRReference] = None