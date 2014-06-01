import Asteroid
import Ship
import Bullet
#from MeteorGame import game

def MakeScreenObject(game, vals, id=None):
    if vals["is_alive"] == False:
        return None
    
    #print "make object"
    #return 
    obj = None
    type = vals["type"]
    if type == "AsteroidObject":
        obj = Asteroid.AsteroidObject(game,id)
    if type == "ShipObject":
        obj = Ship.ShipObject(game,id)
    if type == "BulletObject":
        obj = Bullet.BulletObject(None,game)
        
    LoadScreenObject(obj, vals)
    return obj

def LoadScreenObject(obj, vals):
    type = vals["type"]
    if type == "ShipObject":
        obj.direction = vals['direction']
        obj.lives = vals["lives"]
        obj.invis_time = vals['invis_time']
    if type == 'BulletObject':
        obj.time_life = vals['time_life']
    obj.position_x = vals["position_x"]
    obj.position_y = vals["position_y"]
    obj.speed_x = vals["speed_x"]
    obj.speed_y = vals["speed_y"]
    
    
