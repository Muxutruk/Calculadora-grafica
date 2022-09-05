
import pygame
from sys import exit


from Tang import tang
from Exponencial import expo
from cubica import cubo
from Escaler import escalera
from seno import seno
from Parabola import cuadrado
from Potencianegativa import potNegativa
from Rand import rand

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((700,400))
font = pygame.font.Font("bahnschrift.ttf", 20)
text = font.render("1 = Tan(x), 2 = Log(x), 3 = Rand(x), 4 = x^3, 5 = Escalera, 6 = Sin(x), 7 = x^2", True, "white")
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tang()
            elif event.key == pygame.K_2:
                expo()
            elif event.key == pygame.K_3:
                rand()
            elif event.key == pygame.K_4:
                cubo()
            elif event.key == pygame.K_5:
                escalera()
            elif event.key == pygame.K_6:
                seno()
            elif event.key == pygame.K_7:
                cuadrado()
            elif event.key == pygame.K_8:
                potNegativa()
            
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(text,(0,0))

    pygame.display.update()