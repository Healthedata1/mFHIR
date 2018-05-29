---
title: mFHIR HomePage
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

{% include publish-box.html %}


<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}


<!-- end TOC -->

## mFHIR Overview

### R24 Server

{% include img.html img="R24_Overview.png" %}

## Base Use case

<!----- Conversion time: 4.03 seconds.


Using this Markdown file:

1. Cut and paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* GD2md-html version 1.0β11
* Wed Apr 25 2018 15:25:21 GMT-0700 (PDT)
* Source doc: https://docs.google.com/open?id=1tudkVkvTjxBSUkUrxVjrYGrocbH_Lw_kPQP8jUbOhUQ
----->


### Description

The patient determined by e.g., <http://tools.acc.org/ASCVD-Risk-Estimator-Plus/#!/calculate/estimate/> to be at moderate CV risk based on blood pressure, BMI, diet and exercise, blood glucose. Patient has a primary care physician (PCP). PCP and the patient jointly decide on improving exercise to meet AHA/WHO/CDC guidelines of150 minutes of moderate exercise (3-6 METS) every week, which they have refined into a mutually agreed upon step goal of 4000 steps daily. PCP prescribes the collection of steps using an mHealth device, to track daily steps and average daily and weekly steps. The patient is given an Open mHealth-compliant/supported consumer device (e.g., FitBit, GoogleFit, Misfit) by the clinic, or the patient already has an Open mHealth-compliant/supported device.


At the next scheduled visit (e.g., in 90 days), the PCP and patient will jointly review during a clinic visit the daily step count and daily and weekly averages in the past 90 days vs the goal of 4000 daily steps. They will do this using a FHIR app that presents the data graphically within the EHR session.



### Actors


1. Patient
1. Primary care physician (PCP)
1. FHIR-enabled**  ** EHR
1. a mHealth data server (called ** R24 Server**  in this use case) with FHIR server running SMART-on-FHIR protocols for authentication/authorization, etc.
1. Patient's step counter sensor (called ** StepSensor**  in this use case) -- specific product, may be the patient's phone
1. Data store for the Step-Counter Device output (e.g., cloud and/or phone (e.g., GoogleFit, HealthKit)) that either offers data directly in Open mHealth format using an Open mHealth endpoint, or is supported by Shimmer
1. FHIR app (called ** mDATA**  in this use case) -- has roles for PCP, onboarding staff, and patient


### Assumptions, Pre-Conditions and Constraints

1. Is one way data flow, PCP initiates the pull of data into the EHR session (i.e., PCP launches FHIR app).
1. No data is being written to the EHR.
1. The mDATA FHIR app supports user roles of PCP, onboarding staff, and patient. mDATA has Shimmer in it. mDATA has access to the following EHR data about the patient
1.  email
1. cell phone #
1. patient portal credentials
1. PCP has authorization to mDATA
1. Data that is presented in mDATA FHIR app is not persisted in the FHIR app, but could be.
1. EHR is FHIR-enabled, with security/access provisions in place that allows FHIR apps to
1. read data from an external data source (e.g., R24 server)
1. read EHR data into the app to provide clinical context (patient ID/name, weight)
1. Patient is known to provider and has an EHR record and a unique MRN
1. EHR may or may not have a patient portal. Patient may or may not already have patient portal credentials.
1. Patient has a smartphone that can run a web or native FHIR app
1. R24 has security/access provisions in place
1. R24 server makes a copy of the data from StepSensor and persists that data in a data store (OMOP in this use case)
1. This use case describes the collection of only a single data variable (step count) from a single device (StepSensor)
1. No real-time or threshold or triggered alerts

### Basic Flow

#### Order step count and set up StepSensor
{:.no_toc}

