# What if 2 nodes have the same value? Should I operate on them by memory address instead of value?
# Add case for unconnected node

class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.edges = []

class Graph(object):
    def __init__(self):
        self.vertices = {}

    def addVertex(self, label):
        if label not in self.vertices:
            self.vertices[label] = Vertex(label)
        else:
            print('Error: Vertex %s already exists' % label)

    def addEdge(self, vertex1, vertex2):
        if vertex2 not in self.vertices.get(vertex1).edges:
            self.vertices.get(vertex1).edges.append(vertex2)
            self.vertices.get(vertex2).edges.append(vertex1)
        else:
            print('Error: Edge %s-%s already exists' % (vertex1, vertex2))

    def DFS(self, StartVertex):
        stack = []
        visited = []
        stack.append(StartVertex)
        while len(stack) > 0:
            u = stack.pop()
            if u not in visited:
                visited.append(u)
                for e in g.vertices.get(u).edges:
                    stack.append(e)
        f = open('DFS Result.txt', 'w')
        f.write(str(visited))
        f.close()
        return visited

    def BFS(self, StartVertex):
        queue = []
        visited = []
        queue.append(StartVertex)
        while len(queue) > 0:
            u = queue.pop(0)
            if u not in visited:
                visited.append(u)
                for e in g.vertices.get(u).edges:
                    queue.append(e)
        f = open('BFS Result.txt', 'w')
        f.write(str(visited))
        f.close()
        return visited

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


    g.addEdge('A', 'S')
    g.addEdge('S', 'G')
    g.addEdge('S', 'C')
    g.addEdge('G', 'F')
    g.addEdge('G', 'H')
    g.addEdge('H', 'E')
    g.addEdge('A', 'B')
    g.addEdge('C', 'F')
    g.addEdge('C', 'E')
    g.addEdge('C', 'D')

    print('DFS: ', g.DFS('A'))
    print('BFS: ', g.BFS('A'))
    print('Vertices:', g.vertices)
    print('A edges: ', g.vertices.get('A').edges)
    print('B edges: ',g.vertices.get('B').edges)