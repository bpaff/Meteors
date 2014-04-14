'''
Created on Apr 13, 2014

@author: Steven
'''
import pygame
import Game


if __name__ == "__main__":
    pygame.init()
    gameinit=Game.Game()
    gameinit.width,gameinit.height=800,600
    screen=pygame.display.set_mode((gameinit.width,gameinit.height))
    gameinit.spawn()