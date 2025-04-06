import pygame
import os
def load_image(dir):
    images = [i for i in os.listdir(dir)]
    sprites = {}
    i = 1
    for image in images:
        sp = []
        hell = "hell"+str(i)
        i +=1
        img = pygame.transform.scale2x(pygame.image.load(os.path.join(dir,image)))
        for im in range(4):
            surface = pygame.Surface((32,32), pygame.SRCALPHA,32)
            rect = pygame.Rect(im * 32, 0, 32,32)
            surface.blit(img,(0,0), rect)
            sp.append(surface)
        sprites[hell] = sp
        
    return sprites
  
    

    
class Character:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.width = 74
        self.height = 74
        self.current = 0
        self.mood = "hell1"
        self.load = load_image("sprites")
        self.time = 0
    
    def update(self, screen):
        self.time += 1
        surface = self.load[self.mood][self.current]
        
        if self.time > 20:
            self.current = (self.current + 1) % 4
            self.time = 0
        print(self.current)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:self.mood = "hell1"
        if keys[pygame.K_s]:self.mood = "hell2"
       
        
        screen.blit(surface,(self.x,self.y))
        
    