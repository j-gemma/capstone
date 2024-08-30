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

pyke_engine = u.assert_facts(synth, num_inputs, pyke_engine)
pyke_engine.get_kb('synthesizer').dump_specific_facts()

# print(processed_synth)
# u.print_connections(processed_synth)
#pyke_engine = u.assert_control_inputs(num_inputs, pyke_engine)
#pyke_engine = u.assert_gene_types(synth, num_inputs, pyke_engine)
#pyke_engine = u.assert_connections(processed_synth, pyke_engine)

#pyke_engine.get_kb('synthesizer').dump_specific_facts()

pyke_engine.activate('synth')
#with pyke_engine.prove_goal('synthesizer.output_type($module, $type)') as gen:
#  for vars, plan in gen:
#    print(vars['module'], vars['type'])
#

#with pyke_engine.prove_goal('synth.input_type($module, $input_index, $type, $connected)') as gen:
#  for vars, plan in gen:
#    print('Module {} input {} has type {}, connected to module {}'.format(vars['module'], vars['input_index'], vars['type'], vars['connected']))

#with pyke_engine.prove_goal('synth.input_types_connections($module, $type1, $connection1, $type2, $connection2)') as gen:
#  for vars, plan in gen:
#    print('Module {} input 1 type {}, connected to module {}, input 2 type {}, connected to module {}'.format(vars['module'], vars['type1'], vars['connection1'], vars['type2'], vars['connection2']))

#with pyke_engine.prove_goal('synth.pd_object($index, $object, $output_type)') as gen:
#  for vars, plan in gen:
#    print('Module {} is pd object type {} with output type {}'.format(vars['index'], vars['object'], vars['output_type']))

#with pyke_engine.prove_goal('synth.complete_module3($index, $type1, $connected_module1, $type2, $connected_module2, $type3, $connected_module3, $pd_object, $gene_type, $output_type)') as gen:
#  for vars, plan in gen:
#    print('Module {} input 1 has type {} from module {}, input 2 has type {} from module {}, input 3 has type {} from module {}.  Module {} pd object {} based on inputs and gene type {}. Module {} output type {}.'.format(vars['index'], vars['type1'], vars['connected_module1'], vars['type2'], vars['connected_module2'], vars['type3'], vars['connected_module3'], vars['pd_object'], vars['gene_type'], vars['output_type']))
#for i in range(len(synth)):
  #goal1 = 'synth.complete_module2({}, $type1, $connected_module1, $type2, $connected_module2, $pd_object, $gene_type, $output_type)'.format(i)

#with pyke_engine.prove_goal('synth.complete_module2($index, $type1, $connected_module1, $type2, $connected_module2, $pd_object, $gene_type, $output_type)') as gen:
#  for vars, plan in gen:
#    print(len(vars)) 
#print('Module {} input 1 has type {} from module {}, input 2 has type {} from module {}, Module {} pd object {} based on inputs and gene type {}, with output type {}.'.format(vars['index'], vars['type1'], vars['connected_module1'], vars['type2'], vars['connected_module2'], vars['index'], vars['pd_object'], vars['gene_type'], vars['output_type']))


with pyke_engine.prove_goal('synth.complete_module2($index, $type1, $connected_module1, $type2, $connected_module2, $pd_object, $gene_type, $output_type)') as gen:
  for vars, plan in gen:
    print('Module {} input 1 has type {} from module {}, input 2 has type {} from module {}, Module {} pd object {} based on inputs and gene type {}, with output type {}.'.format(vars['index'], vars['type1'], vars['connected_module1'], vars['type2'], vars['connected_module2'], vars['index'], vars['pd_object'], vars['gene_type'], vars['output_type']))

#with pyke_engine.prove_goal('synth.pd_object($index, $pd_object, $output_type)') as gen:
#  for vars, plan in gen:
#    print(str(vars['index']) + ': ' + vars['pd_object'] + ', ' + vars['output_type'])



