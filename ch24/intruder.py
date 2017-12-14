#Zhang Chenyang Rex FSM

# ACTION:
# PB for Press button
# EP for Enter PIN
# SA for Sensor activated
# 2MP for 2 minutes pass
# STATE:
# SI for system inactive
# SA for system active
# AM for Alert mode
# ABR for Alarm bell rings

State = 'Start';
if State == 'Start':
    State = 'SI';
print();
print('system inactive');
print();
while True:
    print('PB for Press button');
    print('EP for Enter PIN');
    print('SA for Sensor activated');
    print('2MP for 2 minutes pass');
    print('input the action, if you want to quit, entry QUIT');
    Act = input('Entry: ');
    if Act == 'QUIT':
        break
    if State == 'SI':
        if Act == 'PB':
            State = 'SA';
        else:
            pass
    elif State == 'SA':
        if Act == 'EP':
            State = 'SI';
        elif Act == 'PB':
            State = 'SA';
        elif Act == 'SA':
            State = 'AM';
        else:
            pass
    elif State == 'AM':
        if Act == 'PB':
            pass
        elif Act == 'EP':
            State = 'SI';
        elif Act == '2MP':
            State = 'ABR';
    elif State == 'ABR':
        if Act == 'EP':
            State = 'SI';
        elif Act == 'PB':
            pass
        else:
            pass
    if State == 'SI':
        print();
        print('///////////////////');
        print('/                 /');
        print('/ System inactive /');
        print('/                 /');
        print('///////////////////');
        print();
    elif State == 'SA':
        print();
        print('/////////////////');
        print('/               /');
        print('/ System active /');
        print('/               /');
        print('/////////////////');
        print();
    elif State == 'AM':
        print();
        print('//////////////');
        print('/            /');
        print('/ Alert mode /');
        print('/            /');
        print('//////////////');
        print();
    elif State == 'ABR':
        print();
        print('////////////////////');
        print('/                  /');
        print('/ Alarm bell rings /');
        print('/                  /');
        print('////////////////////');
        print();
        for i in range(10):
            print('ring!!!')
        print();
            





        
