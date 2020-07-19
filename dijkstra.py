import heapq

def main():

    data = []
    with open('dijkstraData.txt') as file:
        for line in file.readlines():
            data.append(line)

    G = {}
    V = []
    for i in range(len(data)):
        weighted_edges = data[i].split()
        heads = int(weighted_edges.pop(0))
        V.append(heads)
        edges_dict = {}
        for j in weighted_edges:
            tails, weight = j.split(",")
            edges_dict[int(tails)] = int(weight)
        G[heads] = edges_dict

    dijkstra(G,V)
    
    result = calculate_distances(G, 1)
    tmp = []
    for key in [7,37,59,82,99,115,133,165,188,197]:
        tmp.append(result[key])
    print(tmp)



# heap implementation
# reference from: https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. 
        # We only process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances



# WORKING, non heap implementation
def dijkstra(G, V):

    X = [V[0]] # vertices processed so far
    A = {} # computed shortest path distances
    A[V[0]] = 0

    while X != V:
        scores = []
        data_v = []
        data_w = []
        # check that v is in X (heads amongst processed vertices)
        for v in X:
            for w in G[v].keys():
                # check that w is in V-X (tails amongst unprocessed vertices)
                if w not in X:
                    # computes dijkstra's greedy score
                    data_v.append(v)
                    data_w.append(w)
                    greedy_score = A[v] + G[v][w]
                    scores.append(greedy_score)
    
        w_min = data_w[scores.index(min(scores))]
        X.append(w_min)
        A[w_min] = min(scores)
        X.sort()

    tmp = []
    for key in [7,37,59,82,99,115,133,165,188,197]:
        tmp.append(A[key])
    print(tmp)


if __name__ == "__main__":
    main()