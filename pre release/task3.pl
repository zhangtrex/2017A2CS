character(jim).
character(jenny).
character_type(jim,prince).
character_type(jenny,princess).
has_skill(jim,fly).
has_skill(jenny,invisibility).
pet(jim,horse).
pet(jenny,bird).
animal(horse).
animal(bird).
skill(fly).
skill(invisibility).


character(habib).
animal(fish).
skill(time_travel).

pet(habib,fish).
character_type(habib,explorer).
has_skill(habib,timetravel).


onlyonepet(X,Y) :-
  character(X),
  animal(Y).


character(rex).
animal(dog).
skill(singularity).

pet(rex,dog).
character_type(rex,scientist).
has_skill(rex,singularity).

