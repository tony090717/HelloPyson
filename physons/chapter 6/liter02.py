import turtle
t = turtle.Turtle()
t.shape("turtle")
n = int(input("몇각형을 만들고 싶으세요?"))
for i in range(n):
    if n >= 10:
        t. forward(50)
        t.left(360/n)
    else :
        t. forward(100)
        t.left(360/n)
