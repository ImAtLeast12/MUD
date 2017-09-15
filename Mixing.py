cordanates = [['NW'],['N'],['NE']],[['W'],['P'],['E']],[['SW'],['S'],['SE']]
food={ 0:['Steak','A good slab of meat.', 100],
       1:['Rice','A bowl of the finest rice.', 20] 
      }#this can be added indefinatly

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
        self.Map=   [[1,  2,  3,  4],
                     [5,  6,  7,  8],
                     [9, 10, 11, 12]]
        
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
        
        self.health = 10
        self.deathText = "It was a bitter sweet end (dramatic pause) alais."
        
    def getPosX(self):
        return self.posX
    def getPosY(self):
        return self.posY
    def getAvaliableDir(self):
        self.bound = self.Map.getBound(self.posX,self.posY)
        
        self.avaliableDirections=[]
        for x in range(len(self.bound)):
            for y in range(len(self.bound)):
                if(self.bound[x][y]!=0):
                    self.avaliableDirections.extend(cordanates[x][y])
        return self.avaliableDirections

    def getMap(self):
        return self.Map.Map

    def attacks(self,e):
        e.health -= 100

    def isAlive(self):
        return self.health > 0

    def kill(self):
        print(self.deathText)
        if self.health < 0:
            del self

m=Map() #generate a map some how
m.addPerimiter() # give the map a perimeter
p=Player(m) # give the player a copy of the map

'''for x in range(5): #Testing for 5 directions
    print('(' + str(p.posX) + ',' + str(p.posY) + ')')
    prettyPrint(p.Map.getBound(p.posX,p.posY))
    print(p.getAvaliableDir())
    Dir = input('Where would you like to go?')
    if (Dir in p.getAvaliableDir()):
        #Then find what direction they need to go
        if('N' in Dir):
            p.posX-=1
        if('S' in Dir):
            p.posX+=1
        if('W' in Dir):
            p.posY-=1
        if('E' in Dir):
            p.posY+=1
    else:
        input('You cann\'t go there')'''


attack ={0:["Test",10,3.0],
         1:["Tes2",20,3.0],
         }

import time

class Attack():
    def __init__(self,a):
        self.name   = a[0]
        self.damage = a[1]
        self.coolDownPeriod = a[2]
        self.cdpLeft= 0.0
        
    def canAttack(self):
        return time.time()-self.cdpLeft>=self.coolDownPeriod

    def attacked(self):
        self.cdpLeft=time.time()

dicAttacks={'1':Attack(attack[0]), '2':Attack(attack[1])}

class Enemmy():
    def __init__(self,a):
        self.damage = a
        self.health = 10
        self.deathText = "It was a bitter sweet end (dramatic pause) alais."

    def isAlive(self):
        return self.health > 0

    def kill(self):
        print(self.deathText)
        if self.health < 0:
            del self
    def attacks(self, p):
        p.health-=100

p = Player(m)
e = Enemmy(Attack(attack[0]))


p.attacks(e)
e.attacks(p)


if not (e.isAlive()):
    e.kill()

if not (p.isAlive()):
    p.kill()


    
while(True):        
    for i in range(len(dicAttacks)):
        x=input()
        if(x in dicAttacks):
            if(dicAttacks[x].canAttack()):
                dicAttacks[x].attacked()
                print(x + ' attacked')
            else:
                print(x + ' can\'t attack yet')
        else:
            print('invalid comand')
                
