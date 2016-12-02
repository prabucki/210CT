'''
TASK OBJECTIVE:

Implement the structure for an unweighted, undirected graph G, where nodes consist of
positive integers. Also, implement a function isPath(v, w), where v and w are vertices in the
graph, to check if there is a path between the two nodes. The path found will be printed to
a text file as a sequence of integer numbers (the node values).

Using the graph structure previously implemented, implement a function isConnected(G)
to check whether or not the graph is strongly connected. The output should be simply 'yes'
or 'no'.
'''

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

    def isPath(self, StartVertex, TargetVertex):
        '''Modified Depth-First Search, that checks whether 2 nodes are connected'''
        stack = []
        visited = []
        Found = False
        stack.append(StartVertex)
        while len(stack) > 0:
            u = stack.pop()

            if u == TargetVertex:   # Target was found
                visited.append(u)
                Found = True
                break

            if u not in visited:
                visited.append(u)
                if len(g.vertices.get(u).edges) == 1: # Dead End
                    visited.pop(-1)
                for e in g.vertices.get(u).edges:
                    stack.append(e)

        # Save result
        f = open('isPath.txt', 'w')
        if Found:
            f.write(str('Path between nodes ' + str(StartVertex) + ' and ' + str(TargetVertex) + ' found: '))
            f.write(str(visited))
        else:
            f.write(str('Path between nodes ' + str(StartVertex) + ' and ' + str(TargetVertex) + ' NOT found!'))
        f.close()
        return Found

    def isConnected(self):
        ''' Checks whether graph is strongly connected by running isPath function between all nodes'''

        Connected = True
        for i in self.vertices:
            for j in self.vertices:
                if i != j:
                    Connected *= g.isPath(i, j) # If one instance of isPath returns "False", result will change to "False"
        if Connected:
            return 'YES'
        else:
            return 'NO'

if __name__ == '__main__':

    # Generate graph
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
    # g.addVertex(56) # Example of not connected graph

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

    print()
    print('-- RESULT --')
    print('isConnected:', g.isConnected())
    print('isPath(1, 5):', g.isPath(1, 5))
    print()
    print('-- OTHER TESTS --')
    print('Vertices (memory locations):', g.vertices)
    print('Vertices (labels): ', g.vertices.keys())
    print('"1" vertex edges: ', g.vertices.get(1).edges)
    print('"2" vertex edges: ',g.vertices.get(2).edges)
