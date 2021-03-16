---
tags: omh2fhir
---

{%hackmd 2yYAoTGSSpiWVb7EWu6v0w %}

# OMH Total Sleep Time DataPoint


## OMH Total Sleep Time DataPoint to FHIR Observation Detailed Mapping

The following Table provides the detailed mapping for the OMH Total Sleep Time DataPoint to the OMH to FHIR Observation Profile TODO: add link to map and profile:
|Index|OMH Total Sleep Time Element|FHIR Attribute|Mapping Instructions|
|---|---|---|---|
|1|total-sleep-time-1.0.json|OMH to FHIR Observation Profile||
|2.1|total_sleep_time|Observation.valueQuantity|see valueQuantity elements below|
|2.2|total_sleep_time.value|Observation.valueQuantity.value|=  total_sleep_time.value|
|2.3|total_sleep_time.unit|Observation.valueQuantity.unit|IF body.descriptive_statistic_denominator is present = concatenation of total_sleep_time.unit  + mapping of body.descriptive_statistic_denominator to column 'Unit' using  the [OMH_FHIR_Descriptive_Statistic_Denominator_Mapping _Table](#)  (for example 'min/day')  ELSE  = total_sleep_time.unit (for example, 'min')|
|2.4|total_sleep_time.unit|Observation.valueQuantity.system|fixed to 'http://unitsofmeasure.org'|
|2.5|total_sleep_time.unit|Observation.valueQuantity.code|IF body.descriptive_statistic_denominator is present = concatenation of mapping of total_sleep_time.unit to column 'FHIR Unit' using  the [OMH_FHIR_Concept_Mapping_Table](#)  + mapping of body.descriptive_statistic_denominator to column 'Code' using  the [OMH_FHIR_Descriptive_Statistic_Denominator_Mapping _Table](#)  (for example 'min/d')  ELSE  =  mapping of total_sleep_time.unit to column 'FHIR Unit' using  the [OMH_FHIR_Concept_Mapping_Table](#) (for example, 'min')|
|3|body.effective_time_frame|Observation.effectivePeriod|see effectivePeriod elements below|
|4|body.effective_time_frame.time_interval|Observation.effectivePeriod|see effectivePeriod elements below|
|4.1|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start|=  body.effective_time_frame.time_interval.start_date_time|
|4.2|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end|=  body.effective_time_frame.time_interval.end_date_time|
|5|body.descriptive_statistic|Observation.code.coding[1]|Map  descriptive statistic to the OMH to FHIR additional Observation codings ( code system http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes).|
|5.1|body.descriptive_statistic|Observation.code.coding[1].code|concatenation of  header.schema_id.name = 'total-sleep-time'  + '-' + body.descriptive_statistic/body.descriptive_statistic_denominator  for example= total-sleep-time-maximum/session|
|5.2|body.descriptive_statistic|Observation.code.coding[1].system|fixed to '"http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes"'|
|5.3|body.descriptive_statistic|Observation.code.coding[1].display|concatenation of  header.schema_id.name = 'total-sleep-time'  + '-' + body.descriptive_statistic/body.descriptive_statistic_denominator  for example= total-sleep-time-maximum/session|
|5|body.descriptive_statistic_denominator|Observation.code.coding[1]|see body.descriptive_statistic above|
|5.A1|body.descriptive_statistic_denominator|Observation.code.coding[1].code|see body.descriptive_statistic above|
|5.A2|body.descriptive_statistic_denominator|Observation.code.coding[1].system|see body.descriptive_statistic above|
|5.A3|body.descriptive_statistic_denominator|Observation.code.coding[1].display|see body.descriptive_statistic above|
|5.B1|body.descriptive_statistic_denominator|Observation.valueQuantity.unit|see body.step_count.unit above|
|5.B2|body.descriptive_statistic_denominator|Observation.valueQuantity.code|see body.step_count.unit above|

## Examples

### OMH total-sleep-time schema instance

The following OMH total-sleep-time schema instance:

~~~json
{
    "header": {
        "id": "f4e9d921-b485-40a3-ad72-8d5c7f4840ba",
        "creation_date_time": "2020-05-30T02:42:31.136858Z",
        "schema_id": {
            "namespace": "omh",
            "name": "total-sleep-time",
            "version": "1.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme total-sleep-time device",
            "source_creation_date_time": "2020-05-30T02:42:31.136858Z",
            "source_data_point_id": "faf655d5-9779-413e-b57a-e3aa6272b29c",
            "modality": "sensed"
        },
        "user_id": "80d614c3-1e0e-4fc4-b586-2907bcec0775"
    },
    "body": {
        "total_sleep_time": {
            "value": 465,
            "unit": "min"
        },
        "effective_time_frame": {
            "time_interval": {
                "start_date_time": "2016-02-05T20:35:00-08:00",
                "end_date_time": "2016-02-06T06:35:00-08:00"
            }
        }
    }
}
~~~

Maps to this FHIR Observation (note that this example does not include the optional Provenance resource)

~~~json
{
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_profile_quantitative_observation"
        ]
    },
    "identifier": [
        {
            "system": "https://omh.org/shimmer/ids",
            "value": "f4e9d921-b485-40a3-ad72-8d5c7f4840ba"
        }
    ],
    "status": "unknown",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "physical-activity",
                    "display": "Physical Activity"
                }
            ]
        }
    ],
    "code": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "248263006",
                "display": "Duration of sleep (observable entity)"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "80d614c3-1e0e-4fc4-b586-2907bcec0775"
        }
    },
    "effectivePeriod": {
        "start": "2016-02-05T20:35:00-08:00",
        "end": "2016-02-06T06:35:00-08:00"
    },
    "issued": "2020-05-30T02:42:31.136858Z",
    "valueQuantity": {
        "value": 465,
        "unit": "min",
        "system": "http://unitsofmeasure.org",
        "code": "min"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme total-sleep-time device"
    }
}
~~~

