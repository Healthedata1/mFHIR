---
title: OMH to FHIR Mapping
layout: default
active: guidance
topofpage: true
sectionnumbering: true
omlschema_url: https://github.com/openmhealth/schemas/blob/master/schema/omh/
loinc_url: https://loinc.org/
sct_url: http://browser.ihtsdotools.org/?perspective=full&conceptId1=
---

{:.no_toc}

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}

### Mapping OMH Schema Mappings to FHIR Elements


Measurements such as steps or heart rate are modeled using OMH schemas.  These models can be used to represent instance of the measurement "over the wire" in JSON.  For example, using the step-count schema, a step count is represented as:

~~~
{
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
      "name": "step_count",
      "version": "1.0"
    },
    "user_id": "306a1202-410d-11e8-842f-0ed5f89f718b"
  },
  "body": {
    "effective_time_frame": {
      "time_interval": {
        "start_date_time": "2015-08-06T05:11:09-07:00",
        "end_date_time": "2015-08-06T23:00:36-06:00"
      }
    },
    "step_count": 7939
  }
}
~~~

The OMH schema can be transformed into FHIR data models - more specifically "Logical Models" that allow for a more 'FHR-like' view of the schema and a way to computationally map between FHIR and omh.  For example, this would allow the following transformation between the step count example and a FHIR representation using the Observation Resource:

{% include img.html img="omh_instance_mapping_1.png" %}

{% include img.html img="omh_instance_mapping_2.png" %}

<br />

**Other mappings:**

- [Example Mapping for OMH Heart Rate Schema](heartrate-example.html)


### Quick Start Mapping Guide 

  Formal FHIR Logical Models are included in this guide for mapping the models directly using a formal mapping syntax. However, the tables and templates below are provided to for quicks mappings an OMH schema instance to a FHIR *quantitative* Observation resource instance.  These can be used to perform simple string substitution and simple concept mappings methods to generate FHIR Observations.  An [example python application] using these tables and string templates is available


#### OMH Header Element to FHIR Element Mapping Table

Each OMH schema for a datapoint is composed of the 'header' and 'body,  This table is a map of the relatively static OMH heady element to the corresponding OMH to FHIR Observation Profile element.  Each datapoint schema represents the body's properties and will be covered individually.

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
|header.acquisition_provenance.last_modification_data_time|None|
|header.acquisition_provenance.modality|Observation.device.extension|
|header.user_id|Observation.subject|
{: .grid}

**Data Point Mapping Table**

Each Datapoint is represented by the body properties and this table is a summarey of the OMH datapoint schema type as represented by the `header.schema_id.name` element to the corresponding FHIR Observation `category` and 'code' elements and default units for quantitative measures.

