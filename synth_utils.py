#synth_utils.py

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
#   print(node_data)
    processed_node_data = [i]
    for address in node_data:
      if address <= i:
        processed_node_data.append(i - address)  # Replace with actual index
      else:
        processed_node_data.append(address % 3)  # Handle out-of-bounds
    processed_synth.append(processed_node_data)

  return processed_synth

def print_connections(processed_synth):
  for item in processed_synth:
    curr = item[0]
    print('Node {} input 1 connected to node {} output\n'.format(curr, item[1]))
    print('Node {} input 2 connected to node {} output\n'.format(curr, item[2]))
    print('Node {} input 3 connected to node {} output\n'.format(curr, item[3]))

def pyke_connections(processed_synth, pyke_engine):
  for item in processed_synth:
    pyke_engine.assert_('synth', 'connected', (item[1], item[2], item[3]))

  return pyke_engine
