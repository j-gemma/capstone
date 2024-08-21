#util.py

#Need: 
#  Module {} input 1 has type {} from module {}, input 2 has type {} from module {}, input 3 has type {} from module {}.  Module {} pd object {} based on inputs and gene type {}. Module {} output type {}.

def process_synth(synth):
  """Processes the synth list, replacing relative addresses with actual node indices.

  Args:
    synth: The input list representing the graph.

  Returns:
    A list of lists where relative addresses are replaced with actual node indices.
  """

  processed_synth = []
  graph_length = len(synth)

  for i in range(3, graph_length - 1):  # Skip first 3 and last elements
    node_data = synth[i][1:4]  # Extract relative addresses
#    print([i])
    processed_node_data = [i, synth[i][0]]
    for address in node_data:
      if address <= i:
        processed_node_data.append(i - address)  # Replace with actual index
      else:
        processed_node_data.append(address % 3)  # Handle out-of-bounds
    processed_synth.append(processed_node_data)

  return processed_synth

def assert_facts(synth, numInputs, pyke_engine):
  print("asserting facts about synthesizer") 

  processed_synth = []
  graph_length = len(synth)

  for i in range(3, graph_length - 1):  # Skip first 3 and last elements
    node_data = synth[i][1:4]  # Extract relative addresses
#    print([i])
    processed_node_data = [i, synth[i][0]]
    for address in node_data:
      if address <= i:
        processed_node_data.append(i - address)  # Replace with actual index
      else:
        processed_node_data.append(address % 3)  # Handle out-of-bounds
    processed_synth.append(processed_node_data)

    pyke_engine = assert_connections(processed_synth, pyke_engine)
    pyke_engine = assert_control_inputs(numInputs, pyke_engine)
    pyke_engine = assert_gene_types(synth, numInputs, pyke_engine)

  return pyke_engine


def print_connections(processed_synth):
  for item in processed_synth:
    curr = item[0]
    print('Node {} input 1 connected to node {} output\n'.format(curr, item[1]))
    print('Node {} input 2 connected to node {} output\n'.format(curr, item[2]))
    print('Node {} input 3 connected to node {} output\n'.format(curr, item[3]))


def assert_connections(processed_synth, pyke_engine):
  for item in processed_synth:
    #print(item)
    for i in range(len(item) - 2):
      curr = item[0]
      pyke_engine.assert_('synthesizer', 'connected', (curr, i + 1, item[i + 2]))
      #print('Module {} input {} connected to output of module {}'.format(curr, i + 1, item[i + 1]))

  return pyke_engine


def assert_control_inputs(num_inputs, pyke_engine):
  for i in range(num_inputs):
    pyke_engine.assert_('synthesizer', 'output_type', (i, 'c'))
    #print('Module {} has output type control'.format(i))
   
  return pyke_engine


def assert_gene_types(synth, num_inputs, pyke_engine):
  for i in range(len(synth) - num_inputs - 1):
    pyke_engine.assert_('synthesizer', 'gene_value', (i + num_inputs, synth[i + num_inputs][0]))

  return pyke_engine



