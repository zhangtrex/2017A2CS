# Roulette game
# programmed by Rex
# special guest: Kevin Yang

import pygame
import math
import sys
import random

from math import *
from pygame.locals import *

pygame.init();
screen = pygame.display.set_mode((1280,800),FULLSCREEN,32);
Clock = pygame.time.Clock();
wheel = pygame.image.load('wheel.png').convert_alpha();
board = pygame.image.load('board.png').convert();
board1 = pygame.image.load('board1.png').convert();
chipimage = pygame.image.load('chip.png').convert_alpha();
ball = pygame.image.load('ball.png').convert_alpha();
f = pygame.font.SysFont('arial',32);
f1 = pygame.font.SysFont('arial',40);
f2 = pygame.font.SysFont('arial',60);
nextrun = f2.render('press left mouse to start another game',False,(255,255,255));

n = [1,20,14,31,9,22,18,29,7,28,12,35,3,26,0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33];

fps = 60;
# degree
wav = 0; # wheel angular velocity
waa = -3; # wheel angular acceleration
wad = 0; # wheel angular displacement
# radian
bav = random.randint(500,800)/100 / fps; # ball angular velocity
baa = -0.4 / fps; # ball angular acceleration
bad = 0; # ball angular displacement
# milimeter
r = 364; # radius
v = 0; # vertical velocity
a = 0; # vertical acceleration

PressMouseCount = 0; # if left mouse pressed, it increment 1

BetSet = [0 for i in range(49)];
BetMultiple = [0 for i in range(49)];

bet = 1;
BetMoney = 100;
Money = 1000;

angs = [0 for i in range(37)];
for i in range(37):
    angs[i] = i*2*pi/37;
angs1 = [0 for i in range(37)];
angs2 = [0 for i in range(37)];
angl = [True for i in range(37)]; # angle set last time (boolean)
angn = [True for i in range(37)]; # angle set now (boolean)
    
check = 0;
wincheck = 0;
winnum = -1;
chippos = [];
winnumprint = -1;

