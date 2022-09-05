def seno():
    import pygame
    from sys import exit
    from math import sin
    x, y = 0,0
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
        y = sin(x/20)*200+200
        pygame.display.update()
        clock.tick(60)
