import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def greedy_best_first_search(start, goal, grid):
    open_set = []
    heapq.heappush(open_set, (0, start))
    visited = set()
    came_from = {}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        visited.add(current)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and
                    grid[neighbor[0]][neighbor[1]] != 1 and neighbor not in visited):
                came_from[neighbor] = current
                heapq.heappush(open_set, (heuristic(neighbor, goal), neighbor))

    return None


grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)
path = greedy_best_first_search(start, goal, grid)

print("Path from start to goal:", path)