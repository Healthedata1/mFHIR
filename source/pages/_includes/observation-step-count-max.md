~~~
{
  "resourceType": "Observation",
	"id": "steps-example //  this is a server assigned resource id",
  "meta": {
  "source" : "Jawbone UP API // mappped from OmhDataPoint.header.acqusitionProvenance.sourceName",
  "profile // Profiles this resource claims to conform to" : ["http://www.fhir.org/guides/mfhir/StructureDefinition/steps"]
}
  "identifier // mapped from OmhDataPoint.header.dataPointId": [{
  "system" : "https://omh.org/shimmer/ids // The namespace for the identifier value",
  "value" : "12341567 // The value that is unique"
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
	"code // mapped from OmhDataPoint.body": {
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
  "value" : "some-user //mapped from OmhDataPoint.header.userId",
},
	},
	"effectivePeriod // mapped from OmhDataPoint.body.effectiveTimeFrame":
  "start" : "2018-04-17T00:00:00Z",
  "end" : "2018-04-24T00:00:00Z"
    }
	"issued": "2018-04-24T17:13:50Z // mapped from OmhDataPoint.header.creationDateTime",
	}
  //valueQuantity: {} the actual results mapped from body.step_count if there is no descriptiveStatistic  
   "device //  could be mapped from OmhDataPoint.header.acqusitionProvenance elements represented as for this example but could capture all as Device/DeviceMetric since the type is  Reference(Device|DeviceComponent|DeviceMetric)" :
   {"display" : "Jawbone UP API, modality =sensed, sourceCreationDateTime = 2018-04-17T17:13:50Z"}
"component // Component results for descriptiveStatistic on if there is a descriptiveStatistic" : [{
"code  // Type of descriptiveStatistic" : {
  "coding" : [
    {
      "system" : "http://hl7.org/fhir/observation-statistics",
      "code" : "maximum",
      "display" : "Maximum",
    }
    ],
    "text" : "Maximum"
  },
  "valueQuantity  // the actual results mapped from body.step_count  - note that I added optional UCUM units mapped from the observation code, description statistics and  descriptive_statistic_denominator": {
		"value //mapped from OmhDataPoint.body.stepCount": 7939,
		"unit": "steps/day",
		"system": "http://unitsofmeasure.org",
		"code": "{steps}/d"
	}
]
}
~~~
