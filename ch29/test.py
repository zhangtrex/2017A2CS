class Toy(object):
    def __init__(self,n,i,p,m):
        self.__name = n;
        self.__ID = i;
        self.__price = p;
        self.__minimumage = m;
    def GetName(self):
        return self.__name
    def GetID(self):
        return self.__ID
    def GetPrice(self):
        return self.__price
    def GetMinimumAge(self):
        return self.__minimumage
    def SetName(self,n):
        self.__name = n;
    def SetID(self,i):
        self.__ID = i;
    def SetPrice(self,p):
        self.__price = p;
    def SetMinimumAge(self,m):
        self.__minimumage = m;
    def PrintDetails(self):
        print(self.__name,self.__ID,self.__price,self.__minimumage);
    
class ComputerGame(Toy):
    def __init__(self,n,i,p,m,c,co):
        Toy.__init__(self,n,i,p,m);
        self.__category = c;
        self.__console = co;
    def GetCategory(self):
        return self.__category
    def GetConsole(self):
        return self.__console
    def SetCategory(self,c):
        self.__category = c;
    def SetConsole(self,co):
        self.__console = co;
    def PrintDetails(self):
        print('computer game');
        Toy.PrintDetails()
        print(self.__category,self.__console);

class Vehiche(Toy):
    def __init__(self,n,i,p,m,t,h,l,w):
        Toy.__init__(self,n,i,p,m);
        self.__type = t;
        self.__height = h;
        self.__length = l;
        self.__weight = w;
    def GetType(self):
        return self.__type
    def GetHeight(self):
        return self.__height
    def GetLength(self):
        return self.__length
    def GetWeight(self):
        return self.__weight
    def SetType(self,t):
        self.__type = t;
    def SetHeight(self,h):
        self.__height = h;
    def SetLength(self,l):
        self,__length = l;
    def SetWeight(self,w):
        self.__weight = w;
    def PrintDetails(self):
        print('vehiche');
        Toy.PrintDetails();
        print(self.__type,self.__height,self.__length,self.__weight);
        





    