|header.schema_id.name|Observation.category.code|Observation.code.system|Observation.code.code|Observation.code.display|observation_value_quantity_unit(s) (list)|descriptive_statistic|descriptive_statistic_denominator|components|
|--|--|--|--|--|--|--|--|--|
|acceleration|physical-activity|http://loinc.org|80493-0|Activity level [Acceleration]|None|False|False|[]|
|ambient_temperature|None|http://loinc.org|60832-3|Room temperature|None|False|False|[]|
|blood_glucose|laboratory|http://loinc.org|2339-0|Glucose Mass/volume in Blood|['mg/dL', 'mmol/L']|True|False|['temporal_relationship_to_sleep', 'temporal_relationship_to_meal']|
|blood_pressure|vital-signs|http://loinc.org|85354-9|Blood pressure panel with all children optional|None|True|False|['diastolic_blood_pressure', 'systolic_blood_pressure']|
|body_fat_percentage|exam|http://loinc.org|41982-0|Percentage of body fat Measured|['%']|True|False|[]|
|body_height|vital-signs|http://loinc.org|8302-2|Body height|['cm', 'in']|False|False|[]|
|body_mass_index|vital-signs|http://loinc.org|39156-5|Body mass index (BMI) Ratio|['kg/m^2']|True|False|[]|
|body_temperature|vital-signs|http://loinc.org|8310-5|Body temperature|['K','F','C']|True|False|['temporal_relationship_to_sleep']|
|body_weight|vital-signs|http://loinc.org|29463-7|Body weight|['kg', 'g', 'lb']|True|False|[]|
|breath_carbon_monoxide|laboratory|http://snomed.info/id|251900003|Expired carbon monoxide concentration (observable entity)|None|False|False|[]|
|calories_burned|physical-activity|http://loinc.org|41981-2|Calories burned|['kcal']|True|True|[]|
|diastolic_blood_pressure|vital-signs|http://loinc.org|8462-4|Diastolic blood pressure|['mmHg']|False|False|[]|
|expiratory_time|exam|http://loinc.org|60739-0|Expiration Time Respiratory system|None|False|False|[]|
|geoposition|physical-activity|http://www.fhir.org/guides/omhtofhir/datapoint-type|geoposition|Geoposition|None|False|False|[]|
|heart_rate|vital-signs|http://loinc.org|8867-4|Heart rate|['beats/min']|True|False|['temporal_relationship_to_physical_activity', 'temporal_relationship_to_sleep']|
|inspiratory_time|exam|http://loinc.org|60740-8|Inspiration Time Respiratory system|None|False|False|[]|
|magnetic_force|physical-activity|http://www.fhir.org/guides/omhtofhir/datapoint-type|magnetic_force|Magnetic Force Panel|None|False|False|[]|
|medication_adherence_percent|Survey|http://snomed.info/id|418633004|Medication compliance (observable entity)|None|False|False|[]|
|minute_volume|exam|http://loinc.org|20139-2|Volume expired 1 minute|None|False|False|[]|
|minutes_moderate_activity|physical-activity|http://snomed.info/id|408581006|Physical activity target moderate exercise (finding)|['min']|False|False|[]|
|orientation|vital-signs|http://www.fhir.org/guides/omhtofhir/datapoint-type|orientation|Gyroscope measurement Panel|None|False|False|[]|
|oxygen_saturation|vital-signs|http://loinc.org|59408-5|Oxygen saturation in Arterial blood by Pulse oximetry|['%']|True|False|['supplemental_oxygen_flow_rate', 'oxygen_therapy_mode_of_administration']|
|pace|physical-activity|http://www.fhir.org/guides/omhtofhir/datapoint-type|pace|Pace|None|False|False|[]|
|physical_activity|physical-activity|http://snomed.info/id|68130003|Physical activity (observable entity)|None|False|False|[]|
|respiratory_rate|vital-signs|http://loinc.org|9279-1|Respiratory Rate|['breaths/min']|True|False|['temporal_relationship_to_physical_activity']|
|rr_interval|exam|http://loinc.org|8637-1|R_R interval by EKG|None|False|False|[]|
|sleep_duration|physical-activity|http://snomed.info/id|248263006|Duration of sleep (observable entity)|['sec', 'min', 'h']|True|True|[]|
|sleep_episode|physical-activity|http://snomed.info/id|258158006|Sleep, function (observable entity)|None|False|False|[]|
|speed|physical-activity|http://ncimeta.nci.nih.gov|C0678536|Speed|None|False|False|[]|
|step_count|physical-activity|http://loinc.org|55423-8|Number of steps in unspecified time Pedometer|['steps']|True|True|[]|
|systolic_blood_pressure|vital-signs|http://loinc.org|8480-6|Systolic blood pressure|['mmHg']|False|False|[]|
|ventilation_cycle_time|exam|http://snomed.info/id|250818005|Ventilation cycle time (observable entity)|None|False|False|[]|
{:.grid}

**Data Point Component Mapping Table**

Some Datapoints properties are represented by the FHIR `Observation.component` element in FHIR.  This table summarizes these OMH datapoint schema properties and list the corresponding OMH propertied name in the  `Component Name` column and its corresponding FHIR Observation component code and valuetype attributes.  This table is used along with the OMH to FHIR concept mapping table to to populate the the Observation template below.

|Component Name|Component Code System|Component Code Code|Component Code Display|Component Value Type|
|--|--|--|--|--|
|body_posture|http://snomed.info/sct|271605009|Position of body and posture (observable entity)|valueCodeableConcept|
|diastolic_blood_pressure|http://loinc.org|8462-4|Diastolic blood pressure|valueQuantity|
|systolic_blood_pressure|http://loinc.org|8480-6|Systolic blood pressure|valueQuantity|
|temporal_relationship_to_meal|http://www.fhir.org/guides/omhtofhir/omh_fhir_observation_codes|relative-to-meal|OMH to FHIR Temporal Relationship To Meal|valueCodeableConcept|
|temporal_relationship_to_physical_activity|http://www.fhir.org/guides/omhtofhir/omh_fhir_observation_codes|relative-to-activity|OMH to FHIR Temporal Relationship To Physical Activity|valueCodeableConcept|
|temporal_relationship_to_sleep|http://www.fhir.org/guides/omhtofhir/omh_fhir_observation_codes|relative-to-sleep|OMH to FHIR Temporal Relationship To Sleep|valueCodeableConcept|
{: .grid}

