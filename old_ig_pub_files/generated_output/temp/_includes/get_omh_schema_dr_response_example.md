
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
