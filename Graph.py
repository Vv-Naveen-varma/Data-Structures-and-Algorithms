# Implementation of Graphs(using Adjacency List)
class Graph:
    def __init__(self):
        self.noOfNodes = 0
        self.adjList = {}

    def addVertex(self,node):
        self.adjList[node] = []
        self.noOfNodes += 1
        return self.adjList
    
# In case of a Directed Graph node1 points to node2 but node2 does not point to node1
    
    # Edges are added considering an UnDirected Graph
    
    def addEdge(self, node1, node2):
        if (node1 not in self.adjList) or (node2 not in self.adjList):
            return 'Invalid Vertex'
        else:
            self.adjList[node1].append(node2)
            self.adjList[node2].append(node1)
            return self.adjList

g = Graph()
g.addVertex('0')
g.addVertex('1')
g.addVertex('2')
g.addVertex('3')
g.addVertex('4')
g.addVertex('5')
print(g.addVertex('6'))
g.addEdge('1','3')
g.addEdge('3','4')
g.addEdge('4','2')
g.addEdge('4','5')
g.addEdge('1','2')
g.addEdge('1','0')
g.addEdge('0','2')
print(g.addEdge('6','5'))
