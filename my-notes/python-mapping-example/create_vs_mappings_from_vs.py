# -*- coding: utf-8 -*-

import json
import sys
import requests
from pprint import pprint
import fhirclient.models.valueset as v
import fhirclient.models.parameters as p

url = 'http://test.fhir.org/r4/CodeSystem/$lookup?system={system}&code={code}'
headers = {'Accept': 'application/fhir+json', 'Content-Type': 'application/fhir+json'}
in_path = '/Users/ehaas/Documents/FHIR/OMHtoFHIR/source/resources'
in_file= 'pygen-valueset-specimen-source'

in_files=[
'pygen-valueset-area-unit-value',
'pygen-valueset-body-location',
'pygen-valueset-body-posture',
'pygen-valueset-day-of-week',
'pygen-valueset-descriptive-statistic-denominator',
'pygen-valueset-duration-unit-value',
'pygen-valueset-intervention-administration-route',
'pygen-valueset-length-unit-value',
'pygen-valueset-magnetic-flux-density-unit-value',
'pygen-valueset-mass-unit-value',
'pygen-valueset-medication-dose-unit',
'pygen-valueset-pace-unit-value',
'pygen-valueset-part-of-day',
'pygen-valueset-position-during-measurement',
'pygen-valueset-specimen-source',
'pygen-valueset-speed-unit-value',
'pygen-valueset-temperature-unit-value',
'pygen-valueset-temporal-relationship-to-meal',
'pygen-valueset-temporal-relationship-to-physical-activity',
'pygen-valueset-temporal-relationship-to-sleep',
'pygen-valueset-volume-unit-value'
]

# create mapping table from vs

def get_rjson(file):  # get json file from path and return as dict
    with open('{in_path}/{file}.json'.format(in_path=in_path,file=file), 'r') as rjson:
        return(json.load(rjson))

# cycle through all codes and create {code:(system,code,display)} table
my_dict={}
for in_file in in_files:
    print('in_file = {}'.format(in_file))
    my_vs = get_rjson('{in_file}'.format(in_file=in_file))
    my_vs = v.ValueSet(my_vs)

    for vs_codes in my_vs.compose.include:
        add_dict = {code.display : [vs_codes.system,code.code,None] for code in vs_codes.concept}

        #add dictionaries together
        my_dict.update(add_dict)

pprint(my_dict)

for k,v in my_dict.items():  # lookup code displays
    # print('omh_concept={concept}, system={system}, code={code}'.format(concept=k,system=v[0],code=v[1]))
    response = requests.get(url=url.format(system=v[0],code=v[1]), headers=headers)
    print('Status == {status}'.format(status=response.status_code))
    if response.status_code == 200:
        '''
        try: 
                print('omh_concept={concept}, system={system}, code={code} display ={display}'.format(concept=k,system=v[0],code=v[1],display=str(response.json())))

        except UnicodeEncodeError:
            print('UnicodeEncodeError for {concept}'.format(concept=k))
        '''
        parameters = response.json()
        
        # print(''.join([i['valueString'] for i in parameters['parameter'] if i['name']=='display']))
        
        v[2]=''.join([i['valueString'] for i in parameters['parameter'] if i['name']=='display'])


# my_dict = {k: tuple(v) for (k,v) in my_dict.items()}

pprint({k: tuple(v) for (k,v) in my_dict.items()})

