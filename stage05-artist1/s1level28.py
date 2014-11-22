"""Stage 5: Puzzle 5 of 10

Now, for practice, draw a triangle and then a square to draw an envelope.
Hint: delete the 'pass' (which does nothing) with your code.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level28')


artist.move_forward(100)
artist.turn_right(120)
artist.move_forward(100)
artist.turn_right(120)
artist.move_forward(100)
artist.turn_left(150)
artist.move_forward(100)
artist.turn_left(90)
artist.move_forward(100)
artist.turn_left(90)
artist.move_forward(100)
artist.check()
