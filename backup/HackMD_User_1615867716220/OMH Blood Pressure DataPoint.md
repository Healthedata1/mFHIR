---
tags: omh2fhir
---

{%hackmd 2yYAoTGSSpiWVb7EWu6v0w %}

# OMH Blood Pressure DataPoint

## OMH Blood Pressure DataPoint to FHIR Observation Detailed Mapping

The following Table provides the detailed mapping for the OMH Blood Pressure DataPoint to the OMH to FHIR Observation Profile TODO: add link to map and profile:
|Index|OMH Blood Pressure Element|FHIR Attribute|Mapping Instructions|
|---|---|---|---|
|1|blood-pressure-3.1.json|OMH to FHIR Observation Profile||
|3|body.effective_time_frame|Observation.effective[x]|Mappping depends on type- see below|
|3.1|body.effective_time_frame.date_time|Observation.effectiveDateTime|=  body.effective_time_frame.date_time|
|3.2|body.effective_time_frame.time_interval|Observation.effectivePeriod|see effectivePeriod elements below|
|3.2.1|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start|=  body.effective_time_frame.time_interval.start_date_time|
|3.2.2|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end|=  body.effective_time_frame.time_interval.end_date_time|
|8.1|body.measurement_location|Observation.bodySite|See bodySite elements below|
|8.2|body.measurement_location|Observation.bodySite.coding[0].code|Map body.measurement_location to column 'FHIR Concept' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|8.3|body.measurement_location|Observation.bodySite.coding[0].system|Map body.measurement_location to column 'FHIR Concept System' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|8.4|body.measurement_location|Observation.bodySite.coding[0].display|Map body.measurement_location to column 'FHIR Concept display' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|10|body.descriptive_statistic|Observation.code.coding[1]|Map  descriptive statistic to the OMH to FHIR additional Observation codings ( code system http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes).|
|10.1|body.descriptive_statistic|Observation.code.coding[1].code|concatenation of  header.schema_id.name = 'blood-pressure'  + '-' + body.descriptive_statistic  for example= blood-pressure-maximum|
|10.2|body.descriptive_statistic|Observation.code.coding[1].system|fixed to '"http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes"'|
|10.3|body.descriptive_statistic|Observation.code.coding[1].display|concatenation of  header.schema_id.name = 'blood-pressure'  + '-' + body.descriptive_statistic  for example= blood-pressure-maximum|
|11|body.temporal_relationship_to_physical_activity|Observation.component[0]|A mapping between temporal-relationship-to-physical-activity and FHIR Observation Component data elements.  Multiple components mapping are appended as a list|
|11.A1|body.temporal_relationship_to_physical_activity|Observation.component[0].code|A mapping between body.temporal_relationship_to_physical_activity and FHIR Observation Component.code data elements.|
|11.A2|body.temporal_relationship_to_physical_activity|Observation.component[0].code.coding[1].code|=  'relative-to-activity'|
|11.A3|body.temporal_relationship_to_physical_activity|Observation.component[0].code.coding[1].system|=  "http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes"|
|11.A4|body.temporal_relationship_to_physical_activity|Observation.component[0].code.coding[1].display|=  'OMH to FHIR Temporal Relationship To Physical Activity'|
|11.B1|body.temporal_relationship_to_physical_activity|Observation.component[0].valueCodeableConcept|A mapping between body.temporal_relationship_to_physical_activity and FHIR Observation Component.valueCodeableConcept data elements.|
|11.B2|body.temporal_relationship_to_physical_activity|Observation.component[0].valueCodeableConcept.coding[0].code|Map body.temporal_relationship_to_physical_activity to column 'FHIR Concept' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|11.B3|body.temporal_relationship_to_physical_activity|Observation.component[0].valueCodeableConcept.coding[0].system|Map body.temporal_relationship_to_physical_activity to column 'FHIR Concept System' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|11.B4|body.temporal_relationship_to_physical_activity|Observation.component[0].valueCodeableConcept.coding[0].display|Map body.temporal_relationship_to_physical_activity to column 'FHIR Concept display' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|11.B5|body.temporal_relationship_to_physical_activity|Observation.component[0].valueCodeableConcept.text|=  body.temporal_relationship_to_physical_activity|
|12|body.body_posture|Observation.component[0]|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list|
|12.A1|body.body_posture|Observation.component[0].code|A mapping between body.body_posture and FHIR Observation Component.code data elements.|
|12.A2|body.body_posture|Observation.component[0].code.coding[1].code|=  '271605009'|
|12.A3|body.body_posture|Observation.component[0].code.coding[1].system|=  'http://snomed.info/sct'|
|12.A4|body.body_posture|Observation.component[0].code.coding[1].display|=  'Position of body and posture (observable entity)'|
|12.B1|body.body_posture|Observation.component[0].valueCodeableConcept|A mapping between body.body_posture and FHIR Observation Component.valueCodeableConcept data elements.|
|12.B2|body.body_posture|Observation.component[0].valueCodeableConcept.coding[0].code|Map body.body_posture to column 'FHIR Concept' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|12.B3|body.body_posture|Observation.component[0].valueCodeableConcept.coding[0].system|Map body.body_posture to column 'FHIR Concept System' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|12.B4|body.body_posture|Observation.component[0].valueCodeableConcept.coding[0].display|Map body.body_posture to column 'FHIR Concept display' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|12.B5|body.body_posture|Observation.component[0].valueCodeableConcept.text|=  body.body_posture|
|13|body.diastolic_blood_pressure|Observation.component[0]|A mapping  between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components are appended as a list|
|13.A1|body.diastolic_blood_pressure|Observation.component[0].code|A mapping between body.diastolic_blood_pressure and FHIR Observation Component.code data elements.|
|13.A2|body.diastolic_blood_pressure|Observation.component[0].code.coding[1].code|=  '8462-4'|
|13.A3|body.diastolic_blood_pressure|Observation.component[0].code.coding[1].system|=  'http://loinc.org'|
|13.A4|body.diastolic_blood_pressure|Observation.component[0].code.coding[1].display|=  'Diastolic blood pressure'|
|13.B1|body.diastolic_blood_pressure|Observation.component[0].valueQuantity|see valueQuantity elements below|
|13.B2|body.diastolic_blood_pressure|Observation.component[0].valueQuantity.value|=  body.diastolic_blood_pressure|
|13.B3|body.diastolic_blood_pressure|Observation.component[0].valueQuantity.unit|=  'mmHg'|
|13.B4|body.diastolic_blood_pressure|Observation.component[0].valueQuantity.system|fixed to 'http://unitsofmeasure.org'|
|13.B5|body.diastolic_blood_pressure|Observation.component[0].valueQuantity.code|=  'mm[Hg]'|
|14|body.systolic_blood_pressure|Observation.component[0]|A mapping  between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components are appended as a list|
|14.A1|body.systolic_blood_pressure|Observation.component[0].code|0|
|14.A2|body.systolic_blood_pressure|Observation.component[0].code.coding[1].code|=  '8480-6'|
|14.A3|body.systolic_blood_pressure|Observation.component[0].code.coding[1].system|=  'http://loinc.org'|
|14.A4|body.systolic_blood_pressure|Observation.component[0].code.coding[1].display|=  'Systolic blood pressure'|
|14.B1|body.systolic_blood_pressure|Observation.component[0].valueQuantity|see valueQuantity elements below|
|14.B2|body.systolic_blood_pressure.value|Observation.component[0].valueQuantity.value|=  body.systolic_blood_pressure.value|
|14.B3|body.systolic_blood_pressure.unit|Observation.component[0].valueQuantity.unit|=  'mmHg'|
|14.B4|body.systolic_blood_pressure.unit|Observation.component[0].valueQuantity.system|fixed to 'http://unitsofmeasure.org'|
|14.B5|body.systolic_blood_pressure.unit|Observation.component[0].valueQuantity.code|=  'mm[Hg]'|

