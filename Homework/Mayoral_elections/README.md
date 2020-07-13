# Mayoral elections
## Mandatory task
In order for all mayoral candidates to have equal opportunities, ballot papers with different orders were prepared. Thus, someone can get a list of candidates ["Anna", "Berta", "Cilka"] and someone else ["Cilka", "Anna", "Berta"]. If we circle Cilka on the first ballot paper, we describe such a ballot paper with [False, False, True]. On the second ballot paper, someone surrounded Cilk and Berta (which makes the ballot paper invalid), which we present with [True, False, True].

- Write a function  votes(circled), which as an argument gets a list that says what is circled and what is not, and returns the number of circled candidates. The  call vote([True, True, False, True]) returns 3.

- Write the function  elected(circled, names), which receives a list of those circled (as in the previous task) and a list of names on the ballot paper, and returns the candidate for whom the voter voted. If more than one name is circled or none, the function should return None, as the ballot is not valid.

- Write the function largest(d), which receives the dictionary d as an argument, finds the largest value, and as a result returns a pair containing the corresponding key and this value. The largest call ({"a": 5, "b": 9, "c": 8, "d": 4}) returns ("b", 9). Values can also be negative!

- Write the function pristej(s, t), which "adds" the dictionary t to the dictionary s. If we have s = {"a": 5, "b": 6, "d": 4} and t = {"b": 3, "c": 8}, the call pristaj (s, t) changes sv { "a": 5, "b": 9, "d": 4, "c": 8}. The function returns nothing.

- Write a winner(ballot) function that receives a list of ballots, for example,
```
[([False, True, True], ["Berrta", "Ana", "Cilka"]),
([False, True, True], ["Berrta", "Ana", "Cilka"]),
([False, False, True], ["Ana", "Cilka", "Berrta"]),
([False, True, False], ["Ana", "Berrta", "Cilka"]),
([False, True, False], ["Berrta", "Ana", "Cilka"])
]
```
It must return the name of the candidate with the most votes and the share of votes  on the valid ballot papers. In the example above, the first two ballots are invalid. The winner is Berrta, who received two votes out of three, so the function returns ("Berrta", 2/3).

- Write the function voleni_vec(circled, names), which receives the same data as the elected, but treats all ballots as valid, and distributes the number of votes among all surrounded candidates. The function returns a dictionary whose keys are the names of the surrounded candidates and the value is 1 divided by the number of surrounded candidates. If we call invited_vec([True, False, True, True], ["Ana", "Berta", "Cilka", "Dani"]), the function returns {"Ana": 1/3, "Cilka": 1 / 3, "Days": 1/3}.

## Additional task
Candidates, of course, promise this and that. Let’s say Ana promises a road, a school, and a bike path. Someone wants a road, a bike path, improved public transportation and free ice cream. There is 2 coverage (road and track), and all the things that are in play here are 5 (road, school, track, transportation, ice cream). Therefore, we will say that the match between Ana’s promises and these desires is 2/5, that is, 0.4.

- Write a function match(promises, cabbage) that calculates the match as described in the paragraph above. In doing so, the promises and wishes are a list of strings, for example ["road", "school", "track"].

- Write the function naj_kandidata(candidates, wishes). This one receives a list of couples (candidate name, promises), for example
```
[("Ana", ["road", "school", "trail"]),
 ("Berta", ["school", "ice cream"]),
 ("Cilka", []),
 ("Days", ["ice cream", "trail", "road", "school"])
]
```
and a wish list, for example ["road", "school"]. The function returns the names of the candidates who best match the wishes - first the first and then the second. In order not to be too complicated, you can assume that there will be no equal places.