<table class = "grid">
  <tr>
   <th>Step
   </th>
   <th>User Action
   </th>
   <th>System Response (optional)
   </th>
  </tr>
  <tr>
   <td>1
   </td>
   <td>PCP launches mDATA within patient encounter on the EHR
   </td>
   <td>mDATA automatically signs in the PCP and shows the PCP screens, and pulls patient's MRN, cell phone #, and email address from the active EHR encounter session
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>PCP submits an order via mDATA to prescribe "average daily and weekly step count between now and next visit" and is done!
   </td>
   <td>mDATA records order for daily step count, average daily steps and average weekly steps for this MRN.
   </td>
  </tr>
  <tr>
   <td rowspan="2" >2
   </td>
   <td>2a. Patient leaves the visit and is directed to the onboarding staff (aka Onboarder). The Onboarder opens an encounter for this patient (who's there in person) in the EHR or any web-enabled device and launches mDATA. The Onboarder reviews the data order, and determines whether the patient already has StepSensor or another acceptable device.

verify phone # and email ---
   </td>
   <td>mDATA automatically signs in the Onboarder, pulls in the MRN for this patient from the active encounter session, and shows the Onboarder the active order for step count for this patient, and the acceptable devices for fulfilling this order.  
   </td>
  </tr>
  <tr>
   <td><em>2.b If patient doesn't already have StepSensor</em>

The Onboarder gives the patient a new StepSensor and helps the patient set up their new StepSensor ID and password
   </td>
   <td>StepSensor creates and authenticates patient to their new StepSensor account.
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td><strong>Downloading patient's mDATA app</strong>

(Onboarder can assist patient with these tasks)

Patient downloads mDATA app from Play or App store onto their own smartphone
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>4
   </td>
   <td><strong>Creating a patient mDATA account</strong>

(Onboarder can assist patient with these tasks)

<span style="text-decoration:underline;">For patients with EHR patient portal credentials</span>

Patient signs into mDATA using their existing patient portal credentials.

<span style="text-decoration:underline;">For patients without EHR patient portal credentials</span>

Patient creates a new account and enters the same email they've given to the EHR. Patient receives an mDATA authentication code at the cell phone number they gave to the EHR. They enter the code and then complete the mDATA account setup by providing a password.
   </td>
   <td><span style="text-decoration:underline;">For patients with EHR patient portal credentials</span>

mDATA creates a patient mDATA account for the patient associated with the submitted portal credentials.

<span style="text-decoration:underline;">For patients without EHR patient portal credentials</span>

mDATA knows which MRN is associated with the submitted email. mDATA sends an authentication code to the cell phone associated with that MRN. Once authenticated, mDATA creates a patient mDATA account for this MRN.
   </td>
  </tr>
  <tr>
   <td>5
   </td>
   <td>Patient uses their mDATA app to connect mDATA to StepSensor using mDATA's Shimmer function: 1) mDATA shows icons including StepSensor, 2) patient taps on StepSensor, 3) mDATA brings up StepSensor's authentication screen, 4) patient enters in his/her StepSensor credentials (from Step 3a above).
   </td>
   <td>Shimmer negotiates OAuth tokens using patient's credentials for StepSensor, generates unique Shimmer User ID for the patient, and binds that Shimmer User ID to that StepSensor account

Shimmer makes the Shimmer User ID available to mDATA, which now has both the patient's MRN and the patient's Shimmer User ID. mDATA stores this mapping in its own datastore. It does not write anything to the EHR.
   </td>
  </tr>
  <tr>
   <td>6
   </td>
   <td>Patients sees in their mDATA app that they are tracking step count and can review their PCP's order. They can see their daily step counts, and average daily and weekly steps, in between clinic visits.
   </td>
   <td>mDATA displays appropriate order and step count data for this patient (see Flow 6b below for how mDATA gets this data).  
   </td>
  </tr>
</table>

#### Flow Identifier:  In-person review of already collected steps data
{:.no_toc}

<table class = "grid">
<tr>
 <th>Step
 </th>
 <th>User Action
 </th>
 <th>System Response (optional)
 </th>
</tr>

  <tr>
   <td>1

   </td>
   <td>At next visit, PCP and patient are in a clinic visit. Provider launches mDATA within patient encounter on the EHR

   </td>
   <td>mDATA automatically signs in the PCP and shows the PCP screens, and pulls patient's MRN from the active EHR encounter session. mDATA accesses mDATA datastore to retrieve the Shimmer ID for this MRN (see Step 5 in flow 6a above).

   </td>
  </tr>
  <tr>
   <td rowspan="4" >2

   </td>
   <td rowspan="4" >Provider's mDATA app displays mHealth data from active mHealth data order for this patient (daily and average daily and weekly step counts since last visit).

