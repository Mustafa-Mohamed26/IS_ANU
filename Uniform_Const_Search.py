import heapq


def uniform_cost_search(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, [start]))

    cost_so_far = {start: 0}

    while priority_queue:
        current_cost, path = heapq.heappop(priority_queue)
        node = path[-1]

        if node == goal:
            return path

        for neighbor, cost in graph.get(node, {}).items():
            new_cost = current_cost + cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(priority_queue, (new_cost, new_path))

    return None


graph = {
    'S': {'A': 2, 'B': 3, 'D': 5},
    'A': {'C': 4},
    'B': {'D': 4},
    'C': {'D': 1, 'G': 2},
    'D': {'G': 5},

}

if __name__ == "__main__":
    start_node = 'S'
    goal_node = 'G'
    ucs_path = uniform_cost_search(graph, start_node, goal_node)

    print("UCS path from S to G:", ucs_path)