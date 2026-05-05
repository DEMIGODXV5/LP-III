print("hello")
def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited) # recursve call


# Adjacency list representation of graph
graph = {
    0: [1, 2], # means Node 0 is connected to node 1 and node 2
    1: [0, 3],
    2: [0],
    3: [1]
}
print(graph)

visited = set()
start_node = int( input("enter the starting node: "))

print("DFS Traversal:")
dfs(graph, start_node, visited)


"""def create_graph():
	n=int(input("enter the no of vertices: "))
	e=int(input("enter the no of edges: "))
	graph={i:[] for i in range(n)}
	print("enter edges (u v): ")
	for _ in range(e):
		u,v=map(int , input().split())
		graph[u].append(v)
		graph[v].append(u)
	return graph

def dfs(graph , node , visited):
	visited.add(node)
	print(node,end=" ")

	for neighbour in graph[node]:
		if neighbour not in visited:
			dfs(graph , neighbour , visited)

graph=create_graph()

start=int(input("enter the starting node: "))
visited=set()

print("DFS Traversal: ")
dfs(graph , start , visited)	
"""


