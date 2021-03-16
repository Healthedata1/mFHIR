---
tags: omh2fhir
---

{%hackmd 2yYAoTGSSpiWVb7EWu6v0w %}

# OMH HeartRate DataPoint 

## OMH HeartRate DataPoint to FHIR Observation Detailed Mapping


The following Table provides the detailed mapping for the OMH HeartRate DataPoint to the OMH to FHIR Observation Profile TODO: add link to profile:

|Index|OMH Heart Rate Element|FHIR Attribute|Mapping Instructions|
|---|---|---|---|
|1|heart-rate-2.0.json|OMH to FHIR Observation Profile||
|2.1|body.heart_rate|Observation.valueQuantity|see valueQuantity elements below|
|2.2|body.heart_rate.value|Observation.valueQuantity.value|=  body.heart_rate.value|
|2.3|body.heart_rate.unit|Observation.valueQuantity.unit|=  'beats/min'|
|2.4|body.heart_rate.unit|Observation.valueQuantity.system|fixed to '"http://unitsofmeasure.org"'|
|2.5|body.heart_rate.unit|Observation.valueQuantity.code|=  '/min'|
|3|body.effective_time_frame|Observation.effective[x]|Mapping depends on type - see below|
|5|body.effective_time_frame.date_time|Observation.effectiveDateTime|=  body.effective_time_frame.date_time|
|4|body.effective_time_frame.time_interval|Observation.effectivePeriod|see effectivePeriod elements below|
|6|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start|=  body.effective_time_frame.time_interval.start_date_time|
|7|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end|=  body.effective_time_frame.time_interval.end_date_time|
|9|body.descriptive_statistic|Observation.code.coding[1]|Map  descriptive statistic to the OMH to FHIR additional Observation codings ( code system http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes).|
|9.1|body.descriptive_statistic|Observation.code.coding[1].code|concatenation of  header.schema_id.name = 'heart-rate'  + '-' + body.descriptive_statistic  for example= heart-rate-maximum|
|9.2|body.descriptive_statistic|Observation.code.coding[1].system|fixed to '"http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes"'|
|9.3|body.descriptive_statistic|Observation.code.coding[1].display|concatenation of  header.schema_id.name = 'heart-rate'  + '-' + body.descriptive_statistic  for example= heart-rate-maximum|
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



## Example Mappings:

### OMH heart-rate schema instance with descripive statistic

The following OMH heart-rate schema instance with descripive statistic:

~~~json
{
    "header": {
        "id": "c18a469c-e034-46fb-8f87-edb95a0e083b",
        "creation_date_time": "2020-05-30T00:24:49.873027Z",
        "schema_id": {
            "namespace": "omh",
            "name": "heart-rate",
            "version": "2.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme heart-rate device",
            "source_creation_date_time": "2020-05-30T00:24:49.873027Z",
            "source_data_point_id": "d0fa9c5c-12cc-42ec-a4dd-8b5c26185d48",
            "modality": "sensed"
        },
        "user_id": "d8ebc5fc-7c2a-4eba-a37e-1cfccf1d024c"
    },
    "body": {
        "heart_rate": {
            "value": 50,
            "unit": "beats/min"
        },
        "effective_time_frame": {
            "time_interval": {
                "start_date_time": "2020-02-05T06:00:00+01:00",
                "end_date_time": "2020-02-06T06:00:00+01:00"
            }
        },
        "descriptive-statistics": "minimum"
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
            "value": "c18a469c-e034-46fb-8f87-edb95a0e083b"
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
                "code": "8867-4",
                "display": "Heart rate"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "d8ebc5fc-7c2a-4eba-a37e-1cfccf1d024c"
        }
    },
    "effectivePeriod": {
        "start": "2020-02-05T06:00:00+01:00",
        "end": "2020-02-06T06:00:00+01:00"
    },
    "issued": "2020-05-30T00:24:49.873027Z",
    "valueQuantity": {
        "value": 50,
        "unit": "beats/min",
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
        "display": "Acme heart-rate device"
    }
}
~~~


### OMH heart-rate schema instance with temporal relationship to sleep
The following OMH heart-rate schema instance with temporal relationship to sleep:
~~~json
{
    "header": {
        "id": "b6ddcb50-0d3d-48eb-b9dd-ecdacac94a69",
        "creation_date_time": "2020-05-30T00:35:35.773317Z",
        "schema_id": {
            "namespace": "omh",
            "name": "heart-rate",
            "version": "2.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme heart-rate device",
            "source_creation_date_time": "2020-05-30T00:35:35.773317Z",
            "source_data_point_id": "bae965cc-fc31-4980-9ac3-fe1fcc0fc179",
            "modality": "sensed"
        },
        "user_id": "f7b52ca1-3a5f-48be-b8a3-54cfca20d4ca"
    },
    "body": {
        "heart_rate": {
            "value": 50,
            "unit": "beats/min"
        },
        "effective_time_frame": {
            "date_time": "2020-02-05T07:25:00-08:00"
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
            "value": "b6ddcb50-0d3d-48eb-b9dd-ecdacac94a69"
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
                "code": "8867-4",
                "display": "Heart rate"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "f7b52ca1-3a5f-48be-b8a3-54cfca20d4ca"
        }
    },
    "effectiveDateTime": "2020-02-05T07:25:00-08:00",
    "issued": "2020-05-30T00:35:35.773317Z",
    "valueQuantity": {
        "value": 50,
        "unit": "beats/min",
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
        "display": "Acme heart-rate device"
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

---
- [name=erichaas]
- [time=Sat, May 30, 2020 1:02 PM]
