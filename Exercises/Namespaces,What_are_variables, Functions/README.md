# Tasks
## List of names
Write a capitalize(xs) function that accepts a list of names and returns a new list in which all names begin with a capital letter. Help yourself with the capitalize() array method. The xs list must remain unchanged after the function call.
```
>>> names = ['marko', 'Miha', 'maja', 'Monika']
>>> capitalize (names)
['Marko', 'Miha', 'Maja', 'Monika']
>>> names
['marko', 'Miha', 'maja', 'Monika']
```
Write the icapitalize(xs) function, which changes the given list so that all names begin with a capital letter.
```
>>> names = ['marko', 'Miha', 'maja', 'Monika']
>>> icapitalize (names)
>>> names
['Marko', 'Miha', 'Maja', 'Monika']
```
## Replacements
Write a function replaced(s, swap) that receives a list of s and a swap dictionary. Returns a new list in which all list items that act as keys in the dictionary are replaced with the corresponding values. Leave items that do not appear in the dictionary alone. The replaced function must not change the specified list with.
```
>>> replaced (["Ana", "Ana", "Berta", "Ana", "Cilka"], {"Ana": "Peter", "Berta": "Ana"})
["Peter", "Peter", "Ana", "Peter", "Cilka"]
```
In addition, write a similar function replace(s, swap), which does not return anything but changes the specified list s accordingly.
```
>>> names = ["Ana", "Ana", "Berta", "Ana", "Cilka"]
>>> replace (names, {"Ana": "Peter", "Berta": "Ana"})
>>> names
["Peter", "Peter", "Ana", "Peter", "Cilka"]
```
## Alternate
Write an function alternate(s) that receives a list of numbers and changes it by removing all numbers up to the next negative number after each positive number, and all numbers up to the next positive number after each negative number. The function should change the specified list and not return anything. In other words, the function retains the first element of each sequence of positive or negative numbers.
```
>>> list = [3, 4, -1, 1, -5, -2, -1, 7, -8]
>>> alternate (list)
>>> list
[3, -1, 1, -5, 7, -8]
```
## Double it
Your task is to write two versions of the function that duplicates the list of lists: from [1,2], [3], [7,1,2]] becomes [1,2], [3], [7,1, 2], [1,2], [3], [7,1,2]]. Functions change the specified list and do not return anything.

The add-same(s) function should duplicate the list by adding the same elements to the end, and the add-the-same (s) function should add the same (but not the same). See the following examples:
```
>>> s = [[1,2], [3], [7,1,2]]
>>> add_same (s)
>>> s [0] .clear ()
>>> s
[[], [3], [7,1,2], [], [3], [7,1,2]]

>>> s = [[1,2], [3], [7,1,2]]
>>> add_enak (s)
>>> s [0] .clear ()
>>> s
[[], [3], [7,1,2], [1,2], [3], [7,1,2]]
```
## Duplicates
Write a unify(s) function that will change the specified list with so that the same list items are actually the same.
```
>>> s = [[1,2], [3], [1,2], [1,2], [3]]
>>> points (s)
>>> s [2] .append (9)
>>> s
[[1, 2, 9], [3], [1, 2, 9], [1, 2, 9], [3]]
```
The opposite problem is if we want to quickly create a list of lists, for example s = [[]] * 10. Write an exception(s) function that will make sure that the same items are not in the list (it will replace them with the same ones).
```
>>> s = [[]] * 10
>>> s [0] .append (1)
>>> s
[1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
>>> except for (s)
>>> s [1] .append (2)
>>> s
[1], [1, 2], [1], [1], [1], [1], [1], [1], [1], [1]]
```
## Take a picture
Write a picture function that accepts the function f and the list [x_1, x_2, ..., x_n] and returns a new list [f (x_1), f (x_2), ..., f (x_n)].
```
>>> paint (abs, [-5, 8, -3, -1, 3])
[5, 8, 3, 1, 3]
>>> paint (len, "Daydream delusion limousine eyelash" .split ())
[8, 8, 9, 7]
```
