import pygame
from pygame import gfxdraw
from settings import *
from somemath import *
from raytracing import trace

def retrace():
    screen.fill(BACKGROUND_COLOR)
    trace(screen)
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    isRunning = True
    clock = pygame.time.Clock()
    retrace()
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    retrace()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
 
