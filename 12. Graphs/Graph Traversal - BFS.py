from collections import deque

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

    def bfs(self,start_vertex = 0):
        visited = [False] * self.num_vertices
        queue = deque([start_vertex])

        bfs_result = []
        visited[start_vertex] = True

        while len(queue) !=0:
            vertex = queue.popleft() 
            print(vertex)
            for neighbour in range(self.num_vertices):

                if(self.adj_matrix[vertex][neighbour]!=0):
                    if(visited[neighbour]== False):
                        queue.append(neighbour)
                        visited[neighbour] = True
    




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



graph.bfs()

