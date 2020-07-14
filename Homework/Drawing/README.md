# Passengers
## Score 6
We have a list of place names and their coordinates. Let's say such.
```
[('Brežice', 68.66, 7.04),
 ('Lenart', 85.20, 78.75),
 ('Rateče', -65.04, 70.04)
]

```
Write a function koordict that returns a dictionary whose keys are place names and the values of the corresponding coordinates, for example
```
{'Brežice`: (68.66, 7.04),
'Lenart': (85.20, 78.75),
'Rateče': (-65.04, 70.04)
}
```
- Write a function distance(place, places) that receives the name of the place and a list of places (that is, a list of triplets with name and coordinates). Returns a set of pairs: the second element is the name of all places in the place except the given place, and the first element is the squares of the distances from the given place to these places. The distance call ("Lenart", places) returns
```
{(5415.895699999999, 'Brežice'),
 (22647.921700000003, 'Rateče')
}
```
So calculate the distances as usual, only the result is not rooted. Why so? We will need distances in order to arrange places by distance. It doesn't matter if they are rooted or not. In practical programs, especially if you are in a very hurry (computer graphics, games ...), we can save some time.

- Write a function neighbor(n, place, places) that returns a set with n places that are closest to the given place. Argument places are again triplets.

- Write a function connection(n, places) that returns a dictionary whose keys are all places and the corresponding values of the set n of the nearest places to each place. If we had a few more places on the list, the call connection(3, places) could be returned
```
{'Brežice': {'Ribnica', 'Lenart', 'Rogaška Slatina'},
 'Lenart': {'Brežice', 'Ljutomer', 'Rogaška Slatina'},
 'Ljutomer': {'Brežice', 'Lenart', 'Rogaška Slatina'},
 'Rateče': {'Ribnica', 'Brežice', 'Rogaška Slatina'}
}
```
If we have places all over Slovenia and we want the five closest places of each place, it returns a dictionary whose keys are the places in the picture, and the corresponding values are the sets of all places against which the dashes point.

- Write the function bidirectionally(d). Imagine that d contains all the above links. The bidirectionally(d) function should compile a new dictionary, adding places that "point" to it to the set of neighbors of each place.

At the key "Trbovlje" we have the crowd {"Velenje", "Celje", "Žalec", "Laško", "Radeče"}. However, connections from Gornji Grad and Litija also point to Trbovlje, so it returns the dictionary in which key "Trbovlje" has the value {"Velenje", "Celje", "Žalec", "Laško", "Radeče", "Gornji Grad" , "Lithium"}.



## Score 7
- Write the function valid_path(path, connections), which receives as an argument a path through places, presented with a list of their names, and the connections that return the functions of connection or two-way. The function checks if the path is valid. The path is valid only if it goes through the links located in the dictionary (that is, through the links in the picture above). Places along the way may be repeated, but we should never go back to the place we just came from. The route ["Ljubljana", "Litija", "Domžale", "Ljubljana", "Litija", "Trbovlje"] is valid, the route `` ["Ljubljana", "Litija", "Ljubljana", "Domžale"] ` but not because we immediately returned from Litija to Ljubljana.

- Write a function select(selection, forbidden) that returns a randomly selected item from a list or set selection that is not the same as forbidden. the selection will usually be a multitude of strings and one of them will be banned, but don’t count on it. (Hint: the random.choice (s) function returns a random element of the list s. If you wanted a random element of a set, it would be best to turn that set into a list.)

- Write the function passenger(start, steps, links), which receives the name of the starting place, the number of steps and the dictionary of connections (as in the previous functions). The function returns a random (but valid!) Path in the form of a list of place names. The list will contain steps + 1 items.


## Score 8
- Write a count(s) function that receives a list of s and returns a dictionary whose keys are list items, the corresponding number values that tell how many times that item appeared in the list. (Yes, you are allowed to use any features found in Python's plug-ins).

- Write the function pristej_slovar(s, t), which adds the dictionary t to the dictionary s and does not return anything. The values in both dictionaries are numbers. The function adds to the s dictionary all keys that are in t and were not in s and their corresponding values. For the keys that appear in both dictionaries, however, v is the sum of the corresponding values. (Yes, the function does the same as in the mayoral election homework, and you can copy it from there.)

- Write a function importance(passengers, steps, connections, normalize). The passenger argument is the number of passengers, the steps are the number of steps each of them takes, and the links are the links. So the function times passengers composes a random path (use the features you already have!) To make the steps step by step through the given links. As a result, it returns a dictionary whose keys are the names of the places, and the values tell how many times all the passengers have visited each place together.

The normalize argument can be True or False. If False, the function tells you how many times each place has been visited. If True, divide the number of visits by the total number of visits to all places, so that the sum of all values ​​in the dictionary is equal to 1.


## Score 9
- Write a function spread(places, links) that gets a set of places and a dictionary of links. Returns a set in which all places that are neighbors of the given places and are not already contained in the set are places.

Call expand ({"Ljubljana", "Lenart", "Žužemberk"}) returns a crowd that includes all the places shown in white in the image below.



- Write a function distance(place1, place2, links) that receives the names of the two places and a dictionary of connections. As a result, it returns the length of the shortest path from kraj1 to kraj2. By "path length" we mean the number of connections. The distance from Vrhnika to Laško is 4.



## Grade 10
- Write the function expand2(places, links), which does a very similar thing to expand, only returns a dictionary instead of a set. The keys of the dictionary are places that can be reached from a given set of places, and the corresponding values tell from which place we get to them. In the case from the penultimate picture, we would have the key "Novo mesto" and the corresponding value would be "Žužemberk" and the key "Domžale" with the corresponding value "Ljubljana". The "Velike Lašče" key can have the corresponding value "Ljubljana" or "Žužemberk".

- Write the function najkrajsa_pot(kraj1, kraj2, connections), which returns the shortest path (again in terms of the number of intermediate places) from kraj1 to kraj2. The call najkrajsa_pot("Dioceses", "Lenart", links) can be returned, for example, ["Dioceses", "Ilirska Bistrica", "Sodražica", "Žužemberk", "Novo mesto", "Radeče", "Šentjur", " Slovenska Bistrica "," Maribor "," Lenart "]. Let's just say that this is not the only route of this length - from Šentjur you could also go through Rogaška Slatina and Ptuj. The function must return one of the shortest possible paths.



## Tests
At the end of the tests, this time there is a dessert. :) If you install the drawing module, which also needs the PyQt module (there are currently only old installation instructions in the Classroom, I will update them once by Wednesday), you can draw pictures and animations, as I prepared above. Right at the bottom of the tests are function calls commented out:
```
# task6_links ()
# naloga6_dvosmerno ()
# naloga7_potnik ()
# task8_importance ()
# naloga9_razsiri ()
# task9_distance ()
# naloga10_pot ()
```
For example, if you want a five-passenger animation, delete # before task8_importance(). When you want to run the tests again, add # again. I recommend running only one function at a time.

Another tip: when it comes to the importance feature, don’t be inspired by how the animation works. Tests will not like this. Write on your own.

## Additional tasks
Since some of you will have too much time during the New Year, you can practice your above-average programming skills like this.

- Write a function that finds the shortest path between two places, taking into account the lengths of the connections as well, not just their number.
- Using the cartoonist module or in any other way (and in, for my sake, in any programming language) draw the above images and animations yourself.
