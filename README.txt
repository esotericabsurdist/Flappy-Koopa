Robert Mitchell

Computer Science - CSUF


****** Koopa's Hunt for Flappy Bird ******

This game is inspired by the popular sidescrolling mobile Flappy bird game
which bears resemblance to the many Nintendo Mario games.
See here: https://en.wikipedia.org/wiki/Flappy_Bird

The context of this game is that the bird character played in Flappy bird
belongs to Bowser in the Mario Universe, but has escaped from the castle
and flown through a landscape of pipes. Bowser sends a Koopa Paratroopa after
the bird to track it down. The game play of Koopa's Hunt for Flappy Bird
consists of the user navigating a Koopa through a similar sequence of pipes,
presumably the pipes that the flappy bird has flown through. If the user
successfully navigates through all pipes, the fate of the flappy bird is revealed.

The goal is to navigate all the pipes until the end.
This is the winning state of the game.


***Controls***
[Space] : Jump
[RETURN]: Continue / Quit(During Game Over Screen)


***Rules***
-The ground does not kill the koopa.(The koopa is unlike a bird in that it can also walk)
-Contacting a pipe will kill the koopa.
-Passing between the two pipes is safe.
-The koopa cannot fly over the pipes.
-The koopa has three lives to beat the game.(in Mario Fashion)


***How to run game***
-Navigate to the directory containing 'koopas_hunt_for_flappy_bird.py'
-Make sure that the included 'sprites' folder is in the same directory as 'koopas_hunt_for_flappy_bird.py'
-Run the python file with no arguments, eg. 'python koopas_hunt_for_flappy_bird.py'


***Notes***
100% of the source is written by myself. It is messy. There are no major known bugs.

Game was built with the following tools:
-Python 64bit v2.7.12
-Pygame 64bit v1.9.2  64bit Pygame can be found at http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame
Relevant Sources of inspiration:
Gravity in Pygame:
http://stackoverflow.com/questions/20976516/adding-gravity-in-pygame
Sprite Sources are either original or take from here:
-https://www.spriters-resource.com/snes/smarioworld/
-https://www.spriters-resource.com/mobile/flappybird/sheet/59894/

The hit box for the Koopa sprite is not perfect. It is infact a rectangle. Further
work is needed to make the hit box resemble the koopa. I am not presently not sure
how to do this. Just to make the game a bit easier, I took 10 pixels off the bottom
of the Koopa's hit box so that the Koopa can drag its feet a bit.

Test on Windows7 and MacOS El Capitan.
The following warning is produced on Windows:
"libpng warning: Interlace handling should be turned on when using png_read_image"
This, it has to do with different RGB formats.
