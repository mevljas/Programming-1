# Tasks 
Some tasks require the use of mathematical constants and functions such as pi, sqrt (square root), sin, cos and the like. Python doesn't have them, but it mysteriously gets them if we add to the beginning of the program:
```
from math import *
```
## Temperature conversion
The program you wrote in the lectures:
```
temp_C = float (input ("Temperature [C]?"))
temp_K = temp_C + 273.15
temp_F = temp_C * 9/5 + 32
print (temp_C, "C is equal to", temp_K, "K or", temp_F, "F")
```
change by converting from Fahrenheit degrees to Celsius and Kelvin. The list of programs should look like this:
```
Temperature [F]? TYPE USER 42
42.0 F is equal to 278.7055555555555 K or 5.555555555555555 C
```
## Circle
Write a program that calculates the area and perimeter of a circle whose radius is given by the user. (You will get the constant π if you write pi, if you wrote from math import * at the beginning of the program, as described above.)
```
The radius of the circle? USER WRITES 4.2
Circle circumference: 26.389378290154262
Circle area: 55.41769440932395
```
## Pythagora's theorem
Write a program that asks the user about the lengths of the legs of a right triangle and prints the length of the hypotenuse. As it says at the top of the page, we use the sqrt function for the root, which we get if we write from math import * at the beginning of the program.
```
Kateta? TYPE USER 3
Kateta? TYPE USER 4
Hypotenuse: 5.0
```
## Well
If we throw a stone into a well and there is water in the well, after a while a chop is heard. Write a program to which the user enters how much time has passed from the moment we dropped the stone to the moment it said chof, and the program displays the depth of the well. If you don't know the equations, use wikipedia
```
Time [s]? TYPE USER 1
Depth of well: 4,905 m
```
## Body mass index
Write a program that asks the user how tall (in centimeters) and how heavy (in kilograms) he/she is. In response, display the user's body mass index (BMI).
```
Height [cm]? TYPE USER 180
Weight [kg]? TYPE USER 75
Body Mass Index: 23.1481481481
```
## Average rating
Write a program in which the user enters the grade given to Ana, Benjamin and Cilka in mathematics. The program should calculate and print the average grade.

A challenge for thinking types: let’s say you don’t want to print an average but a medium grade. If Ana, Benjamin and Cilka got 3, 2 and 5, they would like to print 3. Challenge: program this thing without using conditional sentences or something "advanced". Specifically, use only the input, print, min, and max functions. Tip: min and max can receive any number of arguments. Also think about the fact that you only have three people; at four, that trick wouldn’t work.
```
Rating [Ana]? TYPE USER 2
Rating [Benjamin]? TYPE USER 4
Rating [Cilka]? TYPE USER 5
Average: 3.6666666666666665
Mean value: 4.0
```
An even better challenge: let’s say we have four numbers, a, b, c, and d. We want to print the third number by size. We still use only max and min. Tip: it may be worth calling min and max with only two arguments, but several times. Maybe there is also some solution where we call with more arguments. Maybe; I do not know. :)

# The area of a triangle
Write a program that asks the user about the lengths of the sides of any triangle and displays it's area, and the area of the inscribed and delineated circle.
```
Page length a? TYPE USER 3
Page length b? TYPE USER 4
Page length c? TYPE USER 5
Area of the triangle: 6.0
Surface of the inscribed circle: 3.141592653589793
Area of outlined circle: 19.634954084936208
```
## Quick fingers
If we write at the beginning of the program
```
from time import *
```
we will, among other things, get a time function that returns time in seconds from some point in the distant past. Write a program that asks the user how much is 6 times 7. The user will change his mind and enter the answer. The program should not deal with the answer and whether it is correct or not, but should list how many seconds the person needed to think.

Tip: If you know what time it was before the call to the input function and what time it was after the call, you can calculate how much time has passed in between.
```
What is 6 times 7? TYPE USER 42
You spent 2.503019332885742 s thinking.
```
## Thinking machine
Write a program that asks the user for two numbers. The program prints their product. However, in order to give the impression that he is thinking, he does not print the product immediately, but waits a bit beforehand. To wait, use the sleep function, which you get if it is written at the beginning of the program
```
from time import *
```
You can write three versions of the program. After one, he always waits three seconds. Secondly, he waits randomly long; how long it will wait, you draw with the randint function (for which it is necessary to write from random import * at the beginning of the program); wait between one and five seconds. The third is this: the bigger the product, the harder the bill. The computer should wait as many seconds as the product divided by 10. If it can be multiplied by 6 and 7, wait 4.2 seconds before printing.
```
The first number? TYPE USER 6
Another number? TYPE USER 7
42.0
```
  
# Those who are bored by this task ...
... and because they might complain, they can have fun with things we haven’t learned otherwise.

***You already know how to program, but not in Python?*** Then you know that there are if and while and such things. Write a program that tells you how far you need to shoot. The user must enter different angles and speeds until he hits the target at a given distance. The target is hit if the difference between the actual and actual lightning length is less than so much and so much.

***Already know how to program, and that in Python?*** Somewhere between the cannon and the target is a tree (it can also be very tall; maybe a bean going into the sky). On the branch of this tree (or bean) sits a pig. We would like to hit the pig and the target with the same bullet. So write a program that reads the distance to the target and the distance and height of the pig. The program should display the angle and speed at which the bullet should be fired.

There are two ways to solve the second task. You can write a program that tries to find a solution by one way or another. However, you can use your knowledge of physics or mathematics. Or, better yet, use both.
  
# Task: Two programs that should be fixed
This one should calculate Pythagora's theorem, but it doesn't.
```
a = imput ("first leg")
b = imput ("second leg")
c = sqrt (a ^ 2 + b ^ 2)
print (The length of the hypotenuse is, c)
```

This one asks for two numbers and their product, and displays the user's answers and the right product. But it doesn’t work either!
```
name = input ("What's your name?")
print ("Hello, ', name,' would you practice counting?")
int ("(Come on. Enter the first factor.")
int (input ("And another factor."))
result = a * b
c = input ("How much do you think the product is?")
print ("You wrote that", a, "times", b, "same", c)
print ("The correct answer is", the result)
```
