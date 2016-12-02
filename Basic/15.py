# What if 2 nodes have the same value? Should I operate on them by memory address instead of value? rergesrtertewrtwertwertwertert dfsf

class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.edges = {} # key: vertex label, value: edge weight
        self.tentativeWeight = float('inf')
        self.previousVertex = None

class Graph(object):
    def __init__(self):
        self.vertices = {}

    def addVertex(self, label):
        if label not in self.vertices:
            self.vertices[label] = Vertex(label)
        else:
            print('Error: Vertex %s already exists' % label)

    def addEdge(self, vertex1, vertex2, weight):
        if vertex2 not in self.vertices.get(vertex1).edges:
            self.vertices.get(vertex1).edges[vertex2] = weight
            self.vertices.get(vertex2).edges[vertex1] = weight
        else:
            print('Error: Edge %s-%s already exists' % (vertex1, vertex2))

    def Dijkstra(self, StartVertex, EndVertex):
        StartVertex = self.vertices[StartVertex]
        EndVertex = self.vertices[EndVertex]

        StartVertex.tentativeWeight = 0
        CurrentVertex = StartVertex
        visited = []
        while CurrentVertex != EndVertex:
            for u in CurrentVertex.edges.keys(): # for every adjacent vertex from current one
                u = self.vertices[u]
                if CurrentVertex.tentativeWeight + u.edges[CurrentVertex.label] < u.tentativeWeight:
                    u.tentativeWeight = CurrentVertex.tentativeWeight + u.edges[CurrentVertex.label]
                    u.previousVertex = CurrentVertex

            visited.append(CurrentVertex)

            minimum = float('inf')

            for i in self.vertices.values():
                if i not in visited and i.tentativeWeight < minimum:
                    CurrentVertex = i
                    minimum = i.tentativeWeight

        return CurrentVertex.tentativeWeight


if __name__ == '__main__':

    g = Graph()

    g.addVertex('A')
    g.addVertex('B')
    g.addVertex('C')
    g.addVertex('D')
    g.addVertex('E')
    g.addVertex('F')
    g.addVertex('G')
    g.addVertex('H')
    g.addVertex('S')


    g.addEdge('A', 'S', 5)
    g.addEdge('S', 'G', 1)
    g.addEdge('S', 'C', 2)
    g.addEdge('G', 'F', 10)
    g.addEdge('G', 'H', 63)
    g.addEdge('H', 'E', 0)
    g.addEdge('A', 'B', 23)
    g.addEdge('C', 'F', 1)
    g.addEdge('C', 'E', 3)
    g.addEdge('C', 'D', 3)


    print(g.Dijkstra('A', 'E'))
    print('Vertices:', g.vertices)
    print('A edges: ', g.vertices.get('A').edges)
    print('B edges: ',g.vertices.get('B').edges)