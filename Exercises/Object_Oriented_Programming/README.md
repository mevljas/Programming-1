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

