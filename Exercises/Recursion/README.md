# Tasks
## Family tree
<img src="https://ucilnica.fri.uni-lj.si/file.php/166/vaje/novak.png" 
alt="tree" />

## List of relatives
Write a function list_name_in_family(name) that lists all names in a particular family.
```
>>> print_name_in_family ('Hans')
Hans
>>> print_name_in_family ('Daniel')
Daniel
Elizabeth
Ludvik
Yuri
Franc
Joseph
Alenka
Alexander
Petra
Barbara
Herman
Margaret
Michael
Hans
```
## Family list
Similar to the previous task, only this time the function family_name(name) should return a list of family names.
```
>>> family_names ('Hans')
['Hans']
>>> family_names ('Daniel')
['Daniel', 'Elizabeth', 'Ludvik', 'Yuri', 'Franz', 'Joseph', 'Alenka', 'Alexander', 'Petra', 'Barbara', 'Herman', 'Margaret', ' Mihael ',' Hans']
```
## The youngest
The youngest_in_family (name) function should return the age and name of the youngest member of a particular family.
```
>>> najmlajsi_v_rodbini ('Hans')
(64, 'Hans')
>>> the youngest_in_family ('Daniel')
(5, 'Alenka')
```
## Depth
Write a depth_to(from_name, to_name) function that tells how deep in the family of the person from_name is the person named do_name.
```
>>> depth_to ('Daniel', 'Hans')
1
>>> depth_to ('Adam', 'Hans')
2
>>> depth_to ('Adam', 'Franc')
4
```
## Path
Solve a similar task as the previous one, except that the path_to(from_name, to_name) function should not return the distance to a certain person, but the path to it.
```
>>> pot_do ('Daniel', 'Hans')
['Daniel', 'Hans']
>>> pot_do ('Adam', 'Hans')
['Adam', 'Daniel', 'Hans']
>>> pot_do ('Adam', 'Franc')
['Adam', 'Daniel', 'Elizabeth', 'Yuri', 'Franc']
```
## Lists
At one time, programmers compiled lists of nesting terks. Poor poor, they had no other choice.

## Convert
Write a convert(xs) function that converts the xs list to this archaic notation.
```
>>> convert ([])
()
>>> convert ([1])
(1, ())
>>> convert ([1, 2])
(1, (2, ()))
>>> convert ([5, 4, 6, 7, 1])
(5, (4, (6, (7, (1, ()))))
```
## Length
Write a function length(s) that calculates the length of the list of nested terks.
```
>>> length (())
0
>>> length (1, ()))
1
>>> length (5, (4, (6, (7, (7, 1,))))))
5
```
## Duplicates
Write a function dup(s) that returns a list where each list item is repeated twice.
```
>>> dup (1, (2, ())))
(1, (1, (2, (2, ()))))
>>> dup ((5, (4, (6, 7, 7, 1, ())))))
(5, (5, (4, (4, (6, (6, (7, (7, (1, (1, (,))))))))))
```
## Reverse
Write a function reverse(s) that returns an inverted list.
```
>>> reverse (5, (4, (6, 6, 7, (1, ()))))))
(1, (7, (6, (4, (5, ()))))
```
## The sum
Write a function sum(s) that sums the elements of the nested list s. Help yourself with the instinct function.
```
>>> isinstance ([1, 2, 3], list)
True
>>> isinstance (1, list)
False
>>> sum ([])
0
>>> sum ([1, 2, 3, 4, 5])
15
>>> sum ([1, [], [2, 3, [4]], 5])
15
```
