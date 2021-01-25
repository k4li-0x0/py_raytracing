import pygame
import sys
from settings import *

def getEvents(screen, trace):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    retrace(screen, trace)
                    return True

def retrace(screen, trace):
    screen.fill(BACKGROUND_COLOR)
    trace(screen)
    pygame.display.flip()
