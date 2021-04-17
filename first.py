import pygame

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

    def move(self): 
        global change
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= 1
        if keys[pygame.K_s]:
            self.y += 1
        if keys[pygame.K_a]:
            self.x -= 1
        if keys[pygame.K_d]:
            self.x += 1
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        
        if change == 1:
            if keys[pygame.K_SPACE]:
                self.color = (255, 255, 255)
                change = -1
                pygame.time.delay(100) # Задержка в 5ms
        elif change == -1:
            if keys[pygame.K_SPACE]:
                self.color = (0, 255, 0)
                change = 1
                pygame.time.delay(100)
        
    # def cvet(self, color = (0,0,0)):
    #     s = 0    
    #     keys = pygame.key.get_pressed()
        
    #     if keys[pygame.K_SPACE]:
    #         s += 1
    #         if s == 1:
    #             self.color = (255, 255, 0)
    #         else:
    #             self.color = (0, 255, 0)


running = True

circle_1 = Circle(W // 2, H // 2, 25, (0,255,0))
while running:
    for  i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()

    circle_1.draw(sc)
    circle_1.move()
    # circle_1.cvet()
    
    fps.tick(60)
    pygame.display.update()

    