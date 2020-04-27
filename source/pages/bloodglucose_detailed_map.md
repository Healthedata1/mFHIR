## OMH Blood Glucoe DataPoint to FHIR Observation Detailed Mapping


The following Table provides the detailed mapping for the OMH Blood Glucoe DataPoint to the OMH to FHIR Observation Profile TODO: add link to profile:

Index|OMH Blood Glucose Element|FHIR Attribute|Derived Mapping|Comments
---|---|---|---|---
1|blood-glucose-2.0.json|OMH to FHIR Observation Profile||
2.1|body.blood_glucose|Observation.valueQuantity||see valueQuantity elements below
2.2|body.blood_glucose.value|Observation.valueQuantity.value||1:1 mapping of  number
2.3|body.blood_glucose.unit|Observation.valueQuantity.unit||1:1 mapping of  string
2.4||valueQuantity.system|http://unitsofmeasure.org|fixed to 'http://unitsofmeasure.org'
2.5||valueQuantity.code|OMH_FHIR_Concept_Maps['body.heart_rate.unit']|Concept Mapping
3|body.effective_time_frame|Observation.effective[x]||Mappping depends on type- see below
5|body.effective_time_frame.date_time|Observation.effectiveDateTime||1:1 mapping of  body.effective_time_frame.date_time
4|body.effective_time_frame.time_interval|Observation.effectivePeriod||see effectivePeriod.elements below
6|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start||1:1 mapping of  body.effective_time_frame.time_interval.start_date_time
7|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end||1:1 mapping of  body.effective_time_frame.time_interval.end_date_time
8|body.user_notes|Observation.note[0].text||1:1 mapping of  body.user_notes, optionally can add author and time to the FHIR Annotation datatype
9.1|body.specimen_source|Observation.extension||extension url = 'http://www.fhir.org/mfhir/StructureDefinition/extension-specimenCode'
9.2||Observation.extension[0].url|ttp://www.fhir.org/mfhir/StructureDefinition/extension-specimenCode|fixed to 'ttp://www.fhir.org/mfhir/StructureDefinition/extension-specimenCode'
9.3||Observation.extension[0].valueCodeableConcept||
9.4||Observation.extension[0].valueCodeableConcept.coding[0].system|OMH_FHIR_Concept_Maps['body.X'][0]|for row = body.X = OMH to FHIR Concept Mapping Table  maps to column 'Concept Code System'
9.5||Observation.extension[0].valueCodeableConcept.coding[0].code|OMH_FHIR_Concept_Maps['body.X'][1]|for row = body.X = OMH to FHIR Concept Mapping Table  maps to column 'Concept Code'
9.6||Observation.extension[0].valueCodeableConcept.coding[0].display|OMH_FHIR_Concept_Maps['body.X'][2]|for row = body.X = OMH to FHIR Concept Mapping Table  maps to column 'Concept Code Display'
10|body.descriptive_statistic|Observation.coding[1]||Map  descriptive statistic to the OMH to FHIR additional Observation codings ( code system http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes).
11|body.temporal_relationship_to_physical_activity|Observation.component|component_mapping_table|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list
12|body.temporal_relationship_to_sleep|Observation.component|component_mapping_table|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list
13|temporal_relationship_to_meal|Observation.component|component_mapping_table|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list

Example Mapping:

The following OMH HeartRate schema instance:

```
{
  "body": {
   "descriptive_statistic": "minimum",
   "effective_time_frame": {
      "time_interval": {
         "end_date_time": "2013-06-05T07:25:00Z",
         "start_date_time": "2013-02-05T07:25:00Z"
      }
   },
   "blood_glucose": {
      "value": 120,
      "unit": "mg/dL"
   }
}
```

Maps to this FHIR Observation fragment

~~~
...
"code": {
   "coding": [
      {
         "code": "blood-glucose-minimum",
         "display": "Blood Glucose Minimum",
         "system": "http://hl7.org/fhir/omh_fhir_observation_codes"
      }
   ]
},
{
   "effectivePeriod": {
      "end": "2013-06-05T07:25:00Z",
      "start": "2013-02-05T07:25:00Z"
   },
   "valueQuantity": {
      "value": 120,
      "code": "mg/dL",
      "unit": "mg/dL",
      "system": "http://unitsofmeasure.org"
   }
...
~~~

to make this this FHIR Observation when combine with the OMH Header

~~~
{
   "effectivePeriod": {
      "end": "2013-06-05T07:25:00Z",
      "start": "2013-02-05T07:25:00Z"
   },
   "issued": "2015-09-10T12:43:39.138-06:00",
   "resourceType": "Observation",
   "valueQuantity": {
      "value": 120,
      "code": "mg/dL",
      "unit": "mg/dL",
      "system": "http://unitsofmeasure.org"
   },
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
         },
         {
            "code": "blood-glucose-minimum",
            "display": "Blood Glucose Minimum",
            "system": "http://hl7.org/fhir/omh_fhir_observation_codes"
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
