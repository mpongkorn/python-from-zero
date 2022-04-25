import turtle
tao = turtle.Pen()
tao.shape('turtle')
def hex():
    for i in range(12):
        for n in range(8):
            tao.forward(100)
            tao.left(45)
        tao.right(30)
def go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

go(-100,-50)
hex()