### OMH total-sleep-time schema instance with descriptive statistic


The following OMH total-sleep-time schema instance:

~~~json
{
    "header": {
        "id": "fb8b65cf-0f30-4461-974d-37a18ad865d9",
        "creation_date_time": "2020-05-30T02:44:35.120200Z",
        "schema_id": {
            "namespace": "omh",
            "name": "total-sleep-time",
            "version": "1.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme total-sleep-time device",
            "source_creation_date_time": "2020-05-30T02:44:35.120200Z",
            "source_data_point_id": "da62fdcc-7727-425a-8e68-4ff73c97dba2",
            "modality": "sensed"
        },
        "user_id": "0090e44f-e79d-48a2-b80c-6f533fe494ba"
    },
    "body": {
        "total_sleep_time": {
            "value": 7.25,
            "unit": "h"
        },
        "effective_time_frame": {
            "time_interval": {
                "start_date_time": "2016-02-05T07:00:00-08:00",
                "end_date_time": "2016-06-06T07:00:00-08:00"
            }
        },
        "descriptive_statistic": "average",
        "descriptive_statistic_denominator": "d"
    }
}
~~~

Maps to this FHIR Observation (note that this example does not include the optional Provenance resource)

~~~json
{
    "resourceType": "Observation",
    "meta": {
        "profile": [
            "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_profile_quantitative_observation"
        ]
    },
    "identifier": [
        {
            "system": "https://omh.org/shimmer/ids",
            "value": "fb8b65cf-0f30-4461-974d-37a18ad865d9"
        }
    ],
    "status": "unknown",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "physical-activity",
                    "display": "Physical Activity"
                }
            ]
        }
    ],
    "code": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "248263006",
                "display": "Duration of sleep (observable entity)"
            },
            {
                "system": "http://hl7.org/fhir/omh_fhir_observation_codes",
                "code": "total-sleep-time-average",
                "display": "Total Sleep Time-Average"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "0090e44f-e79d-48a2-b80c-6f533fe494ba"
        }
    },
    "effectivePeriod": {
        "start": "2016-02-05T07:00:00-08:00",
        "end": "2016-06-06T07:00:00-08:00"
    },
    "issued": "2020-05-30T02:44:35.120200Z",
    "valueQuantity": {
        "value": 7.25,
        "unit": "h/day",
        "system": "http://unitsofmeasure.org",
        "code": "h/day/{day}"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme total-sleep-time device"
    }
}
~~~

