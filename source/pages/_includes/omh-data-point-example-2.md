~~~
{  
   "ResourceType":"OmhDataPoint",
   "id" : "example-2",
   "header" : {   
     "dataPointId" : "12341567",   
     "creationDateTime" : "2018-04-17T17:13:51Z",   
     "schemaId" : {   
       "namespace" : "omh",   
       "name" : "step-count",   
       "version" : "1.0"   
     },
     "acquisitionProvenance" : {  
       "sourceName" : "Jawbone UP API",   
       "sourceDataPointId" : "123456",  
       "sourceCreationDateTime" : "2018-04-17T17:13:50Z",  
       "modicationDataTime" : "2018-04-17T17:13:51Z",  
       "modality" : "sensed"  
     },
     "userId" : "user123456"  
   },
   "body" :
   {  
      "ResourceType":"OmhHeartRate",
      "id":"example-2",
      "valueUnit":{  
         "value":78.08,
         "unit":"beats/min",
         "system":"http://unitsofmeasure.org",
         "code":"/min"
      },
      "effectiveTimeFrame":"2018-04-17T17:13:51Z",
      "descriptiveStatistic":"count",
      "temporalRelationshipToPhysicalActivity":"263678003",
      "temporalRelationshipToSleep":"307155000"
   }}
~~~
