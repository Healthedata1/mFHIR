---
tags: omh2fhir
---

{%hackmd 2yYAoTGSSpiWVb7EWu6v0w %}

# OMH Oxygen Saturation DataPoint 

Markdown Transform
## OMH Oxygen Saturation DataPoint to FHIR Observation Detailed Mapping

The following Table provides the detailed mapping for the OMH Oxygen Saturation DataPoint to the OMH to FHIR Observation Profile TODO: add link to map and profile:
|Index|OMH Oxygen Saturation Element|FHIR Attribute|Mapping Instructions|
|---|---|---|---|
|1|oxygen-saturation-2.0.json|OMH to FHIR Observation Profile||
|2.1|oxygen_saturation|Observation.valueQuantity|see valueQuantity elements below|
|2.2|oxygen_saturation.value|Observation.valueQuantity.value|=  oxygen_saturation.value|
|2.3|oxygen_saturation.unit|Observation.valueQuantity.unit|=  '%'|
|2.4|oxygen_saturation.unit|Observation.valueQuantity.system|fixed to 'http://unitsofmeasure.org'|
|2.5|oxygen_saturation.unit|Observation.valueQuantity.code|=  '%'|
|3|body.effective_time_frame|Observation.effective[x]|Mappping depends on type- see below|
|4|body.effective_time_frame.date_time|Observation.effectiveDateTime|=  body.effective_time_frame.date_time|
|5|body.effective_time_frame.time_interval|Observation.effectivePeriod|see effectivePeriod elements below|
|6|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start|=  body.effective_time_frame.time_interval.start_date_time|
|7|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end|=  body.effective_time_frame.time_interval.end_date_time|
|8|body.measurement_method|Observation.code|Header.schema_id.name = 'oxygen-saturation'  mapped to  LOINC code 59408-5 Oxygen saturation in Arterial blood by Pulse oximetry which includes the method and system  properties.|
|9|body.system|Observation.code|Header.schema_id.name = 'oxygen-saturation'  mapped to  LOINC code 59408-5 Oxygen saturation in Arterial blood by Pulse oximetry which includes the method and system  properties.|
|10|body.descriptive_statistic|Observation.code.coding[1]|Map  descriptive statistic to the OMH to FHIR additional Observation codings ( code system http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes).|
|10.1|body.descriptive_statistic|Observation.code.coding[1].code|concatenation of  header.schema_id.name = 'oxygen-saturation'  + '-' + body.descriptive_statistic  for example= oxygen-saturation-maximum|
|10.2|body.descriptive_statistic|Observation.code.coding[1].system|= 'http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes''|
|10.3|body.descriptive_statistic|Observation.code.coding[1].display|concatenation of  header.schema_id.name = 'oxygen-saturation'  + '-' + body.descriptive_statistic  for example= oxygen-saturation-maximum|
|11|body.supplemental_oxygen_flow_rate|Observation.component[0]|A mapping between  and FHIR Observation Component data elements.  Multiple components mapping are appended as a list|
|11.A1|body.supplemental_oxygen_flow_rate|Observation.component[0].code|A mapping between  and FHIR Observation Component.code data elements.|
|11.A2|body.supplemental_oxygen_flow_rate|Observation.component[0].code.coding[1].code|= 3151-8'|
|11.A3|body.supplemental_oxygen_flow_rate|Observation.component[0].code.coding[1].system|= 'http://loinc.org''|
|11.A4|body.supplemental_oxygen_flow_rate|Observation.component[0].code.coding[1].display|= 'Inhaled oxygen flow rate''|
|11.B1|body.supplemental_oxygen_flow_rate|Observation.component[0].valueQuantity|see valueQuantity elements below|
|11.B2|body.supplemental_oxygen_flow_rate.value|Observation.component[0].valueQuantity.value|=  body.supplemental_oxygen_flow_rate.value|
|11.B3|body.supplemental_oxygen_flow_rate.unit|Observation.component[0].valueQuantity.unit|=  body.supplemental_oxygen_flow_rate.unit|
|11.B4|body.supplemental_oxygen_flow_rate.unit|Observation.component[0].valueQuantity.system|= http://unitsofmeasure.org'|
|11.B5|body.supplemental_oxygen_flow_rate.unit|Observation.component[0].valueQuantity.code|= l/min'|
|12|body.oxygen_therapy_mode_of_administration|Observation.component[1]|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list|
|12.A1|body.oxygen_therapy_mode_of_administration|Observation.component[1].code|A mapping between  and FHIR Observation Component.code data elements.|
|12.A2|body.oxygen_therapy_mode_of_administration|Observation.component[1].code.coding[1].code|= 'o2-administration-mode''|
|12.A3|body.oxygen_therapy_mode_of_administration|Observation.component[1].code.coding[1].system|= 'http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes''|
|12.A4|body.oxygen_therapy_mode_of_administration|Observation.component[1].code.coding[1].display|= 'Oxygen Therapy Mode of Administration''|
|12.B1|body.oxygen_therapy_mode_of_administration|Observation.component[1].valueString|=  'nasal cannula'|

## Examples


### OMH oxygen-saturation schema instance

The following OMH oxygen-saturation schema instance:

