# ----------------------
# -                    -
# -   Winter Project   -
# -    Casino Games    -
# -     Black Jack     -
# -   by Rex & Kevin   -
# -                    -
# ----------------------

#  Spade - S / Heart - H / Club - C / Diamond -D

import random

def c(s):
    if len(s) == 0:
        return 0
    if s[len(s)-1] == 'A':
        return s
    

class Card(object):

    def __init__(self, suit, name):
        self.suit = suit;
        self.name = name;

    def __repr__(self):
        return "(suit: %s, name: %s)"%(self.suit, self.name)

class CardSet(object):

    def __init__(self):
        self.data = [];

    def __repr__(self):
        return '%s'%(self.data)

    def draw(self, card):
        self.data.append(card);

    def count(self):
        if len(self.data) == 0:
            return 0
        Sum = 0;
        Flag = 0;
        for c in self.data:
            if c.name == 'A':
                Sum = Sum + 1;
                Flag = 1;
            elif c.name in 'JQK':
                Sum = Sum + 10;
            else:
                Sum = Sum + int(c.name);
        if Sum <= 11 and Flag == 1:
            print(Sum, Sum + 10)
            return Sum, Sum + 10
        else:
            print(Sum)
            return Sum

    def checkblackjack(self):
        if len(self.data) == 2:
            if self.data[0].name == 'A' and self.data[1].name in '10JQK':
                return True
            if self.data[0].name in '10JQK' and self.data[1].name == 'A':
                return True
        return False
        

def DeleteElement(List, Index):
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



CD = InitializeCardDeck(); # Card Deck
a = CardSet();
while True:
    ins = input('d for draw : ');
    if ins == 'd':
        c = CD.pop()
        a.draw(c);
        print(a)
    else:
        print('quit')
        break
    if a.count() > 21:
        print('bomb')
        break
    

    





    
