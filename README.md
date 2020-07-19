# Dijkstras shortest path algorithm

Find the shortest path between the source vertex and other vertices in a directed graph.
Each edge must have a non negative length/weights or else dijkstra's algorithm will not work.
The algorithum is a special kind Breath First Search that favours edges with smaller weights instead of choosing by random.

The algorithm is as follows:
- at the current node, compute the distances between current the node and its neighbours 
- choose the neighbouring node with the smallest distance and mark that node as visited (Dijkstra's greedy criteria)
- repeat the first two steps until all nodes are visited
