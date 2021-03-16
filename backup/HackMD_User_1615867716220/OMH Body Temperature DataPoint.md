---
tags: omh2fhir
---

{%hackmd 2yYAoTGSSpiWVb7EWu6v0w %}

# OMH Body Temperature DataPoint

## OMH Body Temperature DataPoint to FHIR Observation Detailed Mapping

The following Table provides the detailed mapping for the OMH Body Temperature DataPoint to the OMH to FHIR Observation Profile TODO: add link to profile and mapping table:
|Index|OMH Body Temperature Element|FHIR Attribute|Mapping Instructions|
|---|---|---|---|
|1|body-temperature-3.0.json|OMH to FHIR Observation Profile||
|2.1|body_temperature|Observation.valueQuantity|see valueQuantity elements below|
|2.2|body_temperature.value|Observation.valueQuantity.value|=  body_temperature.value|
|2.3|body_temperature.unit|Observation.valueQuantity.unit|=  body_temperature.unit|
|2.4|body_temperature.unit|Observation.valueQuantity.system|fixed to 'http://unitsofmeasure.org'|
|2.5|body_temperature.unit|Observation.valueQuantity.code|Map body_temperature.unit to column 'FHIR Concept' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|3|body.effective_time_frame|Observation.effective[x]|Mappping depends on type- see below|
|3.1|body.effective_time_frame.date_time|Observation.effectiveDateTime|=  body.effective_time_frame.date_time|
|3.2|body.effective_time_frame.time_interval|Observation.effectivePeriod|see effectivePeriod elements below|
|3.2.1|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start|=  body.effective_time_frame.time_interval.start_date_time|
|3.2.2|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end|=  body.effective_time_frame.time_interval.end_date_time|
|8.1|body.measurement_location|Observation.bodySite|See bodySite elements below|
|8.2|body.measurement_location|Observation.bodySIte.coding[0].code|Map body.measurement_location to column 'FHIR Concept' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|8.3|body.measurement_location|Observation.bodySIte.coding[0].system|Map body.measurement_location to column 'FHIR Concept System' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|8.4|body.measurement_location|Observation.bodySIte.coding[0].display|Map body.measurement_location to column 'FHIR Concept display' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|9|body.descriptive_statistic|Observation.code.coding[1]|Map  descriptive statistic to the OMH to FHIR additional Observation codings ( code system http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes).|
|9.1|body.descriptive_statistic|Observation.code.coding[1].code|concatenation of  header.schema_id.name = 'body-temperature'  + '-' + body.descriptive_statistic  for example= body-temperature-maximum|
|9.2|body.descriptive_statistic|Observation.code.coding[1].system|fixed to '"http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes"'|
|9.3|body.descriptive_statistic|Observation.code.coding[1].display|concatenation of  header.schema_id.name = 'body-temperature'  + '-' + body.descriptive_statistic  for example= body-temperature-maximum|
|10|body.temporal_relationship_to_physical_activity|Observation.component[0]|A mapping between temporal-relationship-to-physical-activity and FHIR Observation Component data elements.  Multiple components mapping are appended as a list|
|10.A1|body.temporal_relationship_to_physical_activity|Observation.component[0].code|A mapping between temporal-relationship-to-physical-activity and FHIR Observation Component.code data elements.|
|10.A2|body.temporal_relationship_to_physical_activity|Observation.component[0].code.coding[1].code|=  'relative-to-activity'|
|10.A3|body.temporal_relationship_to_physical_activity|Observation.component[0].code.coding[1].system|=  "http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes"|
|10.A4|body.temporal_relationship_to_physical_activity|Observation.component[0].code.coding[1].display|=  'OMH to FHIR Temporal Relationship To Physical Activity'|
|10.B1|body.temporal_relationship_to_physical_activity|Observation.component[0].valueCodeableConcept|A mapping between body.temporal_relationship_to_physical_activity and FHIR Observation Component.valueCodeableConcept data elements.|
|10.B2|body.temporal_relationship_to_physical_activity|Observation.component[0].valueCodeableConcept.coding[0].code|Map body.temporal_relationship_to_physical_activity to column 'FHIR Concept' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|10.B3|body.temporal_relationship_to_physical_activity|Observation.component[0].valueCodeableConcept.coding[0].system|Map body.temporal_relationship_to_physical_activity to column 'FHIR Concept System' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|10.B4|body.temporal_relationship_to_physical_activity|Observation.component[0].valueCodeableConcept.coding[0].display|Map body.temporal_relationship_to_physical_activity to column 'FHIR Concept display' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|10.B5|body.temporal_relationship_to_physical_activity|Observation.component[0].valueCodeableConcept.text|=  body.temporal_relationship_to_physical_activity|
|11|body.temporal_relationship_to_sleep|Observation.component[0]|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list|
|11.A1|body.temporal_relationship_to_sleep|Observation.component[0].code|A mapping between temporal-relationship-to-sleep and FHIR Observation Component.code data elements.|
|11.A2|body.temporal_relationship_to_sleep|Observation.component[0].code.coding[1].code|=  'relative-to-sleep'|
|11.A3|body.temporal_relationship_to_sleep|Observation.component[0].code.coding[1].system|=  "http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes"|
|11.A4|body.temporal_relationship_to_sleep|Observation.component[0].code.coding[1].display|=  'OMH to FHIR Temporal Relationship To Sleep'|
|11.B1|body.temporal_relationship_to_sleep|Observation.component[0].valueCodeableConcept|A mapping between body.temporal_relationship_to_sleep and FHIR Observation Component.valueCodeableConcept data elements.|
|11.B2|body.temporal_relationship_to_sleep|Observation.component[0].valueCodeableConcept.coding[0].code|Map body.temporal_relationship_to_sleep to column 'FHIR Concept' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|11.B3|body.temporal_relationship_to_sleep|Observation.component[0].valueCodeableConcept.coding[0].system|Map body.temporal_relationship_to_sleep to column 'FHIR Concept System' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|11.B4|body.temporal_relationship_to_sleep|Observation.component[0].valueCodeableConcept.coding[0].display|Map body.temporal_relationship_to_sleep to column 'FHIR Concept display' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|11.B5|body.temporal_relationship_to_sleep|Observation.component[0].valueCodeableConcept.text|=  body.temporal_relationship_to_sleep|



