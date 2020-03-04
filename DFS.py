from collections import defaultdict

class Graph():

    #first constructor for setting up the values inside the class
    def __init__(self):
        self.graph = defaultdict(list)
        self.f = []
        self.d = []

    #great let us define some edges
    def addEdge(self,u,v):
        self.graph[u].append(v)
    #great now set up a method for initializing the dfs
    def DFS(self,u):
        #great now create an array which will be visited
        n = max(self.graph.keys())+1
        color = [0] * (n)
        pie = [None]*(n)
        self.f = [None]*(n)
        self.d = [None]*n
        time = 0
        # check if all the nodes are visited if are not visited
        for i in color:
            if i == 0:
                #lDFS
                self.DFSUTIL(u,color,pie,time)

    def DFSUTIL(self,u,color,pie,time):
        color[u] = 1
        time = time+1
        self.d[u]=time

        print(u)
        for edges in self.graph[u]:
            if color[edges] == 0:
                pie[edges] = u
                self.DFSUTIL(edges,color,pie,time)
        color[u]=2
        self.f[u]= time+1


g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,5)
g.addEdge(5,4)
print("Following is DFS from (starting from vertex 0)")
g.DFS(0)
print(g.d)
print(g.f)