#!/usr/bin/env python3

import sys, os, json
import fhir_templates as f  # fhir json string templates
import omh_fhir_concept_mapping_table as maps  
import test_omh_fhir_mapping as unit_tests
from partial_formatter import PartialFormatter
from pdb import set_trace as bp
from stringcase import spinalcase, titlecase, snakecase
from pprint import pprint

fmt= PartialFormatter()


#================ convert json object to nametuple - able to access using dot notation ===========

def _json_object_hook(d):
     return type('X', (object,), d)()


def json2obj(data):
     return json.loads(data, object_hook=_json_object_hook)


def scrub_dict(d):
    unwanted = ['', u'', None, [], {}, 'None', -1]
    if type(d) is dict:
        return dict((k, scrub_dict(v)) for k, v in d.items() if v not in unwanted and scrub_dict(v))
    elif type(d) is list:
        return [scrub_dict(v) for v in d if v not in unwanted and scrub_dict(v)]
    else:
        return d


def omh_to_fhir(data):

    # create an python object from the json schema
    x = json2obj(data)

    # get schema name  ( e.g. 'step_count')
    schema_id = x.header.schema_id.name



    # map code and category from schema_id.name and set some default values
    observation_category_code = f.omh_datatype_mapping[schema_id][0]
    observation_category_display = f.omh_datatype_mapping[schema_id][1]
    observation_code_system = f.omh_datatype_mapping[schema_id][2]
    observation_code_code = f.omh_datatype_mapping[schema_id][3]
    observation_code_display = f.omh_datatype_mapping[schema_id][4]
    descriptive_statistic = f.omh_datatype_mapping[schema_id][6]
    descriptive_statistic_denominator = f.omh_datatype_mapping[schema_id][7]
    
    print('Observation.category =  {category}'.format(category=observation_category_code))
    print('Observation.code = {code} ({display})'.format(code=observation_code_code, display=observation_code_display))

    # get actual numeric value - may need to inspect schema path to find it.
    try:
        observation_value_quantity_value = getattr(x.body,schema_id)
        try:
            observation_value_quantity_value = getattr(observation_value_quantity_value,'value')
            observation_value_quantity_unit = getattr(observation_value_quantity_value,'unit')
            observation_value_quantity_system = 'http://unitsofmeasure.org'
            observation_value_quantity_code = maps.concept_maps[observation_value_quantity_unit][1]
        except AttributeError:  # no value and unit element like in step step_count
            observation_value_quantity_unit = f.omh_datatype_mapping[schema_id][5][0]  # use default
            observation_value_quantity_system = 'http://unitsofmeasure.org'
            observation_value_quantity_code = maps.concept_maps[observation_value_quantity_unit][1]
    except AttributeError:  # no value element like in blood_pressure panel
        observation_value_quantity_value = -1  # assign as a null value for now
        observation_value_quantity_system = 'None'
        observation_value_quantity_unit = 'None' 
        observation_value_quantity_code = 'None'



    # print(observation_value_quantity_value)

    # todo map to appropriate ucum units create table lookup.

    try: # mapping unit from descriptive_statistic_denominator for valueQuantity
        statistic_key = x.body.descriptive_statistic_denominator
        observation_value_quantity_unit = '{numerator}{denominator}'.format(
        numerator=observation_value_quantity_unit,
        denominator=f.omh_denominator_value[statistic_key][0]
        )
        observation_value_quantity_code = '{numerator}{denominator}'.format(
        numerator=observation_value_quantity_code,
        denominator=f.omh_denominator_value[statistic_key][1]
        )
    except AttributeError:
        pass #  use default units variables

    try:# additional  codings for stats
        addl_observation_coding_system = 'http://hl7.org/fhir/omh_fhir_observation_codes' 
        addl_observation_coding_code = '{}-{}'.format(spinalcase(schema_id), spinalcase(x.body.descriptive_statistic))
        addl_observation_coding_display ='{} {}'.format(titlecase(schema_id), titlecase(x.body.descriptive_statistic))
    except AttributeError:
        addl_observation_coding_system='None'
        addl_observation_coding_code='None'
        addl_observation_coding_display='None'

    #map specimen_source codes to specimen code extension using the concepts from the specimen_source valueset.
    try:
        observation_specimen_code_extension_url = 'http://www.fhir.org/mfhir/StructureDefinition/omh_fhir_extension_observation_specimen_code'
        observation_specimen_code_system = maps.concept_maps[x.body.specimen_source][0]
        observation_specimen_code_code = maps.concept_maps[x.body.specimen_source][1]
        observation_specimen_code_display = maps.concept_maps[x.body.specimen_source][2]
        observation_specimen_code_text = x.body.specimen_source
    except AttributeError: #no specimen_source
        observation_specimen_code_system = 'None'
        observation_specimen_code_code = 'None'
        observation_specimen_code_display = 'None'
        observation_specimen_code_extension_url = 'None'
        observation_specimen_code_text = 'None'

    #add components 
    observation_componentx = []
    for component in f.omh_component_mapping:
        try:
            component_name = getattr(x.body,component)
            observation_component_code_system = f.omh_component_mapping[component][0]
            observation_component_code_code = f.omh_component_mapping[component][1]
            observation_component_code_display = f.omh_component_mapping[component][2]
            if f.omh_component_mapping[component][3] == 'valueCodeableConcept': #look up code mappings (e.g. temporal_relationship_to_sleep)
                observation_component_value_codeableconcept_system = maps.concept_maps[component_name][0]
                observation_component_value_codeableconcept_code = maps.concept_maps[component_name][1]
                observation_component_value_codeableconcept_display = maps.concept_maps[component_name][2]
                observation_component_value_codeableconcept_text = component_name
                observation_component_value_quantity_value = -1
                observation_component_value_quantity_unit = 'None'
                observation_component_value_quantity_system = 'None'
                observation_component_value_quantity_code = 'None'

            else: # enter values directly ( e.g. blood pressure )
                observation_component_value_quantity_value = getattr(component_name,'value')
                # print(component, observation_component_value_quantity_value)
                observation_component_value_quantity_unit =  getattr(component_name,'unit')
                observation_component_value_quantity_system = 'http://unitsofmeasure.org'
                observation_component_value_quantity_code = maps.concept_maps[observation_component_value_quantity_unit][1]
                observation_component_value_codeableconcept_system = 'None'
                observation_component_value_codeableconcept_code = 'None'
                observation_component_value_codeableconcept_display = 'None'
                observation_component_value_codeableconcept_text = 'None'

                
            observation_componentx.append(fmt.format(
                f.observation_componentx_template,
                observation_component_code_system=observation_component_code_system,
                observation_component_code_code=observation_component_code_code,
                observation_component_code_display=observation_component_code_display,
                observation_component_value_codeableconcept_system=observation_component_value_codeableconcept_system,
                observation_component_value_codeableconcept_code=observation_component_value_codeableconcept_code,
                observation_component_value_codeableconcept_display=observation_component_value_codeableconcept_display,
                observation_component_value_codeableconcept_text=observation_component_value_codeableconcept_text,
                observation_component_value_quantity_value=observation_component_value_quantity_value,
                observation_component_value_quantity_unit=observation_component_value_quantity_unit,
                observation_component_value_quantity_system=observation_component_value_quantity_system,
                observation_component_value_quantity_code=observation_component_value_quantity_code
            ))
        except AttributeError:  # no component in this instance
            pass
    # print('observation_componentx ={}'.format(','.join(observation_componentx)))
    observation_componentx = ','.join(observation_componentx) # change to string for string formatting

    omh_obs_json = fmt.format(f.omh_obs_templ,
        server_assigned_resource_id=None,
         # additional  codings for stats
        addl_observation_coding_system=addl_observation_coding_system,
        addl_observation_coding_display=addl_observation_coding_display,
        addl_observation_coding_code=addl_observation_coding_code,
        #specimen_source mappings
        observation_specimen_code_system =observation_specimen_code_system,
        observation_specimen_code_code=observation_specimen_code_code,
        observation_specimen_code_display=observation_specimen_code_display,
        # add components
        observation_componentx=observation_componentx,
        # header mappings
        header=x.header,
        # body mappings (time mappings)
        body=x.body,
        # codes, value, units
        observation_category_code = observation_category_code,
        observation_category_display = observation_category_display,
        observation_code_system = observation_code_system,
        observation_code_code = observation_code_code,
        observation_code_display = observation_code_display,
        # measure value
        observation_value_quantity_value = observation_value_quantity_value,
        observation_value_quantity_unit = observation_value_quantity_unit,
        observation_value_quantity_system = observation_value_quantity_system,
        observation_value_quantity_code = observation_value_quantity_code,
        descriptive_statistic = descriptive_statistic,
        descriptive_statistic_denominator = descriptive_statistic_denominator,
        )
        
    # print(omh_obs_json)
    # delete Nulls using scrunbd function this is one way or could load in the fhir python library
    # convert json to dict
    omh_obs_dict = json.loads(omh_obs_json)
    omh_obs_dict = scrub_dict(omh_obs_dict)
    # ....and back to json
    
    print('*********************this OMH datapoint file**************')
    print(json_string)

    print('******maps to this FHIR Observation**********')
    print(json.dumps(omh_obs_dict, indent=3))


