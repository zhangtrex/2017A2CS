# Zhang Chenyang Rex S3C3 OP1
# Hash Table

S = [None for i in range(10)];

def Hash(v):
    n = v % 10;
    return n

def Insert(v):
    global S
    i = Hash(v);
    n = i;
    while S[n] != None:
        n = n + 1;
        if n == i:
            return 'No free space'
        elif n == 10:
            n = 0;
    S[n] = v;

def Search(v):
    global S
    i = Hash(v);
    n = i;
    while S[n] != None:
        if S[n] == v:
            return 1
        else:
            if n == 9:
                n = 0;
            else:
                n = n + 1;
            if n == i:
                return 0
    return 0




