import turtle
import time

wn = turtle.Screen()
wn.title("The War of the Species: Humans vs The Aliens")
wn.setup(800, 600)
wn.tracer(0)
#wn.bgpic("space.png")

def quit1():
    global running
    running = False
    quit()

class Player1(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("yellow")
        self.penup()
        self.goto(-350, 0)
        self.shape("triangle")
        self.speed(0)
        self.dy = 0




    def up(self):
        self.dy = 0.05
    
    def down(self):
        self.dy = -0.05
    def move(self):
        self.sety(self.ycor() + self.dy)

        if self.ycor() > 280:
            self.sety(-280)
            self.dy = 0.05

        elif self.ycor() < -280:
            self.sety(280)
            self.dy = -0.05
        
class Missile(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("red")
        self.penup()
        self.goto(-350, 0)
        self.shapesize(0.3, 0.3, 0)
        self.shape("triangle")
        self.speed(0)
        self.dx = -0.02
        self.hideturtle()

    def fire(self):
        self.showturtle()
        self.goto(player.xcor(), player.ycor())
        self.dx = 0.5
        turtle.write("M1 released on the Humans", move = False, align = "left", font = ("Arial", 16, "normal"))
        turtle.hideturtle()
        turtle.clear()
        print("M1 released on the Humans")
    def move(self):
        self.setx(self.xcor() + self.dx)
class Player2(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("red")
        self.penup()
        self.goto(350, 0)
        self.shape("triangle")
        self.speed(0)
        self.setheading(180)
        self.dy = 0
        self.dx = 0

    def up(self):
        self.dy = 0.05
    def down(self):
        self.dy = -0.05

    def move(self):
        self.sety(self.ycor() + self.dy)

        if self.ycor() > 280:
            self.sety(-280)
            self.dy = 0.05
        
        elif self.ycor() < -280:
            self.sety(280)
            self.dy = -0.05

    
class Missile2(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("blue")
        self.penup()
        
        self.goto(350, 0)
        self.shape("triangle")
        self.shapesize(0.3, 0.3, 0)
        self.speed(0)
        self.dx = 0.02
        self.hideturtle()

    

    def fire(self):
        self.showturtle()
        self.goto(player2.xcor(), player2.ycor())
        self.dx = -0.5
        turtle.write("M2 released on the Aliens", move = False, align = "right", font = ("Arial", 16, "normal"))
        turtle.hideturtle()
        turtle.clear()
        print("M2 released on the Aliens")
    def move(self):
        self.setx(self.xcor() + self.dx)

'''
class Nuclear_missileS2(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("blue")
        self.penup()
        self.goto(350, 0)
        self.shape("square")
        self.shapesize(5, 1, 0)
        self.speed(0)
        self.dx = 0.02
        self.hideturtle()

    

    def fire(self):
        self.showturtle()
        self.goto(player2.xcor(), player2.ycor())
        self.dx = -0.5
    
        
        turtle.write("Nuclear Bomb striked! on the Aliens",move = False, align = "Center",font = ("Arial", 16, "bold"))
        turtle.hideturtle()        
        
        turtle.clear()
        print("Nuclear Bomb striked on Aliens")

    def move(self):
        self.setx(self.xcor() + self.dx)


''''''
class Nuclear_missileS1(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("blue")
        self.penup()
        self.goto(350, 0)
        self.shape("square")
        self.shapesize(5, 1, 0)
        self.speed(0)
        self.dx = -0.02
        self.hideturtle()

    

    def fire(self):
        self.showturtle()
        self.goto(player.xcor(), player.ycor())
        self.dx = 0.5
        
        turtle.write("Nuclear Bomb striked! on Humans",move = False, align = "Center",font = ("Arial", 16, "bold"))
        turtle.hideturtle()        
        turtle.clear()
        print("Nuclear Bomb striked on Humans")

    def move(self):
        self.setx(self.xcor() + self.dx)
        
''''''
class defendMissile2(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("black")
        self.shape("square")
        self.dx= 0
        self.penup()
        self.goto(350, 0)
        self.shapesize(1, 5, 0)
        self.speed(0)
        self.hideturtle()

    def fire(self):
        self.showturtle()
        self.goto(player.xcor(), player.ycor())
        self.dx = 0.5
        
    def move(self):
        self.setx(self.xcor() + self.dx)
'''
'''
class d(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("blue")
        self.penup()
        self.goto(player2.xcor(), player2.ycor())
        self.speed(0)
        self.hideturtle()
        self.dx = 0

    def fire(self):
        self.showturtle()
        self.goto(self.xcor() + self.ycor())
        self.dx = -0.5

    def move(self):
        self.setx(self.xcor() + self.dx)
'''
 
player = Player1()
missile = Missile()
player2 = Player2()
#nuke1 = Nuclear_missileS1()
#nuke2 = Nuclear_missileS2()
#df = defendMissile2()
missile2 = Missile2()
if player2.distance(missile2) >13:
        print("Got hit!")

turtle.listen()
turtle.onkeypress(player.up, "Up")
turtle.onkeypress(player.down, "Down")
turtle.onkeypress(player2.up, "9")
turtle.onkeypress(player2.down, "3")
turtle.onkeypress(missile.fire, "F5")
turtle.onkeypress(missile2.fire, "F12")
#turtle.onkeypress(nuke2.fire, "s")
#turtle.onkeypress(nuke1.fire, "w")

#turtle.onkeypress(df.fire, "m")
turtle.onkeypress(quit1, "q")

running = True

while running:
    player.move()
    missile.move()
    player2.move()
    missile2.move()
    #nuke2.move()
    #nuke1.move()
    #df.move()
    wn.update() 
 #wn.bye()
    if player2.distance(missile)< 13:
        turtle.write("Aliens win!, the Home is lost.............", move = False, align = "center", font = ("Arial", 16, "normal"))
        print("Game Over")
        player2.hideturtle()
        player.hideturtle()
        turt
        
        '''for i in range(5):
            time.sleep(0.5)
            
            player2.hideturtle()
            time.sleep(0.5)
            player2.showturtle()'''
    if player.distance(missile2)< 13:
        
        turtle.write("Humans win!, the Home is saved.............", move = False, align = "center", font = ("Arial", 16, "normal"))
        print("Game Over")
        '''
    if missile2.distance(df)<5:
        missile2.hideturtle()
        print("Got Defended")
        '''
wn.mainloop()















