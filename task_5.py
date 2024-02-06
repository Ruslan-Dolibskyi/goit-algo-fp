import uuid
import numpy as np
import matplotlib.colors as mcolors
import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def generate_gradient_colors_dynamic(order, start_color, end_color):
    n = len(order)
    start = np.array(mcolors.to_rgb(start_color))
    end = np.array(mcolors.to_rgb(end_color))
    color_map = {}
    for idx, node_val in enumerate(order):
        color_map[node_val] = mcolors.to_hex(
            start + (end - start) * idx / (n - 1))
    return color_map

# Функція для додавання кольорів до дерева
def apply_colors_to_tree(root, color_map):
    if root:
        root.color = color_map.get(root.val, "#FFFFFF")
        apply_colors_to_tree(root.left, color_map)
        apply_colors_to_tree(root.right, color_map)

# DFS алгоритм
def dfs(node, visit_order, colors, idx=0):
    if node:
        node.color = colors[idx]
        visit_order.append(node.val)
        dfs(node.left, visit_order, colors, idx + 1)
        dfs(node.right, visit_order, colors, idx + 1)

# BFS алгоритм
def bfs(root, visit_order, colors):
    queue = Queue()
    queue.put((root, 0))
    while not queue.empty():
        node, idx = queue.get()
        if node:
            node.color = colors[idx]
            visit_order.append(node.val)
            queue.put((node.left, idx + 1))
            queue.put((node.right, idx + 1))


# Створення і обхід дерева у глибину (DFS)
root_dfs = Node(0)
root_dfs.left = Node(4)
root_dfs.left.left = Node(5)
root_dfs.left.right = Node(10)
root_dfs.right = Node(1)
root_dfs.right.left = Node(3)

visit_order_dfs = []
dfs(root_dfs, visit_order_dfs, generate_gradient_colors_dynamic(
    range(6), "#00008B", "#ADD8E6"))
apply_colors_to_tree(root_dfs, generate_gradient_colors_dynamic(
    visit_order_dfs, "#00008B", "#ADD8E6"))
draw_tree(root_dfs)

# Створення і обхід дерева у ширину (BFS)
root_bfs = Node(0)
root_bfs.left = Node(4)
root_bfs.left.left = Node(5)
root_bfs.left.right = Node(10)
root_bfs.right = Node(1)
root_bfs.right.left = Node(3)

visit_order_bfs = []
bfs(root_bfs, visit_order_bfs, generate_gradient_colors_dynamic(
    range(6), "#00008B", "#ADD8E6"))
apply_colors_to_tree(root_bfs, generate_gradient_colors_dynamic(
    visit_order_bfs, "#00008B", "#ADD8E6"))
draw_tree(root_bfs)