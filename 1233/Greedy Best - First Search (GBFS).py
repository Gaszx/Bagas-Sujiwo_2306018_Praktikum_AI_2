import heapq

def gbfs(graph, start, goal, heuristic):
    pq = [(heuristic[start], start, [start])]
    visited = set()
    
    while pq:
        h, node, path = heapq.heappop(pq)
        print("Kunjungi:", node, "dengan heuristik:", h)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor, path + [neighbor]))
    return None

graph = {
    'Garut': ['Bandung', 'Tasikmalaya'],
    'Bandung': ['Jakarta', 'Yogyakarta'],
    'Tasikmalaya': ['Yogyakarta'],
    'Jakarta': ['Surabaya'],
    'Yogyakarta': ['Surabaya', 'Denpasar'],
    'Surabaya': ['Bali'],
    'Denpasar': ['Bali'],
    'Bali': []
}

# perkiraan jarak ke Bali skala relatif
heuristic = {
    'Garut': 7,
    'Bandung': 6,
    'Tasikmalaya': 6,
    'Jakarta': 5,
    'Yogyakarta': 4,
    'Surabaya': 3,
    'Denpasar': 1,
    'Bali': 0
}

start_node = 'Garut'
goal_node = 'Bali'

result = gbfs(graph, start_node, goal_node, heuristic)
if result:
    print("\nJalur dari", start_node, "ke", goal_node, ":", " -> ".join(result))
else:
    print("\nTidak ditemukan jalur dari", start_node, "ke", goal_node)
