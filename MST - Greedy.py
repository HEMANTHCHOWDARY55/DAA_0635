import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    # Function to find the vertex with minimum key value
    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = None

        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v

        return min_index

    # Function to print the MST
    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    # Function to perform MST using Prim's algorithm
    def prim_mst(self):
        key = [sys.maxsize] * self.V  # Key values to pick the minimum weight edge
        parent = [None] * self.V       # Array to store constructed MST
        key[0] = 0                     # Make key 0 so that this vertex is picked as first vertex
        mst_set = [False] * self.V     # To represent set of vertices included in MST

        parent[0] = -1  # First node is always the root of MST

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            # Update key and parent for adjacent vertices of the picked vertex
            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

# Test the program
g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

print("Minimum Spanning Tree using Prim's algorithm:")
g.prim_mst()
