def getMinScore(products_nodes, products_from, products_to):

  import collections    
  map = collections.defaultdict(set)
  for i in range(len(products_from)):
      map[products_from[i]].add(products_to[i])
      map[products_to[i]].add(products_from[i])

  MinSum = float('inf')

  for i in range(len(products_from)):
      for node in products_from:
          if node in map[products_from[i]] and node in map[products_to[i]]:
              productSum = len(map[products_from[i]]) + len(map[products_to[i]]) + len(map[node]) - 6
              MinSum = min(productSum, MinSum)

  return MinSum if MinSum < float('inf') else -1
