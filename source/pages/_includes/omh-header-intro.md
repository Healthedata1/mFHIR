{% assign id = {{page.id}} %}
source file: source/pages/\_includes/{{id}}-intro.md

{{site.data.structuredefinitions.[id].description}}



### Quick Start Mapping Guide 

  Formal FHIR Logical Models are included in this guide for mapping the models directly using a formal mapping syntax. However, the tables and templates below are provided to for quicks mappings an OMH schema instance to a FHIR *quantitative* Observation resource instance.  These can be used to perform simple string substitution and simple concept mappings methods to generate FHIR Observations.


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
|header.acquisition_provenance._last_modification_data_time|None|
|header.acquisition_provenance.modality|Observation.device.extension|
|header.user_id|Observation.subject|
{: .grid}

**Data Point Mapping Table**

Each Datapoint is represented by the body properties and this table is a summarey of the OMH datapoint schema type as represented by the `header.schema_id.name` element to the corresponding FHIR Observation `category` and 'code' elements and default units for quantitative measures.

|header.schema_id.name|Observation.category.code|Observation.code.system|Observation.code.code|Observation.code.display|
|---|---|---|---|---|
|acceleration|physical-activity|http://loinc.org|80493-0|Activity level [Acceleration]|
|ambient_temperature|None|http://loinc.org|60832_3| Room temperature|
|blood_glucose|vital-signs|http://loinc.org|2339_0| Glucose Mass/​volume in Blood|
|blood_pressure|vital-signs|http://loinc.org|85354_9| Blood pressure panel with all children optional|
|body_fat_percentage|exam|http://loinc.org|41982_0| Percentage of body fat Measured |
|body_height|vital-signs|http://loinc.org|8302_2| Body height|
|body_mass_index|vital-signs|http://loinc.org|39156_5| Body mass index (BMI) Ratio|
|body_temperature|vital-signs|http://loinc.org|8310_5| Body temperature|
|body_weight|vital-signs|http://loinc.org|29463_7| Body weight|
|breath_carbon_monoxide|laboratory|http://snomed.info/id|251900003|Expired carbon monoxide concentration (observable entity)|
|calories_burned|physical-activity|http://loinc.org|41981_2| Calories burned|
|diastolic_blood_pressure|vital-signs|http://loinc.org|8462_4| Diastolic blood pressure|
|expiratory_time|exam|http://loinc.org|60739_0| Expiration Time Respiratory system|
|geoposition|physical-activity|http://www.fhir.org/guides/mfhir/datapoint-type|geoposition|Geoposition|
|heart_rate|vital-signs|http://loinc.org|8867_4|Heart rate|
|inspiratory_time|exam|http://loinc.org|60740_8| Inspiration Time Respiratory system|
|magnetic_force|physical-activity|http://www.fhir.org/guides/mfhir/datapoint-type|magnetic_force|Magnetic Force Panel|
|medication_adherence_percent|Survey|http://snomed.info/id|418633004|Medication compliance (observable entity)|
|minute_volume|exam|http://loinc.org|20139_2| Volume expired 1 minute|
|minutes_moderate_activity|physical-activity|http://snomed.info/id|408581006|Physical activity target moderate exercise (finding)|
|orientation|vital-signs|http://www.fhir.org/guides/mfhir/datapoint-type|orientation|Gyroscope measurement Panel|
|oxygen_saturation|vital-signs|http://loinc.org|59408_5|Oxygen saturation in Arterial blood by Pulse oximetry|
|pace|physical-activity|http://www.fhir.org/guides/mfhir/datapoint-type|pace|Pace|
|physical_activity|physical-activity|http://snomed.info/id|68130003|Physical activity (observable entity)|
|respiratory_rate|vital-signs|http://loinc.org|9279_1|Respiratory Rate|
|rr_interval|exam|http://loinc.org|8637_1|R_R interval by EKG|
|sleep_duration|physical-activity|http://snomed.info/id|248263006|Duration of sleep (observable entity)|
|sleep_episode|physical-activity|http://snomed.info/id|258158006|Sleep, function (observable entity)|
|speed|physical-activity|http://ncimeta.nci.nih.gov|C0678536|Speed|
|step_count|physical-activity|http://loinc.org|55423_8|Number of steps in unspecified time Pedometer|
|systolic_blood_pressure|vital-signs|http://loinc.org|8480_6|Systolic blood pressure|
|ventilation_cycle_time|exam|http://snomed.info/id|250818005|Ventilation cycle time (observable entity)|
{:.grid}

#### Observation Template

This FHIR Observation template is an instance view of the above mappings and can be populated with data from OMH schemas to create a FHIR Observation instance.

{% raw %}
~~~
{
       "resourceType": "Observation",
       "id": "{{server_assigned_resource_id}}",   //note 1,2,5
       "meta": {
       "profile" : ["http://www.fhir.org/mfhir/StructureDefinition/omh-to-fhir-observation"]  // note 6
     },
       "identifier"  : [{
       "system" : "https://omh.org/shimmer/ids",  //note 7
       "value" : "{{header.id}}"  //note 3
       }],
       "status": "unknown",  //note 8
       "category": [  //note 9
         {
           "coding": [
             {
               "system": "http://hl7.org/fhir/observation-category",
               "code": "{{observation_category_code}}",
               "display": "{{observation_category_display}}"
             }
           ]
         }
       ],
       "code": {  //note 9
         "coding": [
           {
             "system": "{{observation_code_system}}",
             "code": "{{observation_code_code}}",
             "display": "{{observation_code_display}}"
           }
        ,{
          "system" : "{{addl_observation_code_system}}",
          "code" : "{{addl_observation_coding_code}}",
          "display" : "{{addl_observation_coding_display}}"
        }
         ]
       },
       "subject": { //note 7
         "identifier" : {
       "system" : "https://omh.org/shimmer/patient_ids",
       "value" : "{{header.user_id}}"
     }
       },
       "effectiveDateTime" : "{{body.effective_time_frame.time_interval.date_time}}", //note 4
       "effectivePeriod" : {  //note 4
          "start" : "{{body.effective_time_frame.time_interval.start_date_time}}", 
          "end" : "{{body.effective_time_frame.time_interval.end_date_time}}"
          }, 
       "issued": "{{header.creation_date_time}}",
       "valueQuantity" : {  //note 4
         "value" : {observation_value_quantity_value},
         "unit" : "{{observation_value_quantity_unit}}",
         "system" : "http://unitsofmeasure.org", 
         "code" : "{{observation_value_quantity_code}}"
        },  
        "device" : {
        "extension" : [{
          "url" : "http://www.fhir.org/mfhir/StructureDefinition/observationDeviceModality",
          "valueCode" : "{{header.acquisition_provenance.modality}}"
        }],
        "display" : "{{header.acquisition_provenance.source_name}}"}
        {observation_componentx}  //note 4
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

#### observation_componentx Subtemplates

This FHIR Observation sub template is an instance view of the Observation component element derived from the OMH schema e and can be populated with data to create a FHIR Observation instance.

{% raw %}
~~~
"component" : [{
    "code" : { 
      "coding" : [{ 
        "system" :"http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes",
        "code" : "{{observation_component_code_code}}", 
        "display" : "{{observation_component_code_display}}" }, 
    "valueCodeableConcept" : { 
      "coding" : [{ 
        "system" : "{{observation_component_value_codeableconcept_system}}", 
        "code" : "{{observation_component_value_codeableconcept_code}}", 
        "display" : "{{observation_component_value_codeableconcept_display}}"}
     }]
~~~
{% endraw %}




#### Example

For example see the datapoint Profiles
