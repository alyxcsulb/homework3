import turtle
pen = turtle.Pen()  # same as turtle.Turtle()

position = pen.position()
pen.speed(1)
pen.width(10)
pen.color('red')
pen.goto(-75, 100)
pen.goto(-225, -50)
pen.goto(-125, -125)
pen.up()
pen.home()
pen.down()
pen.color('blue')
pen.goto(75, 100)
pen.goto(225, -50)
pen.goto(125, -125)




turtle.done() # remember to keep at end to keep graphic open