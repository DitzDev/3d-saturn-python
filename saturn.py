# Di buat oleh DitzDev
# Folow my medsos:
# TikTok: @ditz.ofc
# YouTube: @DitzOfc	

from vpython import *
import random

scene = canvas(title="Planet Saturnus",
              width=1920, height=1080,
              background=color.black)
              
for i in range(1000):  # 1000 bintang nih kalau ngeleg kurangin aja
    x = random.uniform(-50, 50)
    y = random.uniform(-50, 50)
    z = random.uniform(-50, 50)
    sphere(pos=vector(x, y, z),
           radius=0.05,
           color=color.white,
           emissive=True)

distant_light(direction=vector(1, 0, 0), color=color.white)

saturn = sphere(pos=vector(0, 0, 0),
               radius=1,
               texture=textures.wood,
               make_trail=False)

ring_outer = ring(pos=vector(0, 0, 0),
                 axis=vector(0, 1, 0),
                 radius=2.5,
                 thickness=0.1,
                 color=color.orange)

ring_middle = ring(pos=vector(0, 0, 0),
                  axis=vector(0, 1, 0),
                  radius=2.2,
                  thickness=0.1,
                  color=vector(0.8, 0.6, 0.4))

ring_inner = ring(pos=vector(0, 0, 0),
                 axis=vector(0, 1, 0),
                 radius=1.8,
                 thickness=0.1,
                 color=vector(0.9, 0.7, 0.5))
# Atur Posisi kamera nya
scene.camera.pos = vector(4, 3, 4)
scene.camera.axis = -scene.camera.pos

# Animasi rotasi
dt = 0.01
while True:
    rate(100)
    
    saturn.rotate(angle=dt, axis=vector(0, 1, 0))
    
    ring_outer.rotate(angle=dt, axis=vector(0, 1, 0))
    ring_middle.rotate(angle=dt, axis=vector(0, 1, 0))
    ring_inner.rotate(angle=dt, axis=vector(0, 1, 0))