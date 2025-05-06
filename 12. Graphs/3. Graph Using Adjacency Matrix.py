# https://visualgo.net/en/graphds

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

graph = GraphAdjacencyMatrix(3)
graph.add_vertex(0,'A')
graph.add_vertex(1,'B')
graph.add_vertex(2,'C')
graph.add_vertex(3,'D')

graph.add_edge(0,1)
graph.add_edge(1,2)

graph.display()

