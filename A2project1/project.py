# ----------------------
# -                    -
# -   Winter Project   -
# -    Casino Games    -
# -     Black Jack     -
# -  by Rex and Kevin  -
# -                    -
# ----------------------

#  Spade - S / Heart - H / Club - C / Diamond -D

import random
import pygame
import sys
from pygame.locals import *
from GameObjects import *

# modules

def DeleteElement(List, Index): # use index in a list to remove the element
    List2 = [];
    for i in range(len(List)-1):
        if i < Index:
            List2.append(List[i]);
        else:
            List2.append(List[i+1]);
    return List2

def InitializeCardDeck():
    L = []; # L for origin card set
    L = L + [Card('S','A'),Card('H','A'),Card('C','A'),Card('D','A')];
    for i in range(2,11,1):
        L = L + [Card('S',str(i)),Card('H',str(i)),Card('C',str(i)),Card('D',str(i))];
    L = L + [Card('S','J'),Card('H','J'),Card('C','J'),Card('D','J')];
    L = L + [Card('S','Q'),Card('H','Q'),Card('C','Q'),Card('D','Q')];
    L = L + [Card('S','K'),Card('H','K'),Card('C','K'),Card('D','K')];
    RL = []; # RL for return card set
    while len(L) != 0:
        i = random.randint(0,len(L)-1);
        RL = RL + [L[i]]
        L = DeleteElement(L,i);
    return RL

# pygame module

def InitializeCardDeckImage():
    CardDeckImageFilename = 'Cards.png';
    CardDeck = pygame.image.load(CardDeckImageFilename).convert();
    CI = {};    #CI for Card Image
    for j in 'SHCD':
        if j == 'S':
            i = 0;
        elif j == 'H':
            i = 1;
        elif j == 'C':
            i = 2;
        elif j == 'D':
            i = 3;
        CI[j+'A'] = CardDeck.subsurface((0,0+i*150),(90,137));
        CI[j+'J'] = CardDeck.subsurface((1000,0+i*150),(90,137));
        CI[j+'Q'] = CardDeck.subsurface((1100,0+i*150),(90,137));
        CI[j+'K'] = CardDeck.subsurface((1200,0+i*150),(90,137));
    for i in range(2,11,1):
        CI['S'+str(i)] = CardDeck.subsurface((100*i-100,0),(90,137));
        CI['H'+str(i)] = CardDeck.subsurface((100*i-100,150),(90,137));
        CI['C'+str(i)] = CardDeck.subsurface((100*i-100,300),(90,137));
        CI['D'+str(i)] = CardDeck.subsurface((100*i-100,450),(90,137));
    CI['Back'] = CardDeck.subsurface((0,600),(90,137));
    return CI

BackgroundImageFilename = 'Board.png';

pygame.init()

pygame.display.set_caption('blackjack');

Screen = pygame.display.set_mode((800,600),0,32);

Background = pygame.image.load(BackgroundImageFilename).convert();

Font1 = pygame.font.SysFont("arial",20);
Font2 = pygame.font.SysFont('arial',40);

Hit = Font1.render('Hit',False,(0,0,0));
Stand = Font1.render('Stand',False,(0,0,0));
Quit = Font1.render('Quit',False,(0,0,0));
Game = Font1.render('Game',False,(0,0,0));
Bust = Font2.render('You Bust',False,(255,0,0));
Win = Font2.render('You win',False,(255,0,0));
Loss = Font2.render('You loss',False,(255,0,0));
Draw = Font2.render("It's a draw",False,(255,0,0));
BlackJack = Font2.render('Black Jack !',False,(255,0,0));
Hint1 = Font2.render('Press Mouse to Start Another Game',True,(0,0,0));

CardImage = InitializeCardDeckImage();

Clock = pygame.time.Clock();

ChooseFlag = 0;
# 0 for nothing, 1 for upper button pressed, 2 for lower button pressed
# 3 for $10, 4 for $50, 5 for $100
StateFlag = 0;
# 0 for startgame, 1 for in game, 2 for dealer, 3 for win,
# 4 for draw, 5 for loss, 6 for bust, 7 for blackjack
PressMouseCount = 0; # 0 for LeftKeyofMouse is not pressed, 1 for pressed
DealerCount = 0;
Money = 1000;
Bet = 10;

