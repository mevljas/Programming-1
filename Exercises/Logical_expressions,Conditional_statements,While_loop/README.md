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

Cashier "competition"
A competitive store around the corner has opted for a special offer: the customer can buy as many products as he wants. Correct the above program by first asking the cashier how many products are in the cart, then asking about the prices of those products, and finally printing the sum again.

Number of products: 3
Item price: 2
Item price: 4
Item price: 1
Total: 7
The solution
"Top shop" box office
The third store decided to compete with the second by having shorter queues at the checkout than the second, where payment takes place slowly because cashiers have to count the products before they can start entering their prices. He corrects the program by not asking about the number of products, but asking about prices until the cashier enters zero.

Item price: 2
Item price: 4
Item price: 1
Item price: 0
Total: 7
The solution
State Agency for Consumer Protection
Due to the flood of suspicious shops around the corners, the National Consumer Protection Agency decided to control the average prices of products in customer baskets. Fix the last or penultimate program so that it also prints the average price.

Item price: 2
Item price: 4
Item price: 1
Item price: 0
Total: 7
Average price: 2.33333333333
(Don’t worry about the ugly printout of the price; government officials are accurate and want to know every last decimal!)

The solution
Current Account
The State Agency for Consumer Protection has announced a project to create a program that will allow consumers to control their current accounts. Users enter receipts and expenses (as positive and negative amounts) into their current account into the program. The program promptly displays the status and stops when the user is in the red for 100 euros or more.

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
The solution
Anonymous Consumer Club
The disintegration of stores has led to shopping addiction. One method of treatment is based on intelligent baskets that accept a maximum of ten items; after that they are locked and the customer can only take them to the cash register. They are also locked if the price of the items reaches (or exceeds) € 100.

Write a program for which the user enters prices and which stops running when the user enters 0 (will no longer buy), when ten numbers are entered, or when the sum of prices reaches or exceeds 100 euros.

Price: 10
Price: 5
Price: 0
You will spend 15 Euros for 2 things.
Beware, the user bought two things even though he entered three prices!

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
