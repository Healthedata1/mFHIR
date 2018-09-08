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
