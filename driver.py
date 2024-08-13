# want to know the module and signal type of the last module in the graph

from deap import base, creator, tools
from pyke import krb_traceback, knowledge_engine
import random
import synth_utils as u

pyke_engine = knowledge_engine.engine(__file__)

# Example usage:
synth = [[0], [0], [0], [5, 1, 4, 6, 295], [9, 2, 10, 5, 14773], [0, 2, 9, 7, 14300], [3, 5, 6, 1, 9520], [7, 9, 3, 3, 4108], [4, 3, 2, 4, 15775], [1]]
processed_synth = u.process_synth(synth)
print(processed_synth)
u.print_connections(processed_synth)
#u.pyke_connections(processed_synth, pyke_engine)


pyke_engine.activate('synth')
#pyke_engine.prove_1_goal('synth.well_defined(graph, $bool)')

