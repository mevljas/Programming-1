# Tasks
## Duplicate elements
Write a duplicate(xs) function that retains only the first occurrence of each element in the xs list and returns a new list.
```
>>> split ([5, 1, 3, 1, 1, 3, 8])
[5, 1, 3, 8]
```
## Eboran
Write a function eboran(s) that receives a string s or sentence (written as words with spaces without punctuation) and returns a new sentence in which all words are inverted.
```
>>> eboran ('this sentence is all wrong too')
'esv ej eboran idut elat kevats'
```
## Cube
Instead of one dice with six sides, some games use different dice. We describe the different possibilities with standard notation: a string of 3d8, for example, means that you roll a cube with eight sides three times and add up the results of individual throws. Write a throw function(cube) that accepts such a string, simulates the corresponding number of dice rolls with a given number of pages, and returns the result.
```
>>> roll ('3d4') # three throw dice with four sides
10
>>> throw ('3d4')
7
>>> throw ('1d20')
16
>>> throw ('20d1') #slightly nonsensical cube with one side
20
Tip: See the functions in the random module.
```
Write also the function expected_value (cube, n), which simulates throwing a given cube n times and returns the average result.
```
>>> expected_value ('3d4', 1000)
7,523 th most common
```
## Day
Write a function day(d, m, l) that returns the name of the day of the week for the given date.
```
>>> day (1, 10, 2018)
'Monday'
```
Tip: See the functions in the calendar module.

## Largest file
Write a maximum(path) function that returns the name of the largest file in the path directory.
```
>>> najvecja ('c: / Users / me / Downloads')
'elephants-dream.mp4'
```
There are no test cases for this feature. Tip: See the functions in the os and os.path modules.

## An ban pet podgan
Write the function an_ban_pet_podgan(xs), which looks for the winner in the countdown "An ban pet podgan" for the list of xs. The winner of the game is the one who is left alone in the end.
```
>>> an_ban_pet_podgan [["Maja", "Janja", "Sabina", "Ina", "Jasna"])
'Jasna'
>>> an_ban_pet_podgan (["Maja", "Janja", "Sabina"])
'Maja'
```
For those of you who have forgotten a little; the whole count reads: "an ban, pet podgan, stiri misi, v'uh-me pisi, vija, vaja, ven." (11 clenov).

## Bogosort
Bogosort is one of the stupider sorting algorithms: it sorts the list by checking that it is organized for each permutation of the elements. (How long will it take on average to find the appropriate permutation?) Write a bogosort (list) function that accepts a list of numbers and returns a new list with the same numbers sorted by size. The permutations function from the itertools module will help you. Do not use the sorted function or the list.sort method for this task.

## XKCD
Write a function xkcd() that returns the title of the currently published xkcd comic.
```
>>> xkcd ()
'Curve-Fitting'
```
Tip: to get the content of the web page at <url>, import the urllib.request module and run:
```
>>> urllib.request.urlopen (<url>) .read (). decode ('utf-8')
'<! DOCTYPE html> \ n <html> \ n <head> \ n…'
```
