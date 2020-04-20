graph = {1: [2,3],
         2: [4,5],
         3: [1,6,7],
         4: [2, 8],
         5: [2, 8],
         6: [3, 7],
         7: [3, 6],
         8: [4, 5]}

def DFS(graph, root):
    visited = []
    def dfs(node):
        visited.append(node)
        for edge in graph[node]:
            if edge not in visited:
                dfs(edge)

    if root:
        dfs(root)

    for node in graph:
        if node not in visited:
            dfs(node)

    return visited

a = DFS(graph, 1)
print(a)