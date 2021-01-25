import pygame
import settings

class Scene:
    def __init__(self, *args):
        self.objects = list(args)

    def add(self, *objects):
        self.objects += list(objects)

    def remove(self, index):
        if index < len(self.objects):
            del self.objects[index]
        else:
            raise IndexError

    def __iter__(self):
        return iter(self.objects)
    
    def __str__(self):
        return str(self.objects)


class Sphere:
    def __init__(self, center, radius, color, specular, reflective):
        self.center = center
        self.radius = radius
        self.color = color
        self.specular = specular
        self.reflective = reflective

    def __str__(self):
        return f"{self.center}, {self.radius}, {self.color}"


class Light:
    def __init__(self, typeof, intensity, pos=None, dirV=None):
        self.type = typeof
        self.intensity = intensity
        self.pos = pos
        self.dir = dirV


class Camera:
    def __init__(self, center=(0, 0, 0), rotation=(0, 0, 0)):
        Camera.center = center
        Camera.rotation = rotation
        Camera.matrix = None


class LoadingSprite(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.index = 0
        self.image = settings.LOADING[self.index]
        self.rect = self.image.get_rect()

    def update(self):
        self.index = (self.index + 1) % 6
        self.image = settings.LOADING[self.index]


class Text(pygame.sprite.Sprite):
    def __init__(self, group, text, pos, size, color):
        super().__init__(group)
        self.index = 0
        font = pygame.font.Font(None, size)
        text = font.render(text, False, color)
        self.image = text
        self.rect = self.image.get_rect().move(*pos)


class Logo(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group)
        self.image = settings.LOADING[6]
        self.rect = self.image.get_rect().move(*pos)

