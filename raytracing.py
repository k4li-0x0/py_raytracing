import pygame
from pygame import gfxdraw
from settings import *
from somemath import *
from Objects import *


def trace(screen):
    O = camera.center
    Camera.matrix = rotMatrix(*degToRad(Camera.rotation))
    for x in range(-WIDTH // 2, WIDTH // 2):
        for y in range(-HEIGHT // 2, HEIGHT // 2):
            D = toViewport((x, y))
            D = rotateCam(D)
            color = TraceRay(O, D, 1, inf)
            xc, yc = coord((x, y))
            gfxdraw.pixel(screen, xc, yc, normalizeRGB(color))
            pygame.display.flip()

def TraceRay(O, D, t_min, t_max):
    close_sphere, close_t = ClosestIntersection(O, D, t_min, t_max)
    if close_sphere == None:
        return BACKGROUND_COLOR
    P = sumPV(O, multi(close_t, D))
    N = subDot(P, close_sphere.center)
    N = multi((1 / sqrt(dot(N, N))), N)
    return multi(ComputeLighting(P, N, antiV(D), close_sphere.specular), close_sphere.color)

def ClosestIntersection(O, D, t_min, t_max):
    close_t = inf
    close_sphere = None
    for obj in SCENE.objects:
        if type(obj) == Sphere:
            t1, t2 = IntersectRaySphere(O, D, obj)
            if (t_min < t1 < t_max) and t1 < close_t:
                close_t = t1
                close_sphere = obj
            if (t_min < t2 < t_max) and t2 < close_t:
                close_t = t2
                close_sphere = obj
    return close_sphere, close_t
    
def ReflectRay(R, N):
    return subDot(2 * multi(dot(R, N), N), R)

def IntersectRaySphere(O, D, sphere):
    C = sphere.center
    r = sphere.radius
    OC = subDot(O, C)
    
    k1 = dot(D, D)
    k2 = 2 * dot(OC, D)
    k3 = dot(OC, OC) - r * r
    
    discriminant = k2 * k2 - 4 * k1 * k3
    if discriminant < 0:
        return inf, inf
    t1 = (-k2 + sqrt(discriminant)) / (2*k1)
    t2 = (-k2 - sqrt(discriminant)) / (2*k1)
    return t1, t2

def ComputeLighting(P, N, V, s):
    i = 0.0
    for light in filter(lambda x: type(x) == Light, SCENE):
        if light.type == "ambient":
            i += light.intensity
        else:
            if light.type == "point":
                L = subDot(light.pos, P)
                t_max = 1
            else:
                L = light.dir
                t_max = inf

            shadow_sphere, shadow_t = ClosestIntersection(P, L, 0.001, t_max)
            if shadow_sphere != None:
                continue
            
            n_dot_l = dot(N, L)
            if n_dot_l > 0:
                i += light.intensity * n_dot_l / (sqrt(dot(N, N)) * sqrt(dot(L, L)))
            if s != -1:
                R = subDot(multi(2 * dot(N, L), N), L)
                r_dot_v = dot(R, V)
                if r_dot_v > 0:
                    i += light.intensity * (r_dot_v / (sqrt(dot(R, R)) * sqrt(dot(V, V)))) ** s
    return i
            
