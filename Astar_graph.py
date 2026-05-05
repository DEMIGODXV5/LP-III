import heapq

def a_star(graph, start, goal, h):
    open_list = [(0, start)]   # (f, node)
    g = {start: 0}             # cost from start
    parent = {start: None}     # to reconstruct path

    while open_list:
        f, node = heapq.heappop(open_list)

        # Goal check
        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]

        # Explore neighbors
        for neigh, cost in graph[node]:
            new_g = g[node] + cost

            if neigh not in g or new_g < g[neigh]:
                g[neigh] = new_g
                f = new_g + h[neigh]
                heapq.heappush(open_list, (f, neigh))
                parent[neigh] = node

    return None


# Graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}

# Heuristic values
h = {
    'A': 3,
    'B': 1,
    'C': 1,
    'D': 0
}

# Call function (FIXED)
result = a_star(graph, 'A', 'D', h)

print("Shortest Path:", result)