#### Observation Template

This FHIR Observation template is an instance view of the above mappings and can be populated with data from OMH schemas to create a FHIR Observation instance.

{% raw %}
~~~
{
       "resourceType": "Observation",
       "id": {{server_assigned_resource_id}},  //note 1,2,6
       "meta": {
       "profile" : ["http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_profile_quantitative_observation"]  // note 7
     },
     "extension" : [{
         "url" : {{observation_specimen_code_extension_url}},
         "valueCodeableConcept": {
         "coding": [
           {
             "system": {{observation_specimen_code_system}},
             "code": {{observation_specimen_code_code}},
             "display": {{observation_specimen_code_display}}
           }
         ],
         "text": {{observation_specimen_code_text}}
       }
    }],
       "identifier"  : [{
       "system" : "https://omh.org/shimmer/ids", //note 7
       "value" : {{header.id}} //note 3
       }],
       "status": "unknown",  //note 9
       "category": [  //note 4
         {
           "coding": [
             {
               "system": "http://hl7.org/fhir/observation-category",
               "code": {{observation_category_code}},
               "display": {{observation_category_display}}
             }
           ]
         }
       ],
       "code": {   //note 4
         "coding": [
           {
             "system": {{observation_code_system}},
             "code": {{observation_code_code}},
             "display": {{observation_code_display}}
           }
        ,{
          "system" : {{addl_observation_coding_system}}, //note 12
          "code" : {{addl_observation_coding_code}},
          "display" : {{addl_observation_coding_display}}
        }
         ]
       },
       "subject": {  //note 8
         "identifier" : {
       "system" : "https://omh.org/shimmer/patient_ids",
       "value" : {{header.user_id}}
     }
       },
       "effectiveDateTime" : {{body.effective_time_frame.date_time}},  //note 11
       "effectivePeriod" : {  //note 11
          "start" : {{body.effective_time_frame.time_interval.start_date_time}}, 
          "end" : {{body.effective_time_frame.time_interval.end_date_time}}
          }, 
       "issued": {{header.creation_date_time}},
       "valueQuantity" : {  //note 10
         "value" : {observation_value_quantity_value},
         "unit" : {{observation_value_quantity_unit}},
         "system" : {{observation_value_quantity_system}}, 
         "code" : {{observation_value_quantity_code}}
        },
        "comment" : {{body.user_notes}},
        "device" : {
        "extension" : [{
          "url" : "http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_observation_device_modality",
          "valueCode" : {{header.acquisition_provenance.modality}}
        }],
        "display" : {{header.acquisition_provenance.source_name}}
        },
        "component": [{observation_componentx}]  //note 5
      }
~~~
{% endraw %}

#### observation_componentx Subtemplates

This FHIR Observation sub template is an instance view of the Observation component element derived from the OMH schema e and can be populated with data to create a FHIR Observation instance.

