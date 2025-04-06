import pygame,os


def loadsprite(dir1, character):
    direction = ["front","back","left","right"]
    sprites = {}
    path = os.path.join("assets",dir1,character)
    for type in os.listdir(path):
        for i,png in enumerate(os.listdir(os.path.join(path, type))):
            image = pygame.image.load(os.path.join(path,type,png))
            imgwidth = image.get_width()
            imgheight = image.get_height()
            
            part = ["body","full","shadow"]
            
            for y in range(int(imgheight/64)):
                imglst = []
                for x in range(int(imgwidth/64)):
                    surface = pygame.Surface((64,64), pygame.SRCALPHA,32)
                    rect = pygame.Rect(x*64,y*64,64,64)
                    surface.blit(image, (0,0), rect)
                    imglst.append(surface)
                    
                sprites[type + part[i] + direction[y]] = imglst
    return sprites
                
            
                    
            
            
            
        
class Character:
    def __init__(self,x,y,spritename):
        self.x = x
        self.y = y
        self.velX = 0
        self.velY = 0
        self.vel = 3
        self.spritename = spritename
        
        self.direction = "front"
        self.currentframe = 0
        self.mood = "Idlefullfront"
        self.loadsprite = loadsprite("playerimage",self.spritename)
        
        self.animationtime = 0
        print(self.loadsprite)
        
    def draw(self,screen):
        self.currentframe = (self.currentframe) % len(self.loadsprite[self.mood])
        self.animationtime += 1
        if self.animationtime >= 10:
            self.currentframe = (self.currentframe + 1) % len(self.loadsprite[self.mood])
            self.animationtime = 0
        screen.blit(self.loadsprite[self.mood][self.currentframe],(self.x,self.y))
        
        
class Player(Character):
    def __init__(self,x,y):
        super().__init__(x,y,"Slime1")
        self.invix, self.inviy = x,y
        
    def playermovements(self):
        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_UP]:
            self.velY, self.direction,self.mood = self.vel,"back","Walkfullback"
            self.invix += self.vel
        elif keys[pygame.K_DOWN]:
            self.velY = -self.vel
            self.direction = "front"
            self.mood = "Walkfullfront"
            self.invix += -self.vel
        else:
            self.velY = 0
            self.mood = "Idlefull"+self.direction
            
        if keys[pygame.K_LEFT]:
            self.velX = self.vel
            self.direction = "left"
            self.mood = "Walkfullleft"
            self.inviy += self.vel
        elif keys[pygame.K_RIGHT]:
            self.velX = -self.vel
            self.direction = "right"
            self.mood = "Walkfullright"
            self.inviy += -self.vel
        else:
            self.velX = 0
            self.mood = "Idlefull" + self.direction
            
            
        print(self.invix//64)
        
            
    
    