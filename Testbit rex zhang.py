def Testbit(num,bit):
    b = num>>bit;
    if b%2 == 1:
        return 1
    else:
        return 0

def Setbit(num,bit):
    if Testbit(num,bit) == 1:
        return num
    else:
        b = 1<<bit;
        return b + num

def Clearbit(num,bit):
    if Testbit(num,bit) == 0:
        return num
    else:
        b = 1<<bit;
        return num - b

def Togglebit(num,bit):
    b = 1<<bit;
    if Testbit(num,bit) == 0:
        return num + b
    else:
        return num - b