## Examples:


### OMH body-temperature schema instance - Basal temperature

The following OMH body-temperature schema instance:

~~~json
{
    "header": {
        "id": "080997cb-224e-499e-8584-90b6d50184c7",
        "creation_date_time": "2020-05-30T01:15:47.285652Z",
        "schema_id": {
            "namespace": "omh",
            "name": "body-temperature",
            "version": "3.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme body-temperature device",
            "source_creation_date_time": "2020-05-30T01:15:47.285652Z",
            "source_data_point_id": "fc18d8d4-9cbf-4163-9514-2ad54fe0397b",
            "modality": "sensed"
        },
        "user_id": "e78f7659-c0d4-4308-8961-ff4180f0dff1"
    },
    "body": {
        "body_temperature": {
            "value": 96.5,
            "unit": "F"
        },
        "effective_time_frame": {
            "date_time": "2013-02-05T06:25:00Z"
        },
        "temporal_relationship_to_sleep": "on waking"
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
            "value": "080997cb-224e-499e-8584-90b6d50184c7"
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
                "code": "8310-5",
                "display": "Body temperature"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "e78f7659-c0d4-4308-8961-ff4180f0dff1"
        }
    },
    "effectiveDateTime": "2013-02-05T06:25:00Z",
    "issued": "2020-05-30T01:15:47.285652Z",
    "valueQuantity": {
        "value": 96.5,
        "unit": "F",
        "system": "http://unitsofmeasure.org",
        "code": "[degF]"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme body-temperature device"
    },
    "component": [
        {
            "code": {
                "coding": [
                    {
                        "system": "http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes",
                        "code": "relative-to-sleep",
                        "display": "OMH to FHIR Temporal Relationship To Sleep"
                    }
                ]
            },
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "307156004",
                        "display": "On waking"
                    }
                ],
                "text": "on waking"
            }
        }
    ]
}
~~~

