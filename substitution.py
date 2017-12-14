C = [[0 for i in range(8)] for j in range(8)];
ACC = 1;
for i in range(8):
    for j in range(8):
        C[i][j] = ACC;
        ACC = ACC + 1;

def Substitution(IC):
    NC =[[0 for i in range(8)] for j in range(8)];
    for i in range(8):
        NC[0][i] = IC[7-i][1];
        NC[1][i] = IC[7-i][3];
        NC[2][i] = IC[7-i][5];
        NC[3][i] = IC[7-i][7];
        NC[4][i] = IC[7-i][0];
        NC[5][i] = IC[7-i][2];
        NC[6][i] = IC[7-i][4];
        NC[7][i] = IC[7-i][6];
    return NC

def Output():
    for i in range(8):
        for j in range(8):
            if len(str(C[i][j])) == 1:
                print(C[i][j],' ',end='');
            else:
                print(C[i][j],'',end='');
        print('');
for i in range(16):
    C = Substitution(C);
    Output()
    print()
