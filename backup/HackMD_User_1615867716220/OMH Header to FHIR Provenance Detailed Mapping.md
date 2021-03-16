---
tags: omh2fhir
---

{%hackmd 2yYAoTGSSpiWVb7EWu6v0w %}

# OMH Header to FHIR Provenance Detailed Mapping

The following Table provides the detailed mapping for the OMH Header to the OMH to FHIR Provenance Profile in order to record the transform data. TODO: add link to profile:

|Index|OMH Header Element|FHIR Attribute|Mapping Instructions|
|---|---|---|---|
|1|header-1.2.json|OMH to FHIR  Provenance Profile||
|1A|None|Provenance.activity.text|fixed to "transform"|
|!B|None|Provenance.target.reference|fixed to "#" since  Provenance  is contained in Observation|
|1C|None|Provenance.recorded|System provided value indicates the instant the omh message was transformed to a FHIR resource.|
|1D|None|Provenance.policy|fixed to "http://www.fhir.org/guides/mfhir/ImplementationGuide/openmhealth.mfhir-0.0.0" Provenance.policy can optionally point to the  omh-fhir ig rules url used for the transformation|
|1E.1|None|Provenance.agent[0].type.coding[0].system|fixed to "http://terminology.hl7.org/CodeSystem/provenance-participant-type"|
|1E.2|None|Provenance.agent[0].type.coding[0].code|fixed to "assembler"|
|1E.3|None|Provenance.agent[0].type.coding[0].display|fixed to "Assembler"|
|1E.4|None|Provenance.agent[0].type.who.reference|Provenance.agent.who references the Organization or Device performing the transformation. For example, "Device/example-r24-server"|
|1F.1|None|Provenance.agent[1].type.text|fixed to "omh-schema"|
|1F.2|None|Provenance.entity[0]|Provenance.entity is optional.  see entity elements below|
|1F.3|None|Provenance.entity[0].role|fixed to "derivation"|
|2.1|header.id|Provenance.entity[0].what.identifier[0].value|concatenation of  "urn:uuid:" + header.id|
|2.2|header.id|Provenance.entity[0].what.identifier[0].system|fixed to "urn:ietf:rfc:3986"|
|3|header.creation_date_time|None||
|4|header.schema_id|None||
|5|header.schema_id.namespace|Provenance.agent[1].type.who.identifier.value|concatenation of  header.schema_id.namespace + header.schema_id.name + header.schema_id.version|
|6|header.schema_id.name|Provenance.agent[1].type.who.identifier.value|concatenation of  header.schema_id.namespace + header.schema_id.name + header.schema_id.version|
|7|header.schema_id.version|Provenance.agent[1].type.who.identifier.value|concatenation of  header.schema_id.namespace + header.schema_id.name + header.schema_id.version|
|8|header.schema_id.url|Provenance.agent[1].type.who.reference|1:1 mapping of  header.schema_id.url|
|9|header.acquisition_provenance|None||
|10.1|header.acquisition_provenance.source_name|Provenance.agent[2].type.coding[0].system|fixed to "http://terminology.hl7.org/CodeSystem/provenance-participant-type"|
|10.2|header.acquisition_provenance.source_name|Provenance.agent[2].type.coding[0].code|fixed to "AUT"|
|10.3|header.acquisition_provenance.source_name|Provenance.agent[2].type.coding[0].display|fixed to Author|
|10.4|header.acquisition_provenance.source_name|Provenance.agent[2].who.display|1:1 mapping of  header.acquisition_provenance.source_name|
|10|header.acquisition_provenance.source_data_point_id|None||
|11|header.acquisition_provenance.source_creation_date_time|None||
|12|header.acquisition_provenance.last_modification_date_time|None||
|13|header.acquisition_provenance.modality|None||
|14|header.user_id|None||


## Example:

### OMH Header schema instance:

~~~json
"header": {
  "id": "243c773b-8936-407e-9c23-270d0ea49cc4",
  "creation_date_time": "2015-09-10T12:43:39.138-06:00",
  "acquisition_provenance": {
    "source_name": "Acme BG API",
    "modality": "sensed",
    "source_updated_date_time": "2015-09-10T18:43:39Z"
  },
  "schema_id": {
    "namespace": "omh",
    "name": "blood_glucose",
    "version": "1.0"
  },
  "user_id": "306a1202-410d-11e8-842f-0ed5f89f718b"
}
~~~

