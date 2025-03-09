def dfs(graph, start, goal):
    stack = [(start, [start])]  # Stack: (node, path)
    visited = set()

    while stack:
        node, path = stack.pop()
        print("Kunjungi:", node)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
goal_node = 'F'

result = dfs(graph, start_node, goal_node)
if result:
    print("\nJalur dari", start_node, "ke", goal_node, ":", " -> ".join(result))
else:
    print("\nTidak ditemukan jalur dari", start_node, "ke", goal_node)
