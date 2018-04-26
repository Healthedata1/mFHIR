---
title: General Guidance and Definitions
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

## Mapping OMH Schema Mappings to FHIR Elements


Measurements such as steps or heart rate are modeled using OMH schemas.  These models can be used to represent instance of the measurement "over the wire" in JSON.  For example, using the step-count schema, a step count is represented as:

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

The OMH schema can be transformed into FHIR data models - more specifically "Logical Models" that allow for a more 'FHR-like' view of the schema and a way to computationally map between FHIR and omh.  For example, this would allow the following transformation between the step count example and a FHIR representation using the Observation Resource:

{% include img.html img="omh_instance_mapping_1.png" %}

{% include img.html img="omh_instance_mapping_2.png" %}

<br />

**Other mappings:**

- [Example Mapping for OMH Heart Rate Schema](heartrate-example.html)

###  Mapping Strategy

In order to map the OMH schema to FHIR, the OMH Schemas are divided conceptually into several categories.  The infrastructural `schema` model serves as a basic blueprint for creation of OMH schema and is not used in the mappings. The infrastructural `data-point` schema provide the basic framework upon which the data-points schemas are based and serves as the backbone for creation of the FHIR logical model. It is made up of a `header` property representing MedicationDispense information and  a `body` property representing one of the omh schemas that represent a measurements i.e., 'a data point'.

#### OMH Header Schema Mapping to FHIR elements

The OMH header schema represent data MedicationDispense and the properties in the header schema map to more than a single FHIR element.  In addition, depending on the depth and level of detail required, there are multiple options to representing MedicationDispense including:

