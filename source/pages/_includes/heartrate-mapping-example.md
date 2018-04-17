*Open mHealth schema representing heart rate:*

~~~
{
  "header": {
    "id": "87ca4312-fbe3-4b24-bab4-17d47ba54e2a",
    "creation_date_time": "2014-01-03T09:14:41Z",
    "acquisition_provenance": {
      "source_name": "generator",
      "source_creation_date_time": "2014-01-03T09:13:41Z",
      "modality": "sensed"
    },
    "user_id": "some-user",
    "schema_id": {
      "namespace": "omh",
      "name": "heart-rate",
      "version": "1.0"
    }
  },
  "body": {
    "effective_time_frame": {
      "date_time": "2014-01-03T09:13:41Z"
    },
    "heart_rate": {
      "unit": "beats/min",
      "value": 79.88711511574905
    }
  },
  "id": "87ca4312-fbe3-4b24-bab4-17d47ba54e2a"
}
~~~

*Transform to OmhDataPoint Logical Model:*

~~~
{
   "ResourceType":"OmhDataPoint",
   "id" : "omh-heart-rate-example",
   "header" : {
     "dataPointId" : "87ca4312-fbe3-4b24-bab4-17d47ba54e2a",
     "creationDateTime" : "2014-01-03T09:14:41Z",
     "schemaId" : {
       "namespace" : "omh",
       "name" : "heart-rate",
       "version" : "1.0"
     },
     "acquisitionProvenance" : {
       "sourceName" : "generator",
       "sourceCreationDateTime" : "2014-01-03T09:13:41Z",
       "modality" : "sensed"
     },
     "userId" : "some-user"
   },
   "body" :
   {
      "ResourceType":"OmhHeartRate",
      "id":"omh-heart-rate-example",
      "valueUnit":{
         "value":79.88711511574905,
         "unit":"beats/min",
         "system":"http://unitsofmeasure.org",
         "code":"/min"
      },
      "effectiveTimeFrame":"2014-01-03T09:13:41Z",
   }}
~~~


*Transform to FHIR Observation:*

~~~
{
   "resourceType":"Observation",
   "id":"omh-heart-rate-example",
   "meta":{
      "source":"generator",
      "profile":[
         "http://www.fhir.org/guides/mfhir/StructureDefinition/heart-rate"
      ]
   },
   "identifier":[
      {
         "system":"https://omh.org/shimmer/ids",
         "value":"87ca4312-fbe3-4b24-bab4-17d47ba54e2a"
      }
   ],
   "status":"unknown",
   "category":[
      {
         "coding":[
            {
               "system":"http://hl7.org/fhir/observation-category",
               "code":"vital-signs",
               "display":"Vital Signs"
            }
         ]
      }
   ],
   "code":{
      "coding":[
         {
            "system":"http://loinc.org",
            "code":"8867-4",
            "display":"Heart rate"
         }
      ],
      "text":"Heart Rate"
   },
   "subject":{
      "identifier":{
         "system":"https://omh.org/shimmer/patient_ids",
         "value":"some-user"
      },
      "effectiveDateTime":"2014-01-03T09:13:41Z",
      "issued":"2014-01-03T09:14:41Z",
      "valueQuantity":{
         "value":79.88711511574905,
         "unit":"beats/min",
         "system":"http://unitsofmeasure.org",
         "code":"/min"
      }
   }
}
~~~
