# Welcome to the OMH To FHIR Quick-Start Guide




- [Introduction](#quick-start-mapping-guide-for-mapping-omh-schema-mappings-to-fhir-elements)
- [OMH Header to FHIR Observation Mapping](#omh-header-to-fhir-observation-detailed-mapping)
- [OMH Heart Rate DataPoint to FHIR Observation Mapping](#omh-heartrate-datapoint-to-fhir-observation-detailed-mapping)
- [OMH Body Temperature DataPoint to FHIR Observation Mapping](#omh-body-temperature-datapoint-to-fhir-observation-detailed-mapping)
- [OMH Blood Glucose DataPoint to FHIR Observation Mapping](#omh-blood-glucose-datapoint-to-fhir-observation-detailed-mapping)
- [PUNCHLIST](#punchlist)


## Quick Start Mapping Guide For Mapping OMH Schema Mappings to FHIR Elements

Measurements such as steps or heart rate are modeled using OMH schemas.  These models can be used to represent instance of the measurement "over the wire" in JSON.  The OMH schema can be transformed into FHIR

The following 9 OMH schemas used to represent instance of the measurement "over the wire" in JSON:

1. blood glucose
1. blood pressure [add property cuff position]
1. body temperature
1. body weight
1. heart rate [resting]
1. O2 saturation
1. respiratory rate
1. sleep duration [-->  total sleep time ]
1. step count [change datatype of property step_count to unit_value]

are composed of the of the OMH header element a body which contains the datapoint schema represents the body's properties.  They are transformed into FHIR using a series of mapping steps to convert the sctructure and content into a corresponding FHIR Observation Profile.

### OMH Header Element to FHIR Element Mapping Table

Each OMH schema for a datapoint is composed of the 'header' and 'body,  This table summarizes the mapping of the OMH header elements to the corresponding OMH to FHIR Observation Profile element.  Each datapoint schema represents the body's properties and will be covered individually.

|OMH element|FHIR element|
|---|---|
|template profile|OMH to FHIR Observation Profile|
|header.id|Observation.identifier|
|header.creation_date_time|Observation.issued|
|header.schema_id|None|
|header.schema_id.namespace|None|
|header.schema_id.name|Observation.category,Observation.code ( see datapoint mapping table below )|
|header.schema_id.version|None|
|header.acquisition_provenance|None|
|header.acquisition_provenance.source_name|Observation.device|
|header.acquisition_provenance.source_data_point_id|Observation.identifier|
|header.acquisition_provenance.source_creation_date_time|None|
|header.acquisition_provenance.modication_data_time|None|
|header.acquisition_provenance.modality|Observation.device.extension|
|header.user_id|Observation.subject|
{: .grid}

The detailed mapping for the OMH header can be found here...

### OMH DataPoint Element to FHIR Element Mapping Table

Each Datapoint is represented by the body properties and this table summarizes of the OMH datapoint schema type as represented by the `header.schema_id.name` element to the corresponding FHIR Observation `category` and 'code' elements and default units for quantitative measures.

header.schema_id.name|Observation.category.code|Observation.code.system|Observation.code.code|Observation.code.display|observation_value_quantity_unit(s) (list)|
--|--|--|--|--|--|
blood_glucose|laboratory|http://loinc.org|2339-0|Glucose Mass/volume in Blood|['mg/dL', 'mmol/L']|
blood_pressure*|vital-signs|http://loinc.org|85354-9|Blood pressure panel with all children optional|None|
body_temperature|vital-signs|http://loinc.org|8310-5|Body temperature|['K','F','C']|
body_weight|vital-signs|http://loinc.org|29463-7|Body weight|['kg', 'g', 'lb']|
heart_rate|vital-signs|http://loinc.org|8867-4|Heart rate|['beats/min']|
oxygen_saturation|vital-signs|http://loinc.org|59408-5|Oxygen saturation in Arterial blood by Pulse oximetry|['%']|
respiratory_rate|vital-signs|http://loinc.org|9279-1|Respiratory Rate|['breaths/min']|
sleep_duration|physical-activity|http://snomed.info/id|248263006|Duration of sleep (observable entity)|['sec', 'min', 'h']|
step_count|physical-activity|http://loinc.org|55423-8|Number of steps in unspecified time Pedometer|['steps']|


**Data Point Component Mapping Table**

Blood Pressure Datapoints has these additional properties that are represented by the FHIR `Observation.component` element in FHIR.  This table summarizes these OMH datapoint schema properties and list the corresponding OMH propertied name in the  `Component Name` column and its corresponding FHIR Observation component code and valuetype attributes.  This table is used along with the OMH to FHIR concept mapping table to to populate the the FHIR Observation profile.

|Component Name|Component Code System|Component Code Code|Component Code Display|Component Value Type|
|--|--|--|--|--|
|cuff_position|http://loinc.org|NNNN-N|Position of cuff [add property cuff position]|
|diastolic_blood_pressure|http://loinc.org|8462-4|Diastolic blood pressure|valueQuantity|
|systolic_blood_pressure|http://loinc.org|8480-6|Systolic blood pressure|valueQuantity|




## OMH Header to FHIR Observation Detailed Mapping


The following Table provides the detailed mapping for the OMH Header to the OMH to FHIR Observation Profile TODO: add link to profile:


|Index|OMH  Header Element|FHIR Attribute|Derived Mapping|Comments|
|---|---|---|---|---|
|1|header-1.2.json|OMH to FHIR Observation Profile|||
|2.1|header.id|identifier[0].value|||1:1 mapping of  string|
|2.2|header.id|identifier[0].system|https://omh.org/shimmer/ids|fixed to 'https://omh.org/shimmer/ids'|
|3|header.creation_date_time|issued||1:1 mapping of  header.creation_date_time|
|4|header.schema_id|None|||
|5|header.schema_id.namespace|None|||
|6A.1|header.schema_id.name|category[0].coding[0].code|data_point_mapping_table|"Maps to column 'Observation.category.code'|
|6A.2|header.schema_id.name|category[0].coding[0].system|http://hl7.org/fhir/observation-category|"fixed to ""http://hl7.org/fhir/observation-category""|
|6B.1|header.schema_id.name|code.coding[0].code|data_point_mapping_table['Observation.code.code']|"Maps to column 'Observation.code.code'|
|6B.2||code.coding[0].system|data_point_mapping_table['Observation.code.system']|"Maps to column 'Observation.code.system'|
|6B.3||code.coding[0].display|data_point_mapping_table['Observation.code.display']|"Maps to column 'Observation.code.display'|
|7|header.schema_id.version|None|||
|8|header.acquisition_provenance|None|||
|9|header.acquisition_provenance.source_name|device.display|1:1 mapping of header.acquisition_provenance.source_name||
|10.1|header.acquisition_provenance.source_data_point_id|identifier[1].value||1:1 mapping of  header.acquisition_provenance.source_data_point_id|
|10.2||identifier[1].system|https://omh.org/source/ids|fixed to 'https://omh.org/source/ids'|
|11|header.acquisition_provenance.source_creation_date_time|None|||
|12|header.acquisition_provenance.modication_date_time|None|||
|13.1|header.acquisition_provenance.modality|device.extension[0].valueCode||1:1 mapping of header.acquisition_provenance.modality|
|13.2||device.extension[0].url|http://www.fhir.org/mfhir/StructureDefinition/extenion-modality|fixed to 'http://www.fhir.org/mfhir/StructureDefinition/extenion-modality'|
|14.1|header.user_id|subject.identifier.value||1:1 mapping of  string|
|14.2||subject.identifier.system|https://omh.org/shimmerM/patient_id|fixed to 'https://omh.org/shimmer/patient_id'|


Example Mapping:

The following OMH Header schema instance:

~~~
"header": {
  "id": "243c773b-8936-407e-9c23-270d0ea49cc4",
  "creation_date_time": "2015-09-10T12:43:39.138-06:00",
  "acquisition_provenance": {
    "source_name": "Jawbone UP API",
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

Maps to the FHIR Observation resource:

~~~
{
   "issued": "2015-09-10T12:43:39.138-06:00",
   "resourceType": "Observation",
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
      "display": "Jawbone UP API",
      "extension": [
         {
            "valueCode": "sensed",
            "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality"
         }
      ]
   },
   "identifier": [
      {
         "value": "243c773b-8936-407e-9c23-270d0ea49cc4",
         "system": "https://omh.org/shimmer/ids"
      }
   ],
   "meta": {
      "profile": [
         "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_profile_quantitative_observation"
      ]
   },
   "status": "unknown",
   "subject": {
      "identifier": {
         "value": "306a1202-410d-11e8-842f-0ed5f89f718b",
         "system": "https://omh.org/shimmer/patient_ids"
      }
   }
}
~~~


## OMH HeartRate DataPoint to FHIR Observation Detailed Mapping


The following Table provides the detailed mapping for the OMH HeartRate DataPoint to the OMH to FHIR Observation Profile TODO: add link to profile:

Index|OMH  Header Element|FHIR Attribute|Derived Mapping|Comments
---|---|---|---|---
1|heart-rate-1.1.json|OMH to FHIR Observation Profile||
2.1|body.heart_rate|Observation.valueQuantity||see valueQuantity elements below
2.2|body.heart_rate.value|Observation.valueQuantity.value||1:1 mapping of  number
2.3|body.heart_rate.unit|Observation.valueQuantity.unit||1:1 mapping of  string
2.4||valueQuantity.system|http://unitsofmeasure.org|fixed to 'http://unitsofmeasure.org'
2.5||valueQuantity.code|OMH_FHIR_Concept_Maps['body.heart_rate.unit']|Concept Mapping
3|body.effective_time_frame|Observation.effective[x]||Mappping depends on type- see below
5|body.effective_time_frame.date_time|Observation.effectiveDateTime||1:1 mapping of  body.effective_time_frame.date_time
4|body.effective_time_frame.time_interval|Observation.effectivePeriod||see effectivePeriod.elements below
6|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start||1:1 mapping of  body.effective_time_frame.time_interval.start_date_time
7|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end||1:1 mapping of  body.effective_time_frame.time_interval.end_date_time
8|body.user_notes|Observation.comment||1:1 mapping of  body.user_notes
9|body.descriptive_statistic|Observation.coding[1]||Map  descriptive statistic to the OMH to FHIR additional Observation codings ( code system http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes).
10|body.temporal_relationship_to_physical_activity|Observation.component|component_mapping_table|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list
11|body.temporal_relationship_to_sleep|Observation.component|component_mapping_table|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list

Example Mapping:

The following OMH HeartRate schema instance:

```
{
  "body": {
 "effective_time_frame": {
    "date_time": "2013-02-05T07:25:00Z"
 },
 "blood_glucose": {
    "value": 95,
    "unit": "mg/dL"
 }
}
}
```

Maps to this FHIR Observation fragment

~~~
...
"effectiveDateTime": "2013-02-05T07:25:00Z",
"valueQuantity": {
   "value": 95,
   "code": "mg/dL",
   "unit": "mg/dL",
   "system": "http://unitsofmeasure.org"
...
~~~

to make this this FHIR Observation when combine with the OMH Header

~~~
{
   "issued": "2015-09-10T12:43:39.138-06:00",
   "effectiveDateTime": "2013-02-05T07:25:00Z",
   "resourceType": "Observation",
   "valueQuantity": {
      "value": 95,
      "code": "mg/dL",
      "unit": "mg/dL",
      "system": "http://unitsofmeasure.org"
   },
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
      "display": "Jawbone UP API",
      "extension": [
         {
            "valueCode": "sensed",
            "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality"
         }
      ]
   },
   "identifier": [
      {
         "value": "243c773b-8936-407e-9c23-270d0ea49cc4",
         "system": "https://omh.org/shimmer/ids"
      }
   ],
   "meta": {
      "profile": [
         "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_profile_quantitative_observation"
      ]
   },
   "status": "unknown",
   "subject": {
      "identifier": {
         "value": "306a1202-410d-11e8-842f-0ed5f89f718b",
         "system": "https://omh.org/shimmer/patient_ids"
      }
   }
}

~~~


## OMH Body Temperature DataPoint to FHIR Observation Detailed Mapping

The following Table provides the detailed mapping for the OMH Body Temperature DataPoint to the OMH to FHIR Observation Profile TODO: add link to profile:

Index|OMH Body Temperature Element|FHIR Attribute|Derived Mapping|Comments
---|---|---|---|---
1|body-temperature-2.0.json|OMH to FHIR Observation Profile||
2.1|body_temperature|Observation.valueQuantity||see valueQuantity elements below
2.2|body_temperature.value|Observation.valueQuantity.value||1:1 mapping of  number
2.3|body_temperature.unit|Observation.valueQuantity.unit||1:1 mapping of  string
2.4||valueQuantity.system|http://unitsofmeasure.org|fixed to 'http://unitsofmeasure.org'
2.5||valueQuantity.code|OMH_FHIR_Concept_Maps['body.body_temperature.unit']Concept Mapping
3|body.effective_time_frame|Observation.effective[x]||Mappping depends on type- see below
5|body.effective_time_frame.date_time|Observation.effectiveDateTime||1:1 mapping of  body.effective_time_frame.date_time
4|body.effective_time_frame.time_interval|Observation.effectivePeriod||see effectivePeriod.elements below
8.1|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start||1:1 mapping of  body.effective_time_frame.time_interval.start_date_time
8.0|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end||1:1 mapping of  body.effective_time_frame.time_interval.end_date_time
8.1|measurement_location|Observation.bodySite||See bodySite elements below
8.2||Observation.bodySIte.coding[0].system|OMH_FHIR_Concept_Maps['body.X'][0]for row = body.X = OMH to FHIR Concept Mapping Table  maps to column 'Concept Code System'
8.3||Observation.bodySIte.coding[0].code|OMH_FHIR_Concept_Maps['body.X'][1]for row = body.X = OMH to FHIR Concept Mapping Table  maps to column 'Concept Code'
8.4||Observation.bodySIte.coding[0].display|OMH_FHIR_Concept_Maps['body.X'][2]for row = body.X = OMH to FHIR Concept Mapping Table  maps to column 'Concept Code Display'
9|body.descriptive_statistic|Observation.coding[1]||Map  descriptive statistic to the OMH to FHIR additional Observation codings ( code system http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes).
10|body.temporal_relationship_to_physical_activity|Observation.component|component_mapping_table|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list
11|body.temporal_relationship_to_sleep|Observation.component|component_mapping_table|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list


Example Mapping:

The following OMH Body Temperature schema instance:

```
{
  "body": {
   "effective_time_frame": {
      "time_interval": {
         "end_date_time": "2015-02-06T06:00:00Z",
         "start_date_time": "2015-02-05T06:00:00Z"
      }
   },
   "descriptive_statistic": "maximum",
   "body_temperature": {
      "value": 96.5,
      "unit": "F"
   },
   "measurement_location": "oral"
  }
}
```

Maps to this FHIR Observation fragment

~~~
...
"code": {
   "coding": [
      {
         "code": "body-temperature-maximum",
         "display": "Body Temperature Maximum",
         "system": "http://hl7.org/fhir/omh_fhir_observation_codes"
      }
   ]
},
{
   "effectivePeriod": {
      "end": "2015-02-06T06:00:00Z",
      "start": "2015-02-05T06:00:00Z"
   },
   "valueQuantity": {
      "value": 96.5,
      "code": "[degF]",
      "unit": "F",
      "system": "http://unitsofmeasure.org"
   },
   "bodySite": {
      "coding": [
         {
            "code": "oral",
            "system": "http://www.fhir.org/guides/mfhir/CodeSystem/intervention-administration-route"
         }
      ],
      "text": "oral"
   },
...
~~~

to make this this FHIR Observation when combine with the OMH Header

~~~
{
   "meta": {
      "profile": [
         "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_profile_quantitative_observation"
      ]
   },
   "bodySite": {
      "coding": [
         {
            "code": "oral",
            "system": "http://www.fhir.org/guides/mfhir/CodeSystem/intervention-administration-route"
         }
      ],
      "text": "oral"
   },
   "category": [
      {
         "coding": [
            {
               "code": "vital-signs",
               "display": "Vital Signs",
               "system": "http://hl7.org/fhir/observation-category"
            }
         ]
      }
   ],
   "code": {
      "coding": [
         {
            "code": "8310-5",
            "display": "Body temperature",
            "system": "http://loinc.org"
         },
         {
            "code": "body-temperature-maximum",
            "display": "Body Temperature-Maximum",
            "system": "http://hl7.org/fhir/omh_fhir_observation_codes"
         }
      ]
   },
   "device": {
      "extension": [
         {
            "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
            "valueCode": "sensed"
         }
      ],
      "display": "Jawbone UP API"
   },
   "effectivePeriod": {
      "end": "2015-02-06T06:00:00Z",
      "start": "2015-02-05T06:00:00Z"
   },
   "identifier": [
      {
         "system": "https://omh.org/shimmer/ids",
         "value": "243c773b-8936-407e-9c23-270d0ea49cc4"
      }
   ],
   "issued": "2015-09-10T12:43:39.138-06:00",
   "status": "unknown",
   "subject": {
      "identifier": {
         "system": "https://omh.org/shimmer/patient_ids",
         "value": "306a1202-410d-11e8-842f-0ed5f89f718b"
      }
   },
   "valueQuantity": {
      "code": "[degF]",
      "system": "http://unitsofmeasure.org",
      "unit": "F",
      "value": 96.5
   },
   "resourceType": "Observation"
}
~~~


## OMH Blood Glucose DataPoint to FHIR Observation Detailed Mapping


The following Table provides the detailed mapping for the OMH Blood Glucose DataPoint to the OMH to FHIR Observation Profile TODO: add link to profile:

Index|OMH Blood Glucose Element|FHIR Attribute|Derived Mapping|Comments
---|---|---|---|---
1|blood-glucose-2.0.json|OMH to FHIR Observation Profile||
2.1|body.blood_glucose|Observation.valueQuantity||see valueQuantity elements below
2.2|body.blood_glucose.value|Observation.valueQuantity.value||1:1 mapping of  number
2.3|body.blood_glucose.unit|Observation.valueQuantity.unit||1:1 mapping of  string
2.4||valueQuantity.system|http://unitsofmeasure.org|fixed to 'http://unitsofmeasure.org'
2.5||valueQuantity.code|OMH_FHIR_Concept_Maps['body.heart_rate.unit']|Concept Mapping
3|body.effective_time_frame|Observation.effective[x]||Mappping depends on type- see below
5|body.effective_time_frame.date_time|Observation.effectiveDateTime||1:1 mapping of  body.effective_time_frame.date_time
4|body.effective_time_frame.time_interval|Observation.effectivePeriod||see effectivePeriod.elements below
6|body.effective_time_frame.time_interval.start_date_time|Observation.effectivePeriod.start||1:1 mapping of  body.effective_time_frame.time_interval.start_date_time
7|body.effective_time_frame.time_interval.end_date_time|Observation.effectivePeriod.end||1:1 mapping of  body.effective_time_frame.time_interval.end_date_time
8|body.user_notes|Observation.note[0].text||1:1 mapping of  body.user_notes, optionally can add author and time to the FHIR Annotation datatype
9.1|body.specimen_source|Observation.extension||extension url = 'http://www.fhir.org/mfhir/StructureDefinition/extension-specimenCode'
9.2||Observation.extension[0].url|ttp://www.fhir.org/mfhir/StructureDefinition/extension-specimenCode|fixed to 'ttp://www.fhir.org/mfhir/StructureDefinition/extension-specimenCode'
9.3||Observation.extension[0].valueCodeableConcept||
9.4||Observation.extension[0].valueCodeableConcept.coding[0].system|OMH_FHIR_Concept_Maps['body.X'][0]|for row = body.X = OMH to FHIR Concept Mapping Table  maps to column 'Concept Code System'
9.5||Observation.extension[0].valueCodeableConcept.coding[0].code|OMH_FHIR_Concept_Maps['body.X'][1]|for row = body.X = OMH to FHIR Concept Mapping Table  maps to column 'Concept Code'
9.6||Observation.extension[0].valueCodeableConcept.coding[0].display|OMH_FHIR_Concept_Maps['body.X'][2]|for row = body.X = OMH to FHIR Concept Mapping Table  maps to column 'Concept Code Display'
10|body.descriptive_statistic|Observation.coding[1]||Map  descriptive statistic to the OMH to FHIR additional Observation codings ( code system http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes).
11|body.temporal_relationship_to_physical_activity|Observation.component|component_mapping_table|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list
12|body.temporal_relationship_to_sleep|Observation.component|component_mapping_table|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list
13|temporal_relationship_to_meal|Observation.component|component_mapping_table|A mapping table between OMH schema ('datapoint_variables') and FHIR Observation Component data elements.  Multiple components mapping are appended as a list

Example Mapping:

The following OMH Blood Glucose schema instance:

```
{
  "body": {
   "descriptive_statistic": "minimum",
   "effective_time_frame": {
      "time_interval": {
         "end_date_time": "2013-06-05T07:25:00Z",
         "start_date_time": "2013-02-05T07:25:00Z"
      }
   },
   "blood_glucose": {
      "value": 120,
      "unit": "mg/dL"
   }
}
```

Maps to this FHIR Observation fragment

~~~
...
"code": {
   "coding": [
      {
         "code": "blood-glucose-minimum",
         "display": "Blood Glucose Minimum",
         "system": "http://hl7.org/fhir/omh_fhir_observation_codes"
      }
   ]
},
{
   "effectivePeriod": {
      "end": "2013-06-05T07:25:00Z",
      "start": "2013-02-05T07:25:00Z"
   },
   "valueQuantity": {
      "value": 120,
      "code": "mg/dL",
      "unit": "mg/dL",
      "system": "http://unitsofmeasure.org"
   }
...
~~~

to make this this FHIR Observation when combine with the OMH Header

~~~
{
   "effectivePeriod": {
      "end": "2013-06-05T07:25:00Z",
      "start": "2013-02-05T07:25:00Z"
   },
   "issued": "2015-09-10T12:43:39.138-06:00",
   "resourceType": "Observation",
   "valueQuantity": {
      "value": 120,
      "code": "mg/dL",
      "unit": "mg/dL",
      "system": "http://unitsofmeasure.org"
   },
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
         },
         {
            "code": "blood-glucose-minimum",
            "display": "Blood Glucose Minimum",
            "system": "http://hl7.org/fhir/omh_fhir_observation_codes"
         }
      ]
   },
   "device": {
      "display": "Jawbone UP API",
      "extension": [
         {
            "valueCode": "sensed",
            "url": "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality"
         }
      ]
   },
   "identifier": [
      {
         "value": "243c773b-8936-407e-9c23-270d0ea49cc4",
         "system": "https://omh.org/shimmer/ids"
      }
   ],
   "meta": {
      "profile": [
         "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_profile_quantitative_observation"
      ]
   },
   "status": "unknown",
   "subject": {
      "identifier": {
         "value": "306a1202-410d-11e8-842f-0ed5f89f718b",
         "system": "https://omh.org/shimmer/patient_ids"
      }
   }
}
~~~


---

## PUNCHLIST

   - Mapping and example for

      1. blood glucose - done
      1. blood pressure [add property cuff position]
      1. body temperature  - done
      1. body weight
      1. heart rate [resting] - done
      1. O2 saturation 
      1. respiratory rate
      1. sleep duration [--  total sleep time ]
      1. step count [change datatype of property step_count to unit_value]

   - add linke to the concept mapping
   - add links:
      1. spreadsheets
      1. terminology
      1. concept Mapping
      1. FHIR profiles
      1. sample code
   - validate examples to FHIR R4
   -  source documentation is all in markdown - consider other documentation toolilng like makedocs or Jekyll for better formatting


---

[Binary]: {{site.data.fhir.path}}binary.html "FHIR Binary Resource documentation"
[DocumentReference]: {{site.data.fhir.path}}documentreference.html "FHIR DocumentReference Resource documentation"
[FHIR search API]: {{site.data.fhir.path}}search.html "FHIR search API documentation"
[code]: {{site.data.fhir.path}}datatypes.html#code "FHIR code definition"
[contained]: {{site.data.fhir.path}}references#contained.html "FHIR contained resource documentation"
[date]: {{site.data.fhir.path}}datatypes.html#date "FHIR date definition"
[dateTime]: {{site.data.fhir.path}}datatypes.html#dateTime "FHIR dateTime definition"
[extensible]: {{site.data.fhir.path}}terminologies.html#extensible
[FHIR API for Binary data]: {{site.data.fhir.path}}binary.html#rest "FServing Binary Resources using the RESTful API"
[instant]: {{site.data.fhir.path}}datatypes.html#instant "FHIR instant definition"
[Location]:{{site.data.fhir.path}}location.html "FHIR Location definition"
[Medication]:{{site.data.fhir.path}}medication.html "FHIR Medication definition"
[MedicationDispense]:{{site.data.fhir.path}}medicationdispense.html "FHIR MedicationDispense definition"
[MedicationRequest]:{{site.data.fhir.path}}medicationrequest.html "FHIR MedicationRequest definition"
[MedicationStatement]:{{site.data.fhir.path}}medicationstatement.html "FHIR MedicationStatement definition"
[Observation]:{{site.data.fhir.path}}observation.html "FHIR Observation definition"
[Pattern]: {{site.data.fhir.path}}https://www.hl7.org/fhir/structuredefinition.html#logical "FHIR logical model"
[Postman Collection]: :https://www.getpostman.com/collections/0a54cd0197a5f2fc98d4
[Quantity]: {{site.data.fhir.path}}datatypes.html#quantity "FHIR Quantity definition"
[Range]: {{site.data.fhir.path}}datatypes.html#range "FHIR Range definition"
[Ratio]: {{site.data.fhir.path}}datatypes.html#ratio "FHIR Ratio definition"
[required]: {{site.data.fhir.path}}terminologies.html#required
[Smart on FHIR Launch]: http://docs.smarthealthit.org/authorization/ "SMART App Authorization Guide"
[string]: {{site.data.fhir.path}}datatypes.html#string "FHIR string definition"
[Timing]: {{site.data.fhir.path}}datatypes.html#timing "FHIR Timing definition"
[todo]: todo.html "still under construction"
[OMH]: http://www.openmhealth.org/index.html
[Open mHealth]: http://www.openmhealth.org/
[OmhBloodGlucose]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_blood-glucose
[OmhStepCount]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_step-count
[OmhCaloriesBurned]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_calories-burned
[OmhGeoposition]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_geoposition
[OmhMinutesModerateActivity]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_minutes-moderate-activity
[OmhPace]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_pace
[OmhSpeed]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_speed
[OmhOrientation]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_orientation
[OmhBodyTemperature]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_body-temperature
[OmhBodyWeight]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_body-weight
[OmhHeartRate]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_heart-rate
[OmhRespiratoryRate]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_respiratory-rate
[OmhBodyHeight]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_body-height
[OmhBloodPressure]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_blood-pressure
[OmhDiastolicBloodPressure]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_diastolic-blood-pressure
[OmhSystolicBloodPressure]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_systolic-blood-pressure
[OmhBodyFatPercentage]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_body-fat-percentage
[OmhBodyMassIndex]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_body-mass-index
[OmhOxygenSaturation]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_oxygen-saturation
[OmhSleepDuration]:http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_sleep-duration
[example python application]: https://github.com/Healthedata1/mFHIR/tree/master/my-notes/python-mapping-example
