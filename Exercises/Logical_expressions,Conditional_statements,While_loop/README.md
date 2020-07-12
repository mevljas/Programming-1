# Tasks
## box office "All for five"
In the "all five" store, customers must always buy exactly five items. For cash registers, therefore, they need software that asks the user (cashier) for five prices; when he enters them, the program displays the sum.
```
Item price: 2
Item price: 4
Item price: 1
Item price: 6
Item price: 3
Total: 16
```

## Cash register "competition"
A competitive store around the corner has opted for a special offer: the customer can buy as many products as he wants. Correct the above program by first asking the cashier how many products are in the cart, then ask about the prices of those products, and finally printing the sum again.
```
Number of products: 3
Item price: 2
Item price: 4
Item price: 1
Total: 7
```
## "Top shop" cash register
The third store decided to compete with the second by having shorter queues at the checkout than the second, where payment takes place slowly because cashiers have to count the products before they can start entering their prices. Correct the program by not asking about the number of products, but asking for prices until the cashier enters zero.
```
Item price: 2
Item price: 4
Item price: 1
Item price: 0
Total: 7
```
## State Agency for Consumer Protection
Due to the flood of suspicious shops around the corners, the National Consumer Protection Agency decided to control the average prices of products in customer baskets. Fix the last or penultimate program so that it also prints the average price.
```
Item price: 2
Item price: 4
Item price: 1
Item price: 0
Total: 7
Average price: 2.33333333333
(Don’t worry about the ugly printout of the price; government officials are accurate and want to know every last decimal!)
```
## Current Account
The State Agency for Consumer Protection has announced a project to create a program that will allow consumers to control their current accounts. Users enter receipts and expenses (as positive and negative amounts) into their current account into the program. The program promptly displays the status and stops when the user is in the red for 100 euros or more.
```
Amendment 23
Condition 23
Amendment 15
Condition 38
Change -30
Condition 8
Amendment 10
Condition 18
Amendment 100
Condition 118
Change -200
Condition -82
Change -50
Condition -132
Bankruptcy
```
## Anonymous Consumer Club
The spreading of stores has led to shopping addiction. One method of treatment is based on intelligent baskets that accept a maximum of ten items; after that they are locked and the customer can only take them to the cash register. They are also locked if the price of the items reaches (or exceeds) € 100.

Write a program for which the user enters prices and which stops running when the user enters 0 (will no longer buy), when ten numbers are entered, or when the sum of prices reaches or exceeds 100 euros.
```
Price: 10
Price: 5
Price: 0
You will spend 15 Euros for 2 things.
```
Beware, the user bought two things even though he entered three prices!
```
Price: 10
Price: 5
Price: 90
You will spend 105 Euros for 3 things.

Price: 1
Price: 1
Price: 1
Price: 1
Price: 1
Price: 1
Price: 1
Price: 1
Price: 1
Price: 1
You will spend 10 euros for 10 things.
```
# Tasks (additional)
## Quadratic equation
Calculate all real solutions of the quadratic equation ax^2 + bx + c = 0, given by arguments a, b and c. Your program should behave as shown below.
```
Enter a: 1
Enter b: 2
Enter c: 1
The equation has one realistic solution: -1.0

Enter a: 1
Enter b: 2
Enter c: 0
The equation has two real solutions: 0.0 and -2.0

Enter a: 1
Enter b: 2
Enter c: 2
The equation has no real solutions.
```
To calculate the root of the number n, add the import math line at the top of the program, and then call the math.sqrt (n) function.

## Counting number 7
The count of 7 is played in such a way that players sitting in a circle, square or some other suitable (if necessary irregular, but preferably convex) polygon in turn speak the numbers from one to infinity, and instead of all numbers that are divisible with 7 or contain the digit 7, say BUM. The player who makes a mistake is eliminated and the count starts from the beginning. So the game goes like this:
```
1 2 3 4 5 6 BUM 8 9 10 11 12 13 BUM 15 16 BUM 18 19 20 BUM 22 23 24 25 26 BUM BUM 29 ...
```
Write a program that prints this sequence up to and including 100.

## Sums
Write a program that calculates the sum of the first n numbers. If the user enters, say, 7, the program might print 28, since 1 + 2 + 3 + 4 + 5 + 6 + 7 equals 28.

The more difficult version of the task is to solve the problem for very large n.
```
Enter the number: 1
1

Enter the number: 7
28
```
## Squares
Write a program that determines if a given number n is a square. Thus, for example, 25 is a square, as it is equal to 5^2. 27 is not a square.

A more difficult version of the task is to solve the problem for very large n without using the math library.
```
Enter the number: 25
The number is a square

Enter the number: 27
The number is not a square
```
## Cubes
At the dice shop, they pack the dice into square-shaped boxes. They have boxes of width 1, 2, 3, 4, 5 ... and so on; 1, 4, 9, 16, 25 ... cubes go in these boxes. If the customer orders, e.g. 20 cubes, we need a box of width 5. Write a program to which the user enters the number of ordered cubes, and the program displays the required size of the box and how many cubes of space is left in the box.

The more difficult version of the task is to solve the problem for very large n.
```
Enter the number of cubes: 20
We need a box of width 5 in which there is room for 5 more cubes
```
## Dividers
Write a program that lists all the divisors of a given number.
```
Enter the number: 18
1
2
3
6
9
18
```
## A triangle of stars
The programming tradition dictates that the first program we write in a new programming language is a program that prints “Hello world”. Unfortunately, it is too late for that.

Furthermore, it is fitting that one of the first programs we write using loops is a program that draws a triangle of asterisks. Let’s stick to at least this and write a program that asks the user for the height of the triangle, and then prints out such a triangle from the asterisks.
```
Enter the height: 4
*
**
***
****
```
In Python, we will make our work easier if we know that we can multiply a string by a number. Three stars are obtained by multiplying the string '*' by 3, ie '*' * 3.

## Spruce
Write a program that draws a spruce from the '*' characters.
```
Enter the height: 4
   *
  ***
 *****
*******
```
