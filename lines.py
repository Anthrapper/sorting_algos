class MetrolLines:
    def __init__(self,src,station,cost,destination,num):
        self.src = src
        self.station=station
        self.destination = destination
        self.cost = cost
        self.num=num
    def __str__(self):
            return str.format("{}--- {} ({} cr)", self.station, self.destination,self.cost)