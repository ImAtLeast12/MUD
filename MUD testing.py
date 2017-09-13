def regenerate2d(length,width):
    m=[]
    for x in range(length):
        m.append([0]*width)
    return m

class Player():
    def __init__(self,Map,bound):
        self.posX=3
        self.posY=2

        self.Map=Map
        self.bound=bound
        
        self.avaliableDirections=[]
        self.notAvaliableDirections=[]
        
    def getPosX(self):
        return self.posX
    def getPosY(self):
        return self.posY
    
    def getMap(self):
        return self.Map

    def getBound(self):
        for x in range(len(self.bound)):
            for y in range(len(self.bound)):
                self.bound[x][y]=self.Map[self.posX-1+x][self.posY-1+y]
        return self.bound
        
    def getDirections(self):
        self.getBound
        self.notAvaliableDirections=[]
        self.avaliableDirections=[]
        for x in range(len(self.bound)):
            for y in range(len(self.bound)):
                if(self.bound[x][y]!=0):
                    self.avaliableDirections.append(cordanates[x][y])                   
        return self.avaliableDirections
    def getStats(self):
        print("X: "+ str(self.getPosX()))
        print("Y: "+ str(self.getPosY()))
        print(self.getMap())
        print(self.getBound())
        print(self.getDirections())

length = 5
width = 5

Map = [[0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 4, 5, 6, 0],
        [0, 7, 8, 9, 0],
        [0, 0, 0, 0, 0]]

bound = regenerate2d(3,3)
player = Player(Map,bound)

cordanates = [["NW"],["N"],["NE"]],[["W"],["P"],["E"]],[["SW"],["S"],["SE"]]

player.getStats()
