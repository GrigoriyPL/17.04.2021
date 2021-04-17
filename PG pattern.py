import pygame

pygame.init()
W, H = 500, 500
SIZE = (W, H)
sc = pygame.display.set_mode(SIZE)
fps = pygame.time.Clock()

running = True

while running:
    for  i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
    sc.fill((0,0,0))

    
    fps.tick(60)
    pygame.display.update()

    