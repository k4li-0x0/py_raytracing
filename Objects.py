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



