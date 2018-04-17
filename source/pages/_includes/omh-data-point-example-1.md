~~~
{  
   "ResourceType":"OmhDataPoint",
   "id" : "example-1",
   "header" : {   
     "dataPointId" : "12341567",   
     "creationDateTime" : "2018-04-17T17:13:51Z",   
     "schemaId" : {   
       "namespace" : "omh",   
       "name" : "step-count",   
       "version" : "1.0"   
     },
     "acquisitionProvenance" : {  
       "sourceName" : "Jawbone UP API>",   
       "sourceDataPointId" : "123456",  
       "sourceCreationDateTime" : "2018-04-17T17:13:50Z",  
       "modicationDataTime" : "2018-04-17T17:13:51Z",  
       "modality" : "sensed"  
     },
     "userId" : "user123456"  
   },
   "body" :
 {
   "ResourceType":"OMHStepCount",
   "id":"example-1",
   "stepCount":7939,
   "effectiveTimeFrame":{  
      "start":"2018-04-17",
      "end":"2018-04-17"
   },
   "descriptiveStatistic":"count",
   "descriptiveStatisticDenominator":"d"
}}
~~~
