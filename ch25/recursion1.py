# zhang chenyang Rex
# codingbat solution for recursion 1

def go(x):
    print(x);
    if x == 10:
        return
    else:
        go(x+2)

def factorial(n):
    
    if n == 1:
        return 1;
    return n * factorial(n-1)

def bunnyEars(n):
    if n == 0:
        return 0
    else:
        return bunnyEars(n - 1) + 2

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2);

def bunnyEars2(n):
    if n == 0:
        return 0;
    elif n % 2 == 0:
        return bunnyEars2(n-1) + 3
    else:
        return bunnyEars2(n-1) + 2

def triangle(n):
    if n == 0:
        return 0
    else:
        return n + triangle(n - 1);

def sumDigits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sumDigits(n//10);

def count7(n):
    if n == 0:
        return 0;
    if n % 10 == 7:
        return 1 + count7(n//10)
    else:
        return count7(n//10)

def count8(n):
    if n == 0:
        return 0
    if (n//10) % 10 == 8 and n % 10 == 8:
        return 2 * count8(n//10)
    elif n % 10 == 8:
        return 1 + count8(n//10)
    else:
        return count8(n//10)

def powerN(n,p):
    if p == 0:
        return 1
    else:
        return n * powerN(n,p-1)

def countX(s):
    if s == '':
        return 0
    else:
        if s[-1:] == 'x':
            return 1 + countX(s[:-1]);
        else:
            return countX(s[:-1]);

def countHi(s):
    if len(s) <= 1:
        return 0
    else:
        if s[len(s)-1] == 'i' and s[len(s)-2] == 'h':
            return 1 + countHi(s[:-1])
        else:
            return countHi(s[:-1])
        
def changeXY(s):
    if s == '':
        return ''
    if s[-1] == 'x':
        return changeXY(s[:-1]) + 'y'
    else:
        return changeXY(s[:-1]) + s[-1]

def changePi(s):
    if s == '':
        return ''
    if s[-1] == 'i' and s[-2] == 'p':
        return changePi(s[:-2]) + '3.14'
    else:
        return changePi(s[:-1]) + s[-1];
    
def noX(s):
    if s == '':
        return ''
    if s[-1] == 'x':
        return noX(s[:-1])
    else:
        return noX(s[:-1]) + s[-1]; 

def array6(a,i):
    if i == len(a):
        return False
    if a[i] == 6:
        return True
    if array6(a,i+1) == True:
        return True
    return False

def array11(a,i):
    if i == len(a):
        return 0
    if a[i] == 11:
        return 1 + array11(a,i+1)
    else:
        return array11(a,i+1)

def array220(a,i):
    if i == len(a)-1:
        return False
    if a[i+1] == 10 * a[i]:
        return True
    if array220(a,i+1) == True:
        return True
    return False

def allStar(a):
    if a == '':
        return ''
    if len(a) == 1:
        return a
    return allStar(a[:-1]) + '*' + a[-1]

def pairStar(s):
    if len(s) == 1:
        return s
    if s[-1] == s[-2]:
        return pairStar(s[:-1]) + '*' + s[-1]
    else:
        return pairStar(s[:-1]) + s[-1]
    
def endX(s):
    if s == '':
        return ''
    if s[0] == 'x':
        return endX(s[1:]) + 'x'
    else:
        return s[0] + endX(s[1:])

def countPairs(s):
    if len(s) == 2:
        return 0
    if s[-1] == s[-3]:
        return countPairs(s[:-1]) + 1
    else:
        return countPairs(s[:-1])

def countAbc(s):
    if len(s) == 2:
        return 0
    if s[-3:] == 'aba' or s[-3:] == 'abc':
        return 1 + countAbc(s[:-1])
    else:
        return countAbc(s[:-1])
    
def count11(s):
    if len(s) == 1 or len(s) == 0:
        return 0
    if s[-2:] == '11':
        return 1 + count11(s[:-2])
    else:
        return count11(s[:-1])

def stringClean(s):
    if len(s) == 1:
        return s
    if s[-1] == s[-2]:
        return stringClean(s[:-1])
    else:
        return stringClean(s[:-1]) + s[-1]
    
def countHi2(s):
    if len(s) == 2 and s == 'hi':
        return 1
    elif len(s) == 2:
        return 0
    if s[-2:] == 'hi' and s[-3] != 'x':
        return 1 + countHi2(s[:-1])
    else:
        return countHi2(s[:-1])

def parentBit(s):
    if s == '':
        return ''
    if ')' in s[:-1]:
        return parentBit(s[:-1])
    elif '(' in s:
        return parentBit(s[:-1]) + s[-1]

    return parentBit(s[:-1])

def nestParen(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return False
    if s[0] == '(' and s[-1] == ')':
        return nestParen(s[1:-1])
    else:
        return False
    if nestParen(s[1:-1]) == False:
        return False

def strCount(s,i):
    if len(s) < len(i):
        return 0
    if s[(-len(i)):] == i:
        return 1 + strCount(s[:(-len(i))],i)
    else:
        return strCount(s[:-1],i)

def strCopies(s,i,n):
    if s == '' and n == 0:
        return True
    elif s == '' and n != 0:
        return False
    if s[(-len(i)):] == i:
        return strCopies(s[:(-len(i))],i,n-1)
    else:
        return strCopies(s[:-1],i,n)

def strDist(s,sub):
    if len(s) == 0:
        return 0
    if s[0:len(sub)] != sub:
        return strDist(s[1:],sub)
    if s[-len(sub):] != sub:
        return strDist(s[:-1],sub)
    return len(s)


print(factorial(5));
print(bunnyEars(10));
print(fibonacci(10));
print(bunnyEars2(5));
print(triangle(5));
print(sumDigits(732235332));
print(count7(7777777777));
print(count8(998817988));
print(powerN(5,5));
print(countX('zxzxcyxy'));
print(countHi('hihijjsihi'))


