# These are settings for the FHIR class generator.
# All paths are relative to the `fhir-parser` directory. You may want to use
# os.path.join() if the generator should work on Windows, too.

from Default.settings import *

# Base URL for where to load specification data from
specification_url = 'http://hl7.org/fhir/R4'

# In which directory to find the templates. See below for settings that start with `tpl_`: these are the template names.
tpl_base = '.'

# Sort resource attributes
sort_resources = False

# classes/resources
write_resources = True
tpl_resource_target = '../model'                   # target directory to write the generated class files to
tpl_codesystems_source = None                   # the template to use as source when writing enums for CodeSystems; can be `None`

# factory methods
write_factory = True
tpl_factory_target = '../model/fhirelementfactory.py'    # where to write the generated factory to

# unit tests
write_unittests = True
tpl_unittest_target = '../tests/model'    # target directory to write the generated unit test files to


# all these files should be copied to dirname(`tpl_resource_target_ptrn`): tuples of (path/to/file, module, array-of-class-names)
manual_profiles = [
    ('fhirabstractbase.py', 'fhirabstractbase', [
        'boolean',
        'string', 'base64Binary', 'code', 'id',
        'decimal', 'integer', 'unsignedInt', 'positiveInt',
        'uri', 'oid', 'uuid',
        'FHIRAbstractBase',
    ]),
    ('fhirabstractresource.py', 'fhirabstractresource', ['FHIRAbstractResource']),
    ('fhirreference.py', 'fhirreference', ['FHIRReference']),
    ('fhirdate.py', 'fhirdate', ['date', 'dateTime', 'instant', 'time']),
    ('fhirsearch.py', 'fhirsearch', ['FHIRSearch']),
    ('fhirelementproperty.py', 'fhirelementproperty', []),
]