## Examples:

### OMH blood-pressure schema instance

The following OMH blood-pressure schema instance:

~~~json
{
    "header": {
        "id": "3f4a6a06-8613-4186-b004-6a1df5bfab0c",
        "creation_date_time": "2020-05-30T01:47:30.787746Z",
        "schema_id": {
            "namespace": "omh",
            "name": "blood-pressure",
            "version": "3.1"
        },
        "acquisition_provenance": {
            "source_name": "Acme blood-pressure device",
            "source_creation_date_time": "2020-05-30T01:47:30.787746Z",
            "source_data_point_id": "901fd78b-1a23-4eac-ba5e-b7a8b168082f",
            "modality": "sensed"
        },
        "user_id": "62d9a6cc-4a8f-455d-926b-6929ff88c635"
    },
    "body": {
        "systolic_blood_pressure": {
            "value": 115,
            "unit": "mmHg"
        },
        "diastolic_blood_pressure": {
            "value": 60,
            "unit": "mmHg"
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
            "value": "3f4a6a06-8613-4186-b004-6a1df5bfab0c"
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
                "code": "85354-9",
                "display": "Blood pressure panel with all children optional"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "62d9a6cc-4a8f-455d-926b-6929ff88c635"
        }
    },
    "effectiveDateTime": "2020-02-05T07:25:00-08:00",
    "issued": "2020-05-30T01:47:30.787746Z",
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme blood-pressure device"
    },
    "component": [
        {
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "8462-4",
                        "display": "Diastolic blood pressure"
                    }
                ]
            },
            "valueQuantity": {
                "value": 60,
                "unit": "mmHg",
                "system": "http://unitsofmeasure.org",
                "code": "mm[Hg]"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "8480-6",
                        "display": "Systolic blood pressure"
                    }
                ]
            },
            "valueQuantity": {
                "value": 115,
                "unit": "mmHg",
                "system": "http://unitsofmeasure.org",
                "code": "mm[Hg]"
            }
        }
    ]
}
~~~

