from collections import defaultdict 
import sys 

class Graph(): 
    def __init__(self, vertices):        
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w]) 
     

    def minDistance(self, i, k): 
  
        min = sys.maxsize
  
        for v in range(self.V): 
            if i[v] < min and k[v] == False: 
                min = i[v] 
                min_index = v 
  
        return min_index 
  

    def Dijkstra(self, s): 
  
        i = [sys.maxsize] * self.V 
        i[s] = 0
        k = [False] * self.V 
        a = {}
  
        for cout in range(self.V): 
  
         
            u = self.minDistance(i, k) 

            k[u] = True

            for v in range(self.V): 
                if self.graph[u][v] > 0 and k[v] == False and i[v] > i[u] + self.graph[u][v]: 
                        i[v] = i[u] + self.graph[u][v] 
  
        for node in range(self.V):
            a.update( {str(node) : i[node]} )
        return a

    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot  
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
        

    def Kruskal(self): 
        a = {}
        result =[] 
        i = 0
        e = 0
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
        parent = [] ; rank = [] 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
        while e < self.V -1 : 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v)
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
        for u,v,weight in result: 
            u = str(u)
            v = str(v)
            a.update( {str(u)+"-"+str(v):weight}) 
            
        return a
 