t = 0; # t for tick

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit();
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit();
    
    PressMouse = pygame.mouse.get_pressed();
    x,y = pygame.mouse.get_pos();

    # press mouse for a long time only count for one press
    if PressMouse[0] == True:
        PressMouseCount = PressMouseCount + 1;
    else:
        PressMouseCount = 0;

    # find the position player bet on
    if bet == 1 and PressMouseCount == 1:
        bx = (x - 840)//80;
        by = (y - 50)//50;
        if by == 0 and 1 < bx < 5:
            if BetSet[0] == 0:
                BetSet[0] = BetMoney;
                Money = Money - BetMoney;
                chippos.append((320,75));
        elif bx == 0 and 0 < by < 13:
            if BetSet[43+(by-1)//2] == 0:
                BetSet[43+(by-1)//2] = BetMoney;
                Money = Money - BetMoney;
                chippos.append((80,150+(by-1)//2*100));
        elif bx == 1 and 0 < by < 13:
            if BetSet[40+(by-1)//4] == 0:
                BetSet[40+(by-1)//4] = BetMoney;
                Money = Money - BetMoney;
                chippos.append((160,200+(by-1)//4*200));
        elif 1 < bx < 5 and 0 < by < 14:
            if BetSet[(by-1)*3+bx-1] == 0:
                BetSet[(by-1)*3+bx-1] = BetMoney;
                Money = Money - BetMoney;
                chippos.append((80+bx*80,75+50*by));

    if wincheck == 1:
        if 36 - block <= 18:
            winnum = n[17 - (36 - block)];
        else:
            winnum = n[54 - (36 - block)];
        print(winnum);
        winnumprint = winnum;

    # restart another game, reinitialize variables
    if wincheck >= 60 and PressMouseCount == 1:
        wav = 0;
        waa = -3;
        baa = -0.4 / fps
        bav = random.randint(500,800)/100/fps;
        bad = 0;
        r = 364;
        v = 0;
        a = 0;
        angs1 = [0 for i in range(37)];
        angs2 = [0 for i in range(37)];
        angl = [True for i in range(37)];
        angn = [True for i in range(37)];
        check = 0;
        wincheck = 0;
        winnum = -1;
        chippos = [];
        BetSet = [0 for i in range(49)];
        BetMultiple = [0 for i in range(49)];
        bet = 1;
        t = 0;
        winnumprint = -1;

    # add the money the player win on his/her bet
    if winnum != -1:
        if winnum == 0:
            BetMultiple[0] = 36;
        else:
            BetMultiple[winnum] = 36;
            BetMultiple[37+(winnum-1)%3] = 3;
            BetMultiple[40+(winnum-1)//12] = 3;
            if winnum <= 18:
                BetMultiple[43] = 2;
            else:
                BetMultiple[48] = 2;
            if winnum % 2 == 1:
                BetMultiple[47] = 2;
            else:
                BetMultiple[44] = 2;
            if winnum in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
                BetMultiple[45] = 2;
            else:
                BetMultiple[46] = 2;
        for i in range(49):
            Money += BetMultiple[i]*BetSet[i];
        winnum = -1;

    # calculate movement of the wheel
    wav = wav + waa / fps;
    wad = wad + wav;
    if wav >= 0:
        waa = 0;
        wav = 0;
    elif t / fps >= 1:
        waa = 0.1;

    # calculate movement of the ball
    bav = bav + baa / fps;
    bad = bad + bav;
    # when the ball has low angular velocity, it move to the center of the wheel
    if bav < 2.64 / fps:
        a = -254 / fps;
        v = v + a;
        r = r + v / fps;

    # calculate velocity of the ball when it bounces with the inner wall 
    if r < 216:
        r = 216;
        v = abs(v)*random.randint(50,90)/100;
    
    # avd is angular velocity difference between the wheel and the ball
    avd = - fps * wav / 360 * 2 * pi + bav * fps;
    # find which position the ball will be stopped by the wheel
    if avd <= 1.5 and check == 0 and r <= 260:
        for i in range(37):
            angs1[i] = (angs[i] + 2*pi/360*wad)%(2*pi) - (bad + 0.0785)%(2*pi);
            if 0 <= angs1[i] < 2*pi/37:
                block = i;
                check = 1;
                print('yes');

    if check == 1:
        if (block * 2*pi/37 + 2*pi/360*wad)%(2*pi) - (bad+0.02)%(2*pi) <= 0:
            baa = waa / 360 * 2*pi;
            bav = wav / 360 * 2*pi;
            bet = 0;
            wincheck += 1;
#        print((block * 2*pi/37 + 2*pi/360*wad)%(2*pi) - (bad)%(2*pi))

    avd = - fps * wav / 360 * 2 * pi + bav * fps;
    if 216 <= r <= 260 and avd > 1.5 and check == 0:
        for i in range(37):
            angs2[i] = bad%(2*pi) - (angs[i] + 2*pi/360*wad)%(2*pi);
            if angs2[i] >= 0:
                angn[i] = True;
            else:
                angn[i] = False;
        for i in range(37):
            if not angl[i] and angn[i]:
                bav = bav - avd * random.randint(30,90)/1000 / fps;
                break
        for i in range(37):
            angl[i] = angn[i];

    wheelr = pygame.transform.rotate(wheel,-wad);
    xw = 400 - wheelr.get_width()/2;
    yw = 400 - wheelr.get_height()/2;
    xb = 385 - cos(bad) * r;
    yb = 385 - sin(bad) * r;
    if wad < 0:
        wad = wad + 360;
    if bad > 360:
        bad = bad - 360;

    xf = f.render('x '+str(x),False,(255,255,255));
    yf = f.render('y '+str(y),False,(255,255,255));
    moneyimage = f.render('Money: '+str(Money),False,(255,255,255));
    
    t = t + 1;
    screen.blit(board,(0,0));
    screen.blit(board1,(800,0));
    screen.blit(wheelr,(xw,yw));
    screen.blit(ball,(xb,yb));
    for c in chippos:
        screen.blit(chipimage,(c[0]+800-15,c[1]-15));
    screen.blit(xf,(0,10));
    screen.blit(yf,(0,50));
    if winnumprint != -1:
        screen.blit(f.render('win number is '+str(winnumprint),False,(255,255,255)),(600,10))
    if wincheck >= 60:
        screen.blit(nextrun,(200,200))
    screen.blit(moneyimage,(0,90))
    pygame.display.update();
    Clock.tick(fps);
