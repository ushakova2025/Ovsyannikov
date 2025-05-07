import pygame as p
import sys as s
import math as m
import random as rd
p.init()
w,h=800,600
d=p.display.set_mode((w,h))
p.display.set_caption("Салют Победы")
b=(255,0,51)
f=(255,255,0)
t=(34,139,34)
g=p.font.SysFont("Arial",24)
k=p.font.SysFont("Arial",72,bold=True)
q=[]
def z(a,b,c,o):
    e=[]
    n=m.radians(18)
    for i in range(5):
        x=n+m.radians(72*i)
        l=c[0]+o*m.cos(x)
        v=c[1]+o*m.sin(x)
        e.append((l,v))
        y=x+m.radians(36)
        j=c[0]+(o/2)*m.cos(y)
        u=c[1]+(o/2)*m.sin(y)
        e.append((j,u))
    p.draw.polygon(a,b,e)
def create_firework(x,c):
    n=rd.randint(30,50)
    for _ in range(n):
        a=rd.uniform(0,2*m.pi)
        s=rd.uniform(1,5)
        v=m.cos(a)*s
        e=m.sin(a)*s
        q.append({"pos":[x,c],"vel":[v,e],"color":f,"r":rd.randint(8,12),"l":rd.randint(30,60)})
def draw_text():
    a=g.render("Нажмите пробел",1,t)
    d.blit(a,(10,10))
    c=k.render("С днём Победы!",1,t)
    e=c.get_rect(center=(w//2,h//2))
    d.blit(c,e)
clock=p.time.Clock()
running=True
while running:
    for event in p.event.get():
        if event.type==p.QUIT:
            running=False
        elif event.type==p.KEYDOWN:
            if event.key==p.K_SPACE:
                for _ in range(rd.randint(3,5)):
                    x=rd.randint(100,w-100)
                    y_coord=rd.randint(100,h-100)
                    create_firework(x,y_coord)
    for o in q[:]:
        o["l"]-=1
        if o["l"]<=0:
            q.remove(o)
            continue
        o["vel"][1]+=0.1
        o["pos"][0]+=o["vel"][0]
        o["pos"][1]+=o["vel"][1]
    d.fill(b)
    draw_text()
    for o in q:
        z(d,o["color"],(int(o["pos"][0]),int(o["pos"][1])),o["r"])
    p.display.flip()
    clock.tick(30)
p.quit()
s.exit()
