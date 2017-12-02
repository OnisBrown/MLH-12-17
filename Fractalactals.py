from pydub import *
from turtle import *

while True:
    forward(4)
    left(2)
    if abs(pos()) < 1:
        break

done()
