import pygame
from sys import exit
from pygame import gfxdraw
from settings import *
from logsaver import saveLog
from tracersystem import *
from raytracing import trace

if __name__ == "__main__":
    try:
        pygame.init()
        screen = pygame.display.set_mode(SIZE)
        logo = pygame.image.load("img/logo.ico")
        pygame.display.set_caption("Pygame Ray Tracing")
        pygame.display.set_icon(logo)
        load_group = pygame.sprite.Group()
        load = LoadingSprite(load_group)
        crText = Text(load_group, "Thanks for @PatientZero from Habr.com", (70, 5), 24, "white")
        title = Text(load_group, "Pygame Ray Tracing", (5, 70), 72, "red")
        tutor = Text(load_group, "Press R to trace/retrace image", (5, HEIGHT - 15), 24, "white")
        tutor2 = Text(load_group, "Press F12 to save image", (5, HEIGHT - 35), 24, "white")
        logo = Logo(load_group, (WIDTH / 2 - 60, HEIGHT / 2 - 60))
        isRunning = True
        clock = pygame.time.Clock()
        for i in range(120):
            traced = getEvents(screen, trace)
            if traced:
                break
            screen.fill(BACKGROUND_COLOR)
            load_group.draw(screen)
            load_group.update()
            pygame.display.flip()
            clock.tick(10)
        if not traced:
            retrace(screen, trace)
        while isRunning:
            getEvents(screen, trace)
            pygame.display.flip()
            clock.tick(FPS)
    except Exception as e:
        print(saveLog(e))
        pygame.quit()
        exit(-1)
 