Patient and provider review the data and make clinical decisions.

   </td>
   <td>mDATA sends the patient's Shimmer User ID to the R24 server. authorization/authentication using SMART-on-FHIR protocols R24 receives Shimmer ID.

   </td>
  </tr>
  <tr>
   <td>mDATA accesses active mHealth data orders for this patient, and sends appropriate GET command to R24 server, e.g.,

GET OBSERVATION (PATIENT X, TIME PERIOD, CODE FOR THE OBSERVATION(S) (DAILY STEPS AND AVERAGE WEEKLY), CATEGORY)

   </td>
  </tr>
  <tr>
   <td>R24 server receives GET and



1.  finds the patient's data in the OMOP data store
1.  computes if needs to using the parameters in the GET command
1.  sends data back HTTP: FHIR BUNDLE that includes FHIR observations with a 200 or sends back an error 401/403
   </td>
  </tr>
  <tr>
   <td>
mDATA receives the results of the GET command from the R24 server and displays it to the provider/patient.

   </td>
  </tr>
  <tr>
   <td>6

   </td>
   <td>Provider closes the mDATA app.

   </td>
   <td>mDATA may or may not permanently store the retrieved data in the mDATA datastore.  

   </td>
  </tr>
</table>
<br />

---

### Smart app Workflow

#### Retrieving OMH data in native OMH Schema format
{:.no_toc}


{% include img.html img="smartapp-binary.png" %}

|Step| Description|
|---|---|
|1.|Smart app Launch from Provider EHR. See the [Smart on FHIR Launch] Specification|
|2.|R24 server authenticates and authorizes app to get OMH data|
|3.|Following successful launch, the Smart app request OMH step count data for patient Z as a standard [FHIR search API] on *[DocumentReference]*. It provides an opaque identifier as a search parameter that identifies patient Z and optionally a time range of interest.|
|4.|The R24 server receives the request and either maps the opaque id to its user id list and creates the DocumentReference resource on the fly from a native format or searches its FHIR based datastore for DocumentReference matches.  Note that the DocumentReference is a 'wrapper' and contains context and a link to a [Binary] resource that represents the actual OMH Step Count data.|
|5.|The R24 server returns DocumentReference resources that match the search criteria|
|6.|The smart app receives the DocumentReference resource(s) and processes them one by one extracting the Binary endpoint data. then makes a second request to fetch the Binary resources in the native OMH (json) format using the standard [FHIR API for Binary data] (Note that the data may also be requested as a base64 encoded string as well).|
|8.|The R24 server receives the request for the OMH data in the native JSON format.|
|9.|For successful matches, the R24 Server Return the native OMH JSON file|
|10.|processes/displays the OMH data to the end user|
{:.grid}

##### Example
{:.no_toc}

###### Launch Smart on FHIR App (Steps 1 and 2).
{:.no_toc}

See the [Smart on FHIR Launch] Specification| for examples


######  Fetch FHIR DocumentReference resources containing OMH step count data.  (Steps 3-6)
{:.no_toc}


Includes: Opaque patient identifier, date Range, OMH datapoint common name,  OMH datapoint schema standard codes

|Details|URL|
|---|---|
|OMH Specification|<{{page.OS}}step-count>|
|FHIR STU3 DocumentReference Resource|<{{page.F}}documentreference.html>|
|FHIR STU3 Search API|<{{page.F}}search.html>|
{:.grid}

**Request**

~~~
GET /DocumentReference/?patient.identifier={identifier}

Content-type: application/json+fhir
Accept: application/json+fhir
...other headers...
~~~

