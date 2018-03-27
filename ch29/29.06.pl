writeList([]).
writeList([H|T]) :-
  write(H), 
  nl,
  writeList(T).