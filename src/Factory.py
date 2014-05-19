import Asteroid
import Ship
#from MeteorGame import game

game = None
def MakeScreenObject(objName, id=None):
    #print "make object"
    #return 
    if objName == "AsteroidObject":
        return Asteroid.AsteroidObject(game,id)
    if objName == "ShipObject":
        return Ship.ShipObject(game,id)
    
