import heapq

graph = {
    '5': {'3': 1, '7': 3},
    '3': {'2': 1, '4': 1},
    '7': {'8': 2},
    '2': {},
    '4': {'8': 1},
    '8': {}
}

def heuristic(n):
    H = {
        '5': 6,
        '3': 5,
        '7': 2,
        '2': 4,
        '4': 3,
        '8': 0
    }

    return H[n]

def a_star(graph, start, goal):
    frontier = [(0, start)]
    visited = set()
    parent = {start: None}
    g_score = {start: 0}

    while frontier:
        (f, current) = heapq.heappop(frontier)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return list(reversed(path))

        visited.add(current)

        for neighbour in graph[current]:
            if neighbour not in visited:
                new_g_score = g_score[current] + graph[current][neighbour]

                if neighbour not in g_score or new_g_score < g_score[neighbour]:
                    g_score[neighbour] = new_g_score
                    f_score = new_g_score + heuristic(neighbour)
                    heapq.heappush(frontier, (f_score, neighbour))
                    parent[neighbour] = current

    return None

print(a_star(graph, '5', '8'))
