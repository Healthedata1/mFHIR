'''
subclass Formatter: to gracefully format None and non-existing fields

***************usage*************
fmt=PartialFormatter()
data = {'n': 3, 'k': 3.141594, 'p': {'a': '7', 'b': 8}}
print(fmt.format('{n}, {k:.2f}, {p[a]}, {p[b]}', **data))
# 3, 3.14, 7, 8
del data['k']
data['p']['b'] = None
print(fmt.format('{n}, {k:.2f}, {p[a]:.2f}, {p[b]}', **data))
# 3, ~~, !!, ~~
********************************
'''
import string

class PartialFormatter(string.Formatter):
    def __init__(self, missing='None', bad_fmt='!!'):
        self.missing, self.bad_fmt=missing, bad_fmt

    def get_field(self, field_name, args, kwargs):
        # Handle a key not found
        try:
            val=super(PartialFormatter, self).get_field(field_name, args, kwargs)
            # Python 3, 'super().get_field(field_name, args, kwargs)' works
        except (KeyError, AttributeError):
            val=None,field_name 
        return val

    def format_field(self, value, spec):
        # handle an invalid format
        if value==None: return self.missing
        try:
            return super(PartialFormatter, self).format_field(value, spec)
        except ValueError:
            if self.bad_fmt is not None: return self.bad_fmt   
            else: raise

