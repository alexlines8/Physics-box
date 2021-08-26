import pygame, sys

from pygame.constants import VIDEORESIZE
pygame.font.init()
pygame.mixer.init()
from pygame import time
from pygame.draw import rect

WIN = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
pygame.display.set_caption("Science Box")
WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)
LIGHTBLACK = (15,21,30)
NAVY = (18,44,77)
FPS = 60


def drawWindow():
    width = pygame.Surface.get_width(WIN)
    height = pygame.Surface.get_height(WIN)
    WIN.fill(LIGHTBLACK)
    pygame.draw.rect(WIN, WHITE, (width/8,height/5,width / 2.5 + 2,height / 1.75 + 2))
    pygame.draw.rect(WIN, NAVY, (width/8+1,height/5+1,width / 2.5,height / 1.75))
    pygame.draw.rect(WIN, WHITE, (width/8 * 5,height/5,width / 5 +2,height / 1.75 + 2))
    pygame.draw.rect(WIN, NAVY, (width/8 * 5 +1,height/5 +1,width / 5,height / 1.75))
    pygame.display.update()

class ball():
    x = 0
    y = 0
    vel = 0
    acc = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y



def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            
            if event.type == VIDEORESIZE:
                WIN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        drawWindow()


if __name__ == "__main__":
    main()