---
tags: omh2fhir
---

{%hackmd 2yYAoTGSSpiWVb7EWu6v0w %}

# OMH Body Weight DataPoint

## OMH Body Weight DataPoint to FHIR Observation Detailed Mapping

The following Table provides the detailed mapping for the OMH Body Weight DataPoint to the OMH to FHIR Observation Profile TODO: add link to map and profile:
|Index|OMH Body Weight Element|FHIR Attribute|Mapping Instructions|
|---|---|---|---|
|1|body-weight-2.0.json|OMH to FHIR Observation Profile||
|2.1|body_weight|Observation.valueQuantity|see valueQuantity elements below|
|2.2|body_weight.value|Observation.valueQuantity.value|=  body_weight.value|
|2.3|body_weight.unit|Observation.valueQuantity.unit|=  body_weight.unit|
|2.4|body_weight.unit|Observation.valueQuantity.system|fixed to 'http://unitsofmeasure.org'|
|2.5|body_weight.unit|Observation.valueQuantity.code|Map body_weight.unit to column 'FHIR Concept' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|3|body.effective_time_frame|Observation.effective[x]|Mappping depends on type- see below|
|5|body.effective_time_frame.date_time|Observation.effectiveDateTime|=  body.effective_time_frame.date_time|
|4|body.effective_time_frame.time_interval|Observation.effectivePeriod|see effectivePeriod elements below|
|8.1|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start|=  body.effective_time_frame.time_interval.start_date_time|
|8.0|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end|=  body.effective_time_frame.time_interval.end_date_time|
|9|body.descriptive_statistic|Observation.code.coding[1]|Map  descriptive statistic to the OMH to FHIR additional Observation codings ( code system http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes).|
|9.1|body.descriptive_statistic|Observation.code.coding[1].code|concatenation of  header.schema_id.name = 'body-weight'  + '-' + body.descriptive_statistic  for example= body-weight-maximum|
|9.2|body.descriptive_statistic|Observation.code.coding[1].system|fixed to '"http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes"'|
|9.3|body.descriptive_statistic|Observation.code.coding[1].display|concatenation of  header.schema_id.name = 'body-weight'  + '-' + body.descriptive_statistic  for example= body-weight-maximum|

## Examples:

### OMH body-weight schema instance

The following OMH body-weight schema instance:

~~~json
{
    "header": {
        "id": "052f8cd8-b537-4c6d-b9d7-ea8955b5ca78",
        "creation_date_time": "2020-05-30T01:58:56.116568Z",
        "schema_id": {
            "namespace": "omh",
            "name": "body-weight",
            "version": "2.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme body-weight device",
            "source_creation_date_time": "2020-05-30T01:58:56.116568Z",
            "source_data_point_id": "6f3a11a2-0e34-4ef5-a226-1fd7277e82d0",
            "modality": "sensed"
        },
        "user_id": "16f1819f-06f3-4035-910d-430fcb770200"
    },
    "body": {
        "body_weight": {
            "value": 50,
            "unit": "kg"
        },
        "effective_time_frame": {
            "date_time": "2020-02-05T09:45:00-08:00"
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
            "value": "052f8cd8-b537-4c6d-b9d7-ea8955b5ca78"
        }
    ],
    "status": "unknown",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "vital-signs",
                    "display": "Vital Signs"
                }
            ]
        }
    ],
    "code": {
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "29463-7",
                "display": "Body weight"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "16f1819f-06f3-4035-910d-430fcb770200"
        }
    },
    "effectiveDateTime": "2020-02-05T09:45:00-08:00",
    "issued": "2020-05-30T01:58:56.116568Z",
    "valueQuantity": {
        "value": 50,
        "unit": "kg",
        "system": "http://unitsofmeasure.org",
        "code": "kg"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme body-weight device"
    }
}
~~~

### OMH body-weight schema instance - with descriptive statistic

The following OMH body-weight schema instance:

~~~json
{
    "header": {
        "id": "7a5a99c3-4016-4ad1-b6f6-c6cadbbc6cfc",
        "creation_date_time": "2020-05-30T02:00:21.970018Z",
        "schema_id": {
            "namespace": "omh",
            "name": "body-weight",
            "version": "2.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme body-weight device",
            "source_creation_date_time": "2020-05-30T02:00:21.970018Z",
            "source_data_point_id": "7f60b101-310a-423d-a2c1-498f27a7834d",
            "modality": "sensed"
        },
        "user_id": "9d3cf336-bcbd-4865-9cc2-e1aa54630c3b"
    },
    "body": {
        "body_weight": {
            "value": 49.5,
            "unit": "kg"
        },
        "effective_time_frame": {
            "time_interval": {
                "start_date_time": "2020-02-05T09:45:00-08:00",
                "end_date_time": "2020-03-05T10:40:00-08:00"
            }
        },
        "descriptive_statistic": "minimum"
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
            "value": "7a5a99c3-4016-4ad1-b6f6-c6cadbbc6cfc"
        }
    ],
    "status": "unknown",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "vital-signs",
                    "display": "Vital Signs"
                }
            ]
        }
    ],
    "code": {
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "29463-7",
                "display": "Body weight"
            },
            {
                "system": "http://hl7.org/fhir/omh_fhir_observation_codes",
                "code": "body-weight-minimum",
                "display": "Body Weight-Minimum"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "9d3cf336-bcbd-4865-9cc2-e1aa54630c3b"
        }
    },
    "effectivePeriod": {
        "start": "2020-02-05T09:45:00-08:00",
        "end": "2020-03-05T10:40:00-08:00"
    },
    "issued": "2020-05-30T02:00:21.970018Z",
    "valueQuantity": {
        "value": 49.5,
        "unit": "kg",
        "system": "http://unitsofmeasure.org",
        "code": "kg"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme body-weight device"
    }
}
~~~