### OMH body-temperature schema instance - Valid temperature with measuremet_location

The following OMH body-temperature schema instance:

~~~json
{
    "header": {
        "id": "de15187e-cd8a-46eb-90e7-5ff1303007dc",
        "creation_date_time": "2020-05-30T01:36:06.311337Z",
        "schema_id": {
            "namespace": "omh",
            "name": "body-temperature",
            "version": "3.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme body-temperature device",
            "source_creation_date_time": "2020-05-30T01:36:06.311337Z",
            "source_data_point_id": "8b6aa922-5d03-4471-8e2d-0bc13e3bff6c",
            "modality": "sensed"
        },
        "user_id": "95718638-98b4-4c3d-8040-0301d2b805f4"
    },
    "body": {
        "body_temperature": {
            "value": 97,
            "unit": "F"
        },
        "effective_time_frame": {
            "date_time": "2013-02-05T07:25:00Z"
        },
        "measurement_location": "forehead"
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
            "value": "de15187e-cd8a-46eb-90e7-5ff1303007dc"
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
                "code": "8310-5",
                "display": "Body temperature"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "95718638-98b4-4c3d-8040-0301d2b805f4"
        }
    },
    "effectiveDateTime": "2013-02-05T07:25:00Z",
    "issued": "2020-05-30T01:36:06.311337Z",
    "valueQuantity": {
        "value": 97,
        "unit": "F",
        "system": "http://unitsofmeasure.org",
        "code": "[degF]"
    },
    "bodySite": {
        "coding": [
            {
                "system": "http://www.fhir.org/guides/mfhir/CodeSystem/body-location",
                "code": "forehead"
            }
        ],
        "text": "forehead"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme body-temperature device"
    }
}
~~~

### OMH body-temperature schema instance - valid temperature with statistic

The following OMH body-temperature schema instance:

~~~json
{
    "header": {
        "id": "e694349f-ac2c-4712-86b1-c09152c35667",
        "creation_date_time": "2020-05-30T01:43:16.250809Z",
        "schema_id": {
            "namespace": "omh",
            "name": "body-temperature",
            "version": "3.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme body-temperature device",
            "source_creation_date_time": "2020-05-30T01:43:16.250809Z",
            "source_data_point_id": "3e36c93c-1e40-4f9f-8d9d-8570aec95d55",
            "modality": "sensed"
        },
        "user_id": "2c95c8db-5b06-4651-a606-b51406fcc4d4"
    },
    "body": {
        "body_temperature": {
            "value": 96.5,
            "unit": "F"
        },
        "effective_time_frame": {
            "time_interval": {
                "start_date_time": "2020-02-05T06:00:00-08:00",
                "end_date_time": "2020-02-06T06:00:00-08:00"
            }
        },
        "measurement_location": "oral",
        "descriptive_statistic": "maximum"
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
            "value": "e694349f-ac2c-4712-86b1-c09152c35667"
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
                "code": "8310-5",
                "display": "Body temperature"
            },
            {
                "system": "http://hl7.org/fhir/omh_fhir_observation_codes",
                "code": "body-temperature-maximum",
                "display": "Body Temperature-Maximum"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "2c95c8db-5b06-4651-a606-b51406fcc4d4"
        }
    },
    "effectivePeriod": {
        "start": "2020-02-05T06:00:00-08:00",
        "end": "2020-02-06T06:00:00-08:00"
    },
    "issued": "2020-05-30T01:43:16.250809Z",
    "valueQuantity": {
        "value": 96.5,
        "unit": "F",
        "system": "http://unitsofmeasure.org",
        "code": "[degF]"
    },
    "bodySite": {
        "coding": [
            {
                "system": "http://www.fhir.org/guides/mfhir/CodeSystem/intervention-administration-route",
                "code": "oral"
            }
        ],
        "text": "oral"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme body-temperature device"
    }
}
~~~

~~~




---


