import turtle

t = turtle.Turtle()
list = ["Purple","Red","Orange","Blue","green","Yellow"]
turtle.bgcolor("Black")
for i in range(150):
    t.color(list[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)
t.exitonclick()