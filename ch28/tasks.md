task 28.01

LDM #2
STO A
LDM #10
STO B
LDD A
ADD B
STO C
LDD A
LDD B
XOR #&FF
INC ACC
ADD A
STO D

task 28.02

LDD A
CMP #0
JMP ELSE
STO B
JMP ENDIF
LDD B
DEC ACC
STO B

task 28.03

LDM #1 
STO Number 
LDM #0 
STO Total 
LDM #5 
STO Max 
LOOP: 
LDD Number 
ADD Total 
STO Total 
LDD Number 
INC ACC 
CMP Max 
JPN 
LOOP

28.04 
LDM 0 
STO Count 
LOOP: 
INC Count 
IN 
CMP #N 
JPN 
LOOP

28.05 
LDM 0 
STO Count 
LOOP: 
INC Count 
IN 
CMP #N 
JPN 
LOOP 
OUT

28.06

LDM 0 
STO Count 
LOOP: 
INC Count 
IN 
STO 
JPN 
LOOP 
OUT

1.a To run AND two binary things together .

b #AND 00001111

c 
IN 
AND Mask 
LSL #4 
STO R 
IN 
AND Mask 
OR R 
STO R 
END

LDR #0 
LOOP: 
IN 
STO STRING
INC IX 
CMP #33 
JPN Loop 
END


