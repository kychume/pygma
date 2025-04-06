import pygame
import os
import sys
from map import Map
from character import Player


pygame.init()
WIDTH, HEIGHT = 1000, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("we")


player = Player(WIDTH/2,HEIGHT/2)


def load_image(tilename):
    return pygame.transform.scale2x(pygame.image.load(os.path.join("assets",'tile', tilename)).convert_alpha())

def load_map(movex, movey):
    tileImage = {"original": load_image("tile1.png"),
                 "ok":load_image("k.png"),
                 "notok":load_image("we.png")}
    
    for mapY, row in enumerate(Map):
        for mapX, cell in enumerate(row):
            if cell == 0:
                screen.blit(tileImage["original"], ((mapX * 64) + movex, (mapY * 64 )+ movey))
            if cell == 1:
                screen.blit(tileImage["ok"], ((mapX * 64) + movex, (mapY * 64 )+ movey))
            if cell == 2:
                screen.blit(tileImage["notok"], ((mapX * 64) + movex, (mapY * 64 )+ movey))
                
def draw(movex, movey):
    screen.fill((0,0,0))
    load_map(movex, movey)
    player.playermovements()
    player.draw(screen)
    pygame.display.update()  
    

    
                  
cl = pygame.time.Clock()
running = True
movex, movey = 0,0
move = "front"
while running:
    cl.tick(60)
    ismoving = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
            break
        
    movex += player.velX
    movey += player.velY
    
        
        
    draw(movex, movey)
        
