# Tasks
There will be no Unittests this week.

## Scattered circles
Write a program that draws 50 randomly placed circles, as shown in the figure:

<img src="https://ucilnica.fri.uni-lj.si/file.php/166/vaje/qtslike/krogi.png" 
alt="illustration" />

## Connect with the first
As before, at the same time connect the center of the first circle with the centers of all other circles.

<img src="https://ucilnica.fri.uni-lj.si/file.php/166/vaje/qtslike/krogi_crte_prva.png" 
alt="illustration" />

## Everything connected
Now connect the centers of all the circles with the lines.

<img src="https://ucilnica.fri.uni-lj.si/file.php/166/vaje/qtslike/krogi_crte.png" 
alt="illustration" />

## Circles on a circle
Instead of randomly scattering the dots on the drawing surface, distribute them evenly across the circle

<img src="https://ucilnica.fri.uni-lj.si/file.php/166/vaje/qtslike/krogi_vkrogu.png" 
alt="illustration" />

and, as before, connect them with lines.

<img src="https://ucilnica.fri.uni-lj.si/file.php/166/vaje/qtslike/krogi_vkrogu_povezani.png" 
alt="illustration" />

## Non-intersecting circles
Write a program that randomly scatters 1000 rounds so that

- the center of no circle is inside another circle,
- the circles do not intersect with each other.
The task is solved by randomly inventing the coordinates of the center and radius. If the center of the circle is inside one of the already drawn circles (you will have to remember these), you invent a new center. However, if you find that the circle would intersect with any of the existing circles, reduce the radius of the circle by so much that the circles are just touching.

<img src="https://ucilnica.fri.uni-lj.si/file.php/166/vaje/qtslike/krogi.gif" 
alt="illustration" />

## Mountain
Write a program that creates a random mountain landscape.

<img src="https://ucilnica.fri.uni-lj.si/file.php/166/vaje/qtslike/gora.png" 
alt="illustration" />

You can tackle the task on your own, or you can use an elegant recursive algorithm:

Start with a horizontal line across the entire canvas.

<img src="https://ucilnica.fri.uni-lj.si/file.php/166/vaje/qtslike/gora_0.png" 
alt="illustration" />

Find the point in the middle and raise or lower it by a random number of pixels.

<img src="https://ucilnica.fri.uni-lj.si/file.php/166/vaje/qtslike/gora_1.png" 
alt="illustration" />

Repeat the procedure recursively on the left and right lines. Reduce the interval within which you choose the offset of the midpoint to half. If you chose between numbers from the interval [-200, 200] to move the first midpoint, you will shorten the interval to [-100, 100] for the new midpoint.

<img src="https://ucilnica.fri.uni-lj.si/file.php/166/vaje/qtslike/gora_2.png" 
alt="illustration" />

After four iterations, you can expect something like this:

<img src="https://ucilnica.fri.uni-lj.si/file.php/166/vaje/qtslike/gora_4.png" 
alt="illustration" />
