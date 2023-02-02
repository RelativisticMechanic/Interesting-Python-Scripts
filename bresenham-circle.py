import pygame as pg

screen_surface = None
clock = None

def bresenham_circle(x0, y0, r):
    
def draw():
    bresenham_circle(300, 400, 100)

def main():
    pg.init()
    global screen_surface, clock
    screen_surface = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    running = True
    while running:
        for event in pg.event.get():
            if(event.type == pg.QUIT):
                running = False
        screen_surface.fill((0,0,0))
        draw()
        pg.display.flip()
        clock.tick(60) 
    pg.quit()

if __name__ == "__main__":
    main()