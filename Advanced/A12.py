# What if 2 nodes have the same value? Should I operate on them by memory address instead of value?
# Add case for unconnected node

class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.edges = [] # key: vertex label, value: edge weight
        #self.tentativeWeight = float('inf')
        self.previousVertex = None

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

    def isPath(self, StartVertex, TargetVertex): #Depth-First Search
        stack = []
        visited = []
        Found = False
        stack.append(StartVertex)
        while len(stack) > 0:
            u = stack.pop()
            if u == TargetVertex:
                visited.append(u)
                Found = True
                break
            if u not in visited:
                visited.append(u)
                #if len(g.vertices.get(u).edges) == 1:
                    #visited.pop(-1)
                for e in g.vertices.get(u).edges:
                    stack.append(e)
        f = open('isPath.txt', 'w')
        if Found:
            f.write(str('Path between nodes ' + str(StartVertex) + ' and ' + str(TargetVertex) + ' found: '))
            f.write(str(visited))
        else:
            f.write(str('Path between nodes ' + str(StartVertex) + ' and ' + str(TargetVertex) + ' NOT found!'))
        f.close()
        return Found

    def isConnected(self):
        Connected = True
        for i in self.vertices:
            for j in self.vertices:
                if i != j:
                    Connected *= g.isPath(i, j)
        if Connected:
            return 'YES'
        else:
            return 'NO'

if __name__ == '__main__':

    g = Graph()

    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addVertex(4)
    g.addVertex(5)
    g.addVertex(6)
    g.addVertex(7)
    g.addVertex(8)
    g.addVertex(9)
    g.addVertex(56) # Not Connected

    g.addEdge(1, 9)
    g.addEdge(9, 7)
    g.addEdge(9, 3)
    g.addEdge(7, 6)
    g.addEdge(7, 8)
    g.addEdge(8, 5)
    g.addEdge(1, 2)
    g.addEdge(3, 6)
    g.addEdge(3, 5)
    g.addEdge(3, 4)

    print('isPath: ', g.isPath(1, 56))
    print('Vertices:', g.vertices)
    print('1 edges: ', g.vertices.get(1).edges)
    print('2 edges: ',g.vertices.get(2).edges)
    print('isConnected: ', g.isConnected())