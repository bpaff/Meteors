
import pygame 

class ScreeenObject:
    
    def __init__(self,gameScreen,imgStr):
        #super()
        self.gameScreen = gameScreen
        self.img = pygame.image.load(imgStr)
        self.rect = self.img.get_rect()
        
        self.width= gameScreen.get_width()
        self.height= gameScreen.get_height()
        
        #rect.left = game.width/2
        #rect.top = game.height/2
        self.rect.left = 0
        self.rect.top = 0
        
    def draw(self):
        self.screenedge()
        self.gameScreen.blit(self.img, self.rect)
        
    def screenedge(self):
        if self.rect.left>self.width:
            self.rect.right=0
        if self.rect.top>self.height:
            self.rect.bottom=0
        if self.rect.right<0:
            self.rect.left=self.width
        if self.rect.bottom<0:
            self.rect.top=self.height