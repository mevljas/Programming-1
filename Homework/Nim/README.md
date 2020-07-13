# Nim

[![video](http://img.youtube.com/vi/K6uO9RyvlKw/0.jpg)](https://youtu.be/K6uO9RyvlKw)

## Testing
Tests are attached to the assignment. Your solution must pass the tests, otherwise it is considered wrong and it is as if you did not submit it. Above all, do not copy or post parts of the solution on the forum!

## Task
Since we’ve just learned about features, you’re going to have to write a bunch of features. In the end, they will lead - though not by the shortest route - to a program that will know how to play Nim (well).

Nim starts by placing a few coins in a few lines, for example:
```
1 (4) * * * *
2 (7) * * * * * * *
3 (5) * * * * *
4 (6) * * * * * *
```
Players take turns taking coins. When a player is on the move, he can take any number of coins from any row (but only one). The player who takes the last coin wins. If the first player takes, say, three coins from the second row, we get
```
1 (4) * * * *
2 (4) * * * *
3 (5) * * * * *
4 (6) * * * * * *
```
## Mandatory task
So write the following functions:

- maximum_potency(n) returns the maximum power of the number 2 that is less than or equal to the given number n. The call maximum_potency (22) returns 16, as 32 would be too much. The call maximum_potence (32) returns 32. The number n is a positive real number. Count the number yourself; the use of the math module or something similar in this function is prohibited.
- break (n) returns a list of powers of the number 2 that add up to the given number n; each potency can occur only once. The call break (22) returns [16, 4, 2]. The numbers should be arranged in descending order. Solve the problem by finding the maximum power with the previous function and adding it to the list and subtracting it from the number n. Repeat this until you get 0. You may want to start by thinking about how to solve this task manually, and then program it the same way. (If the task (justifiably) reminds you of converting to binary, don't bother. Don't worry about how ineffective such a conversion is.)
- contains (s, x) returns True if list s contains elemnt x and False if not. We’ve done something similar in rehearsals before, only it will be easier now, with features.
- difference (s, t) receives two lists and returns a new list containing elements that appear in one of the given lists, but not in both. The call difference ([16, 4, 2], [4, 1]) returns [16, 2, 1] (in this or any other order), as these are numbers that only appear in the first or second list. . Each item in the list with (or t) appears in this list only once. When rescuing, it may (but not necessarily) be worth using the function you programmed earlier.
- break_list (s) receives a list of numbers and returns a list of their breaklists. Call break ([22, 5, 13]) returns [[16, 4, 2], [4, 1], [8, 4, 1]]. This should not be difficult: we prepare a new list, then for each element of the list we calculate the breakdown and add it to this, a new list, which we then return at the end.
- sum(s) calculates the sum of the numbers in the given list. Of course, we already know this from lectures, but program it again anyway. Alone. Because it will help you think of the next function that will be almost equal to the sum function! (Although of course we know how to do this, let's say because it will help us with the next function. We take the number 0. To 0 we add the first element; we get, of course, the first element. Then we add the second element. To this sum we add the third. To this we add the fourth ...)
- merge_list (s) receives a list of lists (as returned by the break_list) function and returns all items that appear oddly. He does it with a trick. Let's make an empty list. We calculate the difference between this list and the first list (so we prepared the difference function); the result will of course be the first list. It then calculates the difference between this “difference” and another list. Then the difference between what he just charged and the third list. Calculates the difference between what he just charged and the fourth list. He calculates the difference between what he just charged and the fifth list ... and so on as long as necessary. Again: this function will be very similar to the sum function, except that we do not add up here.

In addition, write a function

- move_computer(s), which receives a list of how many coins are in each row. The function returns a random (but legal!) Move made by the computer. Random means random, not always the same. The move returns in the form of two numbers; the first is the line number (where the first line has the number 0, not 1!) and the second is the number of coins it wants to remove from that line. You can help yourself with the function randint (a, b), which returns a random number between a and including b; to use it, you must write from random import * at the beginning of the program. Also remember that the length of the list s is obtained with len (s).
At the bottom of the task is a program that you can add at the end of your program, and you will be able to play this game against the computer.

The latter function obviously has nothing to do with those before. This is because the computer is playing stupidly. The features from before come in handy if you want to make a program that will (almost) always beat a human. This is an additional task.

## Additional task
Complement the move_computer(s) function by returning the optimal move when it exists. When not, it returns any possible move, as before.

What is the optimal move? One in which his opponent is in a lost position. A lost position is a position to which the following applies: if we break all the numbers into lists (as does the break_list) function and then combine these lists (merge_list) we get an empty list.

Tip for writing a feature (intentionally not entirely clear ). First you need to figure out the current position: break everything into lists and combine them. If you get an empty list, the computer is in a defeated position (unless your opponent makes a mistake). Otherwise, it is necessary to remove what is in the merged list. Now go over all the lines. For each, you calculate the difference between that line and what would need to be removed. the difference tells you how many coins should remain in that line. If this line actually contains at least as many coins, this is the optimal move.

You may not understand the paragraph above because it is not written clearly enough. That's right too. Google and find out what the winning strategy is for Nim. However, don’t broadcast programs you find online, but a feature that uses what you’ve programmed before.

Game
Once you have written the move_computer function, add this to the end of your program, and you will be able to play against the computer. (I could write this myself, except for the printout, which is a bit compressed. But that's not part of the task, because it would be a little harder to test automatically.)

The code below is for your experimenting and playing against the computer. The submitted homework should not contain code for playing against the computer, but only definitions of functions and tests!
```
def printout (s):
    print ("". join (f "{i + 1} ({e}) {'*' * e} \ n" for i, e in enumerate (s)))

def move_human (s):
    while True:
        line = int ("":)
        coins = int (input ("Coins:"))
        if row <len (s) and 0 <coins <= s [row]:
            return line, coins
        print ("You can't.")

def game (s):
    printout (s)
    while True:
        for who, ask and (("Computer", move_computer), ("Man", move_human)):
            row, coins = ask (s)
            s [row] - = coins
            print (who, "takes", coins, "from", line + 1)
            print ()
            printout (s)
            if sum (s) == 0:
                print (who, "won")
                return

# If you don't want to play, but run tests,
# places a character at the beginning of the bottom two lines
from random import randint
game ([randint (3, 10) for _ in range (4)])
```
