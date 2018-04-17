SHIMMER API notes

SHIMs ( API library )
- authentication
- requests
- mapping to Open mHealth
- creates 'data points'
  - data of interest
  - metadata:
    - acquisiton provenance
    - dates
    - data source

Resource Server
  -  e.g. R24 Server
  -  handles the API requests - delegating to the right 'shim'


The description and resource map to the loinc,

there is a header with some meta data and a body for the data itself  -

SHIMMER can be replaced by SMART on FHIR and mapping to the profile vs mapping to schema make more sense.

example of a normalized step count data point retrieved from Jawbone


{
    "header": {
        "id": "243c773b-8936-407e-9c23-270d0ea49cc4",
        "creation_date_time": "2015-09-10T12:43:39.138-06:00",
        "acquisition_provenance": {
            "source_name": "Jawbone UP API",
            "modality": "sensed",
            "source_updated_date_time": "2015-09-10T18:43:39Z"
        },
        "schema_id": {
            "namespace": "omh",
            "name": "step-count",
            "version": "1.0"
        }
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
