from turtle import *
from time import *
t=Turtle()
digi=Turtle()
name=Turtle()
t.speed(.01)
s=getscreen()
digi.ht()
ht()
name.ht()
t.penup()
t.pensize(2)
t.goto(-200,0)
t.pendown()
t.pencolor('black')
t.fillcolor('greenyellow')
t.begin_fill()
# Time Variable
hou=int(input("Enter Hours    :"))
minu=int(input("Enter Minutes  :"))
sec=int(input("Enter Second   :"))
for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(150)
    t.lt(90)
t.end_fill()
t.penup()
t.goto(-180,20)
t.pendown()
t.pencolor('black')
t.fillcolor('yellow')
t.begin_fill()
for i in range(2):
    t.fd(260)
    t.lt(90)
    t.fd(110)
    t.lt(90)
t.end_fill()
name.penup()
name.goto(-310,160)
name.pendown()
name.pencolor('aquamarine')
name.write('CREATED BY AVIK MAHATO',font=('verdana',25,'bold'))
t.penup()
t.goto(-107,.5)
t.pencolor('Darkblue')
t.write('STOPWATCH',font=('arial',12,'bold'))
digi.ht()
t.ht()
digi.penup()
digi.goto(-156,50)
digi.pendown()
while hou>0 or minu>0 or sec>-1:
    if sec<=0 and minu !=0:
        minu-=1
        sec=59
    if minu<=0 and hou !=-1 and hou!=0:
        hou-=1
        minu=59
        sec=59
    digi.clear()
    digi.write('%d : %d : %d '%(hou,minu,sec),font=('vedana',35,'bold'))
    sec-=1
    sleep(1)
