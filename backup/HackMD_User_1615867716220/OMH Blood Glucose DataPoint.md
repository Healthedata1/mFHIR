---
tags: omh2fhir
---

{%hackmd 2yYAoTGSSpiWVb7EWu6v0w %}

# OMH Blood Glucose DataPoint

## OMH Blood Glucose DataPoint to FHIR Observation Detailed Mapping

The following Table provides the detailed mapping for the OMH Blood Glucose DataPoint to the OMH to FHIR Observation Profile TODO: add link to map and profile:
|Index|OMH Blood Glucose Element|FHIR Attribute|Mapping Instructions|
|---|---|---|---|
|1|blood-glucose-3.0.json|OMH to FHIR Observation Profile||
|2.1|body.blood_glucose|Observation.valueQuantity|see valueQuantity elements below|
|2.2|body.blood_glucose.value|Observation.valueQuantity.value|=  body.blood_glucose.value|
|2.3|body.blood_glucose.unit|Observation.valueQuantity.unit|=  body.blood_glucose.unit|
|2.4|body.blood_glucose.unit|valueQuantity.system|fixed to 'http://unitsofmeasure.org'|
|2.5|body.blood_glucose.unit|valueQuantity.code|Map body.blood_glucose.unit to column 'FHIR Concept' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|3|body.effective_time_frame|Observation.effective[x]|Mappping depends on type- see below|
|5|body.effective_time_frame.date_time|Observation.effectiveDateTime|=  body.effective_time_frame.date_time|
|4|body.effective_time_frame.time_interval|Observation.effectivePeriod|see effectivePeriod.elements below|
|6|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start|=  body.effective_time_frame.time_interval.start_date_time|
|7|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end|=  body.effective_time_frame.time_interval.end_date_time|
|9.1|body.specimen_source|Observation.extension|extension see below for extension elements|
|9.2|body.specimen_source|Observation.extension[0].url|fixed to 'http://hl7.org/fhir/StructureDefinition/observation-specimenCode'|
|9.3|body.specimen_source|Observation.extension[0].valueCodeableConcept|see CodeableConcept below:|
|9.4|body.specimen_source|Observation.extension[0].valueCodeableConcept.coding[0].code|Map body.specimen_source to column 'FHIR Concept' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|9.5|body.specimen_source|Observation.extension[0].valueCodeableConcept.coding[0].system|Map body.specimen_source to column 'FHIR Concept System' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|9.6|body.specimen_source|Observation.extension[0].valueCodeableConcept.coding[0].display|Map body.specimen_source to column 'FHIR Concept Display' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|11.1|body.descriptive_statistic|Observation.code.coding[1].code|concatenation of  header.schema_id.name = 'blood-glucose'  + '-' + body.descriptive_statistic  for example= blood-glucose-maximum|
|11.2|body.descriptive_statistic|Observation.code.coding[1].system|fixed to '"http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes"'|
|11.3|body.descriptive_statistic|Observation.code.coding[1].display|concatenation of  header.schema_id.name = 'blood-glucose'  + '-' + body.descriptive_statistic  for example= blood-glucose-maximum|
|11|body.temporal_relationship_to_physical_activity|Observation.component[0]|A mapping between temporal-relationship-to-physical-activity and FHIR Observation Component data elements.  Multiple components mapping are appended as a list|
|11.A1|body.temporal_relationship_to_physical_activity|Observation.component[0].code|A mapping between temporal-relationship-to-physical-activity and FHIR Observation Component.code data elements.|
|11.A2|body.temporal_relationship_to_physical_activity|Observation.component[0].code.coding[1].code|=  'relative-to-activity'|
|11.A3|body.temporal_relationship_to_physical_activity|Observation.component[0].code.coding[1].system|=  "http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes"|
|11.A4|body.temporal_relationship_to_physical_activity|Observation.component[0].code.coding[1].display|=  'OMH to FHIR Temporal Relationship To Physical Activity'|
|11.B1|body.temporal_relationship_to_physical_activity|Observation.component[0].valueCodeableConcept|A mapping between body.temporal_relationship_to_physical_activity and FHIR Observation Component.valueCodeableConcept data elements.|
|11.B2|body.temporal_relationship_to_physical_activity|Observation.component[0].valueCodeableConcept.coding[0].code|Map body.temporal_relationship_to_physical_activity to column 'FHIR Concept' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|11.B3|body.temporal_relationship_to_physical_activity|Observation.component[0].valueCodeableConcept.coding[0].system|Map body.temporal_relationship_to_physical_activity to column 'FHIR Concept System' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|11.B4|body.temporal_relationship_to_physical_activity|Observation.component[0].valueCodeableConcept.coding[0].display|Map body.temporal_relationship_to_physical_activity to column 'FHIR Concept display' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|11.B5|body.temporal_relationship_to_physical_activity|Observation.component[0].valueCodeableConcept.text|=  body.temporal_relationship_to_physical_activity|
|12|body.temporal_relationship_to_sleep|Observation.component[0]|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list|
|12.A1|body.temporal_relationship_to_sleep|Observation.component[0].code|A mapping between temporal-relationship-to-sleep and FHIR Observation Component.code data elements.|
|12.A2|body.temporal_relationship_to_sleep|Observation.component[0].code.coding[1].code|=  'relative-to-sleep'|
|12.A3|body.temporal_relationship_to_sleep|Observation.component[0].code.coding[1].system|=  "http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes"|
|12.A4|body.temporal_relationship_to_sleep|Observation.component[0].code.coding[1].display|=  'OMH to FHIR Temporal Relationship To Sleep'|
|12.B1|body.temporal_relationship_to_sleep|Observation.component[0].valueCodeableConcept|A mapping between body.temporal_relationship_to_sleep and FHIR Observation Component.valueCodeableConcept data elements.|
|12.B2|body.temporal_relationship_to_sleep|Observation.component[0].valueCodeableConcept.coding[0].code|Map body.temporal_relationship_to_sleep to column 'FHIR Concept' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|12.B3|body.temporal_relationship_to_sleep|Observation.component[0].valueCodeableConcept.coding[0].system|Map body.temporal_relationship_to_sleep to column 'FHIR Concept System' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|12.B4|body.temporal_relationship_to_sleep|Observation.component[0].valueCodeableConcept.coding[0].display|Map body.temporal_relationship_to_sleep to column 'FHIR Concept display' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|12.B5|body.temporal_relationship_to_sleep|Observation.component[0].valueCodeableConcept.text|=  body.temporal_relationship_to_sleep|
|13|temporal_relationship_to_meal|Observation.component|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list|
|13.A1|body.temporal_relationship_to_meal|Observation.component[0].code|A mapping between temporal-relationship-to-meal and FHIR Observation Component.code data elements.|
|13.A2|body.temporal_relationship_to_meal|Observation.component[0].code.coding[1].code|=  'relative-to-meal'|
|13.A3|body.temporal_relationship_to_meal|Observation.component[0].code.coding[1].system|=  "http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes"|
|13.A4|body.temporal_relationship_to_meal|Observation.component[0].code.coding[1].display|=  'OMH to FHIR Temporal Relationship To Meal'|
|13.B1|body.temporal_relationship_to_meal|Observation.component[0].valueCodeableConcept|A mapping between body.temporal_relationship_to_meal and FHIR Observation Component.valueCodeableConcept data elements.|
|13.B2|body.temporal_relationship_to_meal|Observation.component[0].valueCodeableConcept.coding[0].code|Map body.temporal_relationship_to_meal to column 'FHIR Concept' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|13.B3|body.temporal_relationship_to_meal|Observation.component[0].valueCodeableConcept.coding[0].system|Map body.temporal_relationship_to_meal to column 'FHIR Concept System' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|13.B4|body.temporal_relationship_to_meal|Observation.component[0].valueCodeableConcept.coding[0].display|Map body.temporal_relationship_to_meal to column 'FHIR Concept display' using  the [OMH_FHIR_Concept_Mapping_Table](#)|
|13.B5|body.temporal_relationship_to_meal|Observation.component[0].valueCodeableConcept.text|=  body.temporal_relationship_to_meal|

## Examples:

### OMH blood-glucose schema instance - datetime

The following OMH blood-glucose schema instance:

~~~json
{
    "header": {
        "id": "9fa5f90b-620e-4893-a6f3-c9c169bb4bee",
        "creation_date_time": "2020-05-30T03:31:50.560232Z",
        "schema_id": {
            "namespace": "omh",
            "name": "blood-glucose",
            "version": "3.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme blood-glucose device",
            "source_creation_date_time": "2020-05-30T03:31:50.560232Z",
            "source_data_point_id": "dae0e356-1faf-46de-810b-10b36ac1700e",
            "modality": "sensed"
        },
        "user_id": "859fd9f8-a8a3-47aa-ae69-8148eaa411d9"
    },
    "body": {
        "blood_glucose": {
            "unit": "mg/dL",
            "value": 95
        },
        "effective_time_frame": {
            "date_time": "2013-02-05T07:25:00Z"
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
            "value": "9fa5f90b-620e-4893-a6f3-c9c169bb4bee"
        }
    ],
    "status": "unknown",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "laboratory",
                    "display": "Laboratory"
                }
            ]
        }
    ],
    "code": {
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "2339-0",
                "display": "Glucose Mass/volume in Blood"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "859fd9f8-a8a3-47aa-ae69-8148eaa411d9"
        }
    },
    "effectiveDateTime": "2013-02-05T07:25:00Z",
    "issued": "2020-05-30T03:31:50.560232Z",
    "valueQuantity": {
        "value": 95,
        "unit": "mg/dL",
        "system": "http://unitsofmeasure.org",
        "code": "mg/dL"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme blood-glucose device"
    }
}
~~~

