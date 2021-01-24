import pygame


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


class dText(pygame.font.Font):
    def __init__(self, screen, font, size, pos, valueType=int, value=0, onUpdate=None):
        super().__init__(font, size)
        self.screen = screen
        self.pos = pos
        self.value = valueType(value)
        self.onUpdate = onUpdate

    def draw(self):
        text = self.render(str(self.value), True, self.pos)

