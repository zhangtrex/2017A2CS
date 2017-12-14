# Zhang Chenyang Rex S3C3 OP1
# Create a Stack,with push and pop function


# S for stack
# Free & Start for freepointerlist and startpointer
#

class Node(object):
    def __init__(self, content, pointer):
        self.content = content;
        self.pointer = pointer;
    def __str__(self):
        return "(%s,%s)"%(self.content, self.pointer)

def InitialiseStack():
    global S
    for i in range(9):
        S[i] = Node(None,i+1);
    S[9] = Node(None, NullPointer);

def Push(v):
    global S
    global Free
    global Start
    if Free == NullPointer:
        return "no space"
    if Start == NullPointer:
        S[Free] = Node(v, -1);
        Start = 0;
        Free = 1;
        
    else:
        F = S[Free].pointer;
        S[Free] = Node(v, Start);
        Start = Free;
        Free = F;

def Pop():
    global S
    global Free
    global Start
    St = S[Start].pointer
    S[Start] = Node(S[Start].content,Free);
    Free = Start;
    Start = St;
    

def PrintStack():
    n = Start;
    while n != -1:
        print(S[n].content);
        n = S[n].pointer


S = [0 for i in range(10)];
NullPointer = -1;
Start = NullPointer;
Free = 0;
print('3 functions','Push(1 argument), Pop(), PrintStack()')
InitialiseStack()
Push(5115);
PrintStack();
print('Push(5115)');
Push(777);
PrintStack()
print('Push(777)');
Push(234);
PrintStack()
print('Push(234)')
print()
Push(66565);
print('Push(66565)')
PrintStack()
Pop()
print('stack after pop')
PrintStack()

