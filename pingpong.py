from pygame import *

width = 800
haight = 600

map_x = 0
map_y = 0

window = display.set_mode((width,height))
display.set_caption("Game Halicopter")
backround = image.load("map.png")
backround = transform.scale(backround, (1800,1200))
window.blit(backround,(map_x,map_y))

clock = time.Clock()
FPS = 60

game_process = True
while game_process:
    for e in event.get():
        if e .type == QUIT:
            game_process = False
        if e.type == KEYDOWN:
            if e.KEY == k_RIGHT:
                if map_x > width - 1800:
                    map_x -= 5
            if e.KEY =- K_LEFT:
                if map_x < 0:
                    map_x = 5
