from queue import Queue
adj_list = {
    "A":["B","C"],
    "B":["A","C"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "H":["G","F"]
}

visited ={}
parent ={}
bfs_travel_op= []
level = {}
queue = Queue()
for node in adj_list.keys():
    parent[node] = None
    visited[node] = False
    level[node] = -1

print(visited)
s ="A"
visited[s] = True
level[s] = 0
queue.put(s)

while not queue.empty():
    u = queue.get()
    bfs_travel_op.append(u)
    #visited[u] = True
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] +1
            queue.put(v)

print(adj_list)