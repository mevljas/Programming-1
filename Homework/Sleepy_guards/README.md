# Sleepy guards
This is the fourth task from this year’s Advent of Code, only I’ve broken it down into features so it will be a little harder to use solutions from the web. It won’t be impossible to help yourself with them, but I suggest you don’t do that, as that won’t teach you anything.

You can read the original assignment to get started.

## Mandatory task
It will be necessary to write five functions. The first and third are very similar to the exercises. For the second, you can help yourself a lot with an example from a lecture published next to your homework. The fourth is a task to start Programming 1, and the fifth is an undemanding exercise from dictionaries.

- understand (line) gets a string of such form as the lines in the given file (and in the examples below), and returns a string containing (year, month, day, hour, minute, what, who). The first five things are numbers; what they mean is obvious. what is a string that contains a word that follows the timestamp in parentheses, i.e. "Guard", "falls" or "wakes". who is the guard number if it is a line describing the guard (i.e. if something is the same as “Guard”), otherwise it is the same as None.

* understand ("[1518-11-09 23:58] Guard # 853 begins shift") returns (1518, 11, 9, 23, 58, "Guard", 853),
* understand ("[1518-04-02 00:30] falls asleep") returns (1518, 4, 2, 0, 30, "falls", None),
* understand ("[1518-08-11 00:47] wakes up") returns (1518, 8, 11, 0, 47, "wakes", None).
Tip: break at intervals, then help yourself by knowing from which to which character of the string the year, month, day, hour and minute are written.

- read_file (file_name) receives the file name and reads from it information about how the guards fell asleep and woke up. He puts them in a list of triplets containing the guard’s number, the minute he fell asleep, and the minute he woke up. If the file contains
```
[1518-11-01 00:00] Guard # 10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard # 99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard # 10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
```
function returns
```
[(10, 5, 25),
 (10, 30, 55),
 (99, 40, 50),
 (10, 24, 29)]
 ```
**Problem: File lines are not edited.** To get edited lines, type sorted (open (blabla)) instead of open (blabla).

You can help yourself with the previous function and discard everything you don’t need.

- izpis_dogodka (guard, sleeps, wakes up) receives data (three numbers) on when a guard fell asleep and when he woke up, and as a result returns a string with a printout of this event. The call izpis_dogodka (1945, 5, 42) returns "1945: 05-42" and izpis_dogodka (19, 13, 42) returns "19: 13-42". The guard number always occupies four places; the hours and minutes are aligned so that they have 0 in front.

Zero alignment is achieved by adding 0 before the number of places:
```
>>> x = 42
>>> f "{x: 06}"
'000042'
```
- naj_drugi (pairs) receives a list of pairs. Finds the largest second element and returns the corresponding first element. The call naj_drugi ([(5, 3), (8, 9), (13, 5), (10, 7)]) returns 8: the largest second element is 9 and the corresponding first element is 8.

- naj_zaspanec (events) receives a list of threes with the guard's number and the minute when he fell asleep and when he woke up. It returns the number of the guard who slept the most (not just once, but if we add up all his sleep) for the most minutes.

If the guard falls asleep at minute 5 and wakes up at minute 8, it means that he slept at minutes 5, 6 and 7, so he slept for three minutes.

No guard falls asleep before midnight and no one sleeps after 1:00, so you always get the length of your sleep by subtracting the second number from the third.

## Additional task
Write two more functions.

- ever_sleep(guard, events) receives the guard number and lists of triplets as in the previous functions. Returns the minute in which the given guard slept the most.

- naj_cas(events) check all the guards and the minutes in which they sleep. It goes through all the combinations of guards and the minutes they slept. Returns the pair (guard, minute) that is most common.

If guard 99 sleeps for 5 to 8 minutes, this means combinations (99, 5), (99, 6) and (99, 7).

If we have
```
Date ID Minute
            000000000011111111112222222222333333333344444444445555555555
            012345678901234567890123456789012345678901234567890123456789
11-01 # 10 ..... ################################## ########## .....
11-02 # 99 ........................................ ##### ##### ..........
11-03 # 10 ........................ ##### ................ ...............
11-04 # 99 .................................... ######## # ..............
11-05 # 99 ............................................. ########## .....
```
returns (99, 45), as this is the most common combination. Guard 99 slept three times in minute 45; all other combinations are less common.

With these two features, you have completed the solution of the Advent of Code task and can submit it there as well. :)
