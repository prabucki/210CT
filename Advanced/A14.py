'''
TASK OBJECTIVE:

Consider the structure of an undirected weighed graph. Implement an algorithm to find its
maximum cost spanning tree. The output should be the pre-order and post-order traversal
of the tree. Describe the running time of this algorithm.
'''

class TreeNode(object):

    def __init__(self, label):
        self.label = label
        self.children = []

    def addChild(self, child, value):
        self.children.append([child, value])
        TreeNode(child)

class Tree(object):
    def __init__(self, label, child, value):
        self.nodeInsert(label, child, value) # Enter first node

    def nodeInsert(self, label, child, value):
        # find parent node
        tree = TreeNode(label)
        print(tree.label)
        tree.addChild(child, value)

    def findNode(self, label):
        if tree.label != label:
            return None

class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.edges = {} # key: vertex label, value: edge weight
        self.edgesBackup = []
        self.tentativeWeight = float('inf')
        self.previousVertex = None

class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def addVertex(self, label):
        if label not in self.vertices:
            self.vertices[label] = Vertex(label)
        else:
            print('Error: Vertex %s already exists' % label)

    def addEdge(self, vertex1, vertex2, weight):
        if vertex2 not in self.vertices.get(vertex1).edges:

            #Adds edge to sorted list of edges
            self.edges.append([weight, vertex1, vertex2])
            self.vertices.get(vertex1).edges[vertex2] = weight
            self.vertices.get(vertex2).edges[vertex1] = weight
        else:
            print('Error: Edge %s-%s already exists' % (vertex1, vertex2))

    def addCurrentEdge(self, vertex1, vertex2):
        if vertex2 not in self.vertices.get(vertex1).edgesBackup:
            self.vertices.get(vertex1).edgesBackup.append(vertex2)
            self.vertices.get(vertex2).edgesBackup.append(vertex1)
        else:
            print('Error: Edge %s-%s already exists' % (vertex1, vertex2))

    def SortEdges(self):
        alist = self.edges
        for passnum in range(len(alist)-1,0,-1):
            for i in range(passnum):
                if alist[i][0]<alist[i+1][0]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
        return alist

    def SpanningTree(self):
        # Following Kruskal Algorithm to compute maximum weight spanning tree
        if self.isConnected() == 'NO':
            print('Graph is not connected. Spanning tree cannot be created for it')
            return None
        edges = self.SortEdges()
        T = []
        vertices = []
        for i in range(len(edges)):
            if len(T) == 0:
                T.append(edges[0])
                vertices.append(edges[i][1])
                vertices.append(edges[i][2])
            else:
                if self.DetectCycle(edges[i][1], edges[i][2]) == False:
                    if edges[i][1] not in vertices:
                        vertices.append(edges[i][1])
                    if edges[i][2] not in vertices:
                        vertices.append(edges[i][2])
                    T.append(edges[i])
                    self.addCurrentEdge(edges[i][1], edges[i][2])
                else:
                    print('Cycle detected. Edge',edges[i][1], edges[i][2], 'not added.')
        print("Spanning tree created successfully")
        # Label, Child, Value
        t = Tree(T[0][1], T[0][2], T[0][0])
        print(t)
        for i in range(1, len(T)):
                t.nodeInsert(T[i][1], T[i][2], T[i][0])
        return T # [[63, 'G', 'H'], [23, 'A', 'B'], [10, 'G', 'F'], [5, 'A', 'S'], [3, 'C', 'E'], [3, 'C', 'D'], [2, 'S', 'C'], [1, 'S', 'G'], [0, 'H', 'E']]


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

    def isPath(self, StartVertex, TargetVertex):  # Depth-First Search
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
                # if len(g.vertices.get(u).edges) == 1:
                # visited.pop(-1)
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

    def DetectCycle(self, StartVertex, TargetVertex):  # Depth-First Search

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
                for e in self.vertices.get(u).edgesBackup:
                    stack.append(e)
        f = open('isPath.txt', 'w')
        if Found:
            f.write(str('Path between nodes ' + str(StartVertex) + ' and ' + str(TargetVertex) + ' found: '))
            f.write(str(visited))
        else:
            f.write(str('Path between nodes ' + str(StartVertex) + ' and ' + str(TargetVertex) + ' NOT found!'))
        f.close()
        return Found

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

    #print(g.vertices.keys())
    #print(g.Dijkstra('A', 'E'))
    #print('Vertices:', g.vertices)
    #print('A edges: ', g.vertices.get('A').edges)
    #print('B edges: ',g.vertices.get('B').edges)
    #print(g.edges[0])

    print(g.SpanningTree())