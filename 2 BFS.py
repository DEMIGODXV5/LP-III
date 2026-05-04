from collections import deque

def bfs_recursive(queue, visited, graph):
    if not queue:
        return

    node = queue.popleft()
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)

    bfs_recursive(queue, visited, graph)


# Graph (undirected)
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

visited = set()
queue = deque()

start = int(input("Enter starting node: "))

visited.add(start)
queue.append(start)

print("BFS Traversal:")
bfs_recursive(queue, visited, graph)

"""
Enter starting node= 0 or anyhting u want

"""
