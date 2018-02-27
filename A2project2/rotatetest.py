import pygame
import math
import sys
from math import *
from pygame.locals import *

pygame.init();
screen = pygame.display.set_mode((1280,800),FULLSCREEN,32);
Clock = pygame.time.Clock();
wheel = pygame.image.load('wheel.png').convert_alpha();
board = pygame.image.load('board.png').convert();
ball = pygame.image.load('ball.png').convert_alpha();
f = pygame.font.SysFont('arial',32);


fps = 60;
# degree 
wav = 0;
waa = -3;
wad = 0;
# radian
bav = 7 / fps;
baa = -0.5 / fps;
bad = 0;
# milimeter
r = 364;
v = 0;
a = 0;

angs = [0 for i in range(37)];
for i in range(37):
    angs[i] = i*2*pi/37;
angs1 = [0 for i in range(37)];
angs2 = [0 for i in range(37)];
angl = [True for i in range(37)]; # angle set last time (boolean)
angn = [True for i in range(37)]; # angle set now (boolean)
    
check = 0;

t = 0; # t for tick

# coefficient of friction: 0.03-0.04
# stop velocity 0.28m/s (1.12 rad for 0.25m radian)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit();
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit();

    wav = wav + waa / fps;
    wad = wad + wav;
    if wav >= 0:
        waa = 0;
        wav = 0;
    elif t / fps >= 1:
        waa = 0.1;

    bav = bav + baa / fps;
    bad = bad + bav;
    if bav < 2.64 / fps:
        a = -254 / fps;
        v = v + a;
        r = r + v / fps;

    if r < 216:
        r = 216;
        v = abs(v)*0.8;

    avd = - fps * wav / 360 * 2 * pi + bav * fps;
    if avd <= 1.5 and check == 0 and r <= 260:
        for i in range(37):
            angs1[i] = (angs[i] + 2*pi/360*wad)%(2*pi) - (bad + 0.0785)%(2*pi);
            if 0 <= angs1[i] < 2*pi/37:
                block = i;
                check = 1;
                print('yes')

    if 216 <= r <= 260 and avd > 1.5:
        for i in range(37):
            angs2[i] = bad%(2*pi) - (angs[i] + 2*pi/360*wad)%(2*pi);
            if angs2[i] >= 0:
                angn[i] = True;
            else:
                angn[i] = False;
            if not angl[i] and angn[i]:
                bav = bav - avd * 0.05 / fps;
            angl[i] = angn[i];
                
    if check == 1:
        if (block * 2*pi/37 + 2*pi/360*wad)%(2*pi) - (bad)%(2*pi) <= 0:
            baa = waa / 360 * 2*pi;
            bav = wav / 360 * 2* pi;

    wheelr = pygame.transform.rotate(wheel,-wad);
    xw = 400 - wheelr.get_width()/2;
    yw = 400 - wheelr.get_height()/2;
    xb = 385 - cos(bad) * r;
    yb = 385 - sin(bad) * r;
    if wad < 0:
        wad = wad + 360;
    if bad > 360:
        bad = bad - 360;

    x,y = pygame.mouse.get_pos();
    xf = f.render('x '+str(x),False,(255,255,255));
    yf = f.render('y '+str(y),False,(255,255,255));
    
    t = t + 1;
    screen.blit(board,(0,0));
    screen.blit(wheelr,(xw,yw));
    screen.blit(ball,(xb,yb));
    screen.blit(xf,(0,10));
    screen.blit(yf,(0,50));
    pygame.display.update();
    Clock.tick(fps);
