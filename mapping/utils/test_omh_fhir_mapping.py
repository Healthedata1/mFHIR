import json
from pprint import pprint

omh_schema_template = '''{{
  "header": {{
    "id": "243c773b-8936-407e-9c23-270d0ea49cc4",
    "creation_date_time": "2015-09-10T12:43:39.138-06:00",
    "acquisition_provenance": {{
      "source_name": "Jawbone UP API",
      "modality": "sensed",
      "source_updated_date_time": "2015-09-10T18:43:39Z"
    }},
    "schema_id": {{
      "namespace": "omh",
      "name": "{name}",
      "version": "1.0"
    }},
    "user_id": "306a1202-410d-11e8-842f-0ed5f89f718b"
  }},
  "body": {body}
}}'''

test_schemas = [{
'name': 'blood_pressure',
'body':'''{
    "systolic_blood_pressure": {
        "value": 160,
        "unit": "mmHg"
    },
    "diastolic_blood_pressure": {
        "value": 60,
        "unit": "mmHg"
    }
}'''
},

dict(name='blood_pressure',body='''{
    "systolic_blood_pressure": {
        "value": 160,
        "unit": "mmHg"
    },
    "diastolic_blood_pressure": {
        "value": 60,
        "unit": "mmHg"
    },
    "effective_time_frame": {
        "time_interval": {
            "start_date_time": "2013-02-05T07:25:00Z",
            "end_date_time": "2013-06-05T07:25:00Z"
        }
    },
    "body_posture": "sitting",
    "descriptive_statistic": "maximum"
}'''
),
dict(name='blood_pressure',body='''{
    "systolic_blood_pressure": {
        "value": 160,
        "unit": "mmHg"
    },
    "diastolic_blood_pressure": {
        "value": 60,
        "unit": "mmHg"
    },
    "body_posture": "sitting"
}'''
)]

pprint(test_schemas)