### OMH blood-glucose schema instance with descriptive statistic

The following OMH blood-glucose schema instance:

~~~json
{
    "header": {
        "id": "469ac514-1aae-4d1d-93d7-7eea5d376f7a",
        "creation_date_time": "2020-05-30T03:30:35.559919Z",
        "schema_id": {
            "namespace": "omh",
            "name": "blood-glucose",
            "version": "1.2"
        },
        "acquisition_provenance": {
            "source_name": "Acme blood-glucose device",
            "source_creation_date_time": "2020-05-30T03:30:35.559919Z",
            "source_data_point_id": "e0ce6667-2c7f-4245-a3b2-aeb33aa34f94",
            "modality": "sensed"
        },
        "user_id": "624b14ea-46c3-4b8e-abe0-f5e2387201b5"
    },
    "body": {
        "blood_glucose": {
            "unit": "mg/dL",
            "value": 120
        },
        "effective_time_frame": {
            "time_interval": {
                "start_date_time": "2013-02-05T07:25:00Z",
                "end_date_time": "2013-06-05T07:25:00Z"
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
            "value": "469ac514-1aae-4d1d-93d7-7eea5d376f7a"
        }
    ],
    "status": "unknown",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "laboratory",
                    "display": "Laboratory"
                }
            ]
        }
    ],
    "code": {
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "2339-0",
                "display": "Glucose Mass/volume in Blood"
            },
            {
                "system": "http://hl7.org/fhir/omh_fhir_observation_codes",
                "code": "blood-glucose-minimum",
                "display": "Blood Glucose-Minimum"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "624b14ea-46c3-4b8e-abe0-f5e2387201b5"
        }
    },
    "effectivePeriod": {
        "start": "2013-02-05T07:25:00Z",
        "end": "2013-06-05T07:25:00Z"
    },
    "issued": "2020-05-30T03:30:35.559919Z",
    "valueQuantity": {
        "value": 120,
        "unit": "mg/dL",
        "system": "http://unitsofmeasure.org",
        "code": "mg/dL"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme blood-glucose device"
    }
}
~~~

