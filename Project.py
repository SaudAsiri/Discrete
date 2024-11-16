import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if visited[current_node]:
            continue
        visited[current_node] = True

        for neighbor, weight in enumerate(graph[current_node]):
            if weight > 0:  # There's a connection
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def main():
    print("Welcome to Dijkstra's Algorithm!")
    n = int(input("Enter the number of nodes in the graph: "))
    print("Now, enter the adjacency matrix row by row (use 0 for no connection):")

    graph = []
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != n:
            print(f"Error: Each row must contain exactly {n} values.")
            return
        graph.append(row)

    start_node = int(input(f"Enter the starting node (0 to {n - 1}): "))
    if start_node < 0 or start_node >= n:
        print("Error: Starting node must be within the valid range.")
        return

    distances = dijkstra(graph, start_node)
    print("\nShortest distances from node", start_node, "to all other nodes:")
    for i, distance in enumerate(distances):
        print(f"Node {i}: {distance}")

if __name__ == "__main__":
    main()