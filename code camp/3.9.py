import turtle
    
t = turtle.Turtle()
  
# taking radius of initial radius
r = 10
  



def draw_circle(radius):    
    turtle.up()
    turtle.goto(0,radius) # go to (0, radius)
    turtle.begin_fill() # start fill
    turtle.down() # pen down
    turtle.color('blue')
    times_y_crossed = 0
    x_sign = 1.0
    while times_y_crossed <= 1:
        turtle.forward(2*math.pi*radius/360.0) # move by 1/360
        turtle.right(1.0)
        x_sign_new = math.copysign(1, turtle.xcor())        
        if(x_sign_new != x_sign):
            times_y_crossed += 1
        x_sign = x_sign_new
    turtle.up() # pen up
    turtle.end_fill() # end fill.
    return


def draw line()

# Loop for printing spiral circle
for i in range(100):
    t.circle(r + i, 45)
