import fhir_templates as f
from pprint import pprint
from stringcase import titlecase
new= {}
print("|{0}|{0}|{0}|{0}|{0}|{0}|{0}|{0}|{0}|{0}|{0}|".format('--'))
for k,v in sorted(f.omh_datatype_mapping.items()):
    new_list =list(v)[0:1] + list(v)[2:]
    print(("|{k}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(k=k,*new_list)))
    
print('{')
for k,v in sorted(f.omh_datatype_mapping.items()):
    new_list = list(v)
    new_list.remove(new_list[5])
    print("'{}': {},".format(k,tuple(new_list)))

print('}')