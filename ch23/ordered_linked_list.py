# Zhang Chenyang Rex S3C3 OP1
# Create a list, having insert node, delete node, and print list function


# Start --> start pointer
# Free --> free pointer
# L --> a list
# v --> search value & insert value
# n,m,o --> value of pointer used in loops

class ListNode(object):
    def __init__(self,data,pointer):
        self.data = data;
        self.pointer = pointer;
    def __str__(self):
        return "(%s, %s)"%(self.data, self.pointer)


def InitialiseList():
    global L
    for i in range(9):
        L[i] = ListNode(None,i+1);
    L[9] = ListNode(None,NullPointer);

def InsertNode(v):
    global Start
    global L
    global Free
    if Free == -1:
        print('No extra space');
    if Start == NullPointer:
        Start = 0;
        Free = 1;
        L[0] = ListNode(v,NullPointer);
    else:
        n = Start;
        if v < L[Start].data:
            F = L[Free].pointer
            L[Free] = ListNode(v,Start);
            Start = Free;
            Free = F;
        else:
            while True:
                if v < L[n].data:
                    m = Start
                    while True:
                        if L[m].pointer == n:
                            break
                        m = L[m].pointer;
                    L[m] = ListNode(L[m].data,Free);
                    L[Free] = ListNode(v,n);
                    Free = L[Free].pointer
                    break
                elif L[n].pointer == NullPointer and v >= L[n].data:
                    F = L[Free].pointer
                    L[Free] = ListNode(v,NullPointer);
                    L[n] = ListNode(L[n].data,Free);
                    Free = F
                    break
                n = L[n].pointer;

def DeleteNode(v):
    global Start
    n = Start;
    while n != -1:
        if L[n].data == v:
            break
        n = L[n].pointer;
    if n == -1:
        return 'no such value'
    m = Free;
    while m != -1:
        if L[m].pointer == -1:
            break
        m = L[m].pointer;
    if n == Start:
        Start = L[n].pointer;
        L[m] = ListNode(L[m].data,n);
        L[n] = ListNode(L[n].data,NullPointer);
    elif L[n].pointer == NullPointer:
        o = Start;
        while True:
            if L[o].pointer == n:
                break
            o = L[o].pointer;
        L[o] = ListNode(L[o].data,NullPointer);
        L[m] = ListNode(L[m].data,n);
    else:
        o = Start;
        while True:
            if L[o].pointer == n:
                break
            o = L[o].pointer;
        L[o] = ListNode(L[o].data,L[n].pointer);
        L[m] = ListNode(L[m].data,n);
        L[n] = ListNode(L[n].data,NullPointer);
        
        
        
            
def PrintList():
    n = Start;
    while n != -1:
        print(L[n].data);
        n = L[n].pointer

def SearchNode(v):
    v = int(v);
    n = Start;
    while n != -1:
        if L[n].data == v:
            return n
        n = L[n].pointer;
    print('no value found');
    
        
    

L = [0 for i in range(10)];
NullPointer = -1;
Start = NullPointer;
Free = 0;

InitialiseList();
print('4 function','PrintList() , SearchNode(), DeleteNode(), InsertNode()')

InsertNode(10);
InsertNode(15);
InsertNode(16);
InsertNode(2);
print('value after insert')
PrintList()
DeleteNode(2);
DeleteNode(15);
print('list after delete 2 and 15')
PrintList();




    