### OMH blood-pressure schema instance - with posture and location

The following OMH blood-pressure schema instance:

~~~json
{
    "header": {
        "id": "44be6623-1b96-4e6d-880f-db5b43baf2c4",
        "creation_date_time": "2020-05-30T01:49:02.722676Z",
        "schema_id": {
            "namespace": "omh",
            "name": "blood-pressure",
            "version": "3.1"
        },
        "acquisition_provenance": {
            "source_name": "Acme blood-pressure device",
            "source_creation_date_time": "2020-05-30T01:49:02.722676Z",
            "source_data_point_id": "4ca1c2e0-df11-4e1b-855c-3e57611914ee",
            "modality": "sensed"
        },
        "user_id": "f1dce69b-b129-4579-be97-2025e5de2326"
    },
    "body": {
        "systolic_blood_pressure": {
            "value": 140,
            "unit": "mmHg"
        },
        "diastolic_blood_pressure": {
            "value": 60,
            "unit": "mmHg"
        },
        "body_posture": "sitting",
        "measurement_location": "left upper arm",
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
            "value": "44be6623-1b96-4e6d-880f-db5b43baf2c4"
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
                "code": "85354-9",
                "display": "Blood pressure panel with all children optional"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "f1dce69b-b129-4579-be97-2025e5de2326"
        }
    },
    "effectiveDateTime": "2020-02-05T07:25:00-08:00",
    "issued": "2020-05-30T01:49:02.722676Z",
    "bodySite": {
        "coding": [
            {
                "system": "http://www.fhir.org/guides/mfhir/CodeSystem/body-location",
                "code": "left upper arm"
            }
        ],
        "text": "left upper arm"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme blood-pressure device"
    },
    "component": [
        {
            "code": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "271605009",
                        "display": "Position of body and posture (observable entity)"
                    }
                ]
            },
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "33586001",
                        "display": "Sitting position"
                    }
                ],
                "text": "sitting"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "8462-4",
                        "display": "Diastolic blood pressure"
                    }
                ]
            },
            "valueQuantity": {
                "value": 60,
                "unit": "mmHg",
                "system": "http://unitsofmeasure.org",
                "code": "mm[Hg]"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "8480-6",
                        "display": "Systolic blood pressure"
                    }
                ]
            },
            "valueQuantity": {
                "value": 140,
                "unit": "mmHg",
                "system": "http://unitsofmeasure.org",
                "code": "mm[Hg]"
            }
        }
    ]
}
~~~

### OMH blood-pressure schema instance - with descriptive statistic

The following OMH blood-pressure schema instance:

