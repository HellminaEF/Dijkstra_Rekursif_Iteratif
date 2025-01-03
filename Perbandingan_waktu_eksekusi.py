import heapq
import time

def dijkstra_iterative(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            return list(reversed(path)), distances[end]

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return None, float('inf')

def dijkstra_recursive(graph, start, end, distances=None, previous_nodes=None, visited=None):
    if distances is None:
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
    if previous_nodes is None:
        previous_nodes = {node: None for node in graph}
    if visited is None:
        visited = set()

    if start == end:
        path = []
        while start is not None:
            path.append(start)
            start = previous_nodes[start]
        return list(reversed(path)), distances[end]

    visited.add(start)

    for neighbor, weight in graph[start]:
        if neighbor not in visited:
            new_distance = distances[start] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = start

    unvisited = {node: distances[node] for node in graph if node not in visited}
    if not unvisited:
        return None, float('inf')

    next_node = min(unvisited, key=unvisited.get)
    return dijkstra_recursive(graph, next_node, end, distances, previous_nodes, visited)

graph = {
    'Children of Echoes': [('Flower-Feather Clan', 50), ('Scions of the Canopy', 45)],
    'Scions of the Canopy': [('Flower-Feather Clan', 40), ('Children of Echoes', 45), ('People of the Springs', 15)],
    'People of the Springs': [('Masters of the Night Wind', 35), ('Scions of the Canopy', 15)],
    'Masters of the Night Wind': [('Flower-Feather Clan', 10), ('People of the Springs', 35)],
    'Flower-Feather Clan': [('Masters of the Night Wind', 10), ('Children of Echoes', 50), ('Scions of the Canopy', 40)]
}

def main():
    print("Wilayah Tersedia:")
    for node in graph.keys():
        print(node)

    # Input start node
    while True:
        start_node = input("\nMasukkan start node: ")
        if start_node in graph:
            break
        print("Node tidak valid. Silakan coba lagi.")

    # Input end node
    while True:
        end_node = input("Masukkan end node: ")
        if end_node in graph:
            break
        print("Node tidak valid. Silakan coba lagi.")

    # Jalankan Iteratif
    start_time = time.time()
    path_iterative, distance_iterative = dijkstra_iterative(graph, start_node, end_node)
    time_iterative = time.time() - start_time

    print(f"\n==== Dijkstra Algorithm (Iterative) ====")
    print(f"Dimulai: {start_node}")
    print(f"Tujuan: {end_node}")
    print(f"Jalur Terpendek: {' -> '.join(path_iterative)}")
    print(f"Jarak Total: {distance_iterative}")
    print(f"Waktu Eksekusi: {time_iterative:.6f} detik")

    # Jalankan Rekursif
    start_time = time.time()
    path_recursive, distance_recursive = dijkstra_recursive(graph, start_node, end_node)
    time_recursive = time.time() - start_time

    print(f"\n==== Dijkstra Algorithm (Recursive) ====")
    print(f"Dimulai: {start_node}")
    print(f"Tujuan: {end_node}")
    print(f"Jalur Terpendek: {' -> '.join(path_recursive)}")
    print(f"Jarak Total: {distance_recursive}")
    print(f"Waktu Eksekusi: {time_recursive:.6f} detik")

if __name__ == "__main__":
    main()