Maps to the FHIR Provenance resource ( note that this example include the optional `Provenance.entity` element which reference the source OMH schema instance):

~~~json
{
  "resourceType": "Provenance",
  "activity": {
    "coding": [
      {
        "system": "http://terminology.hl7.org/CodeSystem/iso-21089-lifecycle",
        "code": "transform",
        "display": "Transform"
      }
    ]
  },
  "target": [
    {
      "reference": "Observation/omh-fhir-example"
    }
  ],
  "recorded": "2020-05-26T11:09:09-07:00",
  "policy": [
    "http://www.fhir.org/guides/mfhir/ImplementationGuide/openmhealth.mfhir-0.0.0"
  ],
  "agent": [
    {
      "type": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/provenance-participant-type",
            "code": "assembler",
            "display": "Assembler"
          }
        ]
      },
      "who": {
        "reference": "Device/example-r24-server"
      }
    },
    {
      "type": {
        "text": "omh-schema"
      },
      "who": {
        "identifier": {
          "value": "blood-glucose-2.0"
        }
      }
    },
    {
      "type": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/provenance-participant-type",
            "code": "author",
            "display": "Author"
          }
        ]
      },
      "who": {
        "display": "Acme BG API"
      }
    }
  ],
  "entity": [
    {
      "role": "derivation",
      "what": {
        "identifier": {
          "system": "urn:ietf:rfc:3986",
          "value": "243c773b-8936-407e-9c23-270d0ea49cc4"
        }
      }
    }
  ]
}
~~~

The following example shows the Provenance resource contained in the Observation resource example from above:

~~~json
{
  "contained": [
    {
      "resourceType": "Provenance",
      "activity": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/iso-21089-lifecycle",
            "code": "transform",
            "display": "Transform"
          }
        ]
      },
      "target": [
        {
          "reference": "#"
        }
      ],
      "recorded": "2020-05-26T11:09:09-07:00",
      "policy": [
        "http://www.fhir.org/guides/mfhir/ImplementationGuide/openmhealth.mfhir-0.0.0"
      ],
      "agent": [
        {
          "type": {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/provenance-participant-type",
                "code": "assembler",
                "display": "Assembler"
              }
            ]
          },
          "who": {
            "reference": "Device/example-r24-server"
          }
        },
        {
          "type": {
            "text": "omh-schema"
          },
          "who": {
            "identifier": {
              "value": "blood-glucose-2.0"
            }
          }
        },
        {
          "type": {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/provenance-participant-type",
                "code": "author",
                "display": "Author"
              }
            ]
          },
          "who": {
            "display": "Acme BG API"
          }
        }
      ],
      "entity": [
        {
          "role": "derivation",
          "what": {
            "identifier": {
              "system": "urn:ietf:rfc:3986",
              "value": "243c773b-8936-407e-9c23-270d0ea49cc4"
            }
          }
        }
      ]
}
  ],
  "category": [
    {
      "coding": [
        {
          "code": "laboratory",
          "display": "Laboratory",
          "system": "http://hl7.org/fhir/observation-category"
        }
      ]
    }
  ],
  "code": {
    "coding": [
      {
        "code": "2339-0",
        "display": "Glucose Mass/volume in Blood",
        "system": "http://loinc.org"
      }
    ]
  },
  "device": {
    "display": "Acme BG API",
    "extension": [
      {
        "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
        "valueCode": "sensed"
      }
    ]
  },
  "identifier": [
    {
      "system": "urn:ietf:rfc:3986",
      "value": "urn:uuid:243c773b-8936-407e-9c23-270d0ea49cc4"
    }
  ],
  "issued": "2015-09-10T12:43:39.138-06:00",
  "meta": {
    "profile": [
      "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_profile_quantitative_observation"
    ]
  },
  "resourceType": "Observation",
  "status": "unknown",
  "subject": {
    "identifier": {
      "system": "urn:ietf:rfc:3986",
      "value": "urn:uuid:306a1202-410d-11e8-842f-0ed5f89f718b"
    }
  }
}
~~~
