factorial(1, 1).
factorial(N, F) :-
  M is N - 1,
  factorial(M, X),
  F is N * X.

bunnyEars(0, 0).
bunnyEars(N, F) :-
  M is N - 1,
  bunnyEars(M, X),
  F is X + 2.

fibonacci(0,0).
fibonacci(1,1).
fibonacci(X,Y) :-
  M is X - 1,
  N is X - 2,
  fibonacci(M,A),
  fibonacci(N,B),
  Y is A + B.

bunnyEars2(0,0).
bunnyEars2(X,Y) :-
  M is X - 1,
  bunnyEars2(M,Z),
  A is M mod 2,
  Y is Z + 2 + A.

triangle(0,0).
triangle(X,Y) :-
  M is X - 1,
  triangle(M,Z),
  Y is Z + M + 1.

sumDigits(0,0).
sumDigits(X,Y) :-
  A is X div 10,
  B is X mod 10,
  sumDigits(A,Z),
  Y is B + Z.

count7(0,0).
count7(X,Y) :-
  A is X div 10,
  B is X mod 10,
  C is B div 7,
  D is B div 8,
  count7(A,Z),
  Y is Z + C - D.