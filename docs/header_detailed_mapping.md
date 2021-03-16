## OMH Header to FHIR Observation Detailed Mapping


The following Table provides the detailed mapping for the OMH Header to the OMH to FHIR Observation Profile TODO: add link to profile:


|Index|OMH  Header Element|FHIR Attribute|Derived Mapping|Comments|
|---|---|---|---|---|
|1|header-1.2.json|OMH to FHIR Observation Profile|||
|2.1|header.id|identifier[0].value|||1:1 mapping of  string|
|2.2|header.id|identifier[0].system|https://omh.org/shimmer/ids|fixed to 'https://omh.org/shimmer/ids'|
|3|header.creation_date_time|issued||1:1 mapping of  header.creation_date_time|
|4|header.schema_id|None|||
|5|header.schema_id.namespace|None|||
|6A.1|header.schema_id.name|category[0].coding[0].code|data_point_mapping_table|"Maps to column 'Observation.category.code'|
|6A.2|header.schema_id.name|category[0].coding[0].system|http://hl7.org/fhir/observation-category|"fixed to ""http://hl7.org/fhir/observation-category""|
|6B.1|header.schema_id.name|code.coding[0].code|data_point_mapping_table['Observation.code.code']|"Maps to column 'Observation.code.code'|
|6B.2||code.coding[0].system|data_point_mapping_table['Observation.code.system']|"Maps to column 'Observation.code.system'|
|6B.3||code.coding[0].display|data_point_mapping_table['Observation.code.display']|"Maps to column 'Observation.code.display'|
|7|header.schema_id.version|None|||
|8|header.acquisition_provenance|None|||
|9|header.acquisition_provenance.source_name|device.display|1:1 mapping of header.acquisition_provenance.source_name||
|10.1|header.acquisition_provenance.source_data_point_id|identifier[1].value||1:1 mapping of  header.acquisition_provenance.source_data_point_id|
|10.2||identifier[1].system|https://omh.org/source/ids|fixed to 'https://omh.org/source/ids'|
|11|header.acquisition_provenance.source_creation_date_time|None|||
|12|header.acquisition_provenance.last_modification_date_time|None|||
|13.1|header.acquisition_provenance.modality|device.extension[0].valueCode||1:1 mapping of header.acquisition_provenance.modality|
|13.2||device.extension[0].url|http://www.fhir.org/mfhir/StructureDefinition/extenion-modality|fixed to 'http://www.fhir.org/mfhir/StructureDefinition/extenion-modality'|
|14.1|header.user_id|subject.identifier.value||1:1 mapping of  string|
|14.2||subject.identifier.system|https://omh.org/shimmerM/patient_id|fixed to 'https://omh.org/shimmer/patient_id'|


Example Mapping:

The following OMH Header schema instance:

~~~
"header": {
  "id": "243c773b-8936-407e-9c23-270d0ea49cc4",
  "creation_date_time": "2015-09-10T12:43:39.138-06:00",
  "acquisition_provenance": {
    "source_name": "Jawbone UP API",
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

~~~
{
   "issued": "2015-09-10T12:43:39.138-06:00",
   "resourceType": "Observation",
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
      "display": "Jawbone UP API",
      "extension": [
         {
            "valueCode": "sensed",
            "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality"
         }
      ]
   },
   "identifier": [
      {
         "value": "243c773b-8936-407e-9c23-270d0ea49cc4",
         "system": "https://omh.org/shimmer/ids"
      }
   ],
   "meta": {
      "profile": [
         "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_profile_quantitative_observation"
      ]
   },
   "status": "unknown",
   "subject": {
      "identifier": {
         "value": "306a1202-410d-11e8-842f-0ed5f89f718b",
         "system": "https://omh.org/shimmer/patient_ids"
      }
   }
}
~~~
