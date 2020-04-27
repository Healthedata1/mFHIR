## OMH HeartRate DataPoint to FHIR Observation Detailed Mapping


The following Table provides the detailed mapping for the OMH HeartRate DataPoint to the OMH to FHIR Observation Profile TODO: add link to profile:

Index|OMH  Heart Rate|HL7 FHIR Observation|Derived Mapping|Comments
---|---|---|---|---|
1|heart-rate-1.1.json|OMH to FHIR Observation Profile||
7|body.heart_rate|Observation.valueQuantity||
2|body.effective_time_frame|None||
3|body.effective_time_frame.time_interval|None||
4|body.effective_time_frame.date_time|Observation.effectiveDateTime||1:1 mapping of  body.effective_time_frame.date_time
5|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start||1:1 mapping of  body.effective_time_frame.time_interval.start_date_time
6|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end||1:1 mapping of  body.effective_time_frame.time_interval.end_date_time
8|body.user_notes|Observation.comment||1:1 mapping of  body.user_notes
9|body.descriptive_statistic|Observation.coding||Map  descriptive statistic to the OMH to FHIR additional Observation codings ( code system http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes).
10|body.temporal_relationship_to_physical_activity|Observation.component|component_mapping_table|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list
11|body.temporal_relationship_to_sleep|Observation.component|component_mapping_table|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list

Example Mapping:

The following OMH HeartRate schema instance:

```
{
  "body": {
 "effective_time_frame": {
    "date_time": "2013-02-05T07:25:00Z"
 },
 "blood_glucose": {
    "value": 95,
    "unit": "mg/dL"
 }
}
}
```

Maps to this fragment FHIR Observation

~~~
...
"effectiveDateTime": "2013-02-05T07:25:00Z",
"valueQuantity": {
   "value": 95,
   "code": "mg/dL",
   "unit": "mg/dL",
   "system": "http://unitsofmeasure.org"
...
~~~

to make this this FHIR Observation:

~~~
{
   "issued": "2015-09-10T12:43:39.138-06:00",
   "effectiveDateTime": "2013-02-05T07:25:00Z",
   "resourceType": "Observation",
   "valueQuantity": {
      "value": 95,
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
