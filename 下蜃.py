#下蜃
from vpython import *
import math


scene = canvas(background=vec(0.8, 0.8, 0.8), width=1200, height=300, center = vec(700,0,0), fov = 0.004)
floor = box(pos = vector(500, 0, 0), color = color.yellow, size = vec(500, 0.1, 0.1))

arrow(pos=vector(0, 0, 0), axis=vector(0, 30, 0), shaftwidth = 1, color = color.green)
for i in range(15):
    n = 1.01
    angle = pi/2-(i+1)*pi/100
    angle2 = pi/2+(i+1)*pi/100
    bounce = 0
    bounce2 = 1
    ray = sphere (pos=vec(0, 30, 0), color = color.blue, radius = 0.01, make_trail=True)
    ray.v = vector (sin(angle), -cos(angle), 0)
    dt = 0.002
    t = 0
    while True:
        rate(50000000)
        t += 1
        ray.pos = ray.pos + ray.v*dt
        if ray.pos.x > 300:
                break
        if angle < pi/2 and bounce == 0:
            if abs(n/(n-0.000001)*sin(angle)) < 1:
                angle = asin(n/(n-0.000001)*sin(angle))
                ray.v = vector (sin(angle), -cos(angle), 0)
            else:
                ray.v = vector (sin(angle), cos(angle), 0)
                bounce = 1
        if bounce == 1 :
            angle = asin(n/(n+0.000001)*sin(angle))
            ray.v = vector (sin(angle), cos(angle), 0)
    
    vision = sphere (pos= ray.pos, color = color.red, radius = 0.01, make_trail=True)
    if bounce ==0:
        vision.v = vector (-sin(angle), cos(angle), 0)
    else:
        vision.v = vector (-sin(angle), -cos(angle), 0)
    while True:
        rate(5000000)
        vision.pos = vision.pos + vision.v*dt
    
        if vision.pos.y < 0:
            print(vision.pos.x)
            break
        
    while True:
        rate(5000000)
        vision.pos = vision.pos + vision.v*dt
        
        if vision.pos.x < -250:
            break
        
    ray2 = sphere (pos=vec(0, 0, 0), color = color.black, radius = 0.01, make_trail=True)
    ray2.v = vector (sin(angle2), -cos(angle2), 0)
    dt = 0.002
    t = 0
    while True:
        rate(50000000)
        t += 1
        ray2.pos = ray2.pos + ray2.v*dt
        if ray2.pos.x > 300:
            break
            '''
        if angle2 < pi/2 and bounce2 == 0:
            if abs(n/(n-0.000001)*sin(angle2)) < 1:
                angle2 = asin(n/(n-0.000001)*sin(angle2))
                ray2.v = vector (sin(angle2), -cos(angle2), 0)
            else:
                ray2.v = vector (sin(angle2), cos(angle2), 0)
                bounce2 = 1
                '''
        if bounce2 == 1 :
            angle2 = asin(n/(n+0.000001)*sin(angle2))
            ray2.v = vector (sin(angle2), cos(angle2), 0)
    
    vision2 = sphere (pos= ray2.pos, color = color.green, radius = 0.01, make_trail=True)
    if bounce2 ==0:
        vision2.v = vector (-sin(angle2), cos(angle2), 0)
    else:
        vision2.v = vector (-sin(angle2), -cos(angle2), 0)
    while True:
        rate(5000000)
        vision2.pos = vision2.pos + vision2.v*dt
    
        if vision2.pos.y < 0:
            print(vision2.pos.x)
            break
        
    while True:
        rate(5000000)
        vision2.pos = vision2.pos + vision2.v*dt
        
        if vision2.pos.x < -50:
            break
