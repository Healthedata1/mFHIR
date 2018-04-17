---
title: General Guidance and Definitions
layout: default
active: guidance
---

{:.no_toc}

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}

## [Introduction](#)
{:.self-link}

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

####  Mapping Strategy

In order to map the OMH schema to FHIR, the OMH Schemas are divided conceptually into several categories.  The infrastructural `schema` model serves as a basic blueprint for creation of OMH schema and is not used in the mappings. The infrastructural `data-point` schema provide the basic framework upon which the data-points schemas are based and serves as the backbone for creation of the FHIR logical model. It is made up of a `header` property representing provenance information and  a `body` property representing one of the omh schemas that represent a measurements i.e., 'a data point'.

##### OMH Header Schema Mapping to FHIR elements

The OMH header schema represent data provenance and the properties in the header schema map to more than a single FHIR element.  In addition, depending on the depth and level of detail required, there are multiple options to representing provenance including:

- [Provenance]({{site.data.fhir.path}}/provenance.html)resource
- [meta.source]({{site.data.fhir.path}}/resource.html#Meta) element
- inline Resource elements

These options are summarized in the table below and described in detail in the data point logical model mappings.

|Index|Source = OMH Schema|Target = FHIR Element|OMH FHIR Logical Model|
|---|---|---|---|
|21|[header-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/header-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html)\|[Provenance]({{site.data.fhir.path}}/observation.html)  Profile||
|22|[header-1.1.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/header-1.1.json)|[Observation]({{site.data.fhir.path}}/observation.html)\|[Provenance]({{site.data.fhir.path}}/observation.html)  Profile||
|23|[header-1.2.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/header-1.2.json)|[Observation]({{site.data.fhir.path}}/observation.html)\|[Provenance]({{site.data.fhir.path}}/observation.html)  Profile||
{:.grid}

The rest of the omh schemas represent either data points or more granular reusable elements or concepts that can be referenced within the data-point schemas. Each reusable omh schema can be divided into three categories for the purposes of FHIR mapping: primitive data-types, complex dataypes and valuesets. The reusable schemas are mapped directly to fhir artifacts as described below and these mapping replace the omh schema references when transforming the OMH data point schema into a FHIR Logical Model.

#####  OMH Schema Mappings to FHIR Primitive Data Types

The schemas representing primitive data-types are mapped directly to the corresponding FHIR primitive dataypes as follows:

|Index|Source = OMH Schema|Target = FHIR Element|Example|
|---|---|---|---|
|1|[activity-name-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/activity-name-1.0.json)|[string]({{site.data.fhir.path}}/dataypes.html#string)||
|2|[date-time-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/date-time-1.0.json)|[dateTime]({{site.data.fhir.path}}/dataypes.html#dateTime)\|[instant]({{site.data.fhir.path}}/dataypes.html#instant)||
|3|[full-date-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/full-date-1.0.json)|[date]({{site.data.fhir.path}}/dataypes.html#date)\|[dateTime]({{site.data.fhir.path}}/dataypes.html#dateTime)||
|4|[local-time-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/local-time-1.0.json)|[string]({{site.data.fhir.path}}/dataypes.html#string)||
{:.grid}

##### OMH Schema Mappings to FHIR Complex Data Types

The schemas representing complex data-types are mapped directly to the corresponding FHIR complex datatypes as summarized in the table below:

-  Note that the 'unit-value' schemas are mapped to the FHIR *Quantity* or *Range* datatypes.
   -  Where the unit value is fixed such as for *acceleration-unit-value-1.0.json*, a pattern is associated with the schema
   -  Where the unit value is an enumeration of units a FHIR *ValueSet* is associated with the schema.
   -  Both the patterns and ValueSets contain **UCUM** based units.
-  Patterns are directly applied to the FHIR logical models when the schema is referenced.
-  For data point schemas that reference schemas associated with ValueSets (such as *unit-value-1.0.json*), the actual units and hence the patterns applied to the FHIR logical models are defined by the data point schema themselves.

|Index|Source = OMH Schema|Target = FHIR Element|FHIR Quantity Pattern or ValueSet|Example|
|---|---|---|---|---|
|1|[acceleration-unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/acceleration-unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|{"unit":"m/s^2","system":"http://unitsofmeasure.org","code":"m/s2"
|2|[angular-velocity-unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/angular-velocity-unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|{"unit":"ad/s","system":"http://unitsofmeasure.org","code":"ad/s"
|3|[area-unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/area-unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|[area-unit-value](valueset-area-unit-value.html)||
|4|[duration-unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/duration-unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|[duration-unit-value](valueset-duration-unit-value.html)||
|5|[duration-unit-value-range-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/duration-unit-value-range-1.0.json)|[Range]({{site.data.fhir.path}}/dataypes.html#Range)|[duration-unit-value](valueset-duration-unit-value.html)||
|6|[frequency-unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/frequency-unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|[duration-unit-value](valueset-duration-unit-value.html)||
|7|[kcal-unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/kcal-unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|{"unit":"kcal","system":"http://unitsofmeasure.org","code":"kcal"
|8|[length-unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/length-unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|[length-unit-value](valueset-length-unit-value.html)||
|9|[magnetic-flux-density-unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/magnetic-flux-density-unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|[magnetic-flux-density-unit-value](valueset-magnetic-flux-density-unit-value.html)||
|10|[mass-unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/mass-unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|[mass-unit-value](valueset-mass-unit-value.html)||
|11|[medication-dose-unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/medication-dose-unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|[medication-dose-unit-value](valueset-medication-dose-unit-value.html)||
|12|[medication-dose-unit-value-range-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/medication-dose-unit-value-range-1.0.json)|[Range]({{site.data.fhir.path}}/dataypes.html#Range)|[medication-dose-unit-value](valueset-medication-dose-unit-value.html)||
|13|[pace-unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/pace-unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|[pace-unit-value](valueset-pace-unit-value.html)||
|14|[plane-angle-unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/plane-angle-unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|{"unit":"deg","system":"http://unitsofmeasure.org","code":"deg"
|15|[speed-unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/speed-unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|[speed-unit-value](valueset-speed-unit-value.html)||
|16|[temperature-unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/temperature-unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|[temperature-unit-value](valueset-temperature-unit-value.html)||
|17|[unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|[unit-value]({{site.data.fhir.path}}/valueset-ucum-common.html)||
|18|[unit-value-range-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/unit-value-range-1.0.json)|[Range]({{site.data.fhir.path}}/dataypes.html#Range)|[unit-value]({{site.data.fhir.path}}/valueset-ucum-common.html)||
|19|[volume-unit-value-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/volume-unit-value-1.0.json)|[Quantity]({{site.data.fhir.path}}/dataypes.html#Quantity)|[volume-unit-value](valueset-volume-unit-value.html)||
|20|[time-frame-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/time-frame-1.0.json)|[dateTime]({{site.data.fhir.path}}/dataypes.html#dateTime)\|[Period]({{site.data.fhir.path}}/dataypes.html#Period)||
|21|[time-interval-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/time-interval-1.0.json)|\|[Period]({{site.data.fhir.path}}/dataypes.html#Period)||
{:.grid}

##### OMH Schema Mappings to FHIR ValueSets

The schemas representing valuesets have been directly mapped a corresponding FHIR ValueSet:

|Index|Source = OMH Schema|Target = FHIR ValueSet|
|---|---|---|
|1|[body-location-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/body-location-1.0.json)|[body-location](valueset-body-location.html)|
|2|[body-posture-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/body-posture-1.0.json)|[body-posture](valueset-body-posture.html)|
|3|[day-of-week-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/day-of-week-1.0.json)|[day-of-week](valueset-day-of-week.html)|
|4|[descriptive-statistic-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/descriptive-statistic-1.0.json)|[descriptive-statistic](valueset-descriptive-statistic.html)|
|5|[descriptive-statistic-1.1.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/descriptive-statistic-1.1.json)|[descriptive-statistic](valueset-descriptive-statistic.html)|
|6|[descriptive-statistic-1.2.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/descriptive-statistic-1.2.json)|[descriptive-statistic](valueset-descriptive-statistic.html)|
|7|[descriptive-statistic-denominator-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/descriptive-statistic-denominator-1.0.json)|[descriptive-statistic-denominator](valueset-descriptive-statistic-denominator.html)|
|8|[intervention-administration-route-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/intervention-administration-route-1.0.json)|[intervention-administration-route](valueset-intervention-administration-route.html)|
|9|[intervention-administration-route-2.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/intervention-administration-route-2.0.json)|[intervention-administration-route](valueset-intervention-administration-route.html)|
|10|[medication-dose-unit-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/medication-dose-unit-1.0.json)|[medication-dose-unit](valueset-medication-dose-unit.html)|
|11|[part-of-day-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/part-of-day-1.0.json)|[part-of-day](valueset-part-of-day.html)|
|12|[position-during-measurement-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/position-during-measurement-1.0.json)|[position-during-measurement](valueset-position-during-measurement.html)|
|13|[specimen-source-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/specimen-source-1.0.json)|[specimen-source](valueset-specimen-source.html)|
|14|[temporal-relationship-to-meal-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/temporal-relationship-to-meal-1.0.json)|[temporal-relationship-to-meal](valueset-temporal-relationship-to-meal.html)|
|15|[temporal-relationship-to-meal-1.1.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/temporal-relationship-to-meal-1.1.json)|[temporal-relationship-to-meal](valueset-temporal-relationship-to-meal.html)|
|16|[temporal-relationship-to-meal-1.2.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/temporal-relationship-to-meal-1.2.json)|[temporal-relationship-to-meal](valueset-temporal-relationship-to-meal.html)|
|17|[temporal-relationship-to-physical-activity-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/temporal-relationship-to-physical-activity-1.0.json)|[temporal-relationship-to-physical-activity](valueset-temporal-relationship-to-physical-activity.html)|
|18|[temporal-relationship-to-sleep-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/temporal-relationship-to-sleep-1.0.json)|[temporal-relationship-to-sleep](valueset-temporal-relationship-to-sleep.html)|
{:.grid}

##### OMH Schema Mappings to FHIR Resources

Logical Models for each datapoint schema are then mapped to the corresponding FHIR resource profiles as listed in the table below:

|Index|Source = OMH Schema|Target = FHIR Element|OMH FHIR Logical Model|
|---|---|---|---|
|1|[acceleration-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/acceleration-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|2|[ambient-temperature-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/ambient-temperature-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|3|[blood-glucose-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/blood-glucose-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|4|[blood-glucose-2.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/blood-glucose-2.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|5|[blood-pressure-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/blood-pressure-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|6|[blood-pressure-2.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/blood-pressure-2.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|7|[body-fat-percentage-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/body-fat-percentage-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|8|[body-height-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/body-height-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|9|[body-mass-index-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/body-mass-index-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|10|[body-mass-index-2.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/body-mass-index-2.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|11|[body-temperature-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/body-temperature-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|12|[body-temperature-2.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/body-temperature-2.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|13|[body-weight-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/body-weight-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|14|[breath-carbon-monoxide-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/breath-carbon-monoxide-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|15|[calories-burned-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/calories-burned-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|16|[calories-burned-2.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/calories-burned-2.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|18|[diastolic-blood-pressure-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/diastolic-blood-pressure-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|19|[expiratory-time-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/expiratory-time-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|20|[geoposition-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/geoposition-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|24|[heart-rate-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/heart-rate-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|25|[heart-rate-1.1.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/heart-rate-1.1.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|26|[inspiratory-time-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/inspiratory-time-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|27|[magnetic-force-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/magnetic-force-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|28|[medication-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/medication-1.0.json)|[Medication]({{site.data.fhir.path}}/medication.html) Profile||
|29|[medication-adherence-percent-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/medication-adherence-percent-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|30|[medication-adherence-percent-2.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/medication-adherence-percent-2.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|31|[medication-prescription-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/medication-prescription-1.0.json)|[MedicationRequest]({{site.data.fhir.path}}/medicationrequest.html) Profile||
|32|[medication-prescription-2.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/medication-prescription-2.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|33|[minute-volume-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/minute-volume-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|34|[minutes-moderate-activity-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/minutes-moderate-activity-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|35|[orientation-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/orientation-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|36|[oxygen-saturation-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/oxygen-saturation-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|37|[pace-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/pace-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|38|[patient-medication-schedule-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/patient-medication-schedule-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|39|[patient-medication-schedule-2.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/patient-medication-schedule-2.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|40|[pharmacy-medication-dispensing-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/pharmacy-medication-dispensing-1.0.json)|[MedicationDispense]({{site.data.fhir.path}}/medicationdispense.html) Profile||
|41|[pharmacy-medication-dispensing-2.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/pharmacy-medication-dispensing-2.0.json)|[MedicationDispense]({{site.data.fhir.path}}/medicationdispense.html) Profile||
|42|[physical-activity-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/physical-activity-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|43|[physical-activity-1.1.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/physical-activity-1.1.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|44|[physical-activity-1.2.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/physical-activity-1.2.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|45|[reason-single-medication-dose-not-taken-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/reason-single-medication-dose-not-taken-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|46|[respiratory-rate-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/respiratory-rate-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|47|[rr-interval-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/rr-interval-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|50|[single-medication-dose-taken-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/single-medication-dose-taken-1.0.json)|[MedicationStatement]({{site.data.fhir.path}}/medicationstatement.html) Profile||
|51|[sleep-duration-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/sleep-duration-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|52|[sleep-duration-2.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/sleep-duration-2.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|53|[sleep-episode-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/sleep-episode-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|54|[speed-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/speed-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|55|[step-count-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/step-count-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|56|[step-count-2.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/step-count-2.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|57|[systolic-blood-pressure-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/systolic-blood-pressure-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
|58|[ventilation-cycle-time-1.0.json](https://github.com/openmhealth/schemas/blob/master/schema/omh/ventilation-cycle-time-1.0.json)|[Observation]({{site.data.fhir.path}}/observation.html) Profile||
{:.grid}

##### Mapping Example

The transformation from the OMH data-point schema to the FHIR Logical models and from the FHIR Logical model to the FHIR resource is straightforward and conceptual mappings are provided for each.  The following example illustrates transforming from the step-count omh schema to a FHIR observation.  The process can be automated using omh schemas and one of several FHIR libraries that are available.

*Mapping from the source MHealth file to the OMH Logical Model*

In this section the following Open MHealth data-point instance  will be transfored to a FHIR Observation.

{% include source_mHealth_file.md %}

The first step is to map from the Open MHealth data-point schema to the OmhDataPoint Logical Model.  The source JSON data is transformed following the *first* [mapping table](StructureDefinition-omh-data-point.html#sd-3-2-mappings) provided in the OmhDataPoint Logical Model and referencing the formal [StructureDefinition](StructureDefinition-omh-data-point.html#sd-3-1formal-views-of-profile-content) for the structural details.  So for example from the example source file below, based on the mapping table `OmhDataPoint.header.id` is translated to `OmhDataPoint.header.dataPointId` which a primitive `id` dataype.

 The OmhDataPoint `body` element is a choice of other logical models based on the datapoint schema listed above. These models are their mappings are referenced to complete the mapping. For example, `properties.body.effective_time_frame` is mapped to the OMHStepCount Logical Model and data transformed based on its [mapping table](StructureDefinition-omh-step-count.html#sd-1-2-mappings)
A complex data element  such as `effective_time_frame` is mapped to the `OMHStepCount.effectiveTimeFrame` element which is a FHIR [Period]({{site.data.fhir.path}}/dataypes.html#Period) whose detailed structure is available in the FHIR specification and can accessed by following the links in the logical model.  Here is how the Period datatype maps to the effective_time_frame

|effective_time_frame.time_interval|FHIR Period data type|
|---|---|
effective_time_frame.time_interval.start_date_time|effectiveTimeFrame.start|
effective_time_frame.time_interval.end_date_time|effectiveTimeFrame.end|
{: .grid}

After mapping all the elements in the source file to the OmhDataPoint Logical Model, we get the following OmhDataPoint json file:

{% include omh-data-point-worked-example.md %}

The next step is to map from the OmhDataPoint Logical Model to the appropriate FHIR resource, which in this case is [Observation]({{site.data.fhir.path}}/observation.html)).  Similar to the first step, The OMH logica model JSON data is transformed to the FHIR Resource following the *second* [mapping table](StructureDefinition-omh-data-point.html#sd-3-2-mappings) provided in the OmhDataPoint Logical Model and referencing the formal definitions of the FHIR resource the structural details.  Since the OMH Logical Model and the FHIR Resource share the same datatypes the process is relatively straight.  In some cases there are no mappings because the element are infrasture related only to the OMH schemas.  In other cases there are choices on how to transform the data and the use case and best practices should determine the outcome.

For example, the OmhDataPoint.dataPointId is mapped to Observation.identifier, OmhDataPoint.header.namespace is unmapped.  Again, the OmhDataPoint `body` element is a choice of other logical models based on the datapoint schema listed above. Note that in many cases the Logical Model maps to the FHIR element `Observation.code` with a fixed value for code and code system. In this example the OmhStepCount Logical Model maps to Observation.code with LOINC =55423-8. The other element are mapped as above - for example, OmhDataPoint.body.stepCount is mapped to Observation.valueQuantity.  As a result of the mapping the following Observation resource is derived:

{% include observation-worked-example.md %}

<br />
