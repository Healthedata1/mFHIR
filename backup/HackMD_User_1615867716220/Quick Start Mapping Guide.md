---
tags: omh2fhir
---

{%hackmd 2yYAoTGSSpiWVb7EWu6v0w %}

# Quick Start Mapping Guide


## Quick Start Mapping Guide For Mapping OMH Schema Mappings to FHIR Elements

Measurements such as steps or heart rate are modeled using [OMH schemas](https://www.openmhealth.org/documentation/#/schema-docs/schema-library).  These models can be used to represent instance of the measurement "over the wire" in JSON.  Each OMH instance represents a datapoint such as body weight or temperature.  It is composed of a "header" and "body" element whose properties are defined by a [header schema](http://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_header) and the individual datapoint schemas including the following 9 OMH schemas which are the subject of this guide:

1. [Blood Glucose](https://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_blood-glucose)
1. [Blood Pressure](https://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_blood-pressure)
1. [Body Temperature](https://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_body-temperature)
1. [Body Weight](https://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_body-weight)
1. [Heart Rate](https://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_heart-rate)
1. [Oxygen Saturation](https://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_oxygen-saturation)
1. [Respiratory Rate](https://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_respiratory-rate)
1. [Total Sleep Time](https://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_total-sleep-time)
1. [Step Count](https://www.openmhealth.org/documentation/#/schema-docs/schema-library/schemas/omh_step-count)

These OMH schema can be transformed into [FHIR](http://hl7.org/fhir/) using a series of mapping steps to convert the structure and content into a corresponding FHIR Observation resource and optionally, a [contained] FHIR Provenance resource as a record of the transformation as illustrated in the figure 1:

**figure 1**
![](https://i.imgur.com/dMywg9h.png)



The next section outlines the mapping of the OMH header schema to the both the FHIR Observation and Provenance resources. The subsequent sections below cover the mapping of the individual data point schema properties to the remaining FHIR Observation elements.

### OMH Header Element to FHIR Element Mapping Table

The following 2 tables summarize the mapping of the OMH header elements to the corresponding OMH to FHIR Observation and the optional Provenance resource.

**OMH Header to Observation Mapping Table**


| OMH element                                             | FHIR element                                                                |
| ------------------------------------------------------- | --------------------------------------------------------------------------- |
| template profile                                        | OMH to FHIR Observation Profile                                             |
| header. id                                              | Observation.identifier                                                      |
| header.creation_date_time                               | Observation.issued                                                          |
| header.schema_id                                        | None                                                                        |
| header.schema_id.namespace                              | None                                                                        |
| header.schema_id.name                                   | Observation.category,Observation.code ( see datapoint mapping table below ) |
| header.schema_id.version                                | None                                                                        |
| header.acquisition_provenance                           | None                                                                        |
| header.acquisition_provenance.source_name               | Observation.device                                                          |
| header.acquisition_provenance.source_data_point_id      | Observation.identifier                                                      |
| header.acquisition_provenance.source_creation_date_time | None                                                                        |
| header.acquisition_provenance.modication_data_time      | None                                                                        |
| header.acquisition_provenance.modality                  | Observation.device.extension                                                |
| header.user_id                                          | Observation.subject                                                         |
<!--{: .grid}-->

The detailed mapping for the OMH header to FHIR Observation can be found [OMH Header Detailed Mapping](/KNSo9U0eTWaqLJRDqbKbWg)

**OMH Header to Provenance Mapping Table**

|OMH element|FHIR element|
|---|---|
|template profile|OMH to FHIR Provenance Profile|
|header.id|Provenance.entity.what.identifier.value (optional)|
|header.creation_date_time|None|
|header.schema_id|Provenance.agent.who.identifier|
|header.schema_id.namespace|Provenance.agent.who.identifier|
|header.schema_id.name|None|
|header.schema_id.version|Provenance.agent.who.identifier|
|header.acquisition_provenance|None|
|header.acquisition_provenance.source_name|Provenance.entity.agent.who.display|
|header.acquisition_provenance.source_data_point_id|None|
|header.acquisition_provenance.source_creation_date_time|None|
|header.acquisition_provenance.last_modification_data_time|None|
|header.acquisition_provenance.modality|None|
|header.user_id|None|
<!--{: .grid}-->

The detailed mapping for the OMH header to FHIR Provenance can be found [OMH Header Detailed Mapping](/KNSo9U0eTWaqLJRDqbKbWg)

### OMH DataPoint Element to FHIR Element Mapping Table

Each Datapoint is represented by the body properties and this table summarizes of the OMH datapoint schema type as represented by the `header.schema_id.name` element to the corresponding FHIR Observation `category` and 'code' elements and default units for quantitative measures. The detailed mapping for each datapoint can be found in the appropriate section in the [Quick Start Mapping Guide](/CncEQ4ewSYOKPPy1GxXpCQ)

header.schema_id.name|Observation.category.code|Observation.code.system|Observation.code.code|Observation.code.display|observation_value_quantity_unit(s) (list)|
--|--|--|--|--|--|
blood_glucose|laboratory|http://loinc.org|2339-0|Glucose Mass/volume in Blood|['mg/dL', 'mmol/L']|
blood_pressure*|vital-signs|http://loinc.org|85354-9|NA*|
body_temperature|vital-signs|http://loinc.org|8310-5|Body temperature|['K','F','C']|
body_weight|vital-signs|http://loinc.org|29463-7|Body weight|['kg', 'g', 'lb']|
heart_rate|vital-signs|http://loinc.org|8867-4|Heart rate|['beats/min']|
oxygen_saturation|vital-signs|http://loinc.org|59408-5|Oxygen saturation in Arterial blood by Pulse oximetry|['%']|
respiratory_rate|vital-signs|http://loinc.org|9279-1|Respiratory Rate|['breaths/min']|
total_sleep_time|physical-activity|http://snomed.info/id|248263006|Duration of sleep (observable entity)|['sec', 'min', 'h']|
step_count|physical-activity|http://loinc.org|55423-8|Number of steps in unspecified time Pedometer|['steps']|

\* The Blood Pressure schema does not have units,  references systolic and diastolic blood pressure schemas which do.  These "subschemas" are mapped to the FHIR `Observation.component` element discussed in the next section. 

### Data Point Component Mapping Table

  This table summarizes these OMH datapoint schema properties and list the corresponding OMH propertied name in the  `Component Name` column and its corresponding FHIR Observation component code and valuetype attributes.  This table is used along with the OMH to FHIR concept mapping table to to populate the the FHIR Observation profile.

|Component Name|Component Code System|Component Code Code|Component Code Display|Component Value Type|
|--|--|--|--|--|
|diastolic_blood_pressure|http://loinc.org|8462-4|Diastolic blood pressure|valueQuantity|
|systolic_blood_pressure|http://loinc.org|8480-6|Systolic blood pressure|valueQuantity|

