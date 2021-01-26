import pygame
from sys import exit
from PIL import Image
from settings import *

def getEvents(screen, trace):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    retrace(screen, trace)
                    return True
                if event.key == pygame.K_F12:
                    saveimg(image)

def saveimg(image):
    path = os.getenv("USERPROFILE") + "\\Pictures\\pytracer\\"
    if os.path.isdir(path):
        dirs = list()
        for i in os.listdir(path):
            current = i[:i.rfind(".")]
            if i[i.rfind(".") + 1:] == "png" and\
                current.isdigit():
                dirs.append(int(current))
        dirs.sort()
        image.save(path + f"{dirs[-1] + 1}.png")
    else:
        os.makedirs(path)
        image.save(path + "1.png")

def retrace(screen, trace):
    screen.fill(BACKGROUND_COLOR)
    trace(screen)
    pygame.display.flip()