- [MedicationDispense]({{site.data.fhir.path}}/MedicationDispense.html)resource
- [meta.source]({{site.data.fhir.path}}/resource.html#Meta) element
- inline Resource elements

These options are summarized in the table below and described in detail in the data point logical model mappings.

|Source = OMH Schema|Target = FHIR Element|OMH FHIR Logical Model|
|---|---|---|
|[header-1.2.json]({{page.omlschema_url}}header-1.2.json)|[Observation][Observation]\|[MedicationDispense][MedicationDispense]  Profile||
{:.grid}

The rest of the omh schemas represent either data points or more granular reusable elements or concepts that can be referenced within the data-point schemas. Each reusable omh schema can be divided into two categories for the purposes of FHIR mapping: primitive data-types, complex datatypes. In addition some of the schemas enumerate values which these are [bound]({{site.data.fhir.path}}//terminologies.html)) to a FHIR ValueSet.  The reusable schemas are mapped directly to fhir artifacts as described below and these mapping replace the omh schema references when transforming an OMH data point schema into a FHIR Logical Model.

####  OMH Schema Mappings to FHIR Primitive Data Types

In this table, the schemas representing primitive data-types are mapped directly to the corresponding FHIR primitive datatype.  Listed in the *FHIR ValueSet* column the corresponding FHIR ValueSets and [binding strength]({{site.data.fhir.path}}/datatypes.html#code) for the schemas that map to the FHIR `code` dataype.:

|Source = OMH Schema|Target = FHIR Element|Target = FHIR ValueSet(binding strength)|FHIR Example|
 |---|---|---|[---]({{page.loinc_url}}--)|
|[activity-name-1.0.json]({{page.omlschema_url}}activity-name-1.0.json)|[string][string]|||
|[date-time-1.0.json]({{page.omlschema_url}}date-time-1.0.json)|[dateTime][dateTime]\|[instant][instant]|||
|[full-date-1.0.json]({{page.omlschema_url}}full-date-1.0.json)|[date][date]\|[dateTime][dateTime]|||
|[local-time-1.0.json]({{page.omlschema_url}}local-time-1.0.json)|[string][string]|||
|[body-location-1.0.json]({{page.omlschema_url}}body-location-1.0.json)|[code][code]|[body-location](valueset-body-location.html)|
|[body-posture-1.0.json]({{page.omlschema_url}}body-posture-1.0.json)|[code][code]|[body-posture](valueset-body-posture.html)|
|[day-of-week-1.0.json]({{page.omlschema_url}}day-of-week-1.0.json)|[code][code]|[day-of-week](valueset-day-of-week.html)|
|[descriptive-statistic-1.2.json]({{page.omlschema_url}}descriptive-statistic-1.2.json)|[code][code]|[descriptive-statistic](valueset-descriptive-statistic.html)||
|[descriptive-statistic-denominator-1.0.json]({{page.omlschema_url}}descriptive-statistic-denominator-1.0.json)|[code][code]|[descriptive-statistic-denominator](valueset-descriptive-statistic-denominator.html)||
|[intervention-administration-route-2.0.json]({{page.omlschema_url}}intervention-administration-route-2.0.json)|[code][code]|[intervention-administration-route](valueset-intervention-administration-route.html)||
|[medication-dose-unit-1.0.json]({{page.omlschema_url}}medication-dose-unit-1.0.json)|[code][code]|[medication-dose-unit](valueset-medication-dose-unit.html)||
|[part-of-day-1.0.json]({{page.omlschema_url}}part-of-day-1.0.json)|[code][code]|[part-of-day](valueset-part-of-day.html)||
|[position-during-measurement-1.0.json]({{page.omlschema_url}}position-during-measurement-1.0.json)|[code][code]|[position-during-measurement](valueset-position-during-measurement.html)||
|[specimen-source-1.0.json]({{page.omlschema_url}}specimen-source-1.0.json)|[code][code]|[specimen-source](valueset-specimen-source.html)||
|[temporal-relationship-to-meal-1.2.json]({{page.omlschema_url}}temporal-relationship-to-meal-1.2.json)|[code][code]|[temporal-relationship-to-meal](valueset-temporal-relationship-to-meal.html)||
|[temporal-relationship-to-physical-activity-1.0.json]({{page.omlschema_url}}temporal-relationship-to-physical-activity-1.0.json)|[code][code]|[temporal-relationship-to-physical-activity](valueset-temporal-relationship-to-physical-activity.html)||
|[temporal-relationship-to-sleep-1.0.json]({{page.omlschema_url}}temporal-relationship-to-sleep-1.0.json)|[code][code]|[temporal-relationship-to-sleep](valueset-temporal-relationship-to-sleep.html)||
{:.grid}


#### OMH Schema Mappings to FHIR Complex Data Types

The schemas representing complex data-types are mapped directly to the corresponding FHIR complex datatypes as summarized in the table below:

-  Note that the 'unit-value' schemas are mapped to the FHIR *Quantity* or *Range* datatypes.
   -  Where the unit value is fixed such as for *acceleration-unit-value-1.0.json*, a pattern[Pattern] is associated with the schema
   -  Where the unit value is an enumeration of units a FHIR *ValueSet* is associated with the schema.
   -  Both the patterns and ValueSets contain **UCUM** based units.
-  Patterns are directly applied to the FHIR logical models when the schema is referenced.
-  For data point schemas that reference schemas associated with ValueSets (such as *unit-value-1.0.json*), the actual units and hence the patterns applied to the FHIR logical models are defined by the data point schema themselves.

|Source = OMH Schema|Target = FHIR Element|FHIR Quantity Pattern or ValueSet|FHIR Example|
 |---|---|---|[---]({{page.loinc_url}}--)|
|[acceleration-unit-value-1.0.json]({{page.omlschema_url}}acceleration-unit-value-1.0.json)|[Quantity][Quantity]|{"unit":"m/s^2","system":"http://unitsofmeasure.org","code":"m/s2"}|
|[angular-velocity-unit-value-1.0.json]({{page.omlschema_url}}angular-velocity-unit-value-1.0.json)|[Quantity][Quantity]|{"unit":"ad/s","system":"http://unitsofmeasure.org","code":"ad/s"}
|[area-unit-value-1.0.json]({{page.omlschema_url}}area-unit-value-1.0.json)|[Quantity][Quantity]|[area-unit-value](valueset-area-unit-value.html)||
|[duration-unit-value-1.0.json]({{page.omlschema_url}}duration-unit-value-1.0.json)|[Quantity][Quantity]|[duration-unit-value](valueset-duration-unit-value.html)||
|[duration-unit-value-range-1.0.json]({{page.omlschema_url}}duration-unit-value-range-1.0.json)|[Range][Range]|[duration-unit-value](valueset-duration-unit-value.html)||
|[frequency-unit-value-1.0.json]({{page.omlschema_url}}frequency-unit-value-1.0.json)|[Quantity][Quantity]|[duration-unit-value](valueset-duration-unit-value.html)||
|[kcal-unit-value-1.0.json]({{page.omlschema_url}}kcal-unit-value-1.0.json)|[Quantity][Quantity]|{"unit":"kcal","system":"http://unitsofmeasure.org","code":"kcal"}
|[length-unit-value-1.0.json]({{page.omlschema_url}}length-unit-value-1.0.json)|[Quantity][Quantity]|[length-unit-value](valueset-length-unit-value.html)||
|[magnetic-flux-density-unit-value-1.0.json]({{page.omlschema_url}}magnetic-flux-density-unit-value-1.0.json)|[Quantity][Quantity]|[magnetic-flux-density-unit-value](valueset-magnetic-flux-density-unit-value.html)||
|[mass-unit-value-1.0.json]({{page.omlschema_url}}mass-unit-value-1.0.json)|[Quantity][Quantity]|[mass-unit-value](valueset-mass-unit-value.html)||
|[medication-dose-unit-value-1.0.json]({{page.omlschema_url}}medication-dose-unit-value-1.0.json)|[Quantity][Quantity]|[medication-dose-unit-value](valueset-medication-dose-unit-value.html)||
|[medication-dose-unit-value-range-1.0.json]({{page.omlschema_url}}medication-dose-unit-value-range-1.0.json)|[Range][Range]|[medication-dose-unit-value](valueset-medication-dose-unit-value.html)||
|[pace-unit-value-1.0.json]({{page.omlschema_url}}pace-unit-value-1.0.json)|[Quantity][Quantity]|[pace-unit-value](valueset-pace-unit-value.html)||
|[plane-angle-unit-value-1.0.json]({{page.omlschema_url}}plane-angle-unit-value-1.0.json)|[Quantity][Quantity]|{"unit":"deg","system":"http://unitsofmeasure.org","code":"deg"}
|[speed-unit-value-1.0.json]({{page.omlschema_url}}speed-unit-value-1.0.json)|[Quantity][Quantity]|[speed-unit-value](valueset-speed-unit-value.html)||
|[temperature-unit-value-1.0.json]({{page.omlschema_url}}temperature-unit-value-1.0.json)|[Quantity][Quantity]|[temperature-unit-value](valueset-temperature-unit-value.html)||
|[unit-value-1.0.json]({{page.omlschema_url}}unit-value-1.0.json)|[Quantity][Quantity]|[unit-value]({{site.data.fhir.path}}/valueset-ucum-common.html)||
|[unit-value-range-1.0.json]({{page.omlschema_url}}unit-value-range-1.0.json)|[Range][Range]|[unit-value]({{site.data.fhir.path}}/valueset-ucum-common.html)||
|[volume-unit-value-1.0.json]({{page.omlschema_url}}volume-unit-value-1.0.json)|[Quantity][Quantity]|[volume-unit-value](valueset-volume-unit-value.html)||
|[time-frame-1.0.json]({{page.omlschema_url}}time-frame-1.0.json)|[dateTime][dateTime]\|[Period]({{site.data.fhir.path}}/datatypes.html#Period)||
|[time-interval-1.0.json]({{page.omlschema_url}}time-interval-1.0.json)|\|[Period]({{site.data.fhir.path}}/datatypes.html#Period)||
{:.grid}

#### OMH datapoint Schema Mappings to FHIR Resources

Logical Models for each datapoint schema are mapped to a FHIR Logical Model before being mapped to the target FHIR resource profile as listed in the table below.  The concept code for the measurement is in the description property of the schema are listed in the *Observation.code* column. For Schema that are mapped to `Observation`, this code is mapped to `code` in then Observation resource.:

|Source = OMH Schema|OMH FHIR Logical Model|Target = FHIR Element|Observation.code|
 |---|---|---|[---]({{page.loinc_url}}--)|
|[acceleration-1.0.json]({{page.omlschema_url}}acceleration-1.0.json)|[Acceleration](StructureDefinition-omh-acceleration.html)|[Observation][Observation] Profile|[mFHIR code (Acceleration Panel)][todo]|
 |[ambient-temperature-1.0.json]({{page.omlschema_url}}ambient-temperature-1.0.json)|[AmbientTemperature](StructureDefinition-omh-ambient-temperature.html)|[Observation][Observation] Profile|[60832-3  Room temperature]({{page.loinc_url}}60832-3)|
 |[blood-glucose-2.0.json]({{page.omlschema_url}}blood-glucose-2.0.json)|[BloodGlucose](StructureDefinition-omh-blood-glucose.html)|[Observation][Observation] Profile|[2339-0  Glucose [Mass/​volume] in Blood]({{page.loinc_url}}2339-0)|
 |[blood-pressure-2.0.json]({{page.omlschema_url}}blood-pressure-2.0.json)|[BloodPressure](StructureDefinition-omh-blood-pressure.html)|[Observation][Observation] Profile|[85354-9  Blood pressure panel with all children optional]({{page.loinc_url}}85354-9)|
 |[body-fat-percentage-1.0.json]({{page.omlschema_url}}body-fat-percentage-1.0.json)|[BodyFatPercentage](StructureDefinition-omh-body-fat-percentage.html)|[Observation][Observation] Profile|[41982-0  Percentage of body fat Measured ]({{page.loinc_url}}41982-0)|
 |[body-height-1.0.json]({{page.omlschema_url}}body-height-1.0.json)|[BodyHeight](StructureDefinition-omh-body-height.html)|[Observation][Observation] Profile|[8302-2  Body height]({{page.loinc_url}}8302-2)|
 |[body-mass-index-2.0.json]({{page.omlschema_url}}body-mass-index-2.0.json)|[BodyMassIndex](StructureDefinition-omh-body-mass-index.html)|[Observation][Observation] Profile|[39156-5  Body mass index (BMI) [Ratio]]({{page.loinc_url}}39156-5)|
 |[body-temperature-2.0.json]({{page.omlschema_url}}body-temperature-2.0.json)|[BodyTemperature](StructureDefinition-omh-body-temperature.html)|[Observation][Observation] Profile|[8310-5  Body temperature]({{page.loinc_url}}8310-5)|
 |[body-weight-1.0.json]({{page.omlschema_url}}body-weight-1.0.json)|[BodyWeight](StructureDefinition-omh-body-weight.html)|[Observation][Observation] Profile|[29463-7  Body weight]({{page.loinc_url}}29463-7)|
 |[breath-carbon-monoxide-1.0.json]({{page.omlschema_url}}breath-carbon-monoxide-1.0.json)|[breath-carbon-monoxide](StructureDefinition-omh-breath-carbon-monoxide.html)|[Observation][Observation] Profile|[251900003 Expired carbon monoxide concentration (observable entity)]({{page.sct_url}}251900003)|
 |[calories-burned-2.0.json]({{page.omlschema_url}}calories-burned-2.0.json)|[CaloriesBurned](StructureDefinition-omh-calories-burned.html)|[Observation][Observation] Profile|[41981-2  Calories burned]({{page.loinc_url}}41981-2)|
 |[diastolic-blood-pressure-1.0.json]({{page.omlschema_url}}diastolic-blood-pressure-1.0.json)|[DiastolicBloodPressure](StructureDefinition-omh-diastolic-blood-pressure.html)|[Observation][Observation] Profile|[8462-4  Diastolic blood pressure]({{page.loinc_url}}8462-4)|
 |[expiratory-time-1.0.json]({{page.omlschema_url}}expiratory-time-1.0.json)|[ExpiratoryTime](StructureDefinition-omh-expiratory-time.html)|[Observation][Observation] Profile|[60739-0  Expiration [Time] Respiratory system]({{page.loinc_url}}60739-0)|
|[geoposition-1.0.json]({{page.omlschema_url}}geoposition-1.0.json)|[Geoposition](StructureDefinition-omh-geoposition.html)|[Location][Location] Profile||
 |[heart-rate-1.1.json]({{page.omlschema_url}}heart-rate-1.1.json)|[HeartRate](StructureDefinition-omh-heart-rate.html)|[Observation][Observation] Profile|[8867-4 Heart rate]({{page.loinc_url}}8867-4)|
 |[inspiratory-time-1.0.json]({{page.omlschema_url}}inspiratory-time-1.0.json)|[InspiratoryTime](StructureDefinition-omh-inspiratory-time.html)|[Observation][Observation] Profile|[60740-8  Inspiration [Time] Respiratory system]({{page.loinc_url}}60740-8)|
|[magnetic-force-1.0.json]({{page.omlschema_url}}magnetic-force-1.0.json)|[MagneticForce](StructureDefinition-omh-magnetic-force.html)|[Observation][Observation] Profile|[mFHIR code (Magnetic Force Panel)][todo]|
|[medication-1.0.json]({{page.omlschema_url}}medication-1.0.json)|[Medication](StructureDefinition-omh-medication.html)|[Medication][Medication] Profile||
 |[medication-adherence-percent-2.0.json]({{page.omlschema_url}}medication-adherence-percent-2.0.json)|[MedicationAdherencePercent](StructureDefinition-omh-medication-adherence-percent.html)|[Observation][Observation] Profile|[418633004 Medication compliance (observable entity)]({{page.sct_url}}418633004)|
|[medication-prescription-2.0.json]({{page.omlschema_url}}medication-prescription-2.0.json)|[MedicationPrescription](StructureDefinition-omh-medication-prescription.html)|[MedicationRequest][MedicationRequest] Profile||
 |[minute-volume-1.0.json]({{page.omlschema_url}}minute-volume-1.0.json)|[MinuteVolume](StructureDefinition-omh-minute-volume.html)|[Observation][Observation] Profile|[20139-2  Volume expired 1 minute]({{page.loinc_url}}20139-2)|
 |[minutes-moderate-activity-1.0.json]({{page.omlschema_url}}minutes-moderate-activity-1.0.json)|[MinutesModerateActivity](StructureDefinition-omh-minutes-moderate-activity.html)|[Observation][Observation] Profile|[408581006 Physical activity target moderate exercise (finding)]({{page.sct_url}}408581006)|
|[orientation-1.0.json]({{page.omlschema_url}}orientation-1.0.json)|[Orientation](StructureDefinition-omh-orientation.html)|[Observation][Observation] Profile|[mFHIR code (Gyroscope measurement Panel)][todo]|
 |[oxygen-saturation-1.0.json]({{page.omlschema_url}}oxygen-saturation-1.0.json)|[OxygenSaturation](StructureDefinition-omh-oxygen-saturation.html)|[Observation][Observation] Profile|[59408-5 Oxygen saturation in Arterial blood by Pulse oximetry]({{page.loinc_url}}59408-5)|
|[pace-1.0.json]({{page.omlschema_url}}pace-1.0.json)|[Pace](StructureDefinition-omh-pace.html)|[Observation][Observation] Profile|[mFHIR code (Pace)][todo]|
|[patient-medication-schedule-2.0.json]({{page.omlschema_url}}patient-medication-schedule-2.0.json)|[PatientMedicationSchedule](StructureDefinition-omh-patient-medication-schedule.html)|[Observation][Observation] Profile|???|
|[pharmacy-medication-dispensing-2.0.json]({{page.omlschema_url}}pharmacy-medication-dispensing-2.0.json)|[PharmacyMedicationDispensing](StructureDefinition-omh-pharmacy-medication-dispensing.html)|[MedicationDispense][MedicationDispense] Profile||
 |[physical-activity-1.2.json]({{page.omlschema_url}}physical-activity-1.2.json)|[PhysicalActivity](StructureDefinition-omh-physical-activity.html)|[Observation][Observation] Profile|[68130003 Physical activity (observable entity)]({{page.sct_url}}68130003)|
|[reason-single-medication-dose-not-taken-1.0.json]({{page.omlschema_url}}reason-single-medication-dose-not-taken-1.0.json)|[ReasonSingleMedicationDoseNotTaken](StructureDefinition-omh-reason-single-medication-dose-not-taken.html)|[MedicationStatement][MedicationStatement]  Profile||
 |[respiratory-rate-1.0.json]({{page.omlschema_url}}respiratory-rate-1.0.json)|[RespiratoryRate](StructureDefinition-omh-respiratory-rate.html)|[Observation][Observation] Profile|[9279-1 Respiratory Rate]({{page.loinc_url}}9279-1)|
 |[rr-interval-1.0.json]({{page.omlschema_url}}rr-interval-1.0.json)|[RrInterval](StructureDefinition-omh-rr-interval.html)|[Observation][Observation] Profile|[8637-1 R-R interval by EKG]({{page.loinc_url}}8637-1)|
|[single-medication-dose-taken-1.0.json]({{page.omlschema_url}}single-medication-dose-taken-1.0.json)|[SingleMedicationDoseTaken](StructureDefinition-omh-single-medication-dose-taken.html)|[MedicationStatement][MedicationStatement] Profile||
 |[sleep-duration-2.0.json]({{page.omlschema_url}}sleep-duration-2.0.json)|[SleepDuration](StructureDefinition-omh-sleep-duration.html)|[Observation][Observation] Profile|[248263006 Duration of sleep (observable entity)]({{page.sct_url}}248263006)|
 |[sleep-episode-1.0.json]({{page.omlschema_url}}sleep-episode-1.0.json)|[SleepEpisode](StructureDefinition-omh-sleep-episode.html)|[Observation][Observation] Profile|[258158006 Sleep, function (observable entity)]({{page.sct_url}}258158006)|
|[speed-1.0.json]({{page.omlschema_url}}speed-1.0.json)|[Speed](StructureDefinition-omh-speed.html)|[Observation][Observation] Profile|C0678536 NCIT code|
 |[step-count-2.0.json]({{page.omlschema_url}}step-count-2.0.json)|[StepCount](StructureDefinition-omh-step-count.html)|[Observation][Observation] Profile|[55423-8 Number of steps in unspecified time Pedometer]({{page.loinc_url}}55423-8)|
 |[systolic-blood-pressure-1.0.json]({{page.omlschema_url}}systolic-blood-pressure-1.0.json)|[SystolicBloodPressure](StructureDefinition-omh-systolic-blood-pressure.html)|[Observation][Observation] Profile|[8480-6 Systolic blood pressure]({{page.loinc_url}}8480-6)|
 |[ventilation-cycle-time-1.0.json]({{page.omlschema_url}}ventilation-cycle-time-1.0.json)|[VentilationCycleTime](StructureDefinition-omh-ventilation-cycle-time.html)|[Observation][Observation] Profile|[250818005 Ventilation cycle time (observable entity)]({{page.sct_url}}250818005)|
{:.grid}

### Mapping Example

The transformation from the OMH data-point schema to the FHIR Logical models and from the FHIR Logical model to the FHIR resource is straightforward and conceptual mappings are provided for each.  The following example illustrates transforming from the step-count omh schema to a FHIR observation.  The process can be automated using omh schemas and one of several FHIR libraries that are available.

*Mapping from the source MHealth file to the OMH Logical Model*

In this section the following Open MHealth data-point instance  will be transfored to a FHIR Observation.

{% include source_mHealth_file.md %}

The first step is to map from the Open MHealth data-point schema to the OmhDataPoint Logical Model.  The source JSON data is transformed following the *first* [mapping table](StructureDefinition-omh-data-point.html#sd-3-2-mappings) provided in the OmhDataPoint Logical Model and referencing the formal [StructureDefinition](StructureDefinition-omh-data-point.html#sd-3-1formal-views-of-profile-content) for the structural details.  So for example from the example source file below, based on the mapping table `OmhDataPoint.header.id` is translated to `OmhDataPoint.header.dataPointId` which a primitive `id` datatype.

 The OmhDataPoint `body` element is a choice of other logical models based on the datapoint schema listed above. These models are their mappings are referenced to complete the mapping. For example, `properties.body.effective_time_frame` is mapped to the OMHStepCount Logical Model and data transformed based on its [mapping table](StructureDefinition-omh-step-count.html#sd-1-2-mappings)
A complex data element  such as `effective_time_frame` is mapped to the `OMHStepCount.effectiveTimeFrame` element which is a FHIR [Period]({{site.data.fhir.path}}/datatypes.html#Period) whose detailed structure is available in the FHIR specification and can accessed by following the links in the logical model.  Here is how the Period datatype maps to the effective_time_frame

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


[code]: {{site.data.fhir.path}}/datatypes.html#code "FHIR code definition"
[string]: {{site.data.fhir.path}}/datatypes.html#string "FHIR string definition"
[dateTime]: {{site.data.fhir.path}}/datatypes.html#dateTime "FHIR dateTime definition"
[instant]: {{site.data.fhir.path}}/datatypes.html#instant "FHIR instant definition"
[date]: {{site.data.fhir.path}}/datatypes.html#date "FHIR date definition"
[Quantity]: {{site.data.fhir.path}}/datatypes.html#quantity "FHIR Quantity definition"
[Range]: {{site.data.fhir.path}}/datatypes.html#range "FHIR Range definition"
[Medication]:{{site.data.fhir.path}}/medication.html "FHIR Medication definition"
[MedicationRequest]:{{site.data.fhir.path}}/medicationrequest.html "FHIR MedicationRequest definition"
[MedicationStatement]:{{site.data.fhir.path}}/medicationstatement.html "FHIR MedicationStatement definition"
[MedicationDispense]:{{site.data.fhir.path}}/medicationdispense.html "FHIR MedicationDispense definition"
[Observation]:{{site.data.fhir.path}}/observation.html "FHIR Observation definition"
[MedicationDispense]:{{site.data.fhir.path}}/MedicationDispense.html "FHIR MedicationDispense definition"
[Location]:{{site.data.fhir.path}}/location.html "FHIR Location definition"
[todo]: todo.html "still under construction"
[Pattern]: {{site.data.fhir.path}}/#ElementDefinition.pattern_x_ "FHIR pattern definition"
