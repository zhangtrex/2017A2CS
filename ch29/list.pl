my_last(X,[X]).
my_last(X,[_|Y]) :-
  my_last(X,Y).

my_2last(X,[X,_]).
my_2last(X,[_|Y]) :-
  my_2last(X,Y).

k_ele(X,[X|_],1).
k_ele(X,[_|Y],Z) :-
  A is Z - 1,
  k_ele(X,Y,A).

number([],0).
number([_|T],L) :-
  number(T,X),
  L is X + 1.

myappend([],L,L).
myappend([H|T],L,[H|R]) :-
  myappend(T,L,R).

reverse([],X,X).
reverse([H|T],R,L) :-
  reverse(T,R,[H|L]).

palindrome(X) :-
  reverse(X,Y,[]),
  Y == X.

  