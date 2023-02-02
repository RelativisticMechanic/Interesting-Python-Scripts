import numpy as np
import pygame as pg
import math

pg.init()
screen_surface = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

p = np.array([[50, 60], [80, 100], [100, 450], [40, 200]])
selected_p = None


def lerp(p1, p2, t):
    return p1 + (p2 - p1)*t

def DrawBezierCurve():

    previous_point = None
    for t in np.arange(0, 1.01, 0.01):
        A = lerp(p[0], p[1], t)
        B = lerp(p[1], p[2], t)
        C = lerp(p[2], p[3], t)
        D = lerp(A, B, t)
        E = lerp(B, C, t)
        F = lerp(D, E, t)
        #print(C)
        F = (int(F[0]), int(F[1]))
        clr_1 = np.array([200, 50, 0])
        clr_2 = np.array([50, 200, 0])

        clr = t * clr_1 + (1 - t)*clr_2
        if(previous_point):
            #pg.draw.line(screen_surface, (int(clr[0]), int(clr[1]), int(clr[2])), previous_point, A, 2)
            #pg.draw.line(screen_surface, (int(clr[0]), int(clr[1]), int(clr[2])), previous_point, B, 2)
            #pg.draw.line(screen_surface, (int(clr[0]), int(clr[1]), int(clr[2])), previous_point, C, 2)
            #pg.draw.line(screen_surface, (int(clr[0]), int(clr[1]), int(clr[2])), previous_point, D, 2)
            pg.draw.aaline(screen_surface, (int(clr[0]), int(clr[1]), int(clr[2])), previous_point, F)
        previous_point = F
        
    pg.draw.circle(screen_surface, (0, 0, 0), p[0], 4, 0)
    pg.draw.circle(screen_surface, (0, 0, 0), p[1], 4, 0)
    pg.draw.circle(screen_surface, (0, 0, 0), p[2], 4, 0)
    pg.draw.circle(screen_surface, (0, 0, 0), p[3], 4, 0)


def main():
    running = True
    while running:
        for event in pg.event.get():
            if(event.type == pg.QUIT):
                running = False
            if(event.type == pg.MOUSEBUTTONDOWN):
                m_x, m_y = pg.mouse.get_pos()
                for idx, pt in enumerate(p):
                    if((pt[0] - m_x)**2 + (pt[1] - m_y)**2 < 16):
                        global selected_p
                        selected_p = idx
            elif(event.type == pg.MOUSEBUTTONUP):
                selected_p = None
            
        if(selected_p != None):
            p[selected_p] = np.array(pg.mouse.get_pos())
        
        screen_surface.fill((200,200,240))
        
        DrawBezierCurve()
        pg.display.flip()
    clock.tick(60)
main()
pg.quit()