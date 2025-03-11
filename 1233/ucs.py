import heapq

def ucs(graph, start, goal):
    pq = [(0, start, [start])]
    visited = {}
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        print("Kunjungi:", node, "dengan biaya:", cost)
        if node == goal:
            return path, cost
        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost
        for neighbor, step_cost in graph.get(node, []):
            heapq.heappush(pq, (cost + step_cost, neighbor, path + [neighbor]))
    return None, None

# Graph berbobot dengan biaya langkah antar simpul
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

start_node = 'A'
goal_node = 'F'

path, min_cost = ucs(graph, start_node, goal_node)
if path:
    print("\nJalur terpendek dari", start_node, "ke", goal_node, ":", " -> ".join(path))
    print("Biaya minimum:", min_cost)
else:
    print("\nTidak ditemukan jalur dari", start_node, "ke", goal_node)
