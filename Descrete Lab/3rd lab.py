def color_nodes(graph):
  # Order nodes in descending degree
  nodes = sorted(list(graph.keys()), key=lambda x: len(graph[x]), reverse=True)
  color_map = {}

  for node in nodes:
    available_colors = [True] * len(nodes)
    for neighbor in graph[node]:
      if neighbor in color_map:
        color = color_map[neighbor]
        available_colors[color] = False
    for color, available in enumerate(available_colors):
      if available:
        color_map[node] = color
        break

  return color_map


if __name__ == '__main__':
  graph = {
    'a': list('bcd'),
    'b': list('ac'),
    'c': list('abdef'),
    'd': list('ace'),
    'e': list('cdf'),
    'f': list('ce')
  }
  print(color_nodes(graph))
  # {'c': 0, 'a': 1, 'd': 2, 'e': 1, 'b': 2, 'f': 2}