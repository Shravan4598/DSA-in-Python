class GraphAdjacencyMatrix:
    def __init__(self,num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [None] * num_vertices
        self.adj_matrix = [ [0] * num_vertices for row in range(num_vertices)]
    
    def add_vertex(self,index,label):
        if( index >=0 and index <self.num_vertices):
            self.vertices[index] = label
        else:
            print("Index OOB")

    def add_edge(self,source,destination,weight=1):
        if 0 <= source < self.num_vertices and 0<= destination <self.num_vertices:
            self.adj_matrix[source][destination] = weight
            self.adj_matrix[destination][source] = weight # Undirected Graph
    
    def display(self):

        for index ,label in enumerate(self.vertices):
            if label !=None:
                print(f"Vertex Index : {index}, label :{label} ")
        
        for row in self.adj_matrix:
            print(row)

    
    def dfs(self):
        dfs_result = []
        visited = [False] * self.num_vertices
        for vertex in range(self.num_vertices):
            if(visited[vertex] == False):
                print("Calling for a component")
                self.dfs_recursive(vertex,dfs_result,visited)
    
    def dfs_recursive(self,vertex,dfs_result,visited):
        print(vertex)
        dfs_result.append(vertex)
        visited[vertex] = True

        for neighbor in range(self.num_vertices):
            if(vertex == neighbor):
                continue
            
            if(self.adj_matrix[vertex][neighbor] == 1):
                if(visited[neighbor]== False):
                    self.dfs_recursive(neighbor,dfs_result,visited)
        


graph = GraphAdjacencyMatrix(7)
graph.add_vertex(0,'A')
graph.add_vertex(1,'B')
graph.add_vertex(2,'C')
graph.add_vertex(3,'D')
graph.add_vertex(4,'E')
graph.add_vertex(5,'F')
graph.add_vertex(6,'F')

graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2,3)
graph.add_edge(3,4)
graph.add_edge(2,4)
# graph.add_edge(0,5)
graph.add_edge(5,6)

graph.dfs()

