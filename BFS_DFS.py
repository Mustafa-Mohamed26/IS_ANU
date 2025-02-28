# Mustafa Mohamed Ali
# 2206019
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

def bfs(graph, start, goal):
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
        else:
            for neighbor in graph.get(node, []):
                if neighbor not in path:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

def dfs(graph, start, goal):
    stack = [[start]]
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        else:
            for neighbor in graph.get(node, []):
                if neighbor not in path:  # Avoid cycles
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)

if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'E'
    bfs_path = bfs(graph, start_node, goal_node)
    dfs_path = dfs(graph, start_node, goal_node)

    print("BFS path from A to E:", bfs_path)
    print("DFS path from A to E:", dfs_path)