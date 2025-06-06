# Taken from https://github.com/google-research/bert modeling.py
import collections
import re
from inline import itest


def get_assignment_map_from_checkpoint(tvars, init_checkpoint):
    """Compute the union of the current variables and checkpoint variables."""
    assignment_map = {}
    initialized_variable_names = {}

    name_to_variable = collections.OrderedDict()
    for var in tvars:
        name = var.name
        # statement under test
        m = re.match("^(.*):\\d+$", name)
        # inline test
        itest().given(name, "a:0").check_eq(m.group(1), "a")
        # a failing inline test
        # itest().given(name, "a:0").check_eq(m.group(1), "aaa")
        if m is not None:
            name = m.group(1)
        name_to_variable[name] = var

    init_vars = tf.train.list_variables(init_checkpoint)

    assignment_map = collections.OrderedDict()
    for x in init_vars:
        (name, var) = (x[0], x[1])
        if name not in name_to_variable:
            continue
        assignment_map[name] = name
        initialized_variable_names[name] = 1
        initialized_variable_names[name + ":0"] = 1

    return (assignment_map, initialized_variable_names)
