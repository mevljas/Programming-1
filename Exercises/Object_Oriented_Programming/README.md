# Tasks - classes (Turtle)
There will be no Unittests this week.

## A reversible turtle
To warm up, add the turnAround method to the turtle, turning it in the opposite direction.

## Turtle+
Add the setWidth and setColor methods to the Turtle class to determine the thickness and color of the line left behind by the turtle. We will use them as follows:
```
>>> t.forward (20)
>>> t.setWidth (10)
>>> t.forward (20)
>>> t.setColor (risar.rdeca)
>>> t.forward (20)
```
## Pen indicator
Add an indicator to the drawing of the turtle, whether the feather is lowered or not. When programming, make sure that combinations, such as, also work correctly
```
>>> t.penUp ()
>>> t.hide ()
>>> t.show ()
```
After that, the pen must be invisible because it is raised.
```
>>> t.hide ()
>>> t.penDown ()
```
The feather must be invisible because the turtle is invisible.

A tortoise with a dropped feather

<img src="https://ucilnica.fri.uni-lj.si/file.php/166/vaje/zelva/zelva-pero.png" 
alt="zelva"  />

Turtle with raised feather

<img src="https://ucilnica.fri.uni-lj.si/file.php/166/vaje/zelva/zelva-ne-pero.png" 
alt="zelva" />

Help: Check the turtle's head with self.head.isVisible ().

## Stamp
Add to the stamp() method, which prints the turtle, that is, draws the turtle, which remains drawn as the turtle moves forward, and clearStamps(), which deletes all printed turtles from the current image. Program
```
t.forward (10)
t.stamp ()
t.left ()
t.forward (100)
t.turn (45)
t.forward (20)
t.stamp ()
t.right ()
t.forward (40)
t.left ()
t.forward (40)
t.right ()
t.forward (40)
t.stamp ()
t.right ()
t.forward (40)
t.hide ()
```
draws  
<img src="https://ucilnica.fri.uni-lj.si/file.php/166/zelva/stamps.gif" 
alt="zelva" />

If we then say clearStamps(), the turtles disappear:

<img src="https://ucilnica.fri.uni-lj.si/file.php/166/zelva/stamps-ni-zelv.gif" 
alt="zelva" />

Requirement: the methods must work properly even if we have multiple turtles imprinting and erasing their imprints!

Tip: have stamps save everything they draw in a list, and clearStamps delete the drawing.

## Macro recorder
add methods to the turtle startRecording(), which triggers the macro recorder, stopRecording(), which stops recording and returns the recorded macro, and play (macro), which performs the recording.
```
t = Turtle ()
t.startRecording ()
for i in range (4):
    t.forward (100)
    t.right ()
square = t.stopRecording ()

for i in range (10):
    t.turn (36)
    t.play (square)
risar.stoj ()
```
Tip: If you prepare things correctly, the play method will be like this
```
def play (self, trace):
    for func, pars in trace:
        func (* pars)
```
What does * do in the func (* pars) line?

# Tasks
## Ship
Write the class Ship using the following methods.

- The constructor receives the carrying capacity of the ship.
- loads(weight) loads a package with a given weight. If the total weight thus exceeds the carrying capacity of the ship, so many packages are thrown out of it that the weight is again within the permissible range. Packages are removed in the same order as they were loaded, i.e. the oldest first. The method returns nothing.
- total_weight() returns the total weight of all packages on the ship.
- removed() returns the number of packets that have been removed from the ship so far due to overload.
Let's say we have a ship with a carrying capacity of 42.

- We load it with a package weighing 30 and then a package weighing 10. The total weight is 40.
- We add a package with a weight of 21. Since the carrying capacity is exceeded (30 + 10 + 21 = 61> 42), we throw the first package from the ship, 30. The total weight is now 10 + 21 = 31, there are two packages on the ship and the number of removed is 1 .
- Then we load a package with a weight of 41. The carrying capacity is exceeded (10 + 21 + 41 = 72> 42), so we will throw the first package (10) off the ship. As the carrying capacity is still exceeded, another package is thrown off the ship. Only one package remains, the total weight is 41, the number of removed so far is 3.
- Then we load a package with a weight of 50. We throw a package with a weight of 41 from the ship. Since the carrying capacity is still exceeded, we remove the package that has just been loaded (50). The total weight is 0, the number of removed is 5.

## City
Write a class A city that represents a city placed on a grid.

- The constructor receives its width and height.
- The place (x, y) method places the house at the x, y coordinates. The coordinates are numbered from 0 onwards. If we put several houses in the same place, only one is placed.
- The porusi method (x0, y0, x1, y1) demolishes all houses in the rectangle between x0, y0 and x1, y1 inclusive (you can assume that x0 <= x1 and y0 <= y1).
- The free () method should return the number of free fields.
