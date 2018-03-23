female(alice).
female(beth).
female(bella).
female(daisy).

male(alex).
male(bill).
male(blake).
male(charlie).
male(dave).

parent(alice,bill).
parent(alice,beth).
parent(alice,bella).
parent(alice,blake).
parent(alex,bill).
parent(alex,beth).
parent(alex,bella).
parent(alex,blake).
parent(beth,daisy).
parent(beth,dave).
parent(charlie,daisy).
parent(charlie,dave).


marry(alice,alex).
marry(alex,alice).
marry(beth,charlie).
marry(charlie,beth).

brother(X,Y) :-
	parent(Z,X),
	parent(Z,Y),
	X \= Y,
	male(X),
	male(Y).

sister(X,Y) :-
	parent(Z,X),
	parent(Z,Y),
	X \= Y,
	female(X),
	female(Y).

son(X,Y) :-
	parent(Y,X),
	male(X).

daughter(X,Y) :-
	parent(Y,X),
	female(X).




