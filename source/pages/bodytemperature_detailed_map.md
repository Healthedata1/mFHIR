## OMH Body Temperature DataPoint to FHIR Observation Detailed Mapping

The following Table provides the detailed mapping for the OMH Body Temperature DataPoint to the OMH to FHIR Observation Profile TODO: add link to profile:

Index|OMH Body Temperature Element|FHIR Attribute|Derived Mapping|Comments
---|---|---|---|---
1|body-temperature-2.0.json|OMH to FHIR Observation Profile||
2.1|body_temperature|Observation.valueQuantity||see valueQuantity elements below
2.2|body_temperature.value|Observation.valueQuantity.value||1:1 mapping of  number
2.3|body_temperature.unit|Observation.valueQuantity.unit||1:1 mapping of  string
2.4||valueQuantity.system|http://unitsofmeasure.org|fixed to 'http://unitsofmeasure.org'
2.5||valueQuantity.code|OMH_FHIR_Concept_Maps['body.body_temperature.unit']Concept Mapping
3|body.effective_time_frame|Observation.effective[x]||Mappping depends on type- see below
5|body.effective_time_frame.date_time|Observation.effectiveDateTime||1:1 mapping of  body.effective_time_frame.date_time
4|body.effective_time_frame.time_interval|Observation.effectivePeriod||see effectivePeriod.elements below
8.1|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start||1:1 mapping of  body.effective_time_frame.time_interval.start_date_time
8.0|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end||1:1 mapping of  body.effective_time_frame.time_interval.end_date_time
8.1|measurement_location|Observation.bodySite||See bodySite elements below
8.2||Observation.bodySIte.coding[0].system|OMH_FHIR_Concept_Maps['body.X'][0]for row = body.X = OMH to FHIR Concept Mapping Table  maps to column 'Concept Code System'
8.3||Observation.bodySIte.coding[0].code|OMH_FHIR_Concept_Maps['body.X'][1]for row = body.X = OMH to FHIR Concept Mapping Table  maps to column 'Concept Code'
8.4||Observation.bodySIte.coding[0].display|OMH_FHIR_Concept_Maps['body.X'][2]for row = body.X = OMH to FHIR Concept Mapping Table  maps to column 'Concept Code Display'
9|body.descriptive_statistic|Observation.coding[1]||Map  descriptive statistic to the OMH to FHIR additional Observation codings ( code system http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes).
10|body.temporal_relationship_to_physical_activity|Observation.component|component_mapping_table|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list
11|body.temporal_relationship_to_sleep|Observation.component|component_mapping_table|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list


Example Mapping:

The following OMH Body Temperature schema instance:

```
{
  "body": {
   "effective_time_frame": {
      "time_interval": {
         "end_date_time": "2015-02-06T06:00:00Z",
         "start_date_time": "2015-02-05T06:00:00Z"
      }
   },
   "descriptive_statistic": "maximum",
   "body_temperature": {
      "value": 96.5,
      "unit": "F"
   },
   "measurement_location": "oral"
  }
}
```

Maps to this FHIR Observation fragment

~~~
...
"code": {
   "coding": [
      {
         "code": "body-temperature-maximum",
         "display": "Body Temperature Maximum",
         "system": "http://hl7.org/fhir/omh_fhir_observation_codes"
      }
   ]
},
{
   "effectivePeriod": {
      "end": "2015-02-06T06:00:00Z",
      "start": "2015-02-05T06:00:00Z"
   },
   "valueQuantity": {
      "value": 96.5,
      "code": "[degF]",
      "unit": "F",
      "system": "http://unitsofmeasure.org"
   },
   "bodySite": {
      "coding": [
         {
            "code": "oral",
            "system": "http://www.fhir.org/guides/mfhir/CodeSystem/intervention-administration-route"
         }
      ],
      "text": "oral"
   },
...
~~~

to make this this FHIR Observation when combine with the OMH Header

~~~
{
   "meta": {
      "profile": [
         "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_profile_quantitative_observation"
      ]
   },
   "bodySite": {
      "coding": [
         {
            "code": "oral",
            "system": "http://www.fhir.org/guides/mfhir/CodeSystem/intervention-administration-route"
         }
      ],
      "text": "oral"
   },
   "category": [
      {
         "coding": [
            {
               "code": "vital-signs",
               "display": "Vital Signs",
               "system": "http://hl7.org/fhir/observation-category"
            }
         ]
      }
   ],
   "code": {
      "coding": [
         {
            "code": "8310-5",
            "display": "Body temperature",
            "system": "http://loinc.org"
         },
         {
            "code": "body-temperature-maximum",
            "display": "Body Temperature-Maximum",
            "system": "http://hl7.org/fhir/omh_fhir_observation_codes"
         }
      ]
   },
   "device": {
      "extension": [
         {
            "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
            "valueCode": "sensed"
         }
      ],
      "display": "Jawbone UP API"
   },
   "effectivePeriod": {
      "end": "2015-02-06T06:00:00Z",
      "start": "2015-02-05T06:00:00Z"
   },
   "identifier": [
      {
         "system": "https://omh.org/shimmer/ids",
         "value": "243c773b-8936-407e-9c23-270d0ea49cc4"
      }
   ],
   "issued": "2015-09-10T12:43:39.138-06:00",
   "status": "unknown",
   "subject": {
      "identifier": {
         "system": "https://omh.org/shimmer/patient_ids",
         "value": "306a1202-410d-11e8-842f-0ed5f89f718b"
      }
   },
   "valueQuantity": {
      "code": "[degF]",
      "system": "http://unitsofmeasure.org",
      "unit": "F",
      "value": 96.5
   },
   "resourceType": "Observation"
}
~~~