~~~json
{
    "header": {
        "id": "95858035-3be4-4ff4-9acd-abf28bcc6132",
        "creation_date_time": "2020-05-30T01:52:37.530636Z",
        "schema_id": {
            "namespace": "omh",
            "name": "blood-pressure",
            "version": "3.1"
        },
        "acquisition_provenance": {
            "source_name": "Acme blood-pressure device",
            "source_creation_date_time": "2020-05-30T01:52:37.530636Z",
            "source_data_point_id": "1cf6b6f3-98c9-45ab-9cfd-11fbc784ed7a",
            "modality": "sensed"
        },
        "user_id": "4540ac92-0183-4dc1-8e6e-307b4fa945b2"
    },
    "body": {
        "systolic_blood_pressure": {
            "value": 160,
            "unit": "mmHg"
        },
        "diastolic_blood_pressure": {
            "value": 60,
            "unit": "mmHg"
        },
        "effective_time_frame": {
            "time_interval": {
                "start_date_time": "2020-02-05T07:00:00-08:00",
                "end_date_time": "2020-02-12T07:00:00-08:00"
            }
        },
        "body_posture": "sitting",
        "measurement_location": "left wrist",
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
            "value": "95858035-3be4-4ff4-9acd-abf28bcc6132"
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
                "code": "85354-9",
                "display": "Blood pressure panel with all children optional"
            },
            {
                "system": "http://hl7.org/fhir/omh_fhir_observation_codes",
                "code": "blood-pressure-maximum",
                "display": "Blood Pressure-Maximum"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "4540ac92-0183-4dc1-8e6e-307b4fa945b2"
        }
    },
    "effectivePeriod": {
        "start": "2020-02-05T07:00:00-08:00",
        "end": "2020-02-12T07:00:00-08:00"
    },
    "issued": "2020-05-30T01:52:37.530636Z",
    "bodySite": {
        "coding": [
            {
                "system": "http://www.fhir.org/guides/mfhir/CodeSystem/body-location",
                "code": "left wrist"
            }
        ],
        "text": "left wrist"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme blood-pressure device"
    },
    "component": [
        {
            "code": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "271605009",
                        "display": "Position of body and posture (observable entity)"
                    }
                ]
            },
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "33586001",
                        "display": "Sitting position"
                    }
                ],
                "text": "sitting"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "8462-4",
                        "display": "Diastolic blood pressure"
                    }
                ]
            },
            "valueQuantity": {
                "value": 60,
                "unit": "mmHg",
                "system": "http://unitsofmeasure.org",
                "code": "mm[Hg]"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "8480-6",
                        "display": "Systolic blood pressure"
                    }
                ]
            },
            "valueQuantity": {
                "value": 160,
                "unit": "mmHg",
                "system": "http://unitsofmeasure.org",
                "code": "mm[Hg]"
            }
        }
    ]
}
~~~

### OMH blood-pressure schema instance - with posture location and relation to physical activity

The following OMH blood-pressure schema instance:

~~~json
{
    "header": {
        "id": "c87d4272-0f9a-4cf7-bff8-54113e9d4f31",
        "creation_date_time": "2020-05-30T01:54:59.483554Z",
        "schema_id": {
            "namespace": "omh",
            "name": "blood-pressure",
            "version": "3.1"
        },
        "acquisition_provenance": {
            "source_name": "Acme blood-pressure device",
            "source_creation_date_time": "2020-05-30T01:54:59.483554Z",
            "source_data_point_id": "c68a592d-b776-424c-b6cc-f7427a1779d4",
            "modality": "sensed"
        },
        "user_id": "7cc36b4a-ecb1-4b87-a70d-348e27eb4d6d"
    },
    "body": {
        "systolic_blood_pressure": {
            "value": 125,
            "unit": "mmHg"
        },
        "diastolic_blood_pressure": {
            "value": 60,
            "unit": "mmHg"
        },
        "body_posture": "sitting",
        "measurement_location": "left wrist",
        "temporal_relationship_to_physical_activity": "at rest",
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
            "value": "c87d4272-0f9a-4cf7-bff8-54113e9d4f31"
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
                "code": "85354-9",
                "display": "Blood pressure panel with all children optional"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "7cc36b4a-ecb1-4b87-a70d-348e27eb4d6d"
        }
    },
    "effectiveDateTime": "2020-02-05T07:25:00-08:00",
    "issued": "2020-05-30T01:54:59.483554Z",
    "bodySite": {
        "coding": [
            {
                "system": "http://www.fhir.org/guides/mfhir/CodeSystem/body-location",
                "code": "left wrist"
            }
        ],
        "text": "left wrist"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme blood-pressure device"
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
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "271605009",
                        "display": "Position of body and posture (observable entity)"
                    }
                ]
            },
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "33586001",
                        "display": "Sitting position"
                    }
                ],
                "text": "sitting"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "8462-4",
                        "display": "Diastolic blood pressure"
                    }
                ]
            },
            "valueQuantity": {
                "value": 60,
                "unit": "mmHg",
                "system": "http://unitsofmeasure.org",
                "code": "mm[Hg]"
            }
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "8480-6",
                        "display": "Systolic blood pressure"
                    }
                ]
            },
            "valueQuantity": {
                "value": 125,
                "unit": "mmHg",
                "system": "http://unitsofmeasure.org",
                "code": "mm[Hg]"
            }
        }
    ]
}
