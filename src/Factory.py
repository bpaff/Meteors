import Asteroid
#from MeteorGame import game

game = None
def MakeScreenObject(objName, id=None):
    #print "make object"
    #return 
    if objName == "AsteroidObject":
        return Asteroid.AsteroidObject(game,id)
    
