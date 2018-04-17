
PHD IG notes

how to know who is who?

For protection of Personal Health Information (PHI) the Continua profile allows PHGs to be supplied with opaque and unique 'key' by out-of-band means that only the health care provider can link to a patient. Using this approach PHI is never exchanged on the wire and furthermore, does not need to be present on the PHD or PHG.

Useful preconditions:

- Continua PHDs are consumer devices
- Low cost
- Often battery powered and portable
- Typically do not support external time synchronization except from the PHG or patient
- Continua PHGs are consumer devices or applications running on consumer devices
- Are expected to work with most if not all Continua PHDs
- Low cost
- Maybe a dedicated set top box, mobile phone, or personal computer
- Have more computational resources than PHDs
- Are capable of being externally synchronized to UTC and local offset
- In many cases will need to work with PHDs without user intervention
- Health Care Providers may be monitoring thousands of remotely located patients
- Servicing and support of the remote stations needs to be minimized
- To the extent possible Continua PHGs should work with future Continua PHDs
- Patients may have more than one PHD and may change PHDs
- Data will be transferred over the public network
- Patients may be paying for data rates

This is confusing
Based upon these assumptions it is advantageous to design an infrastructure which needs as little maintenance as possible and a **mapping algorithm which handles as many types of PHD specializations** as possible including specializations developed in the future.

Two classes of 11073 20601

1. Medical Device System (MDS) object:
   - describes the device features and properties.
   - mapped to DeviceComponent????
1. Metric object:
   - model measurements
     - The ASN.1 BITs measurement??
       -  Continua has created a code system for this purpose allowing one to map a BITs value to a set of valueCodeableConcepts. The code system has a code for each possible setting, so a 16/32-bit ASN.1 BITs value can result in up to 16/32 codes. Since a BITs value can contain multiple settings, each setting is mapped to an Observation.component.
   - mapped to Observation



a PHD has one hierarchy; all metric information is sourced by a single MDS. The 'medical components' and the 'controller component' of the PoCD model are merged into a single static unit and thus have the same production specification, manufacturer information, and system identifier. The static nature of the PHD means that the lastSystemChange element is never populated.  cf POCD

PHD profile has decided to use the DeviceComponent.productionSpecification element to report both the production specification and manufacturer information to reduce bandwidth!!!!

In most cases a PHD supports only a single specialization such as a Blood Pressure monitor and only one DeviceComponent is needed and that specialization is recorded in this element. **Since there is no way to indicate additional supported specialziations with this element (it has cardinality 1..1), additional child DeviceComponents are needed when multiple specializations and/or sub-profiles are present.

The value entered in this element comes from the System-Type-Spec-List attribute which is unique to the 11073 20601 specification; 11073-10201 does not have such an attribute. If there is more than one specialization, the special HYDRA specialization value is entered here and child DeviceComponent resources are used to map the specializations. If there is only a single specialization but one or more sub profiles., the specialization is entered here and the sub profiles are handled in child DeviceComponents.

Note that sub-profiles are a packaging of objects within a specialization that serve a special use case. For example, the Cardiovascular specialization has numerous objects that can represent all kinds of physical activities from treadmills to skiing. One sub-profile is a minimum set of objects needed to describe a step counter.**

productionSpecification: The production specification such as component revision, serial number, etc. For the 11073 20601 Personal Health Device, the production specification entries come from the Production-Specification, System-Model, and Reg-Cert-Data-List attributes. There will be one productionSpecification entry for each item to be reported.  these elements overlap the inline elements in device.  What exactly is unique/not already present in Device?

e.g this list here:

- Type of Device	DeviceComponent.type.coding.code="MDC 32-bit code for device type"
- Manufacturer name	if DeviceComponent.productionSpecification.specType.coding.code="531970"
then DeviceComponent.productionSpecification.productionSpec="manufacturer name"
- Model number	if DeviceComponent.productionSpecification.specType.coding.code="531969"
then DeviceComponent.productionSpecification.productionSpec="model number"
- serial number	if DeviceComponent.productionSpecification.specType.coding.code="531972"
then DeviceComponent.productionSpecification.productionSpec="serial number"
- system identifier	if DeviceComponent.identifier.system="urn:oid:1.2.840.10004.1.1.1.0.0.1.0.0.1.2680"
then DeviceComponent.identifier.value="system id as 8 2-digit HEX values separated by dashes"
- time synchronization	if DeviceComponent.property.type.coding.code="68220"
then DeviceComponent.property.valueCodeableConcept.coding.code="code for time synchronization"

example here:  http://hl7.org/fhir/uv/phd/2018Jan/PhdParentDeviceComponentProfile.html#PhdParentDeviceComponentJSONExample

11073 subplot  see bold

11073 10101 codes have been defined for the Production-Specification and System-Model sub entries for use in V2 messaging. Though FHIR has provided its own set of codes based upon the names of the 11073-* Production-Specification.spec-type entry, the 11073-10101 codes are used since they are ubiquitous in these PHD-related profiles and **it helps accelerate the acceptance of the MDC coding system in HL7.**


???FHIR requires this element (Coding) to be present IF the production specification being reported is included in the DeviceSpecificationSpecType value set. Currently that is all the possible entries defined in the IEEE 11073 ProductionSpecification attribute. These codes and entries are as follows: Code Description unspecified Unspecified Production Specification serial-number Serial Number part-number Part Number hardware-revision Hardware Revision software-revision Software Revision firmware-revision Firmware Revision protocol-revision Protocol Revision gmdn Global Medical Device Nomencalture


?? using the proposed mapping is both non-extensible and complex as it reverses the 11073-10201 multiple VMDs to 11073-20601 System-Type-Spec-List.   Will enter a comment to use a simple extension and report the extra specializations in the extension as is done in PCD-01. If an extension is used, there will be no need for a Child Device Component profile.
