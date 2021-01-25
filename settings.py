from Objects import *
import os

WIDTH, HEIGHT = SIZE = 500, 500
viewport_size = 1
Z_PROJECTION = 1
FPS = 30
BACKGROUND_COLOR = (0, 0, 0)
LOADING = tuple(map(pygame.image.load,
                    map(os.path.abspath,
                                        [f"img/load{i}.png" for i in range(1, 7)] +
                                        [os.path.abspath("img/logo.png")])))

SCENE = Scene(
    Sphere(
            center=(0, -5, 20),
            radius=5,
            color=(255, 0, 0),
            specular=500,
            reflective=0.25
            ),
    Sphere(
            center=(-15, -5, 50),
            radius=15,
            color=(0, 255, 0),
            specular=100,
            reflective=0.25
            ),
    Sphere(
            center=(15, -5, 50),
            radius=15,
            color=(0, 0, 255),
            specular=10,
            reflective=0.25
            ),
    Sphere(
            center=(0, -500, 150),
            radius=500,
            color=(255, 255, 0),
            specular=10,
            reflective=0.25
            ),
    Light(
        typeof="ambient",
        intensity=0.2
        ),
    
    Light(
        typeof="point",
        intensity=0.6,
        pos=(0, 10, 0)
        ),
    Light(
        typeof="point",
        intensity=0.1,
        pos=(-10, 5, 5)
        ),
    Light(
        typeof="directional",
        intensity=0.4,
        dirV=(3, 4, 4)
        )
    )

camera = Camera(center=(3, 4, 7))
clock = None

