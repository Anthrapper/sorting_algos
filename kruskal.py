from lines import MetrolLines
import pandas as pd


class MetroRoutes:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_route(self, u, v, w,uname,vname):
        self.graph.append([u, v, w,uname,vname])

    def find_route(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_route(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find_route(parent, x)
        yroot = self.find_route(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w,s,d = self.graph[i]
            i = i + 1
            x = self.find_route(parent, u)
            y = self.find_route(parent, v)
            if x != y:
                e = e + 1
                result.append(MetrolLines(u,s,w,d,v))
                self.union(parent, rank, x, y)
        total_cost=0
        print("\nMinimum Cost Routes :\n")
        for x in result:
            print(f"{x.station} --- {x.destination}  ({x.cost} cr)")
            total_cost=x.cost+total_cost
        print(f"\nTotal Cost : {total_cost} Cr" )
def get_data():
    file = pd.read_table("paths.csv", sep=',')
    zipp = zip(file['Src'],file['Station'], file['Cost'],file['Destination'],file['Dst'])
    cells = [MetrolLines(x[0], x[1], x[2], x[3],x[4]) for x in zipp]
    num_nodes=len(set([x for x in file['Destination']]+[ y for y in file['Station']]))
    print("\nPossible Metro Routes: \n")
    for x in cells:
        print(x)
    return cells,num_nodes

if __name__ == "__main__" :
    myList,num_nodes=get_data()
    my_routes = MetroRoutes(num_nodes)
    for i in myList:
        my_routes.add_route(i.src,i.num,i.cost,i.station,i.destination)
    my_routes.kruskal_mst()
