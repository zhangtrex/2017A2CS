# Zhang Chenyang Rex S3C3 Op3
# dictionary


class D(object):
    def __init__(self,key,value):
        self.value = value;
        self.key = key;
    def __str__(self):
        return "(%s, %s)"%(self.key, self.value)

def InitialiseD():
    global Dict
    Dict = [0 for i in range(10)];
    for i in range(10):
        Dict[i] = D(None, None);

def Rex(s):   # s for string
    acc = 0;
    for i in range(len(s)):
        acc = ord(s[i]) + acc;
    acc = str(acc);
    a = 0;
    for i in range(len(acc)):
        a = int(acc[i]) + a;
    a = a % 10;
    return a

def Insert(k,v):
    global Dict
    i = Rex(k);
    n = i;
    while Dict[n].key != None:
        n = n + 1;
        if n == i:
            return 'No free space'
        elif n == 10:
            n = 0
    Dict[n] = D(k,v);

def Search(k):
    global S
    i = Rex(k);
    n = i;
    while Dict[n].key != None:
        if Dict[n].key == k:
            return Dict[n].value;
        else:
            if n == 9:
                n = 0;
            else:
                n = n + 1;
            if n == i:
                return 'No key found'
    return 'No key found'

InitialiseD();
Insert('IP','Internet Protocol');
Insert('TCP','Transmission Control Protocol');
Insert('POP3','Post Office Protocol 3');
Insert('DNS','Domain Name Server');
Insert('HTTP','Hyper Text Transport Protocol');
for i in range(10):
    print(Dict[i]);




