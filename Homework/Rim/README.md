# Rim
## Recursive nim - Rome
You will write some of the functions you wrote for the Nim task - only this time they must be recursive.

## Mandatory task
Write the following functions:

- sum(s) returns the sum of the numbers in the specified list. Of course, we already know this from lectures, but program it again anyway. Alone. The sum, we know, is calculated by adding the sum of the others to the first element.

- contains (s, x) returns True if list s contains element x and False if not. The thing is simple: an empty list obviously does not contain x. Otherwise, check that the first element is equal to x, or that x is contained in the rest of the list.

- maximum_potency(n) returns the maximum power of the number 2 that is less than or equal to the given number n. The call maximum_potency(22) returns 16, as 32 would be too much. The call maximum_potency(32) returns 32. You can assume that n is a positive integer.

How to do it recursively? Simple: the maximum power that goes to n is twice the maximum power that goes to n halves (if we use integer division).

Is this true?

* the maximum potency going into 22 is twice that of the maximum potency going into 11;
* the maximum potency going into 11 is twice that of the maximum potency going into 5;
* the maximum power going to 5 is twice the maximum power going to 2;
* the maximum, the power that goes into 2, is twice as large as the maximum power that goes into 1;
* the maximum power that goes into 1 is 1; (... so the greatest power goes to 2, 2; so it goes to 5 4, so it goes to 11 8, so it goes to 22 16).
## Additional task
- break(n) returns a list of powers of the number 2 that add up to the given number n; each potency can occur only once. The call break(22) returns [16, 4, 2]. The numbers should be arranged in descending order. Solve the task by first finding the maximum power with the previous function. You then find a list that represents the breakdown of the residue and add that potency to it (front).

- without (s, x) receives some list s and returns a new list that is the same as the given list, but without x's. Call without ([5, 4, 1, 2, 1, 1, 3], 1) returns [5, 4, 2, 3]. This feature was not in the original Nim task, but it can come in handy for the next task pack.

## Purely additional tasks, to your delight
- difference(s, t) receives two lists and returns a new list containing elements that appear in one of the given lists, but not in both. The call difference ([16, 4, 2], [4, 1]) returns [16, 2, 1] (in this or any other order), as these are numbers that only appear in the first or second list. . Each item in the list with (or t) appears in this list only once. When rescuing, it may (but not necessarily) be worth using the function you programmed earlier.

- break_list(s) receives a list of numbers and returns a list of their breaklists. Call break ([22, 5, 13]) returns [[16, 4, 2], [4, 1], [8, 4, 1]].

- merge_list(s) receives a list of lists (as returned by the break_list) function and returns all items that appear oddly.
