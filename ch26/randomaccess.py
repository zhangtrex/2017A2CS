# pickle.dump
# zhang chenyang Rex
import pickle
class Car(object):
    def __init__(self, name, year, owner):
        self.name = name;
        self.year = year;
        self.owner = owner;
    def __repr__(self):
        return "(%s,%s,%s)"%(self.name,self.year,self.owner);

def add():
    n = ''; # name
    y = ''; # year
    o = ''; # owner
    while n == '' or len(n) > 20:
        n = input('name of car: ');
        if len(n) > 20:
            print('maximum 20 characters');
    while y == '' or len(y) != 4:
        y = input('year of purchase, must >= 2000');
        for i in y:
            if i not in '1234567890':
                y == '';
                print('incorrect format');
        if len(y) < 4:
            print('year not possible');
    while o == '' or len(o) > 10:
        o = input('owner of car');
        if len(o) > 10:
            print('maximum 10 characters');

    return Car(n+(20-len(n))*' ',int(y),o+(10-len(n))*' ');

def hashf(y):
    return y - 2000;

def save(car):
    file = open('Cars.dat','rb+');
    address = hashf(car.year);
    address = address * 110 + 1;
    file.seek(address);
    pickle.dump(car,file);
    file.close();

def find(year):
    file = open('Cars.dat','rb');
    address = hashf(year) * 110 + 1;
    file.seek(address);
    c = pickle.load(file)
    print(c);
    file.close();

file = open('Cars.dat','wb');
file.close()
a = Car('laferrari           ',2002,'rexzzz    ');
b = Car('veryhandsome666     ',2007,'zzzcccyyy ');
c = Car('wulinghongguang     ',2006,'obmc      ');
save(a);
save(b);
save(c);
find(2002);
find(2006);
find(2007);


