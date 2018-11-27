{% assign id = {{page.id}} %}
source file: source/pages/\_includes/{{id}}-intro.md

{{site.data.structuredefinitions.[id].description}}

#### Scope and Usage

The OMH Step Count schema is represented as a formal FHIR Logical Model in the section below in order to facilitate model to model mappings.  However, the following mapping tables and resource subtemplates are provided for mapping an OMH schema instance to a FHIR resource instance using these templates along with the header templates.

**OMH Step Count to FHIR Observation Resource mappings**

|OMH element|FHIR element|
|---|---|
|OMH Step Count Schema|OMH to FHIR Observation Profile with Observation.code = LOINC 55423-8 (Number of steps in unspecified time Pedometer)|
|body.effective_time_frame|None|
|body.effective_time_frame.time_interval|None|
|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start|
|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end|
|body.step_count|Observation.valueQuantity.value|
|body.descriptive_statistic|Observation.coding (see the mapping tables below)|
|body.descriptive_statistic_denominator|Observation.valueQuantity (see the mapping tables below)|
{: .grid}

**Step Count Descriptive Statistic Mapping Tables**

This table maps the step count descriptive statistic to the OMH to FHIR additional Observation codings ( code system `http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes`). This is a compositional code system derived by concatenatng of the datapoint schema name with the descriptive statistic code in "spinal case"  ( e.g  `step-count-maximum`). If descriptive statistic is absent, the default measure is count and there is no additional coding.

|body.descriptive_statistic|Observation.coding.code|Observation.coding.display|
|---|---|---|
|Null| Null| Null|
|average|average-step-count|Average Step Count|
|maximum|maximum-step-count|Maximum Step Count|
|minimum|minimum-step-count|Minimum Step Count|
|count|count-step-count|Count Step Count|
|totalcount|totalcount-step-count|Totalcount Step Count|
|median|median-step-count|Median Step Count|
|std-dev|std-dev-step-count|Std Dev Step Count|
|sum|sum-step-count|Sum Step Count|
|variance|variance-step-count|Variance Step Count|
|20-percent|20-percent-step-count|20 Percent Step Count|
|80-percent|80-percent-step-count|80 Percent Step Count|
|4-lower|4-lower-step-count|4 Lower Step Count|
|4-upper|4-upper-step-count|4 Upper Step Count|
|4-dev|4-dev-step-count|4 Dev Step Count|
|5-1|5-1-step-count|5 1 Step Count|
|5-2|5-2-step-count|5 2 Step Count|
|5-3|5-3-step-count|5 3 Step Count|
|5-4|5-4-step-count|5 4 Step Count|
|skew|skew-step-count|Skew Step Count|
|kurtosis|kurtosis-step-count|Kurtosis Step Count|
|regression|regression-step-count|Regression Step Count|
{: .grid}

This table maps the step count descriptive statistic denominator to the OMH to FHIR Observation valueQuantity unit and UCUM code. If no descriptive statistic is absent, the default unit is steps ({steps}).

|body.descriptive_statistic_denominator|Observation.valueQuantity.unit|Observation.valueQuantity.code|
|---|---|---|
|Null|steps|{steps}|
|d|steps/day|{steps}/d|
|w|steps/week|{steps}/wk|
|m|steps/month|{steps}/mo|
|episode|steps/episode|{steps}/{episode}|
|session|steps/session|{steps}/{session}|
{: .grid}

#### Example OMH to FHIR step_count datapoint Observation

~~~
{
   "category": [
      {
         "coding": [
            {
               "system": "http://hl7.org/fhir/observation-category",
               "code": "physical-activity",
               "display": "Physical Activity"
            }
         ]
      }
   ],
   "issued": "2015-09-10T12:43:39.138-06:00",
   "resourceType": "Observation",
   "status": "unknown",
   "valueQuantity": {
      "system": "http://unitsofmeasure.org",
      "code": "{steps}",
      "value": 6000,
      "unit": "steps"
   },
   "subject": {
      "identifier": {
         "system": "https://omh.org/shimmer/patient_ids",
         "value": "306a1202-410d-11e8-842f-0ed5f89f718b"
      }
   },
   "code": {
      "coding": [
         {
            "system": "http://loinc.org",
            "code": "55423_8",
            "display": "Number of steps in unspecified time Pedometer"
         }
      ]
   },
   "identifier": [
      {
         "system": "https://omh.org/shimmer/ids",
         "value": "243c773b-8936-407e-9c23-270d0ea49cc4"
      }
   ],
   "device": {
      "extension": [
         {
            "valueCode": "sensed",
            "url": "http://www.fhir.org/mfhir/StructureDefinition/observationDeviceModality"
         }
      ],
      "display": "Jawbone UP API"
   },
   "meta": {
      "profile": [
         "http://www.fhir.org/mfhir/StructureDefinition/omh-to-fhir-observation"
      ]
   },
   "effectivePeriod": {
      "end": "2016-02-05T07:25:00Z",
      "start": "2016-02-05T06:25:00Z"
   }
}
~~~
