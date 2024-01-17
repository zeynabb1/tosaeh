import turtle 
import random

a=0

win=turtle.Screen()
win.setup(600,600)
win.bgcolor('lightblue')
win.title(' لاکپشت زينب کاظم پوربازی')

d=turtle.Turtle()
d.up()
d.goto(-275,275)
d.down()
d.width(5)
for i in range(4):
    d.fd(550)
    d.rt(90)
d.ht()

lak=turtle.Turtle()
lak.shape('turtle')
lak.color('dark blue')
lak.shapesize(2)
lak.up()

bal=turtle.Turtle()
bal.shape('circle')
bal.color('red')
bal.up()
bal.goto(random.randint(-265,265),random.randint(-265,265))


def move_right():
    lak.right(30)
def move_left():
    lak.left(30)

win.listen()
win.onkey(move_right,'Right')
win.onkey(move_left,'Left')


am=turtle.Turtle()
am.up()
am.goto(-270,275)
am.ht()
am.color('darkblue')
am.write('امتیاز'+str(a))

while True:

    lak.fd(1)
    if lak.xcor() > 270 or lak.xcor() < -270 or lak.ycor() > 270 or lak.ycor() < -270:
        lak.right(180)
        a=a-5
        am.clear()
        am.write('امتیاز'+str(a))

    if lak.distance(bal)<20:
        bal.goto(random.randint(-265,265),random.randint(-265,265))
        a=a+10
        am.clear()
        am.write('امتیاز'+str(a))
        if a>=60:
            am.goto(-75,0)
            am.write('شما موفق شدید',font=32)
            break
    

       
    

win.mainloop()