{% raw %}
~~~
,"component" : [{
    "code" : { 
      "coding" : [{ 
        "system" :"http://www.fhir.org/guides/omhtofhir/omh_fhir_observation_codes",
        "code" : "{{observation_component_code_code}}", 
        "display" : "{{observation_component_code_display}}"
         }]
       },
    "valueCodeableConcept" : { 
      "coding" : [{ 
        "system" : "{{observation_component_value_codeableconcept_system}}", 
        "code" : "{{observation_component_value_codeableconcept_code}}", 
        "display" : "{{observation_component_value_codeableconcept_display}}"
        }],
        "text" : "{{observation_component_value_codeableconcept_text}}"
        },
       "valueQuantity" : {
         "value" : {{observation_component_value_quantity_value}},
         "unit" : "{{observation_component_value_quantity_unit}}",
         "system" : "{{observation_component_value_quantity_system}}", 
         "code" : "{{observation_component_value_quantity_code}}"
        }
     }
~~~
{% endraw %}


Notes on template usage:

1. Template variables are represented using the "\{\{}}" syntax
1. Note that when present, FHIR elements cannot be empty.  Therefore, all 'null' values (i.e.,undefined, Null, None, or '' values or empty json objects or lists) are removed from the resource after the OMH data is mapped to it.
1. Variable such as \{\{header.id}} represent OMH data elements in dot notation mapped directly from the header schema.
1. Variables in "snake case" are such as \{\{observation_category_code}}  \{\{observation_code_code}} represent the corresponding dot notation columns in the OMH Data Point Mapping Table provided above(which are based on the OmhDataPoint.header.schema_id.name).
1. the variables \{\{observation-valuex}} (the actual result values), \{\{observation-effectivex}} (the actual times the measurements occurred ) and \{\{observation-componentx}} are subtemplates and are mapped from the body schema for each of the datapoints.
1. \{\{server_assigned_resource_id}} is a assigned by the server when the resource is created and is typically not mapped from the OMH schema instance.
1. The profile element is the FHIR profiles this resource claims will conform to when fully populated.
1. The namespaces, "https://omh.org/shimmer/ids"  and "https://omh.org/shimmer/patient_ids" are use to assign a system to shimmer generated ids.
1. The `status` element is required in FHIR Observation and since omh schema don't have status its values is hardcoded to 'unknown'
1. The measurement value ( e.g., step-count) and units derived from the descriptive statistics schema and can be populated with data to create a FHIR Observation instance.
1. There is a  choice of datetime or time period mappings over which the measurement occurred for the step count schema and can be populated with data it to create a FHIR Observation instance. Note that the empty values will be removed from the instance.
1. Additional codings are derived from the descriptive statistics schema using a compositional code consisting of the concatenation of the datapoint schema name with the descriptive statistic code in "spinal case"  ( e.g  `step-count-maximum`). If the descriptive statistics is absent the schema, there are no additional codings in the OMH to FHIR instance.




###  Mapping Strategy

In order to map the OMH schema to FHIR, the OMH Schemas are divided conceptually into several categories.  The infrastructural `schema` model serves as a basic blueprint for creation of OMH schema and is not used in the mappings. The infrastructural `data-point` schema provide the basic framework upon which the data-points schemas are based and serves as the backbone for creation of the FHIR logical model. It is made up of a `header` property representing MedicationDispense information and  a `body` property representing one of the omh schemas that represent a measurements i.e., 'a data point'.

#### OMH Header Schema Mapping to FHIR elements

The OMH header schema represent data MedicationDispense and the properties in the header schema map to more than a single FHIR element.  In addition, depending on the depth and level of detail required, there are multiple options to representing MedicationDispense including:

- [MedicationDispense]({{site.data.fhir.path}}MedicationDispense.html)resource
- [meta.source]({{site.data.fhir.path}}resource.html#Meta) element
- inline Resource elements

These options are summarized in the table below and described in detail in the data point logical model mappings.

|Source = OMH Schema|Target = FHIR Element|OMH FHIR Logical Model|
|---|---|---|
|[header-1.2.json]({{page.omlschema_url}}header-1.2.json)|[Observation][Observation]\|[MedicationDispense][MedicationDispense]  Profile||
{:.grid}

The rest of the omh schemas represent either data points or more granular reusable elements or concepts that can be referenced within the data-point schemas. Each reusable omh schema are mapped primitive and complex datatypes as shown below. In addition some of these schemas enumerate values which are [bound]({{site.data.fhir.path}}terminologies.html)) to FHIR ValueSets.  The reusable schemas are mapped directly to fhir artifacts as described below and these mapping replace the omh schema references when transforming an OMH data point schema into a FHIR Logical Model.

####  OMH Schema Mappings to FHIR Datatypes

In this table, the schemas representing primitive and complex data-types are mapped directly to the corresponding FHIR datatype.  Listed in the *FHIR ValueSet* column the corresponding FHIR ValueSets and [binding strength]({{site.data.fhir.path}}datatypes.html#code) for the schemas that map to the FHIR `code`, an units values for the `Quantity`, and `Range` dataypes.

-  Where a value is fixed such as for *acceleration-unit-value-1.0.json*, a fixed [Pattern] is associated with the schema which directly applied to the FHIR logical models when the schema is referenced.
-  Where the unit value is an enumeration of units a FHIR *ValueSet* is associated with the schema.
-  Both the patterns and ValueSets contain **UCUM** based units.
-  For data point schemas that reference schemas associated with ValueSets (such as *unit-value-1.0.json*), the actual units and hence the patterns applied to the FHIR logical models van be further constrained by the data point schema themselves.

{% include omh-dt-table.md %}


#### OMH datapoint Schema Mappings to FHIR Resources

Logical Models for each datapoint schema are mapped to a FHIR Logical Model before being mapped to the target FHIR resource profile as listed in the table below.  The concept code for the measurement is in the description property of the schema are listed in the *Observation.code* column. For Schema that are mapped to `Observation`, this code is mapped to `code` in then Observation resource.:

{% include omh-datapoint-table.md %}



### Mapping Example

The transformation from the OMH data-point schema to the FHIR Logical models and from the FHIR Logical model to the FHIR resource is straightforward and demonstrated below.

Note:
- elements with a value of Null are **not**  transmitted in FHIR 
- some elements require a mapping to a codes using the translation tables in this Guide.

**OMH Stepcount Datapoint instance**

~~~
    {
      "header": {
        "id": "243c773b-8936-407e-9c23-270d0ea49cc4",
        "creation_date_time": "2015-09-10T12:43:39.138-06:00",
        "acquisition_MedicationDispense": {
          "source_name": "Jawbone UP API",
          "modality": "sensed",
          "source_updated_date_time": "2015-09-10T18:43:39Z"
        },
        "schema_id": {
          "namespace": "omh",
          "name": "step-count",
          "version": "1.0"
        },
        "user_id": "306a1202-410d-11e8-842f-0ed5f89f718b"
      },
      "body": {
        "effective_time_frame": {
          "time_interval": {
            "start_date_time": "2015-08-06T05:11:09-07:00",
            "end_date_time": "2015-08-06T23:00:36-06:00"
          }
        },
        "step_count": 7939
      }
    }
~~~

Converting this datapoint instance to *dot notation* representation here to show more clearly the mapping to the FHIR Observation Resource data elements

~~~
    O.header
        O.header.id = "243c773b-8936-407e-9c23-270d0ea49cc4"
        O.header.creation_date_time = "2015-09-10T12:43:39.138-06:00"
        O.header.acquisition_MedicationDispense"
          O.header.acquisition_MedicationDispense.source_name = "Jawbone UP API"
          O.header.acquisition_MedicationDispense.modality = "sensed"
          O.header.acquisition_MedicationDispense.source_updated_date_time = "2015-09-10T18:43:39Z"
        O.header.schema_id 
          O.header.schema_id.namespace  = "omh"
          O.header.schema_id.name =  "step-count"
          O.header.schema_id.version = "1.0"
        O.header.user_id = 306a1202-410d-11e8-842f-0ed5f89f718b"
      O.body 
        O.body.effective_time_frame 
          O.body.effective_time_frame.time_interval 
            O.body.effective_time_frame.time_interval.start_date_time = "2015-08-06T05:11:09-07:00"
            O.body.effective_time_frame.time_interval.end_date_time ="2015-08-06T23:00:36-06:00"
        O.body.step_count = 7939
~~~

**This OMH Schema instance maps to the FHIR Observation Resource directly as follows: ** (using the syntax  %(foo) to represent the replacement variables in the resource)
''
~~~
        
        {
          "resourceType": "Observation",
        	"id": "steps-example //  this is a server assigned resource id",
          "meta": {
          "source" : "%(OmhDataPoint.header.acqusitionProvenance.sourceName)",
          "profile // Profiles this resource claims to conform to" : ["http://www.fhir.org/guides/omhtofhir/StructureDefinition/steps"]
        }
          "identifier  : [
          "system" : "https://omh.org/shimmer/ids // The namespace for the identifier value",
          "value" : "%(OmhDataPoint.header.Id)",
          }],
          "status": "unknown // this is required in fhir - omh schema don't have status",
        	"category // optional category field to indicate is an activity vs say a lab result": [  
        		{
        			"coding": [
        				{
        					"system": "http://hl7.org/fhir/observation-category",
        					"code": "activity",
        					"display": "Activity"
        				}
        			]
        		}
        	],
        	"code // code mapping from OmhDataPoint.header.schema_id.name see mapping table in IG": {
        		"coding": [
              {
        				"system": "http://loinc.org",
        				"code": "55423-8",
        				"display": "Number of steps in unspecified time Pedometer"
        			}
        		],
        		"text": "Step count"
        	},
        	"subject": {
        		"identifier" : {
          "system" : "https://omh.org/shimmer/patient_ids // The namespace for the identifier value",
          "value" : "%(OmhDataPoint.header.user_id)",
        },
        	},
        	"effectivePeriod // mapped from OmhDataPoint.body.effectiveTimeFrame":
          "start" : "%(OmhDataPoint.body.effective_time_frame.time_interval.start_date_time)",
          "end" : "%(OmhDataPoint.body.effective_time_frame.time_interval.end_date_time)"
            }
        	"issued": "%(OmhDataPoint.header.creation_date_time)",

        	"valueQuantity  // the actual results mapped from body.step_count  - note that I added optional UCUM units from the lookup tables": {
        		"value": %(OmhDataPoint.body.stepCount),
        		"unit": "steps",
        		"system": "http://unitsofmeasure.org",
        		"code": "{steps}"
        	}
           "device //  could be mapped from OmhDataPoint.header.acqusitionProvenance elements as well" :
           {"display" : "%(OmhDataPoint.header.acqusitionProvenance.sourceName)"}
        }
