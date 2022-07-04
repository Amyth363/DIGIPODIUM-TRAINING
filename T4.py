from cmath import rect
from turtle import *

i = 5
while True:
    rect(i,i)
    left(100)
    i += 5
    if i > 100:
        break
