import fhir_templates as f
import omh_fhir_concept_mapping_table as maps
from pprint import pprint
from stringcase import titlecase, spinalcase
new= {}
print("|{0}|{0}|{0}|{0}|{0}|{0}|{0}|{0}|{0}|".format('--'))
for k,v in sorted(f.omh_datatype_mapping.items()):
    new_list =list(v)[0:1] + list(v)[2:]
    print(("|{k}|{}|{}|{}|{}|{}|{}|{}|{}|".format(k=k,*new_list)))
    
# below is to upate the table in fhir_templates
'''    
print('{')
for k,v in sorted(f.omh_datatype_mapping.items()):
    new_list = list(v)
    new_list.remove(new_list[6])
    print("'{}': {},".format(k,tuple(new_list)))

print('}')
'''
'''
print('[')
for k,v in sorted(f.omh_datatype_mapping.items()):
    if v[5]:
      print("'{}',".format(k))
print(']')
'''

# create descriptive_statistic tables:

header = '''**{schema_title} Descriptive Statistic Mapping Tables**

This table maps the {schema_name} descriptive statistic to the OMH to FHIR additional Observation codings ( code system `http://www.fhir.org/guides/mfhir/omh_fhir_observation_codes`). If the schema element is absent, the default measure is a single measurement and there is no additional coding.

|body.descriptive_statistic|Observation.coding.code|Observation.coding.display|
|---|---|---|'''


stat_codes = [
'average',
'maximum',
'minimum',
'count',
'totalcount',
'median',
'std-dev',
'sum',
'variance',
'20-percent',
'80-percent',
'4-lower',
'4-upper',
'4-dev',
'5-1',
'5-2',
'5-3',
'5-4',
'skew',
'kurtosis',
'regression'
]


for k,v in sorted(f.omh_datatype_mapping.items()):
    if v[6]:
        schema_name = spinalcase(k)
        schema_title = titlecase(k)
        print(header.format(schema_name=schema_name, schema_title=schema_title))
        for stat_code in stat_codes:
            print('|{stat_code}|{obs_code}|{obs_display}|'.format(
            stat_code=stat_code,
            obs_code='{schema_name}-{stat_code}'.format(schema_name=schema_name,stat_code=stat_code),
            obs_display='{schema_title} {stat_code}'.format(schema_title=schema_title,stat_code=titlecase(stat_code))))
        print('{: .grid}\n')
        

# create omh component mapping tables

print("|{0}|{1}|{2}|{3}|{4}|".format('Component Name',
'Component Code System',
'Component Code Code',
'Component Code Display',
 'Component Value Type'))
print("|{0}|{0}|{0}|{0}|{0}|".format('---'))
for k,v in sorted(f.omh_component_mapping.items()):
    new_list = list(v)
    print(("|{k}|{}|{}|{}|{}|".format(k=k,*new_list)))
    
    
# create omh concept mapping tables
print()
print()
print("|{0}|{1}|{2}|{3}|".format('OMH "Term"',
'Concept Code System',
'Concept Code',
'Concept Code Display'))
print("|{0}|{0}|{0}|{0}|".format('---'))
for k,v in sorted(maps.concept_maps.items()):
    new_list = list(v)
    print(("|{k}|{}|{}|{}|".format(k=k,*new_list)))


