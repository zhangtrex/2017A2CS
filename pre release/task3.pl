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

/* 3.1 */
character(habib).
animal(fish).
skill(time_travel).

pet(habib,fish).
character_type(habib,explorer).
has_skill(habib,timetravel).

/* 3.2 */
pet(jim,bird).
onlyapet(X,Y) :-
  animal(Y),
  character(X).

/* 3.3 */
character(rex).
animal(dog).
skill(singularity).

pet(rex,dog).
character_type(rex,scientist).
has_skill(rex,singularity).

/* 3.4 */
/* true
 princess
 jim
 invisibility
 jim
*/

/* 3.5 */
/* pet(jim,Y).
 has_skill(X,fly).
 skill(X).
 character_type(X,princess),pet(X,Y). */

