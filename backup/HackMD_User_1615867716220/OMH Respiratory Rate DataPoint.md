---
tags: omh2fhir
---

{%hackmd 2yYAoTGSSpiWVb7EWu6v0w %}

# OMH Respiratory Rate DataPoint

## OMH Respiratory Rate DataPoint to FHIR Observation Detailed Mapping

The following Table provides the detailed mapping for the OMH Respiratory Rate DataPoint to the OMH to FHIR Observation Profile TODO: add link to profile:
|Index|OMH Respiratory Rate Element|FHIR Attribute|Mapping Instructions|
|---|---|---|---|
|1|respiratory-rate-2.0.json|OMH to FHIR Observation Profile||
|2.1|body.respiratory_rate|Observation.valueQuantity|see valueQuantity elements below|
|2.2|body.respiratory_rate.value|Observation.valueQuantity.value|=  body.respiratory_rate.value|
|2.3|body.respiratory_rate.unit|Observation.valueQuantity.unit|=  body.respiratory_rate.unit|
|2.4|body.respiratory_rate.unit|Observation.valueQuantity.system|fixed to '"http://unitsofmeasure.org"'|
|2.5|body.respiratory_rate.unit|Observation.valueQuantity.code|Map body.respiratory_rate.unit to column 'FHIR Concept' using  the ['/min'](#)|
|3|body.effective_time_frame|Observation.effective[x]|Mapping depends on type - see below|
|5|body.effective_time_frame.date_time|Observation.effectiveDateTime|=  body.effective_time_frame.date_time|
|4|body.effective_time_frame.time_interval|Observation.effectivePeriod|see effectivePeriod elements below|
|6|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start|=  body.effective_time_frame.time_interval.start_date_time|
|7|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end|=  body.effective_time_frame.time_interval.end_date_time|
|9|body.descriptive_statistic|Observation.code.coding[1]|Map  descriptive statistic to the OMH to FHIR additional Observation codings ( code system http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes).|
|9.1|body.descriptive_statistic|Observation.code.coding[1].code|concatenation of  header.schema_id.name = 'respiratory-rate'  + '-' + body.descriptive_statistic  for example= respiratory-rate-maximum|
|9.2|body.descriptive_statistic|Observation.code.coding[1].system|fixed to '"http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes"'|
|9.3|body.descriptive_statistic|Observation.code.coding[1].display|concatenation of  header.schema_id.name = 'respiratory-rate'  + '-' + body.descriptive_statistic  for example= respiratory-rate-maximum|
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


## Examples

### OMH respiratory-rate schema instance

The following OMH respiratory-rate schema instance:

~~~json
{
    "header": {
        "id": "63ab1da1-9509-4c62-95a2-82db55ea9d03",
        "creation_date_time": "2020-05-30T01:01:33.463631Z",
        "schema_id": {
            "namespace": "omh",
            "name": "respiratory-rate",
            "version": "2.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme respiratory-rate device",
            "source_creation_date_time": "2020-05-30T01:01:33.463631Z",
            "source_data_point_id": "94e45f19-0685-408c-b8a6-cd63d58909bf",
            "modality": "sensed"
        },
        "user_id": "e83ee9aa-2c9b-4369-bcc3-b11dfb1854d0"
    },
    "body": {
        "respiratory_rate": {
            "value": 12,
            "unit": "breaths/min"
        },
        "effective_time_frame": {
            "date_time": "2020-02-05T07:25:00-08:00"
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
            "value": "63ab1da1-9509-4c62-95a2-82db55ea9d03"
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
                "code": "9279-1",
                "display": "Respiratory Rate"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "e83ee9aa-2c9b-4369-bcc3-b11dfb1854d0"
        }
    },
    "effectiveDateTime": "2020-02-05T07:25:00-08:00",
    "issued": "2020-05-30T01:01:33.463631Z",
    "valueQuantity": {
        "value": 12,
        "unit": "breaths/min",
        "system": "http://unitsofmeasure.org",
        "code": "/min"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme respiratory-rate device"
    }
}
~~~

### OMH respiratory-rate schema instance with descriptive statistic

The following OMH respiratory-rate schema instance:

~~~json
{
    "header": {
        "id": "34df0871-afde-4c15-9c1c-91e837707a7f",
        "creation_date_time": "2020-05-30T01:04:19.765272Z",
        "schema_id": {
            "namespace": "omh",
            "name": "respiratory-rate",
            "version": "2.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme respiratory-rate device",
            "source_creation_date_time": "2020-05-30T01:04:19.765272Z",
            "source_data_point_id": "1c1e01d9-f149-4334-8320-61bb93b21979",
            "modality": "sensed"
        },
        "user_id": "8902f789-9a5d-4b30-8af7-718176a08bd1"
    },
    "body": {
        "respiratory_rate": {
            "value": 10,
            "unit": "breaths/min"
        },
        "effective_time_frame": {
            "time_interval": {
                "start_date_time": "2020-02-05T07:05:00-08:00",
                "end_date_time": "2020-02-05T08:05:00-08:00"
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
            "value": "34df0871-afde-4c15-9c1c-91e837707a7f"
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
                "code": "9279-1",
                "display": "Respiratory Rate"
            },
            {
                "system": "http://hl7.org/fhir/omh_fhir_observation_codes",
                "code": "respiratory-rate-minimum",
                "display": "Respiratory Rate-Minimum"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "8902f789-9a5d-4b30-8af7-718176a08bd1"
        }
    },
    "effectivePeriod": {
        "start": "2020-02-05T07:05:00-08:00",
        "end": "2020-02-05T08:05:00-08:00"
    },
    "issued": "2020-05-30T01:04:19.765272Z",
    "valueQuantity": {
        "value": 10,
        "unit": "breaths/min",
        "system": "http://unitsofmeasure.org",
        "code": "/min"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme respiratory-rate device"
    }
}
~~~

### OMH respiratory-rate schema instance with temporal relationship to physical activity

The following OMH respiratory-rate schema instance:

~~~json
{
    "header": {
        "id": "68c045f5-2454-49ad-9494-028327e8332f",
        "creation_date_time": "2020-05-30T01:05:59.083823Z",
        "schema_id": {
            "namespace": "omh",
            "name": "respiratory-rate",
            "version": "2.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme respiratory-rate device",
            "source_creation_date_time": "2020-05-30T01:05:59.083823Z",
            "source_data_point_id": "5334f3b6-1b0a-4d51-9817-fc6ae6f2f849",
            "modality": "sensed"
        },
        "user_id": "d693db04-fc7d-4280-9f63-49bb66993652"
    },
    "body": {
        "respiratory_rate": {
            "value": 11,
            "unit": "breaths/min"
        },
        "effective_time_frame": {
            "date_time": "2020-02-05T07:25:00-08:00"
        },
        "temporal_relationship_to_physical_activity": "at rest"
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
            "value": "68c045f5-2454-49ad-9494-028327e8332f"
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
                "code": "9279-1",
                "display": "Respiratory Rate"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "d693db04-fc7d-4280-9f63-49bb66993652"
        }
    },
    "effectiveDateTime": "2020-02-05T07:25:00-08:00",
    "issued": "2020-05-30T01:05:59.083823Z",
    "valueQuantity": {
        "value": 11,
        "unit": "breaths/min",
        "system": "http://unitsofmeasure.org",
        "code": "/min"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme respiratory-rate device"
    },
    "component": [
        {
            "code": {
                "coding": [
                    {
                        "system": "http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes",
                        "code": "relative-to-activity",
                        "display": "OMH to FHIR Temporal Relationship To Physical Activity"
                    }
                ]
            },
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "263678003",
                        "display": "At rest"
                    }
                ],
                "text": "at rest"
            }
        }
    ]
}
~~~


Markdown Transform
