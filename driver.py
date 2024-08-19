# driver.py
# want to know the module and signal type of the last module in the graph

from deap import base, creator, tools
from pyke import krb_traceback, knowledge_engine
import random
import utils as u

pyke_engine = knowledge_engine.engine(__file__)

# Example usage:
synth = [[0], [0], [0], [5, 1, 4, 6, 295], [9, 2, 10, 5, 14773], [0, 2, 9, 7, 14300], [3, 5, 6, 1, 9520], [7, 9, 3, 3, 4108], [4, 3, 2, 4, 15775], [1]]
num_inputs = 3

processed_synth = u.process_synth(synth)
# print(processed_synth)
# u.print_connections(processed_synth)
pyke_engine = u.assert_control_inputs(num_inputs, pyke_engine)
pyke_engine = u.assert_gene_types(synth, num_inputs, pyke_engine)
pyke_engine = u.assert_connections(processed_synth, pyke_engine)



#pyke_engine.get_kb('synthesizer').dump_specific_facts()

pyke_engine.activate('synth')
with pyke_engine.prove_goal('synthesizer.output_type($module, $type)') as gen:
  for vars, plan in gen:
    print(vars['module'], vars['type'])

with pyke_engine.prove_goal('synth.input_type($module, $input_index, $type)') as gen:
  for vars, plan in gen:
    print('Module {} input {} has type {}'.format(vars['module'], vars['input_index'], vars['type']))

with pyke_engine.prove_goal('synth.input_types($module, $type1, $type2)') as gen:
  for vars, plan in gen:
    print('Module {} has output type {}'.format(vars['module'], vars['type1']))

with pyke_engine.prove_goal('synth.pd_object($index, $object, $output_type)') as gen:
  for vars, plan in gen:
    print('Module {} is pd object type {} with output type {}'.format(vars['index'], vars['object'], vars['output_type']))

pyke_engine.get_kb('synthesizer').dump_specific_facts()

