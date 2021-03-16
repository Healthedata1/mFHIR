---
tags: omh2fhir
---

{%hackmd 2yYAoTGSSpiWVb7EWu6v0w %}

# OMH Header to FHIR Observation Detailed Mapping

The following Table provides the detailed mapping for the OMH Header to the OMH to FHIR Observation Profile TODO: add link to profile:


|Index|OMH  Header Element|FHIR Attribute|Mapping Instructions|
|---|---|---|---|
|1|header-1.2.json|OMH to FHIR Observation Profile||
|2.1|header.id||concatenation of  "urn:uuid:" + header.id|
|2.2|header.id|identifier[0].system|fixed to "urn:ietf:rfc:3986"|
|3|header.creation_date_time|issued|= header.creation_date_time|
|4|header.schema_id|None||
|5|header.schema_id.namespace|None||
|6A.1|header.schema_id.name|category[0].coding[0].code|Map header.schema_id.name to column "Observation.category.code" using  the [OMH DataPoint Element to FHIR Element Mapping Table](/d4c66YHxQxi9Xqv_0qBpJA)|
|6A.2|header.schema_id.name|category[0].coding[0].system|fixed to "http://hl7.org/fhir/observation-category"|
|6B.1|header.schema_id.name|code.coding[0].code|Map header.schema_id.name to column "Observation.code.code" using  the [data_point_mapping_table](#)|
|6B.2|header.schema_id.name|code.coding[0].system|Map header.schema_id.name to column "Observation.code.system" using  the [data_point_mapping_table](#)|
|6B.3|header.schema_id.name|code.coding[0].display|Map header.schema_id.name to column "Observation.code.display" using  the [data_point_mapping_table](#)|
|7|header.schema_id.version|None||
|8|header.acquisition_provenance|None||
|9|header.acquisition_provenance.source_name|device.display|= header.acquisition_provenance.source_name|
|10.1|header.acquisition_provenance.source_data_point_id|identifier[1].value|concatenation of  "urn:uuid:" + header.acquisition_provenance.source_data_point_id|
|10.2|header.acquisition_provenance.source_data_point_id|identifier[1].system|fixed to "urn:ietf:rfc:3986"|
|11|header.acquisition_provenance.source_creation_date_time|None||
|12|header.acquisition_provenance.modication_date_time|None||
|13.1|header.acquisition_provenance.modality|device.extension[0].valueCode|= header.acquisition_provenance.modality|
|13.2|header.acquisition_provenance.modality|device.extension[0].url|fixed to "http://www.fhir.org/mfhir/StructureDefinition/extenion-modality"|
|14.1|header.user_id|subject.identifier.value|concatenation of  "urn:uuid:" + header.user_id|
|14.2|header.user_id|subject.identifier.system|fixed to "urn:ietf:rfc:3986"|


## Example:

### OMH Header schema instance:

~~~json
"header": {
  "id": "243c773b-8936-407e-9c23-270d0ea49cc4",
  "creation_date_time": "2015-09-10T12:43:39.138-06:00",
  "acquisition_provenance": {
    "source_name": "Acme BG API",
    "modality": "sensed",
    "source_updated_date_time": "2015-09-10T18:43:39Z"
  },
  "schema_id": {
    "namespace": "omh",
    "name": "blood_glucose",
    "version": "1.0"
  },
  "user_id": "306a1202-410d-11e8-842f-0ed5f89f718b"
}
~~~

Maps to the FHIR Observation resource:

~~~json
{
  
  "category": [
    {
      "coding": [
        {
          "code": "laboratory",
          "display": "Laboratory",
          "system": "http://hl7.org/fhir/observation-category"
        }
      ]
    }
  ],
  "code": {
    "coding": [
      {
        "code": "2339-0",
        "display": "Glucose Mass/volume in Blood",
        "system": "http://loinc.org"
      }
    ]
  },
  "device": {
    "display": "Acme BG API",
    "extension": [
      {
        "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
        "valueCode": "sensed"
      }
    ]
  },
  "identifier": [
    {
      "system": "urn:ietf:rfc:3986",
      "value": "urn:uuid:243c773b-8936-407e-9c23-270d0ea49cc4"
    }
  ],
  "issued": "2015-09-10T12:43:39.138-06:00",
  "meta": {
    "profile": [
      "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_profile_quantitative_observation"
    ]
  },
  "resourceType": "Observation",
  "status": "unknown",
  "subject": {
    "identifier": {
      "system": "urn:ietf:rfc:3986",
      "value": "urn:uuid:306a1202-410d-11e8-842f-0ed5f89f718b"
    }
  }
}
~~~


---
- [name=erichaas]
- [time=Sat, May 30, 2020 1:02 PM]
