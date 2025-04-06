import pygame
import os
import sys
from character import Character

class MainGame:
    def __init__(self):
        pygame.init()
        self.width, self.height = 1000, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        self.player = Character(10,10)
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.run()
    
    
    def run(self):
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                    break
            self.draw()
                
    def draw(self):
        self.screen.fill((0,0,0))
        self.player.update(self.screen)
        
        
        pygame.display.update()
                    
if __name__ == "__main__":
    MainGame()        