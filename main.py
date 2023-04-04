import sys
from collections import deque, defaultdict

graph = defaultdict(dict)
visited = {}
maxflow = 0
INF = 99999

def createEdge(wherefrom, whereto, capacity):
    graph[wherefrom][whereto] = capacity

createEdge('S', 'A', 10)
createEdge('S', 'C', 10)
createEdge('A', 'C', 2)
createEdge('A', 'D', 8)
createEdge('A', 'B', 4)
createEdge('B', 'T', 10)
createEdge('C', 'D', 9)
createEdge('D', 'T', 10)
createEdge('D', 'B', 6)


src = 'S'
sink = 'T'
graph[sink] = {}

allnodes = []
for i in graph:
    allnodes.append(i)
    for j in graph[i]:
        allnodes.append(j)

allnodes = list(set(allnodes))

for i in allnodes:
    if i not in graph:
        graph[i] = {}
    for a in graph:
        if i not in graph[a]:
            graph[a][i] = 0

print(graph)





def bfs(parent):
    visited = {}
    for i in graph:
        visited[i] = False

    queue = deque()
    queue.append(src)
    visited[src] = True
    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if not visited[i] and graph[node][i] > 0:
                queue.append(i)
                visited[i] = True
                parent[i] = node
    return True if visited[sink] else False


def ff():
    parent = {}
    for i in graph:
        parent[i] = -1

    maxflow = 0

    while bfs(parent):
        pathflow = INF
        s = sink
        while s != src:
            pathflow = min(pathflow, graph[parent[s]][s])
            s = parent[s]
        maxflow += pathflow
        v = sink

        while v != src:
            u = parent[v]
            graph[u][v] -= pathflow
            graph[v][u] += pathflow
            v = u

        if pathflow == 0:
            break

    print(maxflow)


ff()