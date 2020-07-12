# Tasks
## Contains
Write a program that determines whether the list of numbers contains the number 42. Define the list at the top of the program:
```
xs = [42, 5, 4, -7, 2, 12, -3, -4, 11, 42, 2]
```
At the end of the program, write:
```
print (videl_sem_42)
if videl_sem_42:
    print ("I really saw 42.")
    ```
There should be no other prints in the program.

The program should print True or False (only once!) And then I really saw 42 if it printed True previously.

Of course, the program must work for any lists and not just for the list in the example. The program will also test if the list does not contain 42.

## Contains a string
Same as the "Contains" task, only this time we will look for the 'Waldo' string in the list of strings. The program should start with
```
xs = ['foo', 'bar', 'baz', 'Waldo', 'foobar']
```
and prints True or False.

## Count
Write a program that counts the number of repetitions of the number 42 in the given list. Define the list at the top of the program as in the first task, and the printout should be as followed: 'The number 42 appears 2 times in the list.'

## Contains a multiple
Write a program that prints True if a multiple of 42 appears in the list of numbers, otherwise it prints False.

## Only multiples
Write a program that prints True if the list of numbers contains only multiples of the number 42, otherwise it prints False.

## Dividers
Write a program that lists all divisors of the number entered by the user.

## The sum of divisors
Write a program that prints the sum of all divisors of the number entered by the user.

## Perfect numbers
Write a program that tells if the given number is perfect. Complete numbers are numbers that are equal to the sum of their divisors (without itself). An example of a perfect number is 28, since it's divisors are 1, 2, 4, 7, 14, and their sum, 1 + 2 + 4 + 7 + 14 is again equal to 28.

## Friendly numbers
220 and 284 are friendly numbers. The divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110. If we add them up, we get 284. The divisors of 284 are 1, 2, 4, 71 and 142. The sum of these numbers is is 220. Write a program to which the user enters a number. The program checks to see if it has this number of friends and, if it has one, displays it. If it doesn't have it, it says that it doesn't have it. Example: if the user enters 220, the program answers 284. If the user enters 222, the program replies that 222 has no friends.

## Prime number
Write a program that checks if a given number is a prime number.

## Prime numbers
Write a program that prints prime numbers between 2 and 100.

## Movies
A list of films and their ratings (on imdb) is given.
```
movies = [
    ('Poletje v skoljki 2', 6.1), 
    ('Ne cakaj na maj', 7.3), 
    ('Pod njenim oknom', 7.1),
    ('Kekec', 8.1), 
    ('Poletje v skoljki', 7.2), 
    ('To so gadi', 7.7),
]
```
Write a program that prints

- names of all films with a score of at least 7.0,
```
Ne cakaj na maj
Pod njenim oknom
Kekec
Poletje v skoljki
To so gadi
```
- the name of the film with the highest rating,
```
Kekec
```
- the name of the first film in the list with a score of at least 7.0,
```
Ne cakaj na maj
```
- average rating of all films in the list,
```
7.25
```
- the names of all the films in which the second part was also shot.
```
Poletje v skoljki
```
## Cinema 2
What if movies and ratings are listed separately?
```
movies = ['Poletje v skoljki 2', 'Ne cakaj na maj', 'Pod njenim oknom', 'Kekec', 'Poletje v skoljki', 'To so gadi']
ratings = [6.1, 7.3, 7.1, 8.1, 7.2, 7.7]
```
Write a program that lists the names and ratings of movies whose titles are made up of three words (contain two spaces).
```
Pod njenim oknom (7.1)
Poletje v skoljki (7.2)
To so gadi (7.7)
```
