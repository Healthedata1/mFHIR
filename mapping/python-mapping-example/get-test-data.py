import sys, os, json
from stringcase import spinalcase, titlecase

test_schemas  = [
'blood_glucose',
'blood_pressure',
'body_fat_percentage',
'body_height',
'body_mass_index',
'body_temperature',
'body_weight',
'calories_burned',
'diastolic_blood_pressure',
'heart_rate',
'minutes_moderate_activity',
'oxygen_saturation',
'respiratory_rate',
'sleep_duration',
'step_count',
'systolic_blood_pressure'
]

print('Current directory ={}'.format(os.getcwd()))

base_path = 'my-notes/python-mapping-example/test-data/omh'

for schema_name in test_schemas: # get files
    schema_path = '{base_path}/{schema_name}/2.0/ShouldPass'.format(base_path=base_path, schema_name=spinalcase(schema_name))
    if os.path.isdir(schema_path):
        pass
    else:
        schema_path = '{base_path}/{schema_name}/1.0/ShouldPass'.format(base_path=base_path, schema_name=spinalcase(schema_name))
    for schema in os.listdir(schema_path):
        print(schema)
        with open('{schema_path}/{schema}'.format(schema_path=schema_path, schema=schema)) as schema_file:
            schema_dict = json.load(schema_file)
            schema_json = json.dumps(schema_dict)
            json_string = unit_tests.omh_schema_template.format(name=schema_name,body=schema_json)
            json_data = json.loads(json_string) # create a dict
            data = json.dumps(json_data, separators=(',', ":")) #minify as json string
            omh_to_fhir(data)

    