**Issues**
1.  Assumed identifiers as 'logical' (opaque Identifiers) and not 'literal' reference to Patient resource (see {{page.F}}references.html.
    1. using a [contained] patient resource to hold the identifier to allow for searching by the identifier as 'chained' search.
    1. need to assign system  ( e.g UUID, or https://omh.r24server/ids )

<!--
https://vonk.furore.com/DocumentReference?patient=1.3.6.1.4.1.21367.2005.3.7.1234
-->

**Response**

~~~
HTTP/1.1 200 OK
Date: Tue, 22 May 2018 03:40:05 GMT
Content-Type: application/fhir+json; charset=utf-8
...other headers...

{
    "resourceType": "Bundle",
    "id": "d3334394-5e24-49d4-b8a2-d0fc004a69",
    "meta": {
        "lastUpdated": "2018-05-24T00:18:35Z"
    },
    "type": "searchset",
    "total": 1,
    "link": [
        {
            "relation": "self",
            "url": "http://test.fhir.org/r3/DocumentReference?_format=application/fhir+json&search-id=901a685f-a483-4e92-8a6e-fb3e14cbfc&&patient.identifier=some%2Duser&_sort=_id"
        }
    ],
    "entry": [
        {
            "fullUrl": "http://test.fhir.org/r3/DocumentReference/omh-stepcount-example",
            "resource": {
                "resourceType": "DocumentReference",
                "id": "omh-stepcount-example",
                "meta": {
                    "versionId": "4",
                    "lastUpdated": "2018-05-23T23:14:29Z"
                },
                "contained": [
                    {
                        "resourceType": "Patient",
                        "id": "p",
                        "identifier": [
                            {
                                "system": "https://omh.org/shimmer/patient_ids",
                                "value": "some-user"
                            }
                        ]
                    }
                ],
                "identifier": [
                    {
                        "system": "urn:ietf:rfc:3986",
                        "value": "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234"
                    }
                ],
                "status": "current",
                "type": {
                    "coding": [
                        {
                            "system": "http://loinc.org",
                            "code": "55423-8",
                            "display": "Step Count"
                        }
                    ]
                },
                "class": {
                    "text": "OMH schema data"
                },
                "subject": {
                    "reference": "#p"
                },
                "created": "2018-05-22T09:35:00+11:00",
                "indexed": "2018-05-22T09:35:00+11:00",
                "content": [
                    {
                        "attachment": {
                            "contentType": "application/json",
                            "url": "http://test.fhir.org/r3/Binary/omh-stepcount-example"
                        }
                    }
                ],
                "context": {
                    "period": {
                        "start": "2018-05-23T08:00:00+11:00",
                        "end": "2018-05-23T08:01:00+11:00"
                    }
                }
            },
            "search": {
                "mode": "match"
            }
        }
    ]
}
~~~

**Issues**

1. Need to assign classes and types codes to identify.
    1. need to assign system  ( e.g OMH )
1. Need to decide how much context to repeat here vs in OMH Schema data
    1. min date range and type of datatpoint


######  Fetch native OMH step count data.  (Steps 7-10)
{:.no_toc}


Includes: Binary id(s)

|Details|URL|
|---|---|
|OMH Specification|<{{page.OS}}step-count>|
|FHIR STU3 Binary Resource|<{{page.F}}binary.html>|
|FHIR STU3 REST API|<{{page.F}}html.html>|
{:.grid}

**Request**

~~~
GET /Binary/{id} or GET /Binary?_id={id}

Accept and Application-type headers absent!
...Other headers...
~~~

**Response**

~~~
HTTP/1.1 200 OK
Connection: close
Content-Type: application/json
...Other Headers...

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

**Issues:**

1. Fetching multiple files
   1. not specified  - may want an operation to zip into folder see this [Zulip Chat](https://chat.fhir.org/#narrow/stream/4-implementers/topic/Requesting.20multiple.20Binary.20Resources)?
2. ...

---



#### Retrieving OMH data as FHIR Observations
{:.no_toc}


{% include img.html img="smartapp-observation.png" %}

|Step| Description|
|---|---|
|1.|Smart app Launch from Provider EHR|
|2.|R24 server authenticates and authorizes app to get OMH data|
|<mark>3.</mark>|<mark>Following successful launch, the Smart app request OMH step count data for patient Z as a standard FHIR search API on *Observation*.  It provides an opaque identifier as a search parameter that identifies patient Z and optionally a time range of interest.</mark>|
|<mark>4.</mark>|<mark>The R24 server receives the request and either maps the opaque id to its user id list and maps the OMH step count schemas to Observation on the fly from a native format or searches its FHIR based datastore for matches.</mark>|
|<mark>5.</mark>|<mark>R24 server returns Observation resources that match the search criteria</mark>|
|<mark>6.</mark>|<mark>The smart app receives the Observation resource(s) and</mark>|
|7.|processes/displays the OMH data to the end user|
{:.grid}

##### Example
{:.no_toc}


###### Launch Smart on FHIR App (Steps 1 and 2)
{:.no_toc}


See the [Smart on FHIR Launch] Specification| for examples


######  Fetch FHIR Observation representing the OMH step count data.  (Steps 3-6)
{:.no_toc}


Includes: Opaque patient identifer, date range, OMH data type as code

|Details|URL|
|---|---|
|OMH Specification|<{{page.OS}}step-count>|
|FHIR STU3 Observation Resource|<{{page.F}}documentreference.html>|
|FHIR STU3 Search API|<{{page.F}}search.html>|
{:.grid}

**Request**

~~~
GET Observation?patient.identifier={identifier}&code=55423-8

Content-type: application/json+fhir
Accept: application/json+fhir
...other headers...
~~~

**Issues**

1.  Assumed identifiers as 'logical' (opaque Identifiers) and not 'literal' reference to Patient resource (see {{page.F}}references.html.
    1. using a [contained] patient resource to hold the identifier to allow for searching by the identifier as 'chained' search.
    1. need to assign system  ( e.g UUID, or https://omh.r24server/ids )
1. Using code to identify datapoint schema
1. search by max and min and other parameters
1. provenance?

**Response**

~~~
HTTP/1.1 200 OK
Connection: close
Content-Type: application/json
...Other Headers...

{
    "resourceType": "Bundle",
    "id": "55f690f4-d5e5-4f26-8fa2-026be61019",
    "meta": {
        "lastUpdated": "2018-05-23T23:48:12Z"
    },
    "type": "searchset",
    "total": 1,
    "link": [
        {
            "relation": "self",
            "url": "http://test.fhir.org/r3/Observation?_format=application/fhir+json&search-id=7db95351-c995-4cbc-b990-1760a91987&&patient.identifier=some%2Duser&_sort=_id"
        }
    ],
    "entry": [
        {
            "fullUrl": "http://test.fhir.org/r3/Observation/stepcount-example",
            "resource": {
                "resourceType": "Observation",
                "id": "stepcount-example",
                "meta": {
                    "versionId": "5",
                    "lastUpdated": "2018-05-23T21:56:09Z"
                },
                "contained": [
                    {
                        "resourceType": "Patient",
                        "id": "p",
                        "identifier": [
                            {
                                "system": "https://omh.org/shimmer/patient_ids",
                                "value": "some-user"
                            }
                        ]
                    }
                ],
                "identifier": [
                    {
                        "system": "https://omh.org/shimmer/ids",
                        "value": "12341567"
                    }
                ],
                "status": "unknown",
                "category": [
                    {
                        "coding": [
                            {
                                "system": "http://snomed.info/sct",
                                "code": "68130003",
                                "display": "Physical activity (observable entity)"
                            }
                        ]
                    }
                ],
                "code": {
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
                    "reference": "#p"
                },
                "effectivePeriod": {
                    "start": "2018-04-17T00:00:00Z",
                    "end": "2018-04-24T00:00:00Z"
                },
                "issued": "2018-04-24T17:13:50Z",
                "device": {
                    "display": "Jawbone UP API, modality =sensed, sourceCreationDateTime = 2018-04-17T17:13:50Z"
                },
                "component": [
                    {
                        "code": {
                            "coding": [
                                {
                                    "system": "http://hl7.org/fhir/observation-statistics",
                                    "code": "maximum",
                                    "display": "Maximum"
                                }
                            ],
                            "text": "Maximum"
                        },
                        "valueQuantity": {
                            "value": 7939,
                            "unit": "steps/day",
                            "system": "http://unitsofmeasure.org",
                            "code": "{steps}/d"
                        }
                    }
                ]
            },
            "search": {
                "mode": "match"
            }
        }
    ]
}
~~~


To view this API in action using the Postman Collection Runner import this [Postman Collection].

<br />


---

{%include link-list.md %}
