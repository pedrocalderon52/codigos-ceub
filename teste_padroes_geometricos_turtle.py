import turtle as tl
import math as mt

colors = {"purple", "black"}

tl.width(2)
tl.speed(15)
"""
#sin function

for x in range(100):
    y = mt.sin(x)
    tl.goto(x*5, y*5)
"""

"""
#circle pattern
for i in range(360):
    tl.right(1)
    tl.up()
    tl.fd(99)
    tl.down()
    tl.fd(1)
    tl.teleport(0,0)"""

#ellipse pattern
for x in range(-20, 21):
    y = abs(30 * (mt.sqrt(1 - ((x**2) / (20**2)))))
    tl.up()
    tl.goto(x*4, y*4)
    tl.down()
    tl.fd(1)











tl.mainloop()
