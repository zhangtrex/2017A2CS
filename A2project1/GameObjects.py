# module Card
# module CardSet

class Card(object):

    def __init__(self, suit, name):
        self.suit = suit;
        self.name = name;

    def __repr__(self):
        return "(suit: %s, name: %s)"%(self.suit, self.name)

    def __str__(self):
        return "(%s,%s)"%(self.suit, self.name)

    def hashfunction(self):
        s = self.suit;
        n = self.name;
        return s+n

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
            return Sum + 10
        else:
            return Sum

    def checkblackjack(self):
        if len(self.data) == 2:
            if self.data[0].name == 'A' and self.data[1].name in '10JQK':
                return True
            if self.data[0].name in '10JQK' and self.data[1].name == 'A':
                return True
        return False

    
