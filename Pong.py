# Pong with Pygame

import pygame
import time
import random
import numpy as np
random.seed()

pygame.init()
size = [640,480]
sizex = size[0]
sizey = size[1]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Game")
isRunning = True

font = pygame.font.SysFont(None, 50)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

pygame.mixer.pre_init(44100,16,2,4096)
pygame.mixer.music.load('foo.mp3')
pygame.mixer.music.play(-1)

class Ball: 
    width = 30
    x = sizex/2-(width/2);
    y = sizey/2-(width/2);
    vx = 0
    vy = 0
    def __init__(self):
        self.x = sizex/2-(self.width/2);
        self.y = sizey/2-(self.width/2);
        self.vx = random.random()
        i = random.randint(0,1)
        z = [-1,1]
        self.vx = z[i]
        i = random.randint(0,1)
        z = [-1,1]
        self.vy = z[i]
    def update(self):
        # Kollision Ball==>Player 1 (a)
        if((self.x)<a.x+a.pl_width and(self.y>a.y and self.y<(a.y+a.pl_height))):
            self.vx = self.vx * (-1)
            if(self.vx>0):
                self.vx=self.vx+0.1
            else:
                self.vx=self.vx-0.1
        elif((self.x)<a.x+a.pl_width and not(self.y>a.y and self.y<(a.y+a.pl_height))):
            field.pt_p2 = field.pt_p2 + 1
            self.__init__()
        # Kollision Ball==>Player 2 (b)
        if((self.x+self.width)>b.x and(self.y>b.y and self.y<(b.y+b.pl_height))):
            self.vx = self.vx * (-1)
            if(self.vx>0):
                self.vx=self.vx+0.1
            else:
                self.vx=self.vx-0.1
        elif((self.x)>b.x+b.pl_width and not(self.y>b.y and self.y<(b.y+b.pl_height))):
            field.pt_p1 = field.pt_p1 + 1
            self.__init__()
        self.x = self.x + self.vx
        if ((self.y<0) or ((self.y+self.width)>sizey)):
            self.vy = self.vy * (-1)
        self.y = self.y + self.vy
    def show(self):
        pygame.draw.rect(screen, WHITE, [self.x, self.y,self.width, self.width])
    
class PongPlayer:
    x = 0
    y = 0
    ppl = 0
    pl_width = 30
    pl_height = 120
    
    def __init__(self, ppl):
        self.ppl = ppl
        if ppl==1:
            self.x = 0
        elif ppl==2:
            self.x = sizex-self.pl_width
        self.y = (sizey/2)-(self.pl_height/2)
    def show(self):
        pygame.draw.rect(screen, WHITE, [self.x, self.y,self.pl_width, self.pl_height])
    def checkButton(self):
        if self.ppl==1:
            key = pygame.key.get_pressed()
            if not (self.y<0):
                if key[pygame.K_w]: self.y = self.y - 1
            if not (self.y + self.pl_height > sizey):
                if key[pygame.K_s]: self.y = self.y + 1
        if self.ppl==2:
            key = pygame.key.get_pressed()
            if not (self.y<0):
                if key[pygame.K_UP]: self.y = self.y - 1
            if not (self.y + self.pl_height > sizey):
                if key[pygame.K_DOWN]: self.y = self.y + 1

class PongUI:
    pt_p1=0
    pt_p2=0
    def __init__(self):
        pygame.draw.line(screen, WHITE, [sizex/2,0], [sizex/2,sizey], 1)
        
    def update(self):
        text = font.render(str(self.pt_p1), True, WHITE)
        screen.blit(text,((sizex/2)-50,0))
        text = font.render(str(self.pt_p2), True, WHITE)
        screen.blit(text,((sizex/2)+25,0))



a = PongPlayer(1)
b = PongPlayer(2)
c = Ball()
field = PongUI()
while isRunning:
    screen.fill(BLACK)
    c.update()
    field.update()
    a.checkButton()
    b.checkButton()
    a.show()
    b.show()
    c.show()
    pygame.display.flip()
    time.sleep(0.005)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False


pygame.quit()
