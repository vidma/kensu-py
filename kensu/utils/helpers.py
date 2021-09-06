import re
from hashlib import sha1


def stacktrace_without_error():
    try:
        raise Exception("no error, just marking stack trace for debugging")
    except Exception:
        import traceback
        traceback.print_stack()


def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


def to_hash_key(o):
    return sha1(str(o).encode()).hexdigest()


def eventually_report_in_mem(o):
    from kensu.utils.kensu_provider import KensuProvider
    kensu = KensuProvider().instance()
    if kensu.report_in_mem:
        o._report()
    return o


def get_absolute_path(path):
    import os
    for prefix in ["abfss", "/abfss", "dbfs", "/dbfs"]:
        if path.startswith(prefix):
            path = path.replace(prefix, '')
            prefix = prefix.replace('/', '')
            return prefix + ':' + path
    return 'file:' + str(os.path.abspath(path))


def maybe_report(o, report):
    from kensu.utils.kensu_provider import KensuProvider
    dam = KensuProvider().instance()
    if report:
        o._report()
    return o


def extract_ksu_ds_schema(kensu, orig_variable, report=False, register_orig_data=False):
    ds = kensu.extractors.extract_data_source(orig_variable, kensu.default_physical_location_ref, logical_naming=kensu.logical_naming)
    schema = kensu.extractors.extract_schema(ds, orig_variable)
    maybe_report(ds, report=report)
    maybe_report(schema, report=report)
    if register_orig_data:
        kensu.real_schema_df[schema.to_guid()] = orig_variable
    return ds, schema


def flatten(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            new_key = new_key + '[]'
            for i in v:
                items.extend(flatten(i, new_key, sep=sep).items())
        else:
            items.append((new_key, type(v).__name__))
    return dict(items)