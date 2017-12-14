Num = 37;
Find = 0;
List = [12,19,23,27,33,37,41,45,56,59,60,62,71,75,80,84,88,92,99];
Init = 0;
Fin = len(List)-1;
while Find == 0:
    a = int((Init + Fin)/2);
    if List[a] == Num:
        print(a+1);
        break
    elif List[a] > Num:
        Init = Init;
        Fin = a-1;
    else:
        Init = a+1;
        Fin = Fin;
    if Init > Fin:
        print('search not found');
        break
        
