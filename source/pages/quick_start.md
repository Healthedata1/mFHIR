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
