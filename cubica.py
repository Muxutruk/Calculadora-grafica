def cubo():
    import pygame
    from sys import exit
    from math import sin
    x, y = -350,0
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
        screen.blit(surface,(x+350,y))
        x = x+1
        y = (x*x*x)/2800+200
        pygame.display.update()
        clock.tick(60)
