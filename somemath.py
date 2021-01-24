from settings import *

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

def normalizeRGB(RGB):
    return (RGB[0] % 255, RGB[1] % 255, RGB[2] % 255)

def sqrt(x):
    return x ** (1/2)
    
