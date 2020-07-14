#Balls
Watch the game [Chain Reaction](https://yvoschaap.com/chainrxn/).

- **For grade 6**: Compose a program that draws one ball of random color that appears at a random spot and moves in a random direction (see details below!). When it comes to the edge, it bounces off, just like you learned in Physics. It should bounce for about twenty seconds, then the program ends.

- **For grade 7**: Same as for grade 6, but the program must draw and guide 30 balls of different random colors moving in different random directions.

- **For grade 8**: In addition to what you did for grade 7, there should be a circle in the picture whose center is where the mouse is at the moment (and of course it moves with the mouse). When the user clicks, let the circle stay where it is and no longer follow the mouse. The program should end when the first of the balls hits the ball we placed with the mouse.

- **For grade 9**: Program one level of play. The game runs as long as there are some exploded balls, and when the last one disappears, it is displayed how many balls exploded. This concludes the program.

- **For a grade of 10**: Program a game with 10 levels. At the beginning of each level, it is written how many balls are in play and how many exploded. In the end, when the last exploded ball disappears, the game continues to the next level if enough balls have exploded. Otherwise, a window appears stating how many balls have exploded and that this is too few; the game is repeated at the same level. Invent meaningful numbers of balls. The rates must, of course, vary.
[![Video](http://img.youtube.com/vi/DXeBpQwOt5g/0.jpg)](http://www.youtube.com/watch?v=DXeBpQwOt5g)

Details:

- The radius of the balls should be 10 points.
- The radius of the ball representing the mouse and the radius of the exploded ball should be 30 points.
- The exploded ball should disappear after four seconds.
- All balls should move at the same speed, namely 5 points per one iteration of the loop; add a 0.02 second pause to the loop. (Hint: Determine a random number between -5 and 5 for the x-component of velocity. Calculate the component y according to Pythagoras.)

In the plotter module, you have two hidden variables related to the mouse:

- drawing.mouse is a line that contains the coordinates of the mouse, if it is located inside the drawing window (otherwise the coordinate where it left that window).

- draw.click is a variable that becomes True when the user clicks the mouse. If you put it back on False, the cartoonist will set it back to True the next time you click it.

If a circle is a circle, paint it with
```
c = circle.pen (). color (). lighter ()
c.setAlpha (192)
krog.setBrush (c)
```
To change the circle radius to, say, 30, call circle.setRect (-30, -30, 60, 60). To hide it, call krog.hide ().

Use QMessageBox.information (None, "window name", "message") to display messages. To do this you will need to import from PyQt5.QtWidgets import QMessageBox.

There are no tests this time.
