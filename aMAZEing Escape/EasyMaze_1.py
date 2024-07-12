import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("aMAZEing Escape")
wn.setup(950, 650)
wn.tracer(0)

# Register Shapes
turtle.register_shape("player_left.gif")
turtle.register_shape("player_right.gif")
turtle.register_shape("TREASURE.gif")
turtle.register_shape("goal.gif")
turtle.register_shape("BLOCKCC.gif")
turtle.register_shape("easy_maze_1.gif")


def erasableWrite(tortoise: object, name: object, font: object, align: object, reuse: object = None) -> object:
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(-400, 100)
    eraser.color("orange")
    eraser.write(name, font=font, align=align)
    return eraser


t = turtle.Turtle()
t.penup()
t.goto(-470, 180)
t.color("white")
style = ('Press Start 2p', 28, 'normal')
t.write('Score:', font=style, move=True)
t.hideturtle()


# Create class
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("pink")
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("player_right.gif")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.gold = 0

    # goto is a turtle command in turtle modules
    # moving the player
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 25

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 25

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 25
        move_to_y = player.ycor()

        self.shape("player_left.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 25
        move_to_y = player.ycor()

        self.shape("player_right.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False


class Door(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("goal.gif")
        self.color("yellow")
        self.penup()
        self.speed(0)


class Complete(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color('black')
        self.penup()
        self.speed(0)


class Score(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("TREASURE.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


levels = [""]

# Define first level

level_1 = [

    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 5, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 5, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 5, 0, 0, 0, 0, 0, 1, 1, 1, 1, 5, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 5, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 5, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 5, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 5, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 5, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 7, 6, 9],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]

# empty list for multiple treasures
treasures = []

# add maze to mazes list
levels.append(level_1)

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
    pen.write(message, font=('Press start 2p', 10, 'normal'))


mode = "dark"
draw_rect_button(pen)


def button_click(x, y):
    global mode
    if Button_x <= x <= Button_x + ButtonLength:
        if Button_y <= y <= Button_y + ButtonWidth:
            if mode == 'dark':
                # screen.bgcolor('white')
                screen.bgpic('easy_maze_1.png')
            else:
                pass

screen.onclick(button_click)  # comment this to stop rectangle button and see circle button


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # get the character at each x,y coordinate
            # note the order of y and x in the next line
            character = level[y][x]
            # calculate the screen x, y coordinates
            screen_x = -300 + (x * 25)
            screen_y = 300 - (y * 25)

            if character == 1:
                pen.goto(screen_x, screen_y)
                pen.shape("BLOCKCC.gif")
                pen.stamp()
                walls.append((screen_x, screen_y))  # insertion of all coordinates

            if character == 9:
                door.goto(screen_x, screen_y)
            if character == 7:
                complete.goto(screen_x, screen_y)
            if character == 6:
                score.goto(screen_x, screen_y)
            if character == 3:
                player.goto(screen_x, screen_y)
            if character == 5:
                treasures.append(Treasure(screen_x, screen_y))


# Create class instances
pen = Pen()
player = Player()
door = Door()
score = Score()
complete = Complete()

# Create unpassable walls through list
walls = []

# Set up the level
setup_maze(levels[1])

# Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

# wn.tracer(0)

# Main Game Loop
while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            treasure.destroy()
            treasures.remove(treasure)

    if player.is_collision(complete):

        t.penup()
        t.goto(-345, -10)
        t.color("white")
        style = ('Press start 2p', 50, 'bold')
        t.write('MAZE COMPLETE!', font=style, move=True)
        t.hideturtle()

    if player.is_collision(score):
        t.penup()
        t.goto(10, -50)
        t.color("white")
        style = ('Press Start 2p', 30, 'bold')
        t.write("Final Score= {}".format(player.gold), font=style, align="center")
        t.hideturtle()

    if player.is_collision(door):
        break

    erasable = erasableWrite(t, player.gold, font=("Press start 2p", 50, "normal"), align="center")
    erasable.clear()
    wn.update()

# screen.title('Creating Buttons in Python Turtle')


