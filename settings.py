from Objects import *

WIDTH, HEIGHT = SIZE = 300, 300
viewport_size = 1;
Z_PROJECTION = 1
FPS = 30
BACKGROUND_COLOR = (0, 0, 0)

SCENE = Scene(
    Sphere(
            center=(0, 0, 20),
            radius=5,
            color=(255, 0, 0),
            specular=500,
            reflective=0.25
            ),
    Sphere(
            center=(-15, -5, 50),
            radius=15,
            color=(0, 255, 0),
            specular=200,
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
            specular=-1,
            reflective=0.25
            ),
    Light(
        typeof="ambient",
        intensity=0.2
        ),
    
    Light(
        typeof="point",
        intensity=0.4,
        pos=(0, 0, 10)
        ),
    Light(
        typeof="directional",
        intensity=0.4,
        dirV=(3, 4, 4)
        )
    )

camera = Camera()
clock = None

