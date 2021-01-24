from settings import *
from numpy import sin, cos, pi
import json

inf = 10 ** 15

def tile(P):
    return ((P[0] - WIDTH // 2), -(P[1] - HEIGHT // 2))

def coord(P):
    return ((P[0] + WIDTH // 2), -P[1] + HEIGHT // 2)

def antiV(V):
    return (-V[0], -V[1], -V[2])

def toViewport(P):
    return (P[0] * (viewport_size / WIDTH), P[1] * (viewport_size / HEIGHT), Z_PROJECTION)

def subDot(P1, P2):
    return (P1[0] - P2[0], P1[1] - P2[1], P1[2] - P2[2])

def dot(P1, P2):
    return P1[0] * P2[0] + P1[1] * P2[1] + P1[2] * P2[2]

def multi(t, P):
    return (t * P[0], t * P[1], t * P[2])

def sumPV(P, V):
    return (P[0] + V[0], P[1] + V[1], P[2] + V[2])

def rotMatrix(z, y, x):
    return ((cos(y), sin(y) * sin(z), -sin(y) * cos(z)),
            (sin(x) * sin(y), cos(x) * cos(z) - sin(x) * cos(y) * sin(z), cos(x) * sin(z) + sin(x) * cos(y) * cos(z)),
            (cos(x) * sin(y), -sin(x) * cos(z) - cos(x) * cos(y) * sin(z), -sin(x) * sin(z) + cos(x) * cos(y) * cos(z))
            )

def degToRad(rot):
    x, y, z = rot
    x *= pi / 180
    y *= pi / 180
    z *= pi / 180
    return x, y, z

def rotateCam(pos):
    rot = camera.matrix
    res = [0] * 3
    for i in range(3):
        for j in range(3):
            res[i] += pos[j] * rot[i][j]
    return tuple(res)

def normalizeRGB(RGB):
    RGB = list(RGB)
    for i in range(3):
        if RGB[i] > 255:
            RGB[i] = 255
    return tuple(RGB)   

def loadScene(path):
    with open(path) as f:
        data = json.load(f)
    print(data)

def sqrt(x):
    return x ** (1/2)
    
