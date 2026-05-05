import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]   # (cost, node)

    total_cost = 0
    mst = []

    while min_heap:
        cost, node = heapq.heappop(min_heap)

        if node not in visited:
            visited.add(node)
            total_cost += cost
            mst.append((node, cost))

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor))

    return mst, total_cost


# Graph
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
    'E': [('C', 10), ('D', 2), ('F', 3)],
    'F': [('D', 6), ('E', 3)]
}

mst, cost = prim(graph, 'A')

print("MST:", mst)
print("Total Cost:", cost)