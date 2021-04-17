import pygame
import random

class My_circle:
    def __init__(self, direct, x, y, rad, color=(0,0,0)): 
        self.x = x
        self.y = y
        self.color = color
        self.rad = rad
        self.direct = direct
    
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.rad) 
    def move (self,W):
        if self.direct == "right":
            self.x += 1
            if self.x > W:
                self.direct = "left"
        else:
            self.x -= 1
            if self.x < 0:
                self.direct = "right"
