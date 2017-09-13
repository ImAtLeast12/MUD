cordanates = [["NW"],["N"],["NE"]],[["W"],["P"],["E"]],[["SW"],["S"],["SE"]]
def regenerate2d(length,width):
    m=[]
    for x in range(length):
        m.append([0]*width)
    return m

def prettyPrint(arr):
    for x in range(len(arr)):
        print(arr[x])
    print()

class Map():
    def __init__(self):
        self.Map=   [[0, 0, 0, 0, 0],
                    [0, 1, 2, 3, 0],
                    [0, 4, 5, 6, 0],
                    [0, 7, 8, 9, 0],
                    [0, 0, 0, 0, 0]]
        
    def getBound(self,px,py):
        bound=[[0,0,0],[0,0,0],[0,0,0]]
        for x in range(len(bound)):
            for y in range(len(bound)):
                bound[x][y]=self.Map[px-1+x][py-1+y]
        bound[1][1]=0 #I want bound  to ignore the players position when I get the directions avalible
        return bound
    def addPerimiter(self):
        x=len(self.Map)
        y=len(self.Map[0])
        newMap = regenerate2d(x+2,y+2)
        for x in range(len(self.Map)):
            for y in range(len(self.Map[0])):
                newMap[1+x][1+y]=self.Map[x][y]
        prettyPrint(newMap)
        self.Map = newMap          

class Player():
    def __init__(self,Map):
        self.posX=1
        self.posY=1

        self.Map=Map
        self.bound=self.Map.getBound(self.posX,self.posY)
        self.avaliableDirections=[]
        
    def getPosX(self):
        return self.posX
    def getPosY(self):
        return self.posY
    def getAvaliableDir(self):
        self.avaliableDirections=[]
        for x in range(len(self.bound)):
            for y in range(len(self.bound)):
                if(self.bound[x][y]!=0):
                    self.avaliableDirections.extend(cordanates[x][y])
        return self.avaliableDirections

    def getMap(self):
        return self.Map.Map

m=Map()
p=Player(m)

m.addPerimiter()

print("x: "+ str(p.posX))
print("y: "+ str(p.posY))
prettyPrint(p.bound)
prettyPrint(p.getMap())
print(p.getAvaliableDir())

for x in range(2):
    Dir = input('Where would you like to go?')
    if (Dir in p.getAvaliableDir()):
        print('all good')
