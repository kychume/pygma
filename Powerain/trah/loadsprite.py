import os
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("OK")

image = pygame.transform.scale2x(pygame.image.load("sprites/slime_explode.png"))
x = 0
y = 0
surface = pygame.Surface((74,74),pygame.SRCALPHA,32)

clock = pygame.time.Clock()

run = True
time = 0
while run:
    t = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    time += 1
    if time > 10:
        x = (x + 1) % 8 
        time = 0
        
    rect = pygame.Rect(x * 74,y, 74,74)
    surface.fill((200,0,0))
    
    
    surface.blit(image, (0, 0),rect)
    
    screen.blit(surface, (0,10))
    pygame.display.update()