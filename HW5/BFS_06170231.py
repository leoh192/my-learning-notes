from collections import defaultdict 
  

class Graph:
 
    def __init__(self): 
        self.graph = defaultdict(list) 


    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s):        
        queue=[]
        queue.append(s)
        not_visited=set()  
        not_visited.add(s)
        visited=[]
        
        while len(queue)!=0:
            vertex=queue.pop(0)  
            vertex_next=self.graph[vertex]  
            
            for i in vertex_next:
                if i not in not_visited: 
                    queue.append(i)
                    not_visited.add(i)  
            visited.append(vertex)  
            
        return visited
    
    def DFS(self, s):
        stack=[]
        stack.append(s)
        not_visited=set()
        not_visited.add(s)
        visited=[]

        while len(stack)!=0:
            vertex=stack.pop()  
            vertex_next=self.graph[vertex]
            
            for i in vertex_next:
                if i not in not_visited:
                    stack.append(i)
                    not_visited.add(i)
            visited.append(vertex)
            
        return visited

