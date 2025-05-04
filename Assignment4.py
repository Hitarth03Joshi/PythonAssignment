# 4. Shortest Path Finder (Using Dijkstra's Algorithm)
# You are given a weighted graph representing cities connected by roads. Each road has a distance
# (weight) associated with it. Write a Python program to determine the shortest path from a specified
# start city to a destination city using Dijkstra's Algorithm.
# Your program should:
# • Accept a graph represented by cities (nodes) and distances (weighted edges).
# • Take input for the start city and the destination city.
# • Clearly print the shortest path and the total distance.
# Example Input:
# cities = {
#  'A': {'B': 5, 'C': 10},
#  'B': {'A': 5, 'C': 3, 'D': 9},
#  'C': {'A': 10, 'B': 3, 'D': 1},
#  'D': {'B': 9, 'C': 1}
# }
# start_city = 'A'
# destination_city = 'D'
# Expected Output:
# Shortest path from

import heapq

def dijkstra(graph, start, end):
    # Priority queue: (distance, city, path)
    heap = [(0, start, [start])]
    visited = set()

    while heap:
        dist, city, path = heapq.heappop(heap)
        if city in visited:
            continue
        visited.add(city)

        if city == end:
            return path, dist

        for neighbor, weight in graph[city].items():
            if neighbor not in visited:
                heapq.heappush(heap, (dist + weight, neighbor, path + [neighbor]))

    return None, float('inf')  # No path found

# Example graph
cities = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 9},
    'C': {'A': 10, 'B': 3, 'D': 1},
    'D': {'B': 9, 'C': 1}
}

# Example usage
start_city = 'A'
destination_city = 'D'

path, total_distance = dijkstra(cities, start_city, destination_city)

if path:
    print(f"Shortest path from {start_city} to {destination_city}: {' -> '.join(path)}")
    print(f"Total distance: {total_distance}")
else:
    print("No path found between the specified cities.")
