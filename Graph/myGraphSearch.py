def dfs(graph, root=None):
    order = []
    visited = []
    def dfs_util(graph, root, visited):
        visited.append(root)
        order.append(root)
        for neighbour in graph[root]:
            if neighbour not in visited:
                dfs_util(graph, neighbour, visited)

    for node in graph:
        if node not in visited:
            dfs_util(graph, node, visited)

    return order


if __name__ == "__main__":
    Graph = {'A': ['C', 'D'],  # 构建树
             'B': ['A', 'E'],
             'C': ['D', 'F'],
             'D': ['B', 'E', 'G'],
             'E': [],
             'F': ['D', 'G'],
             'G': ['E']}

    order = dfs(Graph)
    print(order)