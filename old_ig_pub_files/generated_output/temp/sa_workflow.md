---
title: Smart App Workflow
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


<!-- end TOC -->

### R24 Server Architecture


{% include img-portrait.html img="R24_Overview2.jpg" %}

**FHIR-enabled EHR system**

- A *Open mHealth to FHIR Server* with FHIR server running SMART-on-FHIR protocols for authentication/authorization, etc.
- Patient’s step counter sensor (called ** StepSensor** in this use case) – specific product, may be the patient’s phone
- Data store for the Step-Counter output (e.g., cloud and/or phone (e.g., GoogleFit, HealthKit)) that either offers data directly in - Open mHealth format using an Open mHealth endpoint, or is supported by *Shimmer* or *Granola*
- OmH-on-FHIR Client a SMART on FHIR app – has roles for PCP, onboarding staff, and patient

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

{% include examplebutton.html example="get_omh_schema_dr_response_example" b_title = "Response to `GET /DocumentReference/?...`" %}


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

{% include examplebutton.html example="get_omh_schema_binary_response_example" b_title = "Response to `GET /Binary/{id}`" %}


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


{% include examplebutton.html example="get_fhir_resource_response_example" b_title = "Response to `GET Observation?...`" %}


To view this API in action using the Postman Collection Runner import this [Postman Collection].

<br />

---

{%include link-list.md %}
