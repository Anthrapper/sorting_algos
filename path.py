import pandas as pd

class MetrolLines:
    def __init__(self,src,station,code,cost,dst,num):
        self.src = src
        self.station=station
        self.dst = dst
        self.cost = cost
        self.code=code
        self.num=num

class Routes :

    def __init__(self, num_nodes,edgelist ) :
        self.num_nodes = num_nodes
        self.edgelist  = edgelist
        self.parent    = []
        self.rank      = []
        self.mst       = []

    def checkParent (self, node) :
        if node != self.parent[node] :
            self.parent[node] = self.checkParent(self.parent[node])
        return self.parent[node]


    def get_routes (self) :

        self.edgelist.sort(key = lambda MetroLines: MetroLines.cost)
        self.parent = [None] * self.num_nodes
        self.rank   = [None] * self.num_nodes

        for n in range(self.num_nodes) :
            self.parent[n] = n 
            self.rank[n] = 0  

        for edge in self.edgelist :
            root1 = self.checkParent(edge.src)
            root2 = self.checkParent(edge.num)

            if root1 != root2 :
               self.mst.append(edge)
               if self.rank[root1] < self.rank[root2] :
                  self.parent[root1] = root2
                  self.rank[root2] += 1
               else :
                  self.parent[root2] = root1
                  self.rank[root1] += 1

        print("\n New Metro Routes:\n")
        cost = 0
        for edge in self.mst :
            print(edge.station + " -- " + edge.dst)
            cost += edge.cost
        print("\nMinimum Cost : " +str(cost)+' Cr')


def get_data():
    file = pd.read_table("paths.csv", sep=',')
    zipp = zip(file['Source'],file['Station'], file['Code'], file['Cost'],file['Destination'],file['Num'])
    cells = [MetrolLines(x[0], x[1], x[2], x[3],x[4],x[5]) for x in zipp]
    num_nodes=len(set([x for x in file['Destination']]+[ y for y in file['Station']]))
    return cells,num_nodes

if __name__ == "__main__" :
    myList,num_nodes=get_data()
    g1 = Routes(num_nodes, myList)
    g1.get_routes()