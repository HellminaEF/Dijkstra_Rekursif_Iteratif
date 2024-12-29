import heapq

def dijkstra_iterative(graph, start, end):
    # Inisialisasi jarak dan path
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika sudah mencapai node tujuan
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            return list(reversed(path)), distances[end]

        # Jika jarak saat ini lebih besar dari jarak yang tercatat, lewati
        if current_distance > distances[current_node]:
            continue

        # Cek tetangga
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Update jarak jika ditemukan rute yang lebih pendek
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return None, float('inf')

graph = {
    'Flower-Feather Clan': [('Masters of the Night Wind', 2), ('Children of Echoes', 6), ('Scions of the Canopy', 3)],
    'Masters of the Night Wind': [('Flower-Feather Clan', 2), ('People of the Springs', 4)],
    'Children of Echoes': [('Flower-Feather Clan', 6), ('Scions of the Canopy', 5)],
    'Scions of the Canopy': [('Flower-Feather Clan', 3), ('Children of Echoes', 5), ('People of the Springs', 1)],
    'People of the Springs': [('Masters of the Night Wind', 4), ('Scions of the Canopy', 1)]
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
    path, total_distance = dijkstra_iterative(graph, start_node, end_node)
    
    print(f"\n==== Dijkstra Algorithm (Iterative) ====")
    print(f"Dimulai: {start_node}")
    print(f"Tujuan: {end_node}")
    print(f"Jalur Terpendek: {' -> '.join(path)}")
    print(f"Jarak Total: {total_distance}")

if __name__ == "__main__":
    main()