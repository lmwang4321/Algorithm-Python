class solution:
    def isBipartite(self, G):
        src = list(G.keys())[0]
        colorarr = {}
        colorarr[src] = True
        queue = []
        queue.append(src)
        visited = [src]
        while queue:
            u = queue.pop()
            for n in G[u]:
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
                    colorarr[n] = ~colorarr[u]

        return visited

if __name__ == "__main__":
    Graph = {'A': ['B', 'C', 'D'],
             'B': ['A', 'E', 'G'],
             'C': ['A', 'F'],
             'D': ['A', 'F', 'G'],
             'E': ['B', 'D'],
             'F': ['C', 'D'],
             'G': ['B', 'D']}

    s = solution()
    vis = s.isBipartite(Graph)