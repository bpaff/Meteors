
import pygame 

class ScreeenObject:
    
    def __init__(self,gameScreen,imgStr):
        #super()
        self.gameScreen = gameScreen
        self.img = pygame.image.load(imgStr)
        self.rect = self.img.get_rect()
        
        #rect.left = game.width/2
        #rect.top = game.height/2
        self.rect.left = 0
        self.rect.top = 0
        
    def draw(self):
        self.gameScreen.blit(self.img, self.rect)