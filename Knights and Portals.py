from collections import deque

def shortest_path_with_teleport(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    teleport_positions = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                teleport_positions.append((r, c))

    def bfs(start, end):
        queue = deque([start])
        visited = set([start])
        distance = 0

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) == end:
                    return distance
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 0:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            distance += 1

        return float('inf')

    start = (0, 0)
    end = (rows - 1, cols - 1)
    min_distance = bfs(start, end)

    for teleport in teleport_positions:
        if teleport != start and teleport != end:
            distance_via_teleport = bfs(start, teleport) + bfs(teleport, end) + 1
            min_distance = min(min_distance, distance_via_teleport)

    return min_distance if min_distance != float('inf') else -1

# Example usage
grid = [
    [0, 0, 1],
    [0, 0, 0],
    [1, 0, 0]
]
print(shortest_path_with_teleport(grid))
