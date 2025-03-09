from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        node, path = queue.popleft()
        print("Kunjungi:", node)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

graph = {
    'Jakarta': ['Garut', 'Bogor'],
    'Garut': ['Bandung'],
    'Bogor': ['Depok'],
    'Bandung': ['Surabaya'],
    'Depok': [],
    'Surabaya': ['Bali'],
    'Bali': []
}

start_node = 'Garut'
goal_node = 'Bali'

result = bfs(graph, start_node, goal_node)
if result:
    print("\nJalur dari", start_node, "ke", goal_node, ":", " -> ".join(result))
else:
    print("\nTidak ditemukan jalur dari", start_node, "ke", goal_node)
