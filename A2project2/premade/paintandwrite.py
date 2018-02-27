import pygame
import math
import sys
from math import *
from pygame.locals import *

pygame.init();
screen = pygame.display.set_mode((700,700),0,32);
Clock = pygame.time.Clock();
back = pygame.image.load('board.png').convert();
font = pygame.font.SysFont('Tahoma',36);
n = [1,20,14,31,9,22,18,29,7,28,12,35,3,26,0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33];
screen.blit(back,(0,0));
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit();
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit();
    
    screen.blit(back,(0,0));

    for i in range(len(n)):
        iname = font.render(str(n[i]),True,(255,255,255));
        inamer = pygame.transform.rotate(iname,270-(i+0.5)*360/37);
        xp = 350 + 283 * cos((i+0.5)*2*pi/37) - inamer.get_width()/2;
        yp = 350 + 283 * sin((i+0.5)*2*pi/37) - inamer.get_height()/2;
        screen.blit(inamer,(xp,yp));
        
    pygame.image.save(screen,'board1.png');
    pygame.display.update();
    Clock.tick(3)
