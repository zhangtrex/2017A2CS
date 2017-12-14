# Rex S3 OP1
l=[123,321,132,231,312,456,111];
n = 6
for i in range(6):
    for j in range(n):
        if l[j]>l[j+1]:
            d=l[j];
            l[j]=l[j+1];
            l[j+1]=d;
    n=n-1;
print(l);
            
