def tang(): 
    import pygame
    from sys import exit
    from math import tan
    x, y = 0.1,0
    pygame.init()
    screen = pygame.display.set_mode((700,400))
    pygame.display.set_caption("Game")
    clock = pygame.time.Clock()

    surface =pygame.Surface((5,5))
    surface.fill("red")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(surface,(x,y))
        x = x+1
        y = tan(x/30)*20+200
        pygame.display.update()
        clock.tick(60)