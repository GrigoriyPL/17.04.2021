ffm = 1
import pygame
import random

pygame.init()
W, H = 500, 500
SIZE = (W, H)
sc = pygame.display.set_mode(SIZE)
fps = pygame.time.Clock()
change = 1

class Circle:
    def __init__(self, x, y, rad, color=(0,0,0)): 
        self.x = x
        self.y = y
        self.color = color
        self.rad = rad
    
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.rad) 
    def move (self,):
        global ffm
        if ffm == 1:
            self.x += 5
            if self.x > W:
                self.x = W
                ffm = -1
        elif ffm == -1:
            self.x -= 5
            if self.x < 0:
                self.x = 0
                ffm = 1

            
            

list_of_circles = []
for i in range(100):
    list_of_circles.append(Circle(10,i*5,1*i,random.choices(range(0,256),k=3)))

circle_1 = Circle(W // 2, H // 2, 25, (0,255,0))
running = True

while running:
    for  i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
    sc.fill((0,0,0))
    for i in list_of_circles:
        i.draw(sc)
        i.move()

    
    fps.tick(60)
    pygame.display.update()

    