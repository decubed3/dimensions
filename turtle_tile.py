# Turtle Tile Experimentation
# by David Larsen
# 5.2.2024

import turtle
turtle.shape("turtle")
turtle.color("blue")
turtle.width(.5)
turtle.speed(100)

#FUNCTIONS SECTION

def octagon(size):  #size = length of side for octogon function
    for i in range(8):
        turtle.forward(size)
        turtle.left(45)

def square(size):  #size = length of side for square function
    for i in range(4):
        turtle.forward(size * 2.45)  #adjustment factor since to make a side of square fit into octagon footprint
        turtle.left(90)

def step(position):  #position = forward offset of polygon from previous iteration
    turtle.penup()
    turtle.forward(position)
    turtle.pendown()

def back(position):  #position = back offset to beginning of row after all iterations of row
    turtle.penup()
    turtle.backward(position * (columns))  #using columns value as factor to count back to beginning of row
    turtle.pendown()

def shift(down):
    turtle.goto(turtle.pos() + (0, -(down)))

#INITIALIZE SECTION
size: int = 25  #size of polygon side
position: int = 61  #relative position of whole polygon per iteration
down = position  #ensuring value for shift to next row is equivalent left/right iteration/size
# columns: int = 5
# rows: int = 5

#INPUT PARAMETERS SECTION
poly = turtle.textinput("POLYGON MAP","What polygon would you like?  Enter 'octagon' or 'square':")
col = turtle.textinput("POLYGON MAP","What color would you like?  Enter 'black', 'blue', 'green', or 'red':")
wid = turtle.numinput("POLYGON MAP","What line thickness would you like?  Enter a floating point number:",'',.5,10)
c = turtle.numinput("POLYGON MAP","What number of columns would you like?  Enter numeric integer 2 to 12:",'',2,12)
r = turtle.numinput("POLYGON MAP","What number of rows would you like?  Enter numeric integer 2 to 12:",'',2,12)


#SET VARIABLES SECTION
turtle.color(col)
turtle.width(wid)

columns = int(c)  #converting string value to int for columns
rows = int(r)  #converting string value to int for rows

#MAIN SECTION --- START GETTING LOOPY
for x in range(rows):   #outer loop functions for rows

    for y in range(columns):  #inner loop fucntions for columns
        if poly == 'octagon':
            octagon(size)
        elif poly == 'square':
            square(size)

        size = size * 1
        step(position)
        position = position

    turtle.penup()
    back(position)  #return to beginning of row
    turtle.penup()
    shift(down)  #move down to start of next row
    turtle.pendown()

turtle.Screen().exitonclick()  #PyCharm needs this function to keep the window open


#CODE GRAB BAG
#poly = turtle.textinput("POLYGON MAP","That is not a valid option?  Enter 'octagon' or 'square':")

# print(math)
# octagon(100)
# octagon(75)
# octagon(50)


# NEED TO CONSIDER UPDATING THIS USING EVAL FUNCTIONS ... OR IS WHAT I AM USING ALREADY SUPERIOR???
# ADD A HEXAGON TO LIST ... WILL NEED A DIFFRENT OFFSET AND SHIFT
