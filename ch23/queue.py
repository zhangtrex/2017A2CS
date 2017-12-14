# Zhang Chenyang Rex S3C3 OP1
# create a queue with Queue() and Dequeue() functions


#Q for queue
#Start, Free for Startpointer, Freelistpointer
# m,n -- use for finding the right location to change value

class Node(object):
    def __init__(self, content, pointer):
        self.content = content;
        self.pointer = pointer;
    def __str__(self):
        return "(%s,%s)"%(self.content,self.pointer)

def InitialiseQueue():
    global Q
    Q = [0 for i in range(10)];
    for i in range(9):
        Q[i] = Node(None, i+1);
    Q[9] = Node(None, NullPointer);

def PrintQueue():
    n = Start;
    while n != -1:
        print(Q[n].content);
        n = Q[n].pointer;

def Queue(v):
    global Start
    global Free
    global End
    global Q
    F = Q[Free].pointer;
    if Start == NullPointer:
        Q[Free] = Node(v,NullPointer);
        Start = Free;
        End = Free;
        Free = F;
    else:
        Q[Free] = Node(v,NullPointer);
        Q[End] = Node(Q[End].content,Free);
        End = Free;
        Free = F;

def Dequeue():
    global Q
    global Free
    global Start
    St = Q[Start].pointer;
    Q[Start] = Node(Q[Start].content,Free);
    Free = Start;
    Start = St;
     
        

NullPointer = -1;
Start = NullPointer;
Free = 0;
End = NullPointer;
print('3 functions, Queue(1 argument), Dequeue() and PrintQueue()');
InitialiseQueue();
Queue(12451);
print('Queue(12451)')
PrintQueue();
Queue(415);
print('Queue(415)')
PrintQueue();
Queue(5555);
print('Queue(5555)')
PrintQueue();
Queue(512);
print('Queue(512)')
PrintQueue();
Dequeue()
Dequeue()
print('after 2 Dequeue()');
PrintQueue();
