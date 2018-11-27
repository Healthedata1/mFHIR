{% assign id = {{page.id}} %}
source file: source/pages/\_includes/{{id}}-intro.md

{{site.data.structuredefinitions.[id].description}}

### Scope and Usage

The OMH Heart Rate Quick Start mapping tables and formal FHIR Logical Models are presented in the section below.

### Quick Start Mapping Guide 

The following mapping tables and resource subtemplates are provided for mapping an OMH schema instance to a FHIR resource instance as described in the Quick Start mapping section.

|OMH element|FHIR element|
|---|---|
|OMH Heart Rate Schema|OMH to FHIR Observation Profile with Observation.code = LOINC 8867-4 (Heart rate)|
|body.effective_time_frame|None|
|body.effective_time_frame.time_interval|None|
|body.effective_time_frame.date_time|Observation.effectiveDateTime|
|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start|
|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end|
|body.heart_rate|Observation.valueQuantity.value (see the mapping tables below)|
|body.user_notes|Observation.comment|
|body.descriptive_statistic|Observation.component.code (see the mapping tables below)|
|body.temporal_relationship_to_physical_activity|Observation.component.valueCodeableConcept.code (see the mapping tables below)|
|body.temporal_relationship_to_sleep|Observation.component.valueCodeableConcept.code (see the mapping tables below)|
{: .grid}

**Heart Rate Descriptive Statistic Mapping Tables**

This table maps the heart rate descriptive statistic to the OMH to FHIR additional Observation codings ( code system `http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes`). If the schema element is absent, the default measure is count and there is no additional coding.

|body.descriptive_statistic|Observation.coding.code|Observation.coding.display|
|---|---|---|
|Null| Null| Null|
|average|average-heart-rate|Average Heart Rate|
|maximum|maximum-heart-rate|Maximum Heart Rate|
|minimum|minimum-heart-rate|Minimum Heart Rate|
|count|count-heart-rate|Count Heart Rate|
|totalcount|totalcount-heart-rate|Totalcount Heart Rate|
|median|median-heart-rate|Median Heart Rate|
|std-dev|std-dev-heart-rate|Std Dev Heart Rate|
|sum|sum-heart-rate|Sum Heart Rate|
|variance|variance-heart-rate|Variance Heart Rate|
|20-percent|20-percent-heart-rate|20 Percent Heart Rate|
|80-percent|80-percent-heart-rate|80 Percent Heart Rate|
|4-lower|4-lower-heart-rate|4 Lower Heart Rate|
|4-upper|4-upper-heart-rate|4 Upper Heart Rate|
|4-dev|4-dev-heart-rate|4 Dev Heart Rate|
|5-1|5-1-heart-rate|5 1 Heart Rate|
|5-2|5-2-heart-rate|5 2 Heart Rate|
|5-3|5-3-heart-rate|5 3 Heart Rate|
|5-4|5-4-heart-rate|5 4 Heart Rate|
|skew|skew-heart-rate|Skew Heart Rate|
|kurtosis|kurtosis-heart-rate|Kurtosis Heart Rate|
|regression|regression-heart-rate|Regression Heart Rate|
{: .grid}

**Unit Mapping**

This table maps the heart rate to the OMH to FHIR Observation valueQuantity unit and UCUM code.

|Observation.valueQuantity.value|Observation.valueQuantity.unit|Observation.valueQuantity.code|
|---|---|---|
|body.heart_rate|beats/min|/min|
{: .grid}

**Temporal Relationship Mapping**

This table maps the heart rate Temporal Relationship To Physical Activity and Sleep to the OMH to FHIR Observation.component elements. If the schema element is absent, there is no Observation.component element.

|Observation.component element|Temporal Relationship To Physical Activity|Temporal Relationship To Sleep|
|---|---|---|
|Observation.component.code.system|http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes|http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes|
|Observation.component.code.code|relative-to-activity|relative-to-sleep|
|Observation.component.code.display|OMH to FHIR Temporal Relationship To Physical Activity|OMH to FHIR Temporal Relationship To Sleep|
|Observation.component.valueCodeableConcept.system|http://snomed.info/sct|http://snomed.info/sct|
|Observation.component.valueCodeableConcept.code|`body.temporal_relationship_to_physical_activity`|`body.temporal_relationship_to_sleep`|
{: .grid}

<br />
#### Example OMH to FHIR heart_rate datapoint Observation

~~~
{
   "code": {
      "coding": [
         {
            "code": "8867_4",
            "display": "Heart rate",
            "system": "http://loinc.org"
         }
      ]
   },
   "identifier": [
      {
         "value": "87ca4312-fbe3-4b24-bab4-17d47ba54e2a",
         "system": "https://omh.org/shimmer/ids"
      }
   ],
   "meta": {
      "profile": [
         "http://www.fhir.org/mfhir/StructureDefinition/omh-to-fhir-observation"
      ]
   },
   "comment": "I felt quite dizzy",
   "subject": {
      "identifier": {
         "value": "some-user",
         "system": "https://omh.org/shimmer/patient_ids"
      }
   },
   "resourceType": "Observation",
   "effectiveDateTime": "2013-02-05T07:25:00Z",
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
   "device": {
      "extension": [
         {
            "url": "http://www.fhir.org/mfhir/StructureDefinition/observationDeviceModality",
            "valueCode": "sensed"
         }
      ],
      "display": "generator"
   },
   "component": [
      {
         "code": {
            "coding": [
               {
                  "code": "relative-to-activity",
                  "display": "OMH to FHIR Temporal Relationship To Physical Activity",
                  "system": "http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes"
               }
            ]
         },
         "valueCodeableConcept": {
            "coding": [
               {
                  "code": "at rest",
                  "system": "http://snomed.info/sct"
               }
            ]
         }
      }
   ],
   "issued": "2014-01-03T09:14:41Z",
   "status": "unknown",
   "valueQuantity": {
      "code": "/min",
      "value": 50,
      "unit": "beats/min",
      "system": "http://unitsofmeasure.org"
   }
}
~~~
