import turtle as tl

tl.width(12)
tl.speed(8)
cores_cima = ["#3c97b5", "#000000", "#a61212"]
cores_baixo = ["#d1a40f", "#0b7821"]


tl.teleport(-220, 20)
for cor in cores_cima:
    tl.color(cor)
    tl.circle(100)
    tl.teleport(tl.xcor() + 220, tl.ycor())

tl.teleport(-110, -80)
for cor in cores_baixo:
    tl.color(cor)
    tl.circle(100)
    tl.teleport(tl.xcor() + 220, tl.ycor())

tl.teleport(-220, 20)
tl.color("#3c97b5")
tl.penup()
tl.circle(100, 30)
tl.pendown()
tl.circle(100, 80)
tl.teleport(tl.xcor() + 220, tl.ycor())
tl.penup()
tl.circle(100, 180)
tl.color("black")
tl.pendown()
tl.circle(100, 70)
tl.penup()
tl.circle(100, 30)
tl.pendown()
tl.circle(100, 80)
tl.teleport(220, 20)
tl.setheading(0)
tl.color("#a61212")
tl.penup()
tl.circle(100, 300)
tl.pendown()
tl.circle(100, 60)

tl.mainloop()