class CycleDetection:
    def directed(self, graph):
        white = [graph[i] for i in range(len(graph))]
        gray = []
        black = []

        def dfs(graph, root, white, gray, black):
            white.remove(root)
            gray.append(root)
            for neighbour in graph[root]:
                if neighbour in black:
                    continue
                if neighbour in gray:
                    return True
                if dfs(graph, neighbour, white, gray, black):
                    return True


        for node in graph:
            if node not in black:
                dfs(graph, node, white, gray, black)

    def undirected(self, graph):
        pass

if __name__ == "__main__":

    DiGraph = {'A': ['C', 'D'],  # 构建树
               'B': ['A', 'E'],
               'C': ['D', 'F'],
               'D': ['B', 'E', 'G'],
               'E': [],
               'F': ['D', 'G'],
               'G': ['E']}

    cd = CycleDetection()
    torf = cd.directed(DiGraph)