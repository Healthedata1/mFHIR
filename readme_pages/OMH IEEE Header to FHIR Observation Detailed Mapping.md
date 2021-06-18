[<<back](../README.md)
<!---
tags: omh2fhir
title: IEEE Header Fhir Observation Mapping
--->

<!-- icons -->
<header>
<a href="https://www.openmhealth.org/">
<img align="left" width="25%" height="25%" src="https://www.openmhealth.org/wp-content/themes/openmhealth2015/dist/images/logo@2x.png" alt="Open mHealth">
</a>


<a href="http://hl7.org/fhir">
<img align="right" width="25%" height="25%" src="http://build.fhir.org/assets/images/fhir-logo-www.png" alt="HL7 FHIR">
</a>

<br />

<h3 class="logoHeader" align="center">OMH to FHIR QuickStart Guide</h3>
</header>


<!-- wide style: to accomodate tables -->



# OMH IEEE Header to FHIR Observation Detailed Mapping

The following Table provides the detailed mapping for the OMH IEEE Header to the OMH to FHIR Observation Profile TODO: add link to profile. The OMH IEEE Header Schemas was developed by the IEEE P1752 working group and available [here](https://opensource.ieee.org/omh/1752)


|Index|Upated Header Element|FHIR Element|Mapping Instructions|
|---|---|---|---|
|1|header.$schema|OMH to FHIR Observation Profile|see Observation elements below|
|2|header.$id|None|schema metadata|
|3|header.title|None|schema metadata|
|4|header.description|None|schema metadata|
|5.1|header.properties.uuid|Observation.identifer[n]|see Identifier elements below|
|5.2|header.properties.uuid|Observation.identifier[n].value|concatenation of  'urn:uuid:'+header.properties.uuid|
|5.3||Observation.identifier[n].system|fixed to "urn:ietf:rfc:3986"|
|6A.1|header.properties.schema_id|Observation.category[n]|See CodeableConcept elements below|
|6A.2||Observation.category[n].coding[n]|See Coding elements below|
|6A.3||Observation.category[n].coding[n].system|fixed to "http://hl7.org/fhir/observation-category"|
|7A|header.properties.schema_id.namespace|Observation.category[n].coding[n].code|Map header.properties.schema_id.namespace, header.properties.schema_id.name, header.properties.schema_id.version to column "Observation.category.code" using  the [data_point_mapping_table](#)|
|8A|header.properties.schema_id.name|Observation.category[n].coding[n].code|Map header.properties.schema_id.namespace, header.properties.schema_id.name, header.properties.schema_id.version to column "Observation.category.code" using  the [data_point_mapping_table](#)|
|9A|header.properties.schema_id.version|Observation.category[n].coding[n].code|Map header.properties.schema_id.namespace, header.properties.schema_id.name, header.properties.schema_id.version to column "Observation.category.code" using  the [data_point_mapping_table](#)|
|6B.1|header.properties.schema_id|Observation.code|See CodeableConcept elements below|
|6B.2||Observation.code.coding[n]|See Coding elements below|
|6B.3||Observation.code[n].coding[n].system|fixed to "http://hl7.org/fhir/observation-category"|
|7B.1|header.properties.schema_id.namespace|Observation.code[n].coding[n].code|Map header.properties.schema_id.namespace, header.properties.schema_id.name, header.properties.schema_id.version to column "Observation.category.system" using  the [data_point_mapping_table](#)|
|8B.1|header.properties.schema_id.name|Observation.code[n].coding[n].code|Map header.properties.schema_id.namespace, header.properties.schema_id.name, header.properties.schema_id.version to column "Observation.category.system" using  the [data_point_mapping_table](#)|
|9B.1|header.properties.schema_id.version|Observation.code[n].coding[n].code|Map header.properties.schema_id.namespace, header.properties.schema_id.name, header.properties.schema_id.version to column "Observation.category.system" using  the [data_point_mapping_table](#)|
|7B.2|header.properties.schema_id.namespace|Observation.code[n].coding[n].code|Map header.properties.schema_id.namespace, header.properties.schema_id.name, header.properties.schema_id.version to column "Observation.category.code" using  the [data_point_mapping_table](#)|
|8B.2|header.properties.schema_id.name|Observation.code[n].coding[n].code|Map header.properties.schema_id.namespace, header.properties.schema_id.name, header.properties.schema_id.version to column "Observation.category.code" using  the [data_point_mapping_table](#)|
|9B.2|header.properties.schema_id.version|Observation.code[n].coding[n].code|Map header.properties.schema_id.namespace, header.properties.schema_id.name, header.properties.schema_id.version to column "Observation.category.code" using  the [data_point_mapping_table](#)|
|7B.3|header.properties.schema_id.namespace|Observation.code[n].coding[n].code|Map header.properties.schema_id.namespace, header.properties.schema_id.name, header.properties.schema_id.version to column "Observation.category.display" using  the [data_point_mapping_table](#)|
|8B.3|header.properties.schema_id.name|Observation.code[n].coding[n].code|Map header.properties.schema_id.namespace, header.properties.schema_id.name, header.properties.schema_id.version to column "Observation.category.display" using  the [data_point_mapping_table](#)|
|9B.3|header.properties.schema_id.version|Observation.code[n].coding[n].code|Map header.properties.schema_id.namespace, header.properties.schema_id.name, header.properties.schema_id.version to column "Observation.category.display" using  the [data_point_mapping_table](#)|
|10|header.properties.source_creation_date_time|Observation.issued|= header.properties.source_creation_date_time|
|11.1|header.properties.modality.description|Observation.device.extension[n]|see Extension elements below|
|11.2|header.properties.modality.description|Observation.device.extension[n].valueCode|= header.properties.modality.description|
|11.3||Observation.device.extension[n].url|fixed to "http://www.fhir.org/mfhir/StructureDefinition/extenion-modality"|
|12A.1|header.properties.acquisition_rate|Observation.component[n]|See Observation.Component elements below. Condition:IF not Sampled data|
|12A.2||Observation.component[n].code|see CodeableConcept elements below|
|12A.3||Observation.component[n].code.coding[n]|see Coding elements below|
|12A.4||Observation.component[n].code.coding[n].code|fixed to "260864003"|
|12A.5||Observation.component[n].code.coding[n].system|fixed to ‚Äò‚Äúhttp://snomed.info/sct‚Äù|
|12A.6||Observation.component[n].code.coding[n].display|fixed to "Frequency (attribute)"|
|13A.1||Observation.component[n].valueQuantity|see Quantity elements below. Condition: IF header.properties.acquisition_rate.value is valued|
|13A.2|header.properties.acquisition_rate.value|Observation.component[n].valueQuantity.value|= header.properties.acquisition_rate.value|
|14A.1|header.properties.acquisition_rate.unit|Observation.component[n].valueQuantity.unit|= header.properties.acquisition_rate.unit|
|14A.2|header.properties.acquisition_rate.unit|Observation.component[n].valueQuantity.code|= header.properties.acquisition_rate.unit|
|14A.3||Observation.component[n].valueQuantity.system|fixed to  "http://unitsofmeasure.org"|
|15A.1||Observation.component[n].valueRange|see Range elements below. Condition: IF header.properties.acquisition_rate.low_value is valued|
|15A.2||Observation.component[n].valueRange.low|see Quantity elements below|
|15A.3|header.properties.acquisition_rate.low_value|Observation.component[n].valueRange.low.value|= header.properties.acquisition_rate.low_value|
|16A.1|header.properties.acquisition_rate.unit|Observation.component[n].valueQuantity.unit|= header.properties.acquisition_rate.unit|
|16A.2|header.properties.acquisition_rate.unit|Observation.component[n].valueQuantity.code|= header.properties.acquisition_rate.unit|
|16A.3||Observation.component[n].valueQuantity.system|fixed to  "http://unitsofmeasure.org"|
|17A.1||Observation.component[n].valueRange.high|see Quantity elements below|
|17A.2|header.properties.acquisition_rate.high_value|Observation.component[n].valueRange.high.value|= header.properties.acquisition_rate.high_value|
|18A.1|header.properties.acquisition_rate.unit|Observation.component[n].valueQuantity.unit|= header.properties.acquisition_rate.unit|
|18A.2|header.properties.acquisition_rate.unit|Observation.component[n].valueQuantity.code|= header.properties.acquisition_rate.unit|
|18A.3||Observation.component[n].valueQuantity.system|fixed to  "http://unitsofmeasure.org"|
|12B.1|header.properties.acquisition_rate|Observation.valueSampledData|see SampledData elements below.Condition:IF  Sampled data|
|12B.2||Observation.valueSampledData.origin|map to the data stream schema (default Quantity.value= '0')|
|12B.3||Observation.valueSampledData.dimensions'|map to the data stream schema (default = '1')|
|12B.4||Observation.valueSampledData.data'|map to the data stream schema|
|13B|header.properties.acquisition_rate.value|Observation.valueSampledData.period'|= "1000/header.properties.acquisition_rate.value. Condition:  IF header.properties.acquisition_rate.value is valued|
|14B|header.properties.acquisition_rate.unit|Observation.valueSampledData.period'|= "1000/header.properties.acquisition_rate.value. Condition:  IF header.properties.acquisition_rate.value is valued|
|17B||Observation.valueSampledData.period'|= "Convert units to usec/header.properties.acquisition_rate.high_valueCondition:  IF header.properties.acquisition_rate.low_value is valued|
|18B|header.properties.acquisition_rate.unit|Observation.valueSampledData.period'|= "Convert units to usec/header.properties.acquisition_rate.high_value|
|15B.1|header.properties.acquisition_rate.low_value|Observation.valueSampledData.extension[n]|see Extension elements below. Condition:  IF header.properties.acquisition_rate.low_value is valued|
|15B.2|header.properties.acquisition_rate.low_value|Observation.valueSampledData.extension[n].url|fixed to "http://www.fhir.org/mfhir/StructureDefinition/sampleddata-period-high"|
|15B.3|header.properties.acquisition_rate.low_value|Observation.valueSampledData.extension[n].valueDecimal|= "Convert units to usec/header.properties.acquisition_rate.low_value|
|16B.1|header.properties.acquisition_rate.unit|Observation.valueSampledData.extension[n].valueDecimal|= "Convert units to usec/header.properties.acquisition_rate.low_value|
|16B.2|header.properties.external_datasheets|Observation.extension[n]|see Extension elements below|
|16B.3||Observation.extension[n].url|fixed to "http://hl7.org/fhir/StructureDefinition/workflow-relatedArtifact"|
|19.1||Observation.extension[n].valueRelatedArtifact|see RelatedArtifact elements below|
|19.2||Observation.extension[n].valueRelatedArtifact.type|fixed to "documentation"|
|20|header.properties.external_datasheets.items.properties.datasheet_type|Observation.extension[n].valueRelatedArtifact.label|= header.properties.external_datasheets.items.properties.datasheet_type|
|21|header.properties.external_datasheets.items.properties.datasheet_reference|Observation.extension[n].valueRelatedArtifact.url|= header.properties.external_datasheets.items.properties.datasheet_reference|

## Example:

### OMH Header schema instance:

~~~json
{
    "header": {
        "uuid": "123e4567-e89b-12d3-a456-426655440000",
        "source_creation_date_time": "2019-03-29T09:14:45+01:00",
        "schema_id": {
            "namespace": "ieee",
            "name": "physical-activity",
            "version": "1.0"
        },
        "modality": "sensed",
        "external_datasheets": [
            {
                "datasheet_reference": "iri-of-some-activity-tracker-device"
            },
            {
                "datasheet_type": "study",
                "datasheet_reference": "iri-of-some-study-protocol"
            }
        ]
    }
}
~~~

Maps to the FHIR Observation resource:

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
        "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
        "valueCode": "sensed"
      },
      {
        "url": "http://hl7.org/fhir/StructureDefinition/workflow-relatedArtifact",
        "valueRelatedArtifact": {
          "type": "documentation",
          "uri": "iri-of-some-activity-tracker-device"
        }
      },
      {
        "url": "http://hl7.org/fhir/StructureDefinition/workflow-relatedArtifact",
        "valueRelatedArtifact": {
          "type": "documentation",
          "label": "study",
          "uri": "iri-of-some-study-protocol"
        }
      }
  ],
  "identifier": [
    {
      "system": "urn:ietf:rfc:3986",
      "value": "urn:uuid:123e4567-e89b-12d3-a456-426655440000"
    }
  ],
  "status": "unknown",
  "category": [
    {
      "coding": [
        {
          "code": "physical-activity",
          "display": "Physical Activity",
          "system": "http://hl7.org/fhir/observation-category"
        }
      ]
    }
  ],
  "code": {
    "coding": [
      {
        "code": "129861002",
        "display": " Physical activity finding (finding)",
        "system": "http://snomed.info/id"
      }
    ]
  },
  "issued": "2019-03-29T09:14:45+01:00"
}
~~~


---

[<<back](../README.md)
