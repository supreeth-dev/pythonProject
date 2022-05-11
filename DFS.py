adj_list = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["B","F"],
    "D":[],
    "E":["F"],
    "F":[]
}
colors = {}
parent = {}
travel_time = {}
dfs_travel_output =[]

for node in adj_list.keys():
    colors[node] = "W"
    parent[node] = None
    travel_time[node] = [-1,-1]
print(colors)
print(parent)
print(travel_time)

time = 0
def dfs_util(u):
    global time
    colors[u] = "G"
    travel_time[u][0] = time
    dfs_travel_output.append(u)
    for v in adj_list[u]:
        if(colors[v] == "W"):
            parent[v]= u
            dfs_util(v)
        colors[u] = "B"
        travel_time[u][1] = time
        time = time +1

dfs_util("A")
print(dfs_travel_output)
print(parent)