data = '{"body":{"systolic_blood_pressure":{"value":160,"unit":"mmHg"},"diastolic_blood_pressure":{"value":60,"unit":"mmHg"}},"header":{"creation_date_time":"2015-09-10T12:43:39.138-06:00","user_id":"306a1202-410d-11e8-842f-0ed5f89f718b","id":"243c773b-8936-407e-9c23-270d0ea49cc4","acquisition_provenance":{"source_updated_date_time":"2015-09-10T18:43:39Z","modality":"sensed","source_name":"Jawbone UP API"},"schema_id":{"name":"blood_pressure","namespace":"omh","version":"1.0"}}}'

if __name__ == "__main__":
    # execute only if run as a script
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

    for schema_name in test_schemas: # get test files
        schema_path = '{base_path}/{schema_name}/2.0/ShouldPass'.format(base_path=base_path, schema_name=spinalcase(schema_name))
        if os.path.isdir(schema_path):
            pass
        else:
            schema_path = '{base_path}/{schema_name}/1.0/ShouldPass'.format(base_path=base_path, schema_name=spinalcase(schema_name))
        for schema in os.listdir(schema_path):
            print('Test Schema = {schema}'.format(schema=snakecase(os.path.splitext(schema)[0])))
            with open('{schema_path}/{schema}'.format(schema_path=schema_path, schema=schema)) as schema_file:
                schema_dict = json.load(schema_file)
                schema_json = json.dumps(schema_dict,indent=3)
                json_string = unit_tests.omh_schema_template.format(name=schema_name,body=schema_json)
                json_data = json.loads(json_string) # create a dict
                data = json.dumps(json_data, separators=(',', ":")) #minify as json string
                omh_to_fhir(data)
            
print('end')