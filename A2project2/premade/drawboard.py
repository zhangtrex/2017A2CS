import sys
import pygame
import math
from math import *
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((700,700),0,32);
Clock = pygame.time.Clock();
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit();
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit();
    screen.fill((255,255,255));
    pygame.draw.circle(screen,(255,242,0),(350,350),305);
    pygame.draw.circle(screen,(255,0,0),(350,350),300);
    pygame.draw.circle(screen,(255,242,0),(350,350),265);
    pygame.draw.circle(screen,(255,0,0),(350,350),263);
    pygame.draw.circle(screen,(0,0,0),(350,350),200);
    pygame.draw.circle(screen,(1,98,1),(350,350),195);
    for i in range(37):
        xp = 350 + 300 * cos(2*i*pi/37);
        yp = 350 + 300 * sin(2*i*pi/37);
        pygame.draw.line(screen,(185,122,87),(350,350),(xp,yp),2);
    pygame.draw.circle(screen,(255,255,255),(350,350),120);
#    name = 'board.png';
#    pygame.image.save(screen,name);
    Clock.tick(1);
    pygame.display.update()
    
