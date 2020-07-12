# Tasks
All tasks can be solved nicely with derived lists and derived sets. For and while loops are banned today. Focus on using derived lists.

## The sum of squares
Write a function of the sum_of_ squares(n), which calculates the sum of the squares of the first n natural numbers.

$1^2 + 2^2 + 3^2 ... + 10^2 =? $
```
>>> sum of squares (10)
385
```
Write a function sum_of_squares_pal_(n), which will calculate the sum of squares of all palindrome numbers less than or equal to n? . Palindrome numbers are those that are read from both sides equally. An example of a palindrome number is 12321.

$1^2 + 2^2 + ... + 323^2 + 333^2 + 343^2 + ... + 999^2 =? $
```
>>> sum_of_square_pal(1000)
33454620
```

## Swap letters
Write a function subs(string, position) that moves the letters in a string according to the given new positions.
```
>>> subs ("abc", "0002")
'aaac'
>>> subs ("mosquito", "23401")
'marko'
```
## Mean and standard deviation
Write functions that calculate the mean and standard deviation of the population given by the list of numbers xs.

The standard deviation in the tests is calculated by the formula $\sigma =\sqrt {\frac {\sum_{i=1}^N(x_i-{\overline x})^2}{N}}$.
```
>>> xs = [183, 168, 175, 176, 192, 180]
>>> mean (xs)
179.0
>>> std (xs)
7.43863786814
```
## Morse code
Write the function txt2morse(s), which converts the message s to the Morse code, and the function morse2txt(s), which does the opposite.
```
>>> txt2morse('TE A')
'- .  .-'
>>> txt2morse('HELLO WORLD')
'.... . .-.. .-.. ---  .-- --- .-. .-.. -..'
>>> morse2txt('.... . .-.. .-.. ---  .-- --- .-. .-.. -..')
'HELLO WORLD'
```
In case you forgot, or maybe you never knew, the Morse code looks like this:
```
'A': '.-',
'B': '-...',
'C': '-.-.',
'D': '- ..',
'E': '.',
'F': '..-.',
'G': '-.',
'H': '....',
'I': '..',
'J': '.---',
'K': '-.-',
'L': '.- ..',
'M': '-',
'N': '-.',
'O': '---',
'P': '.--.',
'Q': '--.-',
'R': '.-.',
'S': '...',
'T': '-',
'U': '..-',
'V': '...-',
'W': '.--',
'X': '-..-',
'Y': '-.--',
'Z': '- ..',
'1': '.----',
'2': '..---',
'3': '...--',
'4': '....-',
'5': '.....',
'6': '-....',
'7': '--...',
'8': '--- ..',
'9': '----.',
'0': '-----',
```
## Invert
Write an invert(t) function that will invert (transpose) a 2D table t given as a list of lists of equal lengths. \
```
>>> t = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
>>> turn (t)
[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
## ISBN
Write a valid(s) function that verifies that the specified ISBN is valid.
```
>>> valid ('0306406152'), valid ('0553382578'), valid ('0553293370'), valid ('912115628X') # example valid ...
(True, True, True, True)
>>> valid ('03064061522'), valid ('1553382578'), valid ('91211562811') # ... and invalid ISBN.
(False, False, False)
```