CD = InitializeCardDeck();

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            quit();
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit();

    if len(CD) <= 26 and StateFlag == 0:
        CD = InitializeCardDeck();
    
    Screen.blit(Background,(0,0));
    
    x, y = pygame.mouse.get_pos();
    PressKey = pygame.key.get_pressed();
    PressMouse = pygame.mouse.get_pressed();
    xposi = Font2.render('x: '+str(x),False,(0,0,0));
    yposi = Font2.render('y: '+str(y),False,(0,0,0));

    Screen.blit(xposi,(20,20));
    Screen.blit(yposi,(20,70));

    if PressMouse[0]:
        PressMouseCount = PressMouseCount + 1;
    else:
        PressMouseCount = 0;

    
    if PressMouse[0] and 5 <= x <= 77 and 512 <= y <= 548 and PressMouseCount == 1:
        ChooseFlag = 1;
    elif PressMouse[0] and 5 <= x <= 77 and 560 <= y <= 596 and PressMouseCount == 1:
        ChooseFlag = 2;
    elif PressMouse[0] and 755 <= x <= 794 and 511 <= y <= 550 and PressMouseCount == 1:
        ChooseFlag = 3;
    elif PressMouse[0] and 755 <= x <= 794 and 556 <= y <= 595 and PressMouseCount == 1:
        ChooseFlag = 4;
    elif PressMouse[0] and 690 <= x <= 749 and 556<= y <= 595 and PressMouseCount == 1:
        ChooseFlag = 5;
    
    if PressMouse[0] and StateFlag == 3 and PressMouseCount == 1:
        StateFlag = 0;
        ChooseFlag = 0;
        Money = Money + Bet;
    elif PressMouse[0] and StateFlag == 4 and PressMouseCount == 1:
        StateFlag = 0;
        ChooseFlag = 0;
    elif PressMouse[0] and StateFlag == 5 and PressMouseCount == 1:
        StateFlag = 0;
        ChooseFlag = 0;
        Money = Money - Bet;
    elif PressMouse[0] and StateFlag == 6 and PressMouseCount == 1:
        StateFlag = 0;
        ChooseFlag = 0;
        Money = Money - Bet;
    elif PressMouse[0] and StateFlag == 7 and PressMouseCount == 1:
        StateFlag = 0;
        ChooseFlag = 0;
        Money = Money + 2 * Bet;

    if ChooseFlag == 2 and StateFlag == 0:
        ChooseFlag == 0;
        pygame.quit();
    elif ChooseFlag == 1 and StateFlag == 0:
        ChooseFlag = 0;
        StateFlag = 1;
        CS = CardSet();
        C = CD.pop();
        CS.draw(C);
        C = CD.pop();
        CS.draw(C);
        DCS = CardSet();
        C = CD.pop();
        DCS.draw(C);
        C = CD.pop();
        DCS.draw(C);        
    elif ChooseFlag == 1 and StateFlag == 1:
        C = CD.pop();
        CS.draw(C);
        ChooseFlag = 0;
    elif ChooseFlag == 2 and StateFlag == 1:
        StateFlag = 2;
        ChooseFlag = 0;
    elif ChooseFlag == 3 and StateFlag == 0:
        Bet = 10;
        ChooseFlag = 0;
    elif ChooseFlag == 4 and StateFlag == 0:
        Bet = 50;
        ChooseFlag = 0;
    elif ChooseFlag == 5 and StateFlag == 0:
        Bet = 100;
        ChooseFlag = 0;

    # Other Condition;
    if StateFlag == 1:
        if CS.checkblackjack() == True:
            if DCS.checkblackjack() == True:
                StateFlag = 4;
            else:
                StateFlag = 7;
        elif DCS.checkblackjack() == True:
            StateFlag = 5;
        if CS.count() > 21:
            StateFlag = 6;
        elif len(CS.data) >= 5:
            StateFlag = 2;
    elif StateFlag == 2:
        DealerCount = DealerCount + 1;
        if DealerCount >= 20:
            if DCS.count() < 17:
                C = CD.pop();
                DCS.draw(C);
                DealerCount = 0;
            if DCS.count() > 21:
                StateFlag = 3;
            elif DCS.count() >= 17 or len(DCS.data) == 5:
                if DCS.count() > CS.count():
                    StateFlag = 5;
                elif DCS.count() == CS.count():
                    StateFlag = 4;
                else:
                    StateFlag = 3;
        
    MoneyImage = Font2.render('$'+str(Money),False,(0,0,0));
    BetImage = Font2.render('$'+str(Bet),False,(0,0,0));
    

    # screen
    if StateFlag == 0:
        Screen.blit(Quit,(25,567));
        Screen.blit(Game,(17,519));
    if StateFlag == 1:
        for i in range(len(CS.data)):
            CardI = CardImage[CS.data[i].hashfunction()];
            Screen.blit(CardI,(180+80*i,350));
        CardBackI = CardImage['Back'];
        Screen.blit(CardBackI,(180,100));
        for i in range(1,len(DCS.data),1):
            CardI = CardImage[DCS.data[i].hashfunction()];
            Screen.blit(CardI,(180+80*i,100));
        Screen.blit(Hit,(31,519));
        Screen.blit(Stand,(18,567));
    elif StateFlag == 2:
        for i in range(len(CS.data)):
            CardI = CardImage[CS.data[i].hashfunction()];
            Screen.blit(CardI,(180+80*i,350));
        for i in range(len(DCS.data),):
            CardI = CardImage[DCS.data[i].hashfunction()];
            Screen.blit(CardI,(180+80*i,100));
    elif StateFlag == 3:
        for i in range(len(CS.data)):
            CardI = CardImage[CS.data[i].hashfunction()];
            Screen.blit(CardI,(180+80*i,350));
        for i in range(len(DCS.data)):
            CardI = CardImage[DCS.data[i].hashfunction()];
            Screen.blit(CardI,(180+80*i,100));
        Screen.blit(Win,(330,270));
        Screen.blit(Hint1,(150,200));
    elif StateFlag == 4:
        for i in range(len(CS.data)):
            CardI = CardImage[CS.data[i].hashfunction()];
            Screen.blit(CardI,(180+80*i,350));
        for i in range(len(DCS.data)):
            CardI = CardImage[DCS.data[i].hashfunction()];
            Screen.blit(CardI,(180+80*i,100));
        Screen.blit(Draw,(330,270));    
        Screen.blit(Hint1,(150,200));
    elif StateFlag == 5:
        for i in range(len(CS.data)):
            CardI = CardImage[CS.data[i].hashfunction()];
            Screen.blit(CardI,(180+80*i,350));
        for i in range(len(DCS.data)):
            CardI = CardImage[DCS.data[i].hashfunction()];
            Screen.blit(CardI,(180+80*i,100));
        Screen.blit(Loss,(330,270));
        Screen.blit(Hint1,(150,200));
    elif StateFlag == 6:
        for i in range(len(CS.data)):
            CardI = CardImage[CS.data[i].hashfunction()];
            Screen.blit(CardI,(180+80*i,350));
        for i in range(len(DCS.data)):
            CardI = CardImage[DCS.data[i].hashfunction()];
            Screen.blit(CardI,(180+80*i,100));
        Screen.blit(Bust,(330,270));
        Screen.blit(Hint1,(150,200));
    elif StateFlag == 7:
        for i in range(len(CS.data)):
            CardI = CardImage[CS.data[i].hashfunction()];
            Screen.blit(CardI,(180+80*i,350));
        for i in range(len(DCS.data)):
            CardI = CardImage[DCS.data[i].hashfunction()];
            Screen.blit(CardI,(180+80*i,100));
        Screen.blit(BlackJack,(330,270));
        Screen.blit(Hint1,(150,200));


    Screen.blit(MoneyImage,(700,10));
    Screen.blit(BetImage,(700,50));

    Clock.tick(20);

    pygame.display.update();
