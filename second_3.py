ffm = 1
import pygame
import random
import my_circle

pygame.init()
W, H = 500, 500
SIZE = (W, H)
sc = pygame.display.set_mode(SIZE)
fps = pygame.time.Clock()
change = 1

# class Circle:
#     def __init__(self, direct, x, y, rad, color=(0,0,0)): 
#         self.x = x
#         self.y = y
#         self.color = color
#         self.rad = rad
#         self.direct = direct
    
#     def draw(self,screen):
#         pygame.draw.circle(screen, self.color, (self.x, self.y), self.rad) 
#     def move (self):
#         if self.direct == "right":
#             self.x += 1
#             if self.x > W:
#                 self.direct = "left"
#         else:
#             self.x -= 1
#             if self.x < 0:
#                 self.direct = "right"

            
            

list_of_circles = []
for i in range(100):
    list_of_circles.append(my_circle.My_circle('right', i*5, 1*i, 10, random.choices(range(0,256),k=3)))

circle_1 = my_circle.My_circle(W // 2, H // 2, 25, (0,255,0))
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

    
    fps.tick(200)
    pygame.display.update()

    