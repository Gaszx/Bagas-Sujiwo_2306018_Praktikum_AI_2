import heapq

def a_graph_search(graph, start, goal, heuristic):
    pq = [(heuristic[start], 0, start, [start])]  # (f, g, node, path)
    explored = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)
        print("Kunjungi:", node, "dengan biaya g:", g, "dan heuristik h:", heuristic[node])
        
        if node == goal:
            return path, g

        if node in explored:
            continue
        explored.add(node)

        for neighbor, step_cost in graph.get(node, []):
            if neighbor not in explored:
                heapq.heappush(pq, (g + step_cost + heuristic[neighbor], g + step_cost, neighbor, path + [neighbor]))

    return None, None

graph = {
    'Garut': [('Bandung', 2), ('Tasikmalaya', 3)],
    'Bandung': [('Jakarta', 4), ('Yogyakarta', 5)],
    'Tasikmalaya': [('Yogyakarta', 4)],
    'Jakarta': [('Surabaya', 7)],
    'Yogyakarta': [('Surabaya', 6), ('Denpasar', 3)],
    'Surabaya': [('Bali', 2)],
    'Denpasar': [('Bali', 1)],
    'Bali': []
}

heuristic = {
    'Garut': 10,
    'Bandung': 8,
    'Tasikmalaya': 7,
    'Jakarta': 6,
    'Yogyakarta': 5,
    'Surabaya': 3,
    'Denpasar': 1,
    'Bali': 0
}

start_node = 'Garut'
goal_node = 'Bali'

result, total_cost = a_graph_search(graph, start_node, goal_node, heuristic)
if result:
    print("\nJalur dari", start_node, "ke", goal_node, ":", " -> ".join(result))
    print("Total biaya jalur:", total_cost)
else:
    print("\nTidak ditemukan jalur dari", start_node, "ke", goal_node)
