import turtle
import math
import random

#Create window
win = turtle.Screen()
win.bgcolor("Black")
win.title("aMAZEing Escape")
win.setup(950,650)
win.tracer(0)

#Register shapes
images = ["player_right.gif", "player_left.gif", "TREASURE.gif",
          "GBLOCK.gif", "enemy_left.gif", "enemy_right.gif", "goal.gif", "Medium_Maze2.gif"]

for image in images:
    turtle.register_shape(image)

def erasableWrite(tortoise: object, name: object, font: object, align: object, reuse: object = None) -> object:
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(-390, 130)
    eraser.color("orange")
    eraser.write(name, font=font, align=align)
    return eraser


t = turtle.Turtle()
t.penup()
t.goto(-450, 190)
t.color("pink")
style = ('Press Start 2p', 18, 'normal')
t.write('Score:', font=style, move=True)
t.hideturtle()


#Create Pen - pen can do anything that the turtle can do
class TPen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("GBLOCK.gif")
        self.color("white")
        self.penup()                #move the turtle without drawing anything
        self.speed(0)               #animation speed - speed is zero (the fastest)

#Add the player
class TPlayer(turtle.Turtle):
    def __init__(self):
        turtle. Turtle.__init__(self)
        self.shape("player_right.gif")
        self.color("green")
        self.penup()
        self.speed(0)
        self.gold = 0

    #To move the player
    def go_up(self):
        move_to_x = Player.xcor()         #Calculate the spot to move to
        move_to_y = Player.ycor() + 24
        if (move_to_x, move_to_y) not in walls:        #Check if the space has a wall
             self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = Player.xcor()
        move_to_y = Player.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = Player.xcor() + 24
        move_to_y = Player.ycor()

        self.shape("player_right.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = Player.xcor() - 24
        move_to_y = Player.ycor()

        self.shape("player_left.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

#Adding door on the end of the maze
class Door(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("goal.gif")
        self.color("white")
        self.penup()
        self.speed(0)

class Complete(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color('black')
        self.penup()
        self.speed(0)

class checkscore(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

#Adding treasure
class treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("TREASURE.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
    def destroy(self):
        self.goto(2000,2000)    #Remove the object/turtle off the screen
        self.hideturtle()       #Hide or make the turtle invisible

#Adding enemy
class enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("enemy_left.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])
    #Movement of the enemy
    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = 0
            dy = -24
            self.shape("enemy_left.gif")
        elif self.direction == "right":
            dx = 0
            dy = 24
            self.shape("enemy_right.gif")
        else:
            dx = 0
            dy = 0

        #Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        #Check if there is a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #Choose a different direction
            self.direction = random.choice(["up", "down", "left", "right"])
        #Set timer to move next time
        turtle.ontimer(self.move, t = random.randint(50, 250))

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

#Create diferent sets
sets = [""]

#Second set
set_2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 8, 1, 1, 7, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 7, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 7, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 7, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 7, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 7, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 5, 4],
    [1, 7, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 3, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 7, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 3, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 7, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
 ]

#Add a treasures list
Treasures = []

#Add enemies list
enemies = []

#Add maze to the list of mazes
sets.append(set_2)

screen = turtle.Screen()
screen.setup(950, 650)
screen.bgcolor('#111111')

pen = turtle.Turtle()
pen.hideturtle()
pen.pencolor('#111111')
pen.fillcolor('white')

Button_x = 315
Button_y = 170
ButtonLength = 140
ButtonWidth = 30

mode = 'dark'


def draw_rect_button(pen, message='Show Solution!'):
    pen.penup()
    pen.begin_fill()
    pen.goto(Button_x, Button_y)
    pen.goto(Button_x + ButtonLength, Button_y)
    pen.goto(Button_x + ButtonLength, Button_y + ButtonWidth)
    pen.goto(Button_x, Button_y + ButtonWidth)
    pen.goto(Button_x, Button_y)
    pen.end_fill()
    pen.goto(318, 180)
    pen.write(message, font=('Press start 2p', 8, 'normal'))


mode = "dark"
draw_rect_button(pen)


def button_click(x, y):
    global mode
    if Button_x <= x <= Button_x + ButtonLength:
        if Button_y <= y <= Button_y + ButtonWidth:
            if mode == 'dark':
                # screen.bgcolor('white')
                screen.bgpic("Medium_Maze2.gif")
            else:
                pass

screen.onclick(button_click)  # comment this to stop rectangle button and see circle button

#Create Setup Function
def setup(set):
    for y in range(len(set)):
        for x in range(len(set[y])):
            c = set [y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            #1 represents the walls
            if c == 1:
                Pen.goto(screen_x, screen_y) #goto() - move the turtle to position x,y
                Pen.stamp()   #stamp() - leaves an impression of a turtle shape at the current location
                walls.append((screen_x, screen_y))  #Add coordinate pairs in the walls
            #8 represents the player
            if c == 8:
                Player.goto(screen_x, screen_y)
            #7 represents treasure
            if c == 7:
                Treasures.append(treasure(screen_x, screen_y))
            #3 represents the enemy
            if c == 3:
                enemies.append(enemy(screen_x, screen_y))
            if c == 5:
                complete.goto(screen_x, screen_y)
            if c == 2:
                score.goto(screen_x, screen_y)
            #4 represents the door
            if c == 4:
                door.goto(screen_x, screen_y)

#Create class instances
Pen = TPen()
Player = TPlayer()
door = Door()
score = checkscore()
complete = Complete()

#Create wall coordinate list
walls = []

#Setup the second set of the maze
setup(sets[1])

#Keyboard Binding
turtle.listen()                         # listen() method sets focus on the turtle screen to capture events.
turtle.onkey(Player.go_left, "Left")    #onkey() method invokes the method specific to the captured keystroke. The first argument of onkey() is the function to be called and the second argument is the key.
turtle.onkey(Player.go_right, "Right")
turtle.onkey(Player.go_up, "Up")
turtle.onkey(Player.go_down, "Down")

#Turn off screen updates
win.tracer(0)

#Start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t = 250)     #Tell the enemy to move after 250 milliseconds

#Main game loop
while True:
    #Check for the collision of Player with Treasure
    for treasure in Treasures:
        if Player.is_collision(treasure):
            Player.gold += treasure.gold                    #Add treasure gold to the player gold
            print ("Gold collected: {}".format(Player.gold))
            treasure.destroy()                              #Destroy the treasure
            Treasures.remove(treasure)                      #Remove treasure from the list

    #Iterate through enemy list to see if the player collide
    for enemy in enemies:
        if Player.is_collision(enemy):
            Player.gold -= 5
            print("Gold collected: {}".format(Player.gold))

    if Player.is_collision(complete):
        t.penup()
        t.goto(-345, -10)
        t.color("white")
        style = ('Press start 2p', 38, 'bold')
        t.write('MAZE COMPLETE!', font=style, move=True)
        t.hideturtle()

    if Player.is_collision(score):
        t.penup()
        t.goto(10, -50)
        t.color("white")
        style = ('Press Start 2p', 30, 'bold')
        t.write("Final Score= {}".format(Player.gold), font=style, align="center")
        t.hideturtle()

    if Player.is_collision(door):
        break

    erasable = erasableWrite(t, Player.gold, font=("Press start 2p", 25, "bold"), align="center")
    erasable.clear()

    win.update()

screen = turtle.Screen()

#screen.title('Creating Buttons in Python Turtle')
screen.bgcolor('#111111')
pen = turtle.Turtle()
pen.hideturtle()
pen.pencolor('#111111')
pen.fillcolor('white')

Button_x = 315
Button_y = 170
ButtonLength = 140
ButtonWidth = 30

mode = 'dark'


def draw_rect_button(pen, message = 'Show Solution!'):
    pen.penup()
    pen.begin_fill()
    pen.goto(Button_x, Button_y)
    pen.goto(Button_x + ButtonLength, Button_y)
    pen.goto(Button_x + ButtonLength, Button_y + ButtonWidth)
    pen.goto(Button_x, Button_y + ButtonWidth)
    pen.goto(Button_x, Button_y)
    pen.end_fill()
    pen.goto(318, 180)
    pen.write(message, font = ('Press start 2p', 7, 'normal'))

draw_rect_button(pen)


def button_click(x, y):
    global mode
    if Button_x <= x <= Button_x + ButtonLength:
        if Button_y <= y <= Button_y + ButtonWidth:
            #screen.s('black')
            screen.bgpic('Medium_Maze2.gif')
            mode = 'light'
        else:

            mode = 'dark'

screen.onclick(button_click)  # comment this to stop rectangle button and see circle button

turtle.done()