~~~

<!--

The transformation from the OMH data-point schema to the FHIR Logical models and from the FHIR Logical model to the FHIR resource is straightforward and conceptual mappings are provided for each.  The following example illustrates transforming from the step-count omh schema to a FHIR observation.  The process can be automated using omh schemas and one of several FHIR libraries that are available.

*Mapping from the source MHealth file to the OMH Logical Model*

In this section the following Open MHealth data-point instance  will be transfored to a FHIR Observation.

{% include source_mHealth_file.md %}

The first step is to map from the Open MHealth data-point schema to the OmhDataPoint Logical Model.  The source JSON data is transformed following the *first* [mapping table](StructureDefinition-omh-data-point.html#sd-3-2-mappings) provided in the OmhDataPoint Logical Model and referencing the formal [StructureDefinition](StructureDefinition-omh-data-point.html#sd-3-1formal-views-of-profile-content) for the structural details.  So for example from the example source file below, based on the mapping table `OmhDataPoint.header.id` is translated to `OmhDataPoint.header.dataPointId` which a primitive `id` datatype.

 The OmhDataPoint `body` element is a choice of other logical models based on the datapoint schema listed above. These models are their mappings are referenced to complete the mapping. For example, `properties.body.effective_time_frame` is mapped to the OMHStepCount Logical Model and data transformed based on its [mapping table](StructureDefinition-omh-step-count.html#sd-1-2-mappings)
A complex data element  such as `effective_time_frame` is mapped to the `OMHStepCount.effectiveTimeFrame` element which is a FHIR [Period]({{site.data.fhir.path}}datatypes.html#Period) whose detailed structure is available in the FHIR specification and can accessed by following the links in the logical model.  Here is how the Period datatype maps to the effective_time_frame

|FHIR Period data type|
|---|
effective_time_frame.time_interval.start_date_time|
effective_time_frame.time_interval.end_date_time|
{: .grid}

After mapping all the elements in the source file to the OmhDataPoint Logical Model, we get the following OmhDataPoint json file:

{% include omh-data-point-worked-example.md %}

The next step is to map from the OmhDataPoint Logical Model to the appropriate FHIR resource, which in this case is [Observation][Observation]).  Similar to the first step, The OMH logica model JSON data is transformed to the FHIR Resource following the *second* [mapping table](StructureDefinition-omh-data-point.html#sd-3-2-mappings) provided in the OmhDataPoint Logical Model and referencing the formal definitions of the FHIR resource the structural details.  Since the OMH Logical Model and the FHIR Resource share the same datatypes the process is relatively straight.  In some cases there are no mappings because the element are infrasture related only to the OMH schemas.  In other cases there are choices on how to transform the data and the use case and best practices should determine the outcome.

For example, the OmhDataPoint.dataPointId is mapped to Observation.identifier, OmhDataPoint.header.namespace is unmapped.  Again, the OmhDataPoint `body` element is a choice of other logical models based on the datapoint schema listed above. Note that in many cases the Logical Model maps to the FHIR element `Observation.code` with a fixed value for code and code system. In this example the OmhStepCount Logical Model maps to Observation.code with LOINC =55423-8. The other element are mapped as above - for example, OmhDataPoint.body.stepCount is mapped to Observation.valueQuantity.  As a result of the mapping the following Observation resource is derived:

{% include observation-worked-example.md %}

<br />

**Mapping descriptiveStatistic to Observation**

If there is a descriptiveStatistic element the step count value is mapped to the `Observation.component.value[x]` *instead*  of `Observation.value[x]` as follows:

1. `Observation.valueQuantity` is absent
1.  descriptiveStatistic code is mapped to `Observation.component.code`
1. Step count value is mapped to the `Observation.component.valueQuantity.value
1.  descriptiveStatisticDenominator is mapped to the denominator in `Observation.component.valueQuantity.unit` and `Observation.component.valueQuantity.code`

{% include observation-step-count-max.md %}
-->
<br />

{% include link-list.md %}
