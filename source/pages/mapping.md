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
          "profile // Profiles this resource claims to conform to" : ["http://www.fhir.org/guides/mfhir/StructureDefinition/steps"]
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
