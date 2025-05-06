
d ={ 'A': [('B',1)] , 'B' : [('A',1)]}


for vertex,neighbour in d.items():
    print(f"{vertex} : {neighbour}")

adj_matrix = [ [0] * 5 for row in range(5)]

l1 = ['A','B',None]

for i,j in enumerate(l1):
    print(i,j)