{% assign id = {{page.id}} %}
source file: source/pages/\_includes/{{id}}-intro.md

{{site.data.structuredefinitions.[id].description}}

The OMH header schema is represented as a formal FHIR Logical Model in the section below in order to facilitate model to model mappings.  However, the following table and resource template are provided for mapping an OMH schema instance to a FHIR resource instance.

#### OMH Element to FHIR Element Mapping Table

This table maps the OMH element to the corresponding FHIR Observation element.  

|OMH element|FHIR element|
|---|---|
|template profile|Observation|
|header.id|Observation.identifier|
|header.creation_date_time|Observation.issued|
|header.schema_id|Observation.meta.profile|
|header.schema_id.namespace|Observation.meta.profile|
|header.schema_id.name|Observation.meta.profile|
|header.schema_id.version|Observation.meta.profile|
|header.acquisition_provenance|None|
|header.acquisition_provenance.source_name|Observation.device|
|header.acquisition_provenance.source_data_point_id|Observation.identifier|
|header.acquisition_provenance.source_creation_date_time|None|
|header.acquisition_provenance.modication_data_time|None|
|header.acquisition_provenance.modality|Observation.device.extension|
|header.user_id|Observation.subject|
{: .grid}

#### Observation Template

This FHIR Observation template is an instance view of the above mappings and can be populated with data from an OMH schema to create a FHIR Observation instance.

~~~
{
       "resourceType": "Observation",
       "id": "%(server_assigned_resource_id)",
       "meta": {
       "profile" : ["http://www.fhir.org/mfhir/StructureDefinition/%(header.schema_id.namespace)-%(header.schema_id.name)-%(header.schema_id.version)"]
     }
       "identifier  : [
       "system" : "https://omh.org/shimmer/ids",
       "value" : "%(header.id)",
       }],
       "status": "unknown",
       "category": [  
         {
           "coding": [
             {
               "system": "http://hl7.org/fhir/observation-category",
               "code": "%(observation_category_code)",
               "display": "%(observation_category_display)"
             }
           ]
         }
       ],
       "code: {
         "coding": [
           {
             "system": "http://loinc.org",
             "code": "%(code_from_datapoint_mapping)",
             "display": "%(display_from_datapoint_mapping)"
           }
         ]
       },
       "subject": {
         "identifier" : {
       "system" : "https://omh.org/shimmer/patient_ids",
       "value" : "%(header.user_id)",
     },
       },
       %(observation-effectivex)
       "issued": "%(header.creation_date_time)",
       %(observation-valuex)
        "device" :
        "extension" : [{
          "url" : "http://www.fhir.org/mfhir/StructureDefinition/observationDeviceModality",
          "valueCode" : "%(header.acquisition_provenance.modality)"
        }],
        {"display" : "%(header.acqusitionProvenance.sourceName)"}
     }
~~~

Notes on template usage:

1. Template variables are represented using the `%()` syntax
1. Variable such as `%(header.acquisition_provenance.modality)` represent OMH data elements or mappings from OMH data elements
1. the variables %(observation-valuex) (the actual result values) and %(observation-effectivex) (the actual times the measurements occurred ) are subtemplates since elements that have a choice of data types.  They are mapped to the datapoint body elements
1. %(server_assigned_resource_id) is a assigned by the server when the resource is created and is typically not mapped from the OMH schema instance.
1. The profile element is the FHIR profiles this resource claims will conform to when fully populated.
1. The namespaces, "https://omh.org/shimmer/ids"  and "https://omh.org/shimmer/patient_ids" are use to assign a system to shimmer generated ids.
1. The `status` element is required in FHIR Observation and since omh schema don't have status its values is hardcoded to 'unknonwn'
1. The `category` and 'code' code and display is determined from a translation table that is mapped to the OmhDataPoint.header.schema_id.name.  See  this mapping table.


#### Example

For example see the datapoint Profiles
