from pydub import *
from turtle import *
from numpy import *
import hashlib
#SET THE PATH OF CODEC
AudioSegment.converter = "ffmpeg-20171130-83ecdc9-win32-static/bin/ffmpeg.exe"

song = AudioSegment.from_mp3("Sources/Stevie Nicks.mp3")
print(song.duration_seconds)
raw = fromstring(song._data, int16)
rawFr = song.frame_rate
print(raw.size)
rawString = raw.tostring()
signiture = (hashlib.md5(rawString)).hexdigest()
print(signiture)
inputInterval = 8
inputArray = [int(signiture[i:i+inputInterval],16) for i in range(0, len(signiture), inputInterval)]
parity = ""
step = inputArray[0]/(100*raw.size)

if inputArray[1]%2 == 0:
   parity = "even"
else:
   parity = "odd"

if inputArray[2]<90:
   angle = inputArray[2]
else:
   angle = inputArray[2]%90
   
depth = inputArray[3]/160


def fractal(step, rule, angle, depth, t):
   if depth > 0:
      odd = lambda: fractal(step, "even", angle, depth-1, t)
      even = lambda: fractal(step, "odd", angle, depth-1, t)
      left = lambda: t.left(angle)
      right = lambda: t.right(angle)
      forward = lambda: t.forward(step)
      if rule == "even":
        left(); even(); forward(); right(); even(); forward(); even(); right(); forward(); even(); left();
      if rule == "odd":
        right(); odd(); forward(); left(); odd(); forward(); odd(); left(); forward(); odd(); right();

        
myTurtle = Turtle()
myTurtle.speed(0)

fractal(step, parity, angle, 10, myTurtle)
done()