~~~json
{
    "header": {
        "id": "1deeae29-b50b-46db-851d-b64c7df756df",
        "creation_date_time": "2020-05-30T03:46:23.483351Z",
        "schema_id": {
            "namespace": "omh",
            "name": "oxygen-saturation",
            "version": "2.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme oxygen-saturation device",
            "source_creation_date_time": "2020-05-30T03:46:23.483351Z",
            "source_data_point_id": "1a97e7fb-eb1f-4099-b8fc-09ddc911914b",
            "modality": "sensed"
        },
        "user_id": "cfa9a00d-7147-4871-8876-7c100ae4e8b5"
    },
    "body": {
        "oxygen_saturation": {
            "value": 95,
            "unit": "%"
        },
        "effective_time_frame": {
            "date_time": "2013-02-05T07:25:00-08:00"
        },
        "system": "peripheral capillary",
        "measurement_method": "pulse oximetry"
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
            "value": "1deeae29-b50b-46db-851d-b64c7df756df"
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
                "code": "59408-5",
                "display": "Oxygen saturation in Arterial blood by Pulse oximetry"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "cfa9a00d-7147-4871-8876-7c100ae4e8b5"
        }
    },
    "effectiveDateTime": "2013-02-05T07:25:00-08:00",
    "issued": "2020-05-30T03:46:23.483351Z",
    "valueQuantity": {
        "value": 95,
        "unit": "%",
        "system": "http://unitsofmeasure.org",
        "code": "%"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme oxygen-saturation device"
    }
}
~~~

### OMH oxygen-saturation schema instance - minimum

The following OMH oxygen-saturation schema instance:

~~~json
{
    "header": {
        "id": "f7beea43-b5a6-4cfe-b02f-99b73b988e0a",
        "creation_date_time": "2020-05-30T03:57:29.413990Z",
        "schema_id": {
            "namespace": "omh",
            "name": "oxygen-saturation",
            "version": "1.2"
        },
        "acquisition_provenance": {
            "source_name": "Acme oxygen-saturation device",
            "source_creation_date_time": "2020-05-30T03:57:29.413990Z",
            "source_data_point_id": "8cf7c758-c1b6-461e-9826-a664f777f8d4",
            "modality": "sensed"
        },
        "user_id": "1bda5f88-f1d7-43a9-b6d6-e0fc7da109c5"
    },
    "body": {
        "oxygen_saturation": {
            "value": 93,
            "unit": "%"
        },
        "effective_time_frame": {
            "time_interval": {
                "start_date_time": "2020-02-05T06:00:00+01:00",
                "end_date_time": "2020-02-06T06:00:00+01:00"
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
            "value": "f7beea43-b5a6-4cfe-b02f-99b73b988e0a"
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
                "code": "59408-5",
                "display": "Oxygen saturation in Arterial blood by Pulse oximetry"
            },
            {
                "system": "http://hl7.org/fhir/omh_fhir_observation_codes",
                "code": "oxygen-saturation-minimum",
                "display": "Oxygen Saturation-Minimum"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "1bda5f88-f1d7-43a9-b6d6-e0fc7da109c5"
        }
    },
    "effectivePeriod": {
        "start": "2020-02-05T06:00:00+01:00",
        "end": "2020-02-06T06:00:00+01:00"
    },
    "issued": "2020-05-30T03:57:29.413990Z",
    "valueQuantity": {
        "value": 93,
        "unit": "%",
        "system": "http://unitsofmeasure.org",
        "code": "%"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme oxygen-saturation device"
    }
}
~~~

### OMH oxygen-saturation schema instance - with oxygen

The following OMH oxygen-saturation schema instance:

~~~json
{
    "header": {
        "id": "84f98beb-2d47-4e06-a3cc-0b2e7f72f5f0",
        "creation_date_time": "2020-05-30T04:34:37.314720Z",
        "schema_id": {
            "namespace": "omh",
            "name": "oxygen-saturation",
            "version": "2.0"
        },
        "acquisition_provenance": {
            "source_name": "Acme oxygen-saturation device",
            "source_creation_date_time": "2020-05-30T04:34:37.314720Z",
            "source_data_point_id": "51fc2843-2bb6-44a5-b261-8f6664eb285c",
            "modality": "sensed"
        },
        "user_id": "60012977-b9c6-400a-adac-bcf96864198f"
    },
    "body": {
        "oxygen_saturation": {
            "value": 95,
            "unit": "%"
        },
        "effective_time_frame": {
            "date_time": "2013-02-05T07:25:00Z"
        },
        "supplemental_oxygen_flow_rate": {
            "value": 2.5,
            "unit": "L/min"
        },
        "oxygen_therapy_mode_of_administration": "nasal cannula",
        "system": "peripheral capillary",
        "measurement_method": "pulse oximetry"
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
            "value": "84f98beb-2d47-4e06-a3cc-0b2e7f72f5f0"
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
                "code": "59408-5",
                "display": "Oxygen saturation in Arterial blood by Pulse oximetry"
            }
        ]
    },
    "subject": {
        "identifier": {
            "system": "https://omh.org/shimmer/patient_ids",
            "value": "60012977-b9c6-400a-adac-bcf96864198f"
        }
    },
    "effectiveDateTime": "2013-02-05T07:25:00Z",
    "issued": "2020-05-30T04:34:37.314720Z",
    "valueQuantity": {
        "value": 95,
        "unit": "%",
        "system": "http://unitsofmeasure.org",
        "code": "%"
    },
    "device": {
        "extension": [
            {
                "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
                "valueCode": "sensed"
            }
        ],
        "display": "Acme oxygen-saturation device"
    },
    "component": [
        {
            "code": {
                "coding": [
                    {
                        "system": "http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes",
                        "code": "o2-administration-method",
                        "display": "Oxygen Therapy Mode of Administration"
                    }
                ]
            },
            "valueString": "nasal cannula"
        },
        {
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "3151-8",
                        "display": "Inhaled oxygen flow rate"
                    }
                ]
            },
            "valueQuantity": {
                "value": 2.5,
                "unit": "L/min",
                "system": "http://unitsofmeasure.org",
                "code": "l/min"
            }
        }
    ]
}
~~~
