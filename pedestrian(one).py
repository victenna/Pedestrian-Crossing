import turtle,time
car=turtle.Turtle()
turtle.tracer(2)
car.up()
car.hideturtle()
wn=turtle.Screen()
wn.setup(800,800)
turtle.bgcolor('light blue')
wn.bgpic('street.gif')

#car image========================================

car=['car2.gif','car3.gif','car4.gif']
t0=turtle.Turtle() #car turtle
t0.hideturtle()
t0.up()
t0.setposition(-400,-210)
t0.setheading(12)
t0.showturtle()
def car_(img0):
    wn.addshape(img0)
    t0.shape(img0)
car_(car[0])

#man image===========================================
image1=['man1.gif','man2.gif','man3.gif','man4.gif','man5.gif','man6.gif'] 
t11=turtle.Turtle() #boy turtle

#X1=180
#Y1=-20
def man_(turtle,X,Y,img):
    wn.addshape(img)
    turtle.shape(img)
    turtle.up()
    turtle.goto(X,Y)
    turtle.showturtle()

man_(t11,180,-20,image1[3]) #start man position

 
#sign image for pedestrians===============================
sign=['w_no.gif','w_yes.gif']
t2=turtle.Turtle() #sign turtle
t2.hideturtle()
t2.up()
t2.setposition(90,20)
t2.showturtle()
def sign_(img1):
    wn.addshape(img1)
    t2.shape(img1)
sign_(sign[1])

#traffic light image=============================================
light=['red_light.gif','yellow_light.gif','green_light.gif']
t3=turtle.Turtle() #traffic light
t3.hideturtle()
t3.up()
t3.setposition(350,150)
t3.showturtle()
def light_(img2):
    wn.addshape(img2)
    t3.shape(img2)
light_(light[2])

turtle.tracer(2)

# function man walks===========================

deltaX=5 #determines direction 0f walking (X coordinate)
deltaY=-2.5 #determines  direction of walking (Y coordinate)

q=-1
move=1
r=0

while True:
    q=q+1
    q0=q%3
    time.sleep(0.03)
    if t0.xcor()<-151:
        car_(car[q0])
        move=1
        t0.fd(10*move)
        light_(light[2])
        sign_(sign[0])
        if t0.xcor==-152:
            t0.shape(car[0])
    if t0.xcor()>-152:
        
        if r<30:
            t0.shape(car[0])
            r=r+1
            light_(light[1])
            sign_(sign[0])
                    
        if r>=29 and r<81:
            r=r+1
            q1=q%6
            light_(light[0])
            sign_(sign[1])
            r1=r-29
            man_(t11,180+r1*deltaX,-20+r1*deltaY,image1[q1])
            time.sleep(0.05)
  
        if r>=81:
            car_(car[q0])
            move=1
            t0.fd(10*move)
            light_(light[2])
            sign_(sign[0])
                        
    if t0.xcor()>500:
        q=-1
        man_(t11,180,-20,image1[3])
        r=0
        t0.hideturtle()
        t0.setposition((-400,-210))
        t0.showturtle()

