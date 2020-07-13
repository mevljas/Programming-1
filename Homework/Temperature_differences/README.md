# Temperature differences
These are fictional highest daily temperatures in a few Slovenian cities in the ten days of August 2014. Or 2015, I forgot. Given that they are fictional, it doesn’t even matter much. :)
```
ljubljana = [28, 30, 25, 28, 30, 32, 35, 28, 25, 27]
maribor = [30, 28, 26, 34, 26, 32, 34, 30, 28, 28]
celje = [28, 32, 30, 31, 32, 28, 27, 26, 25, 25]
dill = [32, 35, 35, 31, 32, 34, 35, 30, 28, 28]
kranj = [28, 27, 30, 32, 28, 27, 26, 28, 30, 25]
```
Copy these five lines to the beginning of your program.

**Those of you who already know something more: don’t use indexes when solving tasks. Seriously. It is helpful to learn to program properly. :)**

## Heating up
You do not need to submit these programs, but you can write them so that they will gradually lead you to solve the task.

1. List temperatures in Ljubljana.
2. List temperatures (vapors) in Ljubljana and Maribor.
3. List the differences between temperatures in Ljubljana and Maribor by days.
4. Print the absolute values of the differences between temperatures in Ljubljana and Maribor by days.
## Mandatory task
Write a program that lists the largest difference between the daily temperature in Ljubljana and Maribor and which city was warmer that day. In the above example, the difference is 6, and Maribor is warmer, so the program displays
```
6 Maribor
```
To check if the program really works, change the first two lines to
```
ljubljana = [30, 28, 26, 34, 26, 32, 34, 30, 28, 28]
maribor = [28, 30, 25, 28, 30, 32, 35, 28, 25, 27]
```
and the program must print
```
6 Ljubljana
```
## Additional task
For each day, calculate the average temperature in all five cities. The program should list the number of days when the average temperature exceeded 30 degrees. It displays this information
```
4
```
