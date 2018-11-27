

import json
import enum
import pprint




class schema_id:

    _types_map = {
    }
    _formats_map = {
    }

    
    def as_dict(self):
        d = dict()
        return d

class date_time:

    _types_map = {
    }
    _formats_map = {
    }

    
    def as_dict(self):
        d = dict()
        return d

class OmhHeader:

    _types_map = {
        'creation_date_time': {'type': date_time, 'subtype': None},
        'id': {'type': str, 'subtype': None},
        'acquisition_provenance': {'type': type, 'subtype': None},
        'schema_id': {'type': schema_id, 'subtype': None},
        'user_id': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }

    def __init__(self
            , creation_date_time=None
            , id=None
            , acquisition_provenance=None
            , schema_id=None
            , user_id=None
            ):
        self.__creation_date_time = creation_date_time
        self.__id = id
        self.__acquisition_provenance = acquisition_provenance
        self.__schema_id = schema_id
        self.__user_id = user_id
    
    def _get_creation_date_time(self):
        return self.__creation_date_time
    def _set_creation_date_time(self, value):
        if not isinstance(value, date_time):
            raise TypeError("creation_date_time must be date_time")
        self.__creation_date_time = value
    creation_date_time = property(_get_creation_date_time, _set_creation_date_time)
    
    def _get_id(self):
        return self.__id
    def _set_id(self, value):
        if not isinstance(value, str):
            raise TypeError("id must be str")
        self.__id = value
    id = property(_get_id, _set_id)
    
    def _get_acquisition_provenance(self):
        return self.__acquisition_provenance
    def _set_acquisition_provenance(self, value):
        if not isinstance(value, type):
            raise TypeError("acquisition_provenance must be type")
        self.__acquisition_provenance = value
    acquisition_provenance = property(_get_acquisition_provenance, _set_acquisition_provenance)
    
    def _get_schema_id(self):
        return self.__schema_id
    def _set_schema_id(self, value):
        if not isinstance(value, schema_id):
            raise TypeError("schema_id must be schema_id")
        self.__schema_id = value
    schema_id = property(_get_schema_id, _set_schema_id)
    
    def _get_user_id(self):
        return self.__user_id
    def _set_user_id(self, value):
        if not isinstance(value, str):
            raise TypeError("user_id must be str")
        self.__user_id = value
    user_id = property(_get_user_id, _set_user_id)
    
    def as_dict(self):
        d = dict()
        if self.__creation_date_time is not None:
            d['creation_date_time'] = self.__creation_date_time.as_dict() if hasattr(self.__creation_date_time, 'as_dict') else self.__creation_date_time
        if self.__id is not None:
            d['id'] = self.__id.as_dict() if hasattr(self.__id, 'as_dict') else self.__id
        if self.__acquisition_provenance is not None:
            d['acquisition_provenance'] = self.__acquisition_provenance.as_dict() if hasattr(self.__acquisition_provenance, 'as_dict') else self.__acquisition_provenance
        if self.__schema_id is not None:
            d['schema_id'] = self.__schema_id.as_dict() if hasattr(self.__schema_id, 'as_dict') else self.__schema_id
        if self.__user_id is not None:
            d['user_id'] = self.__user_id.as_dict() if hasattr(self.__user_id, 'as_dict') else self.__user_id
        return d


# ****************** example usage ************************

data ='{"header":{"id":"243c773b-8936-407e-9c23-270d0ea49cc4","creation_date_time":"2015-09-10T12:43:39.138-06:00","acquisition_MedicationDispense":{"source_name":"Jawbone UP API","modality":"sensed","source_updated_date_time":"2015-09-10T18:43:39Z"},"schema_id":{"namespace":"omh","name":"step_count","version":"1.0"},"user_id":"306a1202-410d-11e8-842f-0ed5f89f718b"},"body":{"effective_time_frame":{"time_interval":{"start_date_time":"2015-08-06T05:11:09-07:00","end_date_time":"2015-08-06T23:00:36-06:00"}},"step_count":7939}}'
data2 = '{"id":"243c773b-8936-407e-9c23-270d0ea49cc4","creation_date_time":"2015-09-10T12:43:39.138-06:00","acquisition_MedicationDispense":{"source_name":"Jawbone UP API","modality":"sensed","source_updated_date_time":"2015-09-10T18:43:39Z"},"schema_id":{"namespace":"omh","name":"step_count","version":"1.0"},"user_id":"306a1202-410d-11e8-842f-0ed5f89f718b"}'

data_dict = json.loads(data)
t = OmhHeader()
t.id = "123"
t.schema_id.name='step_count'
print(t.__dict__)



# header_json = json.dumps(header.as_dict(), indent= 3)
# print(header_json)

# *************************************