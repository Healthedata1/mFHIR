from dataclasses import dataclass, fields
from typing import Optional, List, Any, get_type_hints, Union, Mapping


@dataclass
class ElementProperty:
    name: str  # Python name of the element
    json_name: str  # Oiginal JSON name -- may be different if keyword collision
    type: type  # Core element type
    is_list: bool  # True if maximum > 1
    of_many: Optional[str]  # If present, base name of <item>[x] ("item" in this case)
    not_optional: bool  # True if minimum is > 0


def is_union(typ: type) -> bool:
    return getattr(typ, '__origin__', None) is Union


def is_list(typ: type) -> bool:
    if is_union(typ):
        typ = [t for t in typ.__args__ if t is not type(None)][0]
    return getattr(typ, '__origin__', None) is list


def base_type(typ: type) -> type:
    """ Return the inner type for type, removing Union, List, and the like """
    if is_union(typ):
        # Union -- the base is the first non-null type
        return base_type([t for t in typ.__args__ if t is not type(None)][0])
    if is_list(typ):
        # Typing var, return the first argument
        return base_type(typ.__args__[0])
    return typ


def all_types(typ: type, seen: Optional[List[type]] = None) -> Mapping[str, Any]:
    """ Return the complete set of type hints for type typ.  type hints are the annotations with the forward refs
    resolved

    :param typ: Type to return name/type list for
    :param seen: List of types already examined
    :return: map of attribute name to corresponding type
    """

    # The following import is required for the get_type_hints call below
    from .extension import Extension

    rval = {}
    if seen is None:
        seen = {object}
    seen.add(typ)
    for t in typ.mro():
        if t not in seen:
            rval.update(all_types(t, seen))
    rval.update(get_type_hints(typ, localns=locals()))
    return rval


def elementProperties(instance: "FHIRAbstractBase") -> List[ElementProperty]:
    """ Return an ElementProperty entry for every type in instance
    """
    grounded_types = all_types(type(instance))       # This resolves forward references
    rval = []
    from .fhirreference import FHIRReference
    from .backboneelement import BackboneElement
    from .extension import Extension
    if type(instance) is FHIRReference:
        # identifier: Optional[Identifier] = None
        from .identifier import Identifier
        rval.append(
            ElementProperty(name='identifier', json_name='identifier', type=Identifier, is_list=False,
                            of_many=None, not_optional=False))
    elif type(instance) is BackboneElement:
        # modifierExtension: Optional[List[Extension]] = None
        rval.append(
            ElementProperty(name='modifierExtension', json_name='modifierExtension', type=Extension, is_list=True,
                            of_many=None, not_optional=False))

    for f in fields(instance):
        name = f.name
        origin = grounded_types[name]
        typ = base_type(origin)
        if is_union(origin):
            not_optional = type(None) not in origin.__args__
        else:
            not_optional = True
        rval.append(ElementProperty(name, f.metadata.get('orig_name', name), typ, is_list(origin),
                                    f.metadata.get('one_of_many', None), not_optional))
    return rval
