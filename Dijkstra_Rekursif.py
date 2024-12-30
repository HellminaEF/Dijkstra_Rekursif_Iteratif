import heapq

def dijkstra_recursive(graph, start, end, distances=None, previous_nodes=None, visited=None):
    # Inisialisasi pada panggilan pertama
    if distances is None:
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
    if previous_nodes is None:
        previous_nodes = {node: None for node in graph}
    if visited is None:
        visited = set()

    # Basis rekursi: mencapai node tujuan
    if start == end:
        path = []
        while start is not None:
            path.append(start)
            start = previous_nodes[start]
        return list(reversed(path)), distances[end]

    visited.add(start)

    # Proses tetangga
    for neighbor, weight in graph[start]:
        if neighbor not in visited:
            new_distance = distances[start] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = start

    # Pilih node berikutnya dengan jarak terpendek
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
        start_node = input("Masukkan start node: ")
        if start_node in graph:
            break
        print("Node tidak valid. Silakan coba lagi.")

    # Input end node
    while True:
        end_node = input("Masukkan end node: ")
        if end_node in graph:
            break
        print("Node tidak valid. Silakan coba lagi.")

    # Jalankan
    path, total_distance = dijkstra_recursive(graph, start_node, end_node)
    
    print(f"\n==== Dijkstra Algorithm (Recursive) ====")
    print(f"Dimulai: {start_node}")
    print(f"Tujuan: {end_node}")
    print(f"Jalur Terpendek: {' -> '.join(path)}")
    print(f"Jarak Total: {total_distance}")

if __name__ == "__main__":
    main()

# Anggota Kelompok:
# - Hellmina Enjelina Fitri
# - Putri Galuh Mandarizka