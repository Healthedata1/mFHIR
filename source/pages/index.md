---
title: Open mHealth to FHIR HomePage
layout: default
active: home
topofpage: true
sectionnumbering: true
O: http://www.openmhealth.org/
OS: http://www.openmhealth.org/schemas/omh_
F: http://hl7.org/fhir/STU3/
loinc_url: https://loinc.org/
sct_url: http://browser.ihtsdotools.org/?perspective=full&conceptId1=
---

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}


### Introduction

This Implementation Guide describes how to use [Open mHealth] combined with FHIR to pull health data from popular third-party APIs like Google Fit and FitBit and Apple iHealth.  This data is made accessible to a FHIR SMART client either in the native OmH schema format or as FHIR resources (typically FHIR Observations) using the OmH Shimmer application and "Open mHealth to FHIR" server.

Use Cases include:

A patient preventing or managing one or more diseases
Accessing to mHealth data for enterprise level-needs, e.g., to support population health and research purposes

### OMH to FHIR Roadmap

The following OMH schemas are the targets for mapping to FHIR with those in bold type the highest priority for mapping. 

#### Laboratory
1. **[OmhBloodGlucose]**
    - Observation Profile 2339-0 Glucose [Mass/volume] in Blood

#### Physical Activity
1. **[OmhStepCount] (Completed)**
    - Observation Profile 55423-8 Number of steps in unspecified time Pedometer
1. [OmhCaloriesBurned]
   -  Observation Profile 41981-2 Calories burned
1. [OmhGeoposition]
   -  Location Profile  
1. **[OmhMinutesModerateActivity]** (new physical activity guidelines again based on this)
   -  Observation Profile 408581006 Physical activity target moderate exercise (finding)
1. [OmhPace]
   -  Observation Profile Open mHealth to FHIR code (Pace)
1. [OmhSpeed]
   -  Observation Profile C0678536 NCIT code
1. [OmhOrientation]
   -  Observation Profile Open mHealth to FHIR code (Gyroscope measurement Panel)

#### Vitals
1. [OmhBodyTemperature]
   -  Observation Profile 8310-5 Body temperature
1. **[OmhBodyWeight]**
   -  Observation Profile 29463-7 Body weight
1. **[OmhHeartRate] (Completed)**
   -  Observation Profile 8867-4 Heart rate
1. [OmhRespiratoryRate]
   -  Observation Profile 9279-1 Respiratory Rate
1. **[OmhBodyHeight]**
   -  Observation Profile 8302-2 Body height
1. **[OmhBloodPressure]**
   -  Observation Profile 85354-9 Blood pressure panel with all children optional
1. **[OmhDiastolicBloodPressure]**
   -  Observation Profile 8462-4 Diastolic blood pressure
1. **[OmhSystolicBloodPressure]**
   -  Observation Profile 8480-6 Systolic blood pressure
1. [OmhBodyFatPercentage]
   -  Observation Profile 41982-0 Percentage of body fat Measured 
1. **[OmhBodyMassIndex]**
   -  Observation Profile 39156-5 Body mass index (BMI) [Ratio]
1. [OmhOxygenSaturation]
   -  Observation Profile 59408-5 Oxygen saturation in Arterial blood by Pulse oximetry

#### Sleep
1. [OmhSleepDuration]
   -  Observation Profile 248263006 Duration of sleep (observable entity)
<!-- end TOC -->

<br />


---

{%include link-list.md %}
