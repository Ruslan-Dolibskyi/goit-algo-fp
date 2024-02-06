import heapq


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, u, v, weight):
        if u not in self.nodes:
            self.nodes[u] = []
        if v not in self.nodes:
            self.nodes[v] = []
        self.nodes[u].append((v, weight))


def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Пропустити, якщо ми знайдемо більшу відстань у черзі пріоритету
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.nodes[current_node]:
            distance = current_distance + weight

            # Оновіть відстань, якщо знайдено коротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Створюємо граф
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('B', 'C', 2)
graph.add_edge('A', 'C', 4)
graph.add_edge('C', 'D', 1)
graph.add_edge('B', 'D', 3)

# Застосуємо алгоритм Дейкстри з початковою точкою 'A'
shortest_paths = dijkstra(graph, 'A')

# Виведення відстаней до кожного вузла
for node, distance in shortest_paths.items():
    print(f"Короткий шлях від 'A' до '{node}': {distance}")