### OMH blood-glucose schema instance - with temporal relationship to sleep

The following OMH blood-glucose schema instance:

~~~json
{
    "header": {
        "id": "3f657894-8204-434d-a9b4-a3496ae79fcf",
        "creation_date_time": "2020-05-30T03:33:12.483094Z",
        "schema_id": {
            "namespace": "omh",
            "name": "blood-glucose",
            "version": "3.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme blood-glucose device",
            "source_creation_date_time": "2020-05-30T03:33:12.483094Z",
            "source_data_point_id": "d2d7386e-2803-4e83-9e7e-6d202155f7cd",
            "modality": "sensed"
        },
        "user_id": "538c4831-e7c5-43cf-b173-c23653e4f500"
    },
    "body": {
        "blood_glucose": {
            "unit": "mg/dL",
            "value": 95
        },
        "effective_time_frame": {
            "date_time": "2013-02-05T20:25:00Z"
        },
        "temporal_relationship_to_sleep": "before sleeping"
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
            "value": "3f657894-8204-434d-a9b4-a3496ae79fcf"
        }
    ],
    "status": "unknown",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "laboratory",
                    "display": "Laboratory"
                }
            ]
        }
    ],
    "code": {
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "2339-0",
                "display": "Glucose Mass/volume in Blood"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "538c4831-e7c5-43cf-b173-c23653e4f500"
        }
    },
    "effectiveDateTime": "2013-02-05T20:25:00Z",
    "issued": "2020-05-30T03:33:12.483094Z",
    "valueQuantity": {
        "value": 95,
        "unit": "mg/dL",
        "system": "http://unitsofmeasure.org",
        "code": "mg/dL"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme blood-glucose device"
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
                        "code": "307155000",
                        "display": "Before sleeping"
                    }
                ],
                "text": "before sleeping"
            }
        }
    ]
}
~~~

### OMH blood-glucose schema instance - with temporal relationship to a meal

The following OMH blood-glucose schema instance:

~~~json
{
    "header": {
        "id": "23177f74-8cc1-42c3-a0c6-fd71477af504",
        "creation_date_time": "2020-05-30T03:34:38.031901Z",
        "schema_id": {
            "namespace": "omh",
            "name": "blood-glucose",
            "version": "3.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme blood-glucose device",
            "source_creation_date_time": "2020-05-30T03:34:38.031901Z",
            "source_data_point_id": "70786f4d-890e-4012-9445-cde3f1342493",
            "modality": "sensed"
        },
        "user_id": "6d9b1f6e-bffc-47f3-a677-5414845c220a"
    },
    "body": {
        "blood_glucose": {
            "unit": "mg/dL",
            "value": 95
        },
        "effective_time_frame": {
            "date_time": "2013-02-05T07:25:00Z"
        },
        "temporal_relationship_to_meal": "fasting"
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
            "value": "23177f74-8cc1-42c3-a0c6-fd71477af504"
        }
    ],
    "status": "unknown",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "laboratory",
                    "display": "Laboratory"
                }
            ]
        }
    ],
    "code": {
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "2339-0",
                "display": "Glucose Mass/volume in Blood"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "6d9b1f6e-bffc-47f3-a677-5414845c220a"
        }
    },
    "effectiveDateTime": "2013-02-05T07:25:00Z",
    "issued": "2020-05-30T03:34:38.031901Z",
    "valueQuantity": {
        "value": 95,
        "unit": "mg/dL",
        "system": "http://unitsofmeasure.org",
        "code": "mg/dL"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme blood-glucose device"
    },
    "component": [
        {
            "code": {
                "coding": [
                    {
                        "system": "http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes",
                        "code": "relative-to-meal",
                        "display": "OMH to FHIR Temporal Relationship To Meal"
                    }
                ]
            },
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "16985007",
                        "display": "Fasting"
                    }
                ],
                "text": "fasting"
            }
        }
    ]
}
~~~

### OMH blood-glucose schema instance - with everything


The following OMH blood-glucose schema instance:

~~~json
{
    "header": {
        "id": "e6493aae-31da-4ed5-a812-ca963c515401",
        "creation_date_time": "2020-05-30T03:43:00.484828Z",
        "schema_id": {
            "namespace": "omh",
            "name": "blood-glucose",
            "version": "3.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme blood-glucose device",
            "source_creation_date_time": "2020-05-30T03:43:00.484828Z",
            "source_data_point_id": "f670ce71-9072-4c73-80f1-319174e0be6a",
            "modality": "sensed"
        },
        "user_id": "93a24cc0-3467-4a97-a205-d7345716c060"
    },
    "body": {
        "blood_glucose": {
            "unit": "mg/dL",
            "value": 95
        },
        "effective_time_frame": {
            "time_interval": {
                "start_date_time": "2013-02-05T07:25:00Z",
                "end_date_time": "2013-06-05T07:25:00Z"
            }
        },
        "specimen_source": "capillary blood",
        "temporal_relationship_to_meal": "fasting",
        "temporal_relationship_to_sleep": "on waking",
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
    "extension": [
        {
            "url": "http://hl7.org/fhir/StructureDefinition/observation-specimenCode",
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "122554006",
                        "display": "Capillary blood sample"
                    }
                ],
                "text": "capillary blood"
            }
        }
    ],
    "identifier": [
        {
            "system": "https://omh.org/shimmer/ids",
            "value": "e6493aae-31da-4ed5-a812-ca963c515401"
        }
    ],
    "status": "unknown",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "laboratory",
                    "display": "Laboratory"
                }
            ]
        }
    ],
    "code": {
        "coding": [
            {
                "system": "http://loinc.org",
                "code": "2339-0",
                "display": "Glucose Mass/volume in Blood"
            },
            {
                "system": "http://hl7.org/fhir/omh_fhir_observation_codes",
                "code": "blood-glucose-minimum",
                "display": "Blood Glucose-Minimum"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "93a24cc0-3467-4a97-a205-d7345716c060"
        }
    },
    "effectivePeriod": {
        "start": "2013-02-05T07:25:00Z",
        "end": "2013-06-05T07:25:00Z"
    },
    "issued": "2020-05-30T03:43:00.484828Z",
    "valueQuantity": {
        "value": 95,
        "unit": "mg/dL",
        "system": "http://unitsofmeasure.org",
        "code": "mg/dL"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme blood-glucose device"
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
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes",
                        "code": "relative-to-meal",
                        "display": "OMH to FHIR Temporal Relationship To Meal"
                    }
                ]
            },
            "valueCodeableConcept": {
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "16985007",
                        "display": "Fasting"
                    }
                ],
                "text": "fasting"
            }
        }
    ]
}
~~~