capital(vienna).
capital(london).
capital(santiago).
capital(caracas).
capital(tokyo).
cityin(vienna, austria).
cityin(santiago, chile).
cityin(salzburg, austria).
cityin(maracaibo, venezuela).
continent(austria, europe).
continent(chile, southAmerica).
continent(uk, europe).
continent(argentina, southAmerica).
iVisited(vienna).
iVisited(tokyo).
capitalOf(City, Country) :-
  capital(City),
  cityin(City, Country).
europeanCity(City) :-
  cityin(City, Country),
  continent(Country, europe).


/* a */
cityin(london, uk).
iVisited(strasbourg).

/* b */
/* argentina, chile */

/* c */
countriesIVisited(Country) :-
  cityin(City,Country),
  iVisited(City).

/* task 2 */
minimumAge(car, 18).
minimumAge(truck, 21).
age(fred, 19).
age(jack, 22).
age(mike, 17).
age(jhon, 20).
age(emma, 22).
age(sheena, 19).
hasLicence(fred).
hasLicence(jack).
hasLicence(mike).
hasLicence(jhon).
hasLicence(emma).
hasLicence(sheena).
allowedToDrive(X, V) :-
  hasLicence(X),
  minimumAge(V, L),
  age(X, A),
  A >= L.
passedTheoryTest(jack).
passedTheoryTest(emma).
passedTheoryTest(jhon).
passedTheoryTest(fred).
passedDrivingTest(jhon, car).
passedDrivingTest(fred, car).
passedDrivingTest(jack, car).
passedDrivingTest(jack, truck).
passedDrivingTest(sheena, car).
qualifiedDriver(X, V) :-
  allowedToDrive(X, V),
  passedTheoryTest(X),
  passedDrivingTest(X, V).


/* a */
/* age is a fact */
/* allowedtodrive is a rule */

/* b */
/* jack */
/* false */
/* false */

/* c */
/* qualifiedDriver(X,V). */
passTnotD(X) :-
  passedTheoryTest(X),
  not(passedDrivingTest(X,Y)).

/* d */
/* hasLicence(mike). return true */
/* minimiumAge(car,L). return L = 18 */
/* age(mike,A). return A = 17 */
/* A >= L. 17 >= 18 return false */
/* true and false return false */




