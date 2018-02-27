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

Set = [Car('',-1,'') for i in range(100)];
Set[0] = Car('Ford',2011,'Z');
Set[1] = Car('Ferrari',2008,'R');
Set[2] = Car('Benz',2007,'Z');
Set[3] = Car('BMW',2011,'R');
Set[4] = Car('Audi',2017,'Z');
def add(n,y,o):
    i = 0;
    while True:
        if Set[i].name == '':
            Set[i] = Car(n,y,o);
            break
        else:
            i = i + 1;
        if i == 100:
            print('no free space')
            break

def save():
    file = open('CarData.DAT','rb+');
    for i in range(100):
        pickle.dump(Set[i],file);
    file.close();

def load():
    file = open('CarData.DAT','rb');
    Set1 = [];
    for i in range(5):
         Set1.append(pickle.load(file));
    print(Set1)
