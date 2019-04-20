import turtle
t = turtle.Turtle()
t. shape("turtle")
x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))
subx = x1-x2
suby = y1-y2
subx_2= (subx)**2
suby_2= (suby)**2
t.goto(x1,y1)
t.goto(x2,y2)
t.write((subx_2 + suby_2)**0.5)

