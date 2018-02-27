import pygame
import math
import sys
from math import *
from pygame.locals import *

pygame.init();
screen = pygame.display.set_mode((700,700),0,32);
Clock = pygame.time.Clock();
back = pygame.image.load('board1.png');

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit();
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit();
    screen.blit(back,(0,0));
    pygame.draw.circle(screen,(0,0,0),(350,350),120);
    pygame.draw.circle(screen,(78,53,46),(350,350),115);
    pygame.draw.polygon(screen,(255,201,14),((191,367),(350,357),(350,343),(191,333)));
    pygame.draw.polygon(screen,(255,201,14),((367,191),(357,350),(343,350),(333,191)));
    pygame.draw.polygon(screen,(255,201,14),((509,367),(350,357),(350,343),(509,333)));
    pygame.draw.polygon(screen,(255,201,14),((367,509),(357,350),(343,350),(333,509)));
    pygame.draw.circle(screen,(255,201,14),(350,350),35);
    pygame.draw.circle(screen,(255,255,0),(350,350),30);
    pygame.draw.circle(screen,(255,201,14),(350,350),20);
    pygame.draw.circle(screen,(255,201,14),(193,350),25);
    pygame.draw.circle(screen,(255,201,14),(350,193),25);
    pygame.draw.circle(screen,(255,201,14),(507,350),25);
    pygame.draw.circle(screen,(255,201,14),(350,507),25);
    pygame.draw.circle(screen,(255,255,0),(193,350),20);
    pygame.draw.circle(screen,(255,255,0),(350,193),20);
    pygame.draw.circle(screen,(255,255,0),(507,350),20);
    pygame.draw.circle(screen,(255,255,0),(350,507),20);
    board = screen.subsurface((45,45),(610,610));
    pygame.image.save(board,'board2.png');
    
    pygame.display.update();
    Clock.tick(3)
