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
   ...omh datapoint measurement schema (e.g., step-count)...
   }}
~~~
