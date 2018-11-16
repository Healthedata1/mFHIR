from pprint import pprint

D1 = {'OmhHeader': 'OmhHeader',
'dataPointId': 'OmhHeader.id',
'creationDateTime': 'OmhHeader.creation_date_time',
'schemaId': 'properties.header.schema_id',
'namespace': 'header.schema_id.namespace',
'name': 'header.schema_id.name',
'version': 'header.schema_id.version',
'acquisitionProvenance': 'header.acquisition_provenance',
'sourceName': 'header.acquisition_provenance.source_name',
'sourceDataPointId': 'header.acquisition_provenance.source_data_point_id',
'sourceCreationDateTime': 'header.acquisition_provenance.source_creation_date_time',
'modicationDataTime': 'header.acquisition_provenance.modication_data_time',
'modality': 'header.acquisition_provenance.modality',
'userId': 'header.user_id'}

D2 ={'OmhHeader': 'Observation Resource',
'dataPointId': 'Observation.identifier',
'creationDateTime': 'Observation.issued',
'schemaId': 'Observation.meta.profile',
'namespace': 'None',
'name': 'None',
'version': 'None',
'acquisitionProvenance': 'None',
'sourceName': 'Observation.meta.source',
'sourceDataPointId': 'Observation.identifier',
'sourceCreationDateTime': 'None',
'modicationDataTime': 'None',
'modality': 'Observation.device',
'userId': 'Observation.subject'}

print('**OMH to FHIR Observation Resource mappings **')
print('|OMH element|FHIR element|')
print('|---|---|')
for k in D1:
    print('|{}|{}|'.format(D1[k],D2[k]))




