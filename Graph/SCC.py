def SCC(graph):
    S = []
    visited = []

    def dfs(graph, root, visited, S):
        visited.append(root)
        for neighbour in graph[root]:
            if neighbour not in visited:
                dfs(graph, neighbour, visited, S)
        S.append(root)


    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, S)
    gt = reverseGraph(graph)
    while S:
        v = S.pop()
    return S

def reverseGraph(graph):
    new_graph = {}
    for node in graph:
        for neighbour in graph[node]:
            new_graph[neighbour] = node
    return new_graph

if __name__ == "__main__":
    graph = {'0': ['2', '3'],
             '1': ['0'],
             '2': ['1'],
             '3': ['4'],
             '4': []}
    g = reverseGraph(graph)
    print(g)
