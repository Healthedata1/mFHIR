---
tags: omh2fhir
---

{%hackmd 2yYAoTGSSpiWVb7EWu6v0w %}

# OMH Step Count DataPoint

## OMH Step Count DataPoint to FHIR Observation Detailed Mapping

The following Table provides the detailed mapping for the OMH Step Count DataPoint to the OMH to FHIR Observation Profile TODO: add link to map and profile:
|Index|OMH Step Count Element|FHIR Attribute|Mapping Instructions|
|---|---|---|---|
|1|step-count-3.0.json|OMH to FHIR Observation Profile||
|2.1|body.step_count|Observation.valueQuantity|see valueQuantity elements below, if body.descriptive_statistic_denominator is present is modifies the units as described below|
|2.2|body.step_count.value|Observation.valueQuantity.value|=  body.step_count.value|
|2.3|body.step_count.unit|Observation.valueQuantity.unit|IF body.descriptive_statistic_denominatoris present = concatenation of 'steps'  +   mapping of body.descriptive_statistic_denominator to column 'Unit' using  the [OMH_FHIR_Descriptive_Statistic_Denominator_Mapping _Table](#)  (for example 'steps/day')  ELSE  = 'steps'|
|2.4|body.step_count.unit|Observation.valueQuantity.system|fixed to 'http://unitsofmeasure.org'|
|2.5|body.step_count.unit|Observation.valueQuantity.code|IF is present = concatenation of '{steps}'  + mapping of body.descriptive_statistic_denominator to column 'Code' using  the [OMH_FHIR_Descriptive_Statistic_Denominator_Mapping _Table](#)  (for example '{steps}/d')  ELSE  = '{steps}'|
|3|body.effective_time_frame|Observation.effectivePeriod|see effectivePeriod elements below|
|4|body.effective_time_frame.time_interval|Observation.effectivePeriod|see effectivePeriod elements below|
|4.1|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start|=  body.effective_time_frame.time_interval.start_date_time|
|4.2|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end|=  body.effective_time_frame.time_interval.end_date_time|
|5|body.descriptive_statistic|Observation.code.coding[1]|Map  descriptive statistic to the OMH to FHIR additional Observation codings ( code system http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes).|
|5.1|body.descriptive_statistic|Observation.code.coding[1].code|IF body.descriptive_statistic_denominator is present  = concatenation of  header.schema_id.name = 'step-count'  + '-' + body.descriptive_statistic/body.descriptive_statistic_denominator  for example= step-count-maximum/session, ELSE = concatenation of  header.schema_id.name = 'step-count'  + '-' + body.descriptive_statistic for example= step-count-maximum|
|5.2|body.descriptive_statistic|Observation.code.coding[1].system|fixed to '"http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes"'|
|5.3|body.descriptive_statistic|Observation.code.coding[1].display|IF body.descriptive_statistic_denominator is present  = concatenation of  header.schema_id.name = 'step-count'  + '-' + body.descriptive_statistic/body.descriptive_statistic_denominator  for example= step-count-maximum/session, ELSE = concatenation of  header.schema_id.name = 'step-count'  + '-' + body.descriptive_statistic for example= step-count-maximum|
|5|body.descriptive_statistic_denominator|Observation.code.coding[1]|see body.descriptive_statistic above and |
|5.A1|body.descriptive_statistic_denominator|Observation.code.coding[1].code|see body.descriptive_statistic above|
|5.A2|body.descriptive_statistic_denominator|Observation.code.coding[1].system|see body.descriptive_statistic above|
|5.A3|body.descriptive_statistic_denominator|Observation.code.coding[1].display|see body.descriptive_statistic above|
|5.B1|body.descriptive_statistic_denominator|Observation.valueQuantity.unit|see body.step_count.unit above|
|5.B2|body.descriptive_statistic_denominator|Observation.valueQuantity.code|see body.step_count.unit above|

## Examples


### OMH step-count schema instance

The following OMH step-count schema instance:

~~~json
{
    "header": {
        "id": "0bc679ad-18e0-4b31-8ad4-514c068b1bde",
        "creation_date_time": "2020-05-30T02:48:07.649124Z",
        "schema_id": {
            "namespace": "omh",
            "name": "step-count",
            "version": "3.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme step-count device",
            "source_creation_date_time": "2020-05-30T02:48:07.649124Z",
            "source_data_point_id": "6415d547-deb9-40e7-9954-68c0fc20a2f8",
            "modality": "sensed"
        },
        "user_id": "9d2fad2d-3e03-4749-b864-3089f4e8c2a2"
    },
    "body": {
        "step_count": {
            "value": 10600,
            "unit": "steps"
        },
        "effective_time_frame": {
            "time_interval": {
                "start_date_time": "2016-02-05T06:25:00Z",
                "end_date_time": "2016-02-05T07:25:00Z"
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
            "value": "0bc679ad-18e0-4b31-8ad4-514c068b1bde"
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
                "system": "http://loinc.org",
                "code": "55423-8",
                "display": "Number of steps in unspecified time Pedometer"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "9d2fad2d-3e03-4749-b864-3089f4e8c2a2"
        }
    },
    "effectivePeriod": {
        "start": "2016-02-05T06:25:00Z",
        "end": "2016-02-05T07:25:00Z"
    },
    "issued": "2020-05-30T02:48:07.649124Z",
    "valueQuantity": {
        "value": 10600,
        "unit": "steps",
        "system": "http://unitsofmeasure.org",
        "code": "{steps}"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme step-count device"
    }
}
~~~

### OMH step-count schema instance - daily average

The following OMH step-count schema instance:

~~~json
{
    "header": {
        "id": "8f6a786e-6b23-43d3-85ec-ac2fba7503c9",
        "creation_date_time": "2020-05-30T03:23:07.410436Z",
        "schema_id": {
            "namespace": "omh",
            "name": "step-count",
            "version": "3.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme step-count device",
            "source_creation_date_time": "2020-05-30T03:23:07.410436Z",
            "source_data_point_id": "e09923d3-333d-4776-aafa-6d60b1a00f47",
            "modality": "sensed"
        },
        "user_id": "b368544e-2bc6-4352-a726-f89f9d325239"
    },
    "body": {
        "step_count": {
            "value": 12500,
            "unit": "steps"
        },
        "effective_time_frame": {
            "time_interval": {
                "start_date_time": "2016-05-05T07:00:00Z",
                "end_date_time": "2016-06-05T07:00:00Z"
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
            "value": "8f6a786e-6b23-43d3-85ec-ac2fba7503c9"
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
                "system": "http://loinc.org",
                "code": "55423-8",
                "display": "Number of steps in unspecified time Pedometer"
            },
            {
                "system": "http://hl7.org/fhir/omh_fhir_observation_codes",
                "code": "step-count-average/d",
                "display": "Step Count-Average/day"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "b368544e-2bc6-4352-a726-f89f9d325239"
        }
    },
    "effectivePeriod": {
        "start": "2016-05-05T07:00:00Z",
        "end": "2016-06-05T07:00:00Z"
    },
    "issued": "2020-05-30T03:23:07.410436Z",
    "valueQuantity": {
        "value": 12500,
        "unit": "steps/day",
        "system": "http://unitsofmeasure.org",
        "code": "{steps}/d"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme step-count device"
    }
}
~~~

### OMH step-count schema instance - with maximum session

The following OMH step-count schema instance:

~~~json
{
    "header": {
        "id": "a65d9730-849d-4a63-84c6-7e4c0b06ebec",
        "creation_date_time": "2020-05-30T03:27:11.821458Z",
        "schema_id": {
            "namespace": "omh",
            "name": "step-count",
            "version": "3.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme step-count device",
            "source_creation_date_time": "2020-05-30T03:27:11.821458Z",
            "source_data_point_id": "1f291bf1-03a6-403e-a492-6d587ada68a7",
            "modality": "sensed"
        },
        "user_id": "27215a90-d840-48dc-812d-b992c3b11447"
    },
    "body": {
        "step_count": {
            "value": 26000,
            "unit": "steps"
        },
        "effective_time_frame": {
            "time_interval": {
                "start_date_time": "2016-02-05T07:00:00Z",
                "end_date_time": "2016-06-05T07:00:00Z"
            }
        },
        "descriptive_statistic": "maximum",
        "descriptive_statistic_denominator": "session"
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
            "value": "a65d9730-849d-4a63-84c6-7e4c0b06ebec"
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
                "system": "http://loinc.org",
                "code": "55423-8",
                "display": "Number of steps in unspecified time Pedometer"
            },
            {
                "system": "http://hl7.org/fhir/omh_fhir_observation_codes",
                "code": "step-count-maximum/{session}",
                "display": "Step Count-Maximum/session"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "27215a90-d840-48dc-812d-b992c3b11447"
        }
    },
    "effectivePeriod": {
        "start": "2016-02-05T07:00:00Z",
        "end": "2016-06-05T07:00:00Z"
    },
    "issued": "2020-05-30T03:27:11.821458Z",
    "valueQuantity": {
        "value": 26000,
        "unit": "steps/session",
        "system": "http://unitsofmeasure.org",
        "code": "{steps}/{session}"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme step-count device"
    }
}
~~~

### OMH step-count schema instance - with maximum day

The following OMH step-count schema instance:

~~~json
{
    "header": {
        "id": "83efa8ad-5114-4f76-aac1-87317e60b4f4",
        "creation_date_time": "2020-05-30T03:28:32.463195Z",
        "schema_id": {
            "namespace": "omh",
            "name": "step-count",
            "version": "3.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme step-count device",
            "source_creation_date_time": "2020-05-30T03:28:32.463195Z",
            "source_data_point_id": "fc1b059c-0c11-42d9-a34a-76de23e4048c",
            "modality": "sensed"
        },
        "user_id": "e3bc6931-8103-4b56-87fb-11d645524030"
    },
    "body": {
        "step_count": {
            "value": 20500,
            "unit": "steps"
        },
        "effective_time_frame": {
            "time_interval": {
                "start_date_time": "2016-02-05T07:00:00Z",
                "end_date_time": "2016-06-05T07:00:00Z"
            }
        },
        "descriptive_statistic": "maximum",
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
            "value": "83efa8ad-5114-4f76-aac1-87317e60b4f4"
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
                "system": "http://loinc.org",
                "code": "55423-8",
                "display": "Number of steps in unspecified time Pedometer"
            },
            {
                "system": "http://hl7.org/fhir/omh_fhir_observation_codes",
                "code": "step-count-maximum/d",
                "display": "Step Count-Maximum/day"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "e3bc6931-8103-4b56-87fb-11d645524030"
        }
    },
    "effectivePeriod": {
        "start": "2016-02-05T07:00:00Z",
        "end": "2016-06-05T07:00:00Z"
    },
    "issued": "2020-05-30T03:28:32.463195Z",
    "valueQuantity": {
        "value": 20500,
        "unit": "steps/day",
        "system": "http://unitsofmeasure.org",
        "code": "{steps}/d"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme step-count device"
    }
}
~~~

