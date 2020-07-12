# Tasks
## The biggest
Write a function let (xs) that returns the largest number in the xs list. It is ensured that the numbers in absolute value do not exceed $10^{10}$.
```
>>> naj ([5, 1, -6, -7, 2])
5
```
## The greatest absolutist
Write a function naj_abs (xs) that returns the largest number after the absolute value in the xs list.
```
>>> naj_abs ([5, 1, -6, -7, 2])
-7
```
## Number it
Write a number function (xs) that returns a list of the form [(0, xs [0]), (1, xs [1]), ..., (n, xs [n])]. n is equal to the length of the list xs minus one.

You can add new items to the end of the list using the append method.
```
>>> numbers ([4, 4, 4])
[(0, 4), (1, 4), (2, 4)]
>>> numbers ([5, 1, 4, 2, 3])
[(0, 5), (1, 1), (2, 4), (3, 2), (4, 3)]
```
## Body mass index
We have a list of triplets: person's name, weight, height, for example:
```
>>> people = [('Ana', 55, 165), ('Berta', 60, 153)]
```
Write a function bmi (person), which, based on the given list of persons, compiles a list of deuces: name of the person, body mass index.
```
>>> bmi (persons)
[('Ana', 20.202020202020204), ('Berta', 25.63116749967961)]
```
## Body mass index 2
The task is similar to the previous one, except that this time we have the data in a different form:
```
>>> names = ['Ana', 'Berta']
>>> thesis = [55, 60]
>>> height = [165, 153]
>>> bmi2 (names, theses, heights)
[('Ana', 20.202020202020204), ('Berta', 25.63116749967961)]
```
## Prime numbers
Write a function prime_numbers(n) that determines how many prime numbers are smaller than the number n.
```
>>> primitives (10)
4
```
Prime numbers less than 10 are 2, 3, 5, and 7.

The task has two versions of the tests: the easier one should be solved by everyone, and the harder one only the most bitten, as it goes beyond the scope of this subject (hint: Eratosthenes sieve). If you want to test your program with more difficult tests, you need to uncomment them.

## Palindrome
Write a palindrome(s) function that checks if the string is a palindrome. Help yourself with the reversed function.
```
>>> palindrome ('pericarezeracirep')
True
>>> palindrome ('perica')
False
```
## Palindrome numbers
The largest palindrome number that can be obtained as the product of two two-digit numbers is 9009 = 91 * 99. Write the function palindrome_number (), which finds and returns the largest palindrome number that can be obtained as the product of two three-digit numbers.
Source: Project Euler, Problem 4.

## Inversions
Write an inversion function (xs) that counts and returns the number of inversions in the xs list. The list itself contains different numbers! An inversion is a pair of numbers in which the larger number in the list appears before the smaller one. There are four inversions in the list xs = [1, 4, 3, 5, 2]
```
>>> inversions ([1, 4, 3, 5, 2])
4
```
A four appears in front of a triple and a deuce. A triple appears in front of a deuce and a five appears in front of a deuce.
