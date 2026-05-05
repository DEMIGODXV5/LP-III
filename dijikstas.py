import heapq

def dijkstra(graph, start):
    # Step 1: Initialize distances
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    min_heap = [(0, start)]  # (distance, node)

    while min_heap:
        current_dist, node = heapq.heappop(min_heap)

        # Skip if we already found a better path
        if current_dist > dist[node]:
            continue

        # Step 2: Explore neighbors
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight

            # Step 3: Relaxation
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    return dist


# Graph
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 7), ('C', 3)]
}

result = dijkstra(graph, 'A')

print("Shortest distances from A:")
for node in result:
    print(node, ":", result[node])