factorial(1, 1).
factorial(N, F) :-
  M is N - 1,
  factorial(M, X),
  F is N * X.
