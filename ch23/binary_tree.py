# Zhang Chenyang Rex S3C3 OP1
# basic data structure: binary tree

# Node for class node
# Root for the root pointer
# Free for free list pointer
# n for current pointer


class Node(object):
    def __init__(self, lpointer, data, rpointer):
        self.lpointer = lpointer;
        self.data = data;
        self.rpointer = rpointer;
    def __str__(self):
        return "(%s, %s, %s)"%(self.lpointer, self.data, self.rpointer);

def InitialiseTree():
    global T
    global Free
    global Root
    global NullPointer
    Free = 0;
    NullPointer = -2;
    Root = NullPointer;
    T = [0 for i in range(10)];
    for i in range(9):
        T[i] = Node(i+1,None,None);
    T[9] = Node(NullPointer,None,None);

def Insert(v):
    global T
    global Free
    global Root
    if Root == NullPointer:
        F = T[Free].lpointer;
        Root = Free;
        T[Free] = Node(-1, v, -1);
        Free = F;
    else:
        n = Root;
        F = T[Free].lpointer;
        while True:
            if v > T[n].data:
                if T[n].rpointer == -1:
                    T[Free] = Node(-1, v, -1);
                    T[n].rpointer = Free;
                    Free = F;
                    break
                else:
                    n = T[n].rpointer;
            else:
                if T[n].lpointer == -1:
                    T[Free] = Node(-1, v, -1);
                    T[n].lpointer = Free;
                    Free = F;
                    break
                else:
                    n = T[n].lpointer;

def Search(v):
    global Root
    global Free
    global T
    n = Root;
    while True:
        if v > T[n].data:
            if T[n].rpointer == -1:
                print('no such value');
                return 0
            else:
                n = T[n].rpointer
        elif v < T[n].data:
            if T[n].lpointer == -1:
                print('no such value');
                return 0
            else:
                n = T[n].lpointer;
        else:
            return 1    

def P():
    for i in range(10):
        print(T[i]);

InitialiseTree();
Insert(2222);
Insert(1111);
Insert(1500);
Insert(2400);
Insert(1234);
Insert(1200);
Insert(2300);
print('the whole tree is');
P();




