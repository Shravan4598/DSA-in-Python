class GraphAdjacencyList:
    def __init__(self):
        self.V = []
        self.adj_list = {}
    
    def add_vertex(self,vertex):
        if(vertex not in self.V):
            self.V.append(vertex)
            self.adj_list[vertex] = []
        else:
            print(f"Vertex {vertex} already exists")
        
    def add_edges(self,source,destination,weight=1):
            if source in self.V and destination in self.V:
                self.adj_list[source].append((destination,weight))
                self.adj_list[destination].append((source,weight)) # Assuming Undirected Graph
            else:
                 print("One or both vertices not found.")
        
    def display(self):
        # for vertex in self.V:
        #       print(f"Vertex -> {vertex}")
        
        for vertex, neighbour in self.adj_list.items():
                print(f"{vertex} : {neighbour}")


graph = GraphAdjacencyList()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

graph.add_edges('A','B')
graph.add_edges('A','D')
graph.add_edges('B','D')
graph.add_edges('B','C')

graph.display()

