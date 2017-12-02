from pydub import *
from turtle import *
from numpy import *
import hashlib
#SET THE PATH OF CODEC
AudioSegment.converter = "C:\\ffmpeg-20171130-83ecdc9-win32-static\\bin\\ffmpeg.exe"

song = AudioSegment.from_mp3("Sources/Stevie Nicks.mp3")
print(song.duration_seconds)
raw = fromstring(song._data, int16)
rawFr = song.frame_rate
print(raw.size)
rawString = raw.tostring()
signiture = (hashlib.md5(rawString)).hexdigest()
print(signiture)
signitureI = int(signiture, 16)



def hilbert2(step, rule, angle, depth, t):
   if depth > 0:
      a = lambda: hilbert2(step, "a", angle, depth - 1, t)
      b = lambda: hilbert2(step, "b", angle, depth - 1, t)
      left = lambda: t.left(angle)
      right = lambda: t.right(angle)
      forward = lambda: t.forward(step)
      if rule == "a":
        left(); b(); forward(); right(); a(); forward(); a(); right(); forward(); b(); left();
      if rule == "b":
        right(); a(); forward(); left(); b(); forward(); b(); left(); forward(); a(); right();
        
myTurtle = Turtle()
myTurtle.speed(0)
hilbert2(5, "a", 90, 5, myTurtle)

done()
