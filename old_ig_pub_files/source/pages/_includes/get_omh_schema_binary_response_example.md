
~~~
HTTP/1.1 200 OK
Connection: close
Content-Type: application/json
...Other Headers...

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
