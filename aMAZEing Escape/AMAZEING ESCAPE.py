import pygame, sys
import os
from pygame import mixer
#from EasyMaze_2 import *
import turtle
import math
import random

pygame.init()

clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((950, 650))
pygame.display.set_caption("DATAMIN-C")

#BG_play = pygame.image.load("E:/all/pychram/PycharmProjects/cpen65/maze image/Background.png")
#BG_play = pygame.transform.scale(BG_play, (950, 650))
#DEFAULT_IMAGE_SIZE = (950,650)
#BG_play = pygame.transform.scale(BG_play, DEFAULT_IMAGE_SIZE)

#########################################

BG = pygame.image.load(os.path.join("stars5.png"))
BG = pygame.transform.scale(BG, (950, 650))
width = 950

#background music
mixer.music.load("Cute Background.wav")
mixer.music.play(-1)


class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    #def draw(selfself):

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

#font
def get_font(size):
    return pygame.font.Font("font.ttf", size)

#Play Button
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()


        SCREEN.fill("black")
        #SCREEN.blit(BG_play,(0,0))

        PLAY_TEXT = get_font(45).render("Choose Level", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(477, 120))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(477, 600),
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Red")

        PLAY_EASY = Button(image=None, pos=(477, 250),
                            text_input="EASY", font=get_font(40), base_color="White", hovering_color="yellow")

        PLAY_MEDIUM = Button(image=None, pos=(477, 320),
                            text_input="INTERMEDIATE", font=get_font(35), base_color="White", hovering_color="Green")

        #PLAY_HARD = Button(image=None, pos=(477, 390),
                            #text_input="HARD", font=get_font(40), base_color="White", hovering_color="Blue")

        PLAY_EASY.changeColor(PLAY_MOUSE_POS)
        PLAY_EASY.update(SCREEN,)

        PLAY_MEDIUM.changeColor(PLAY_MOUSE_POS)
        PLAY_MEDIUM.update(SCREEN)

        #PLAY_HARD.changeColor(PLAY_MOUSE_POS)
        #PLAY_HARD.update(SCREEN)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if PLAY_EASY.checkForInput(PLAY_MOUSE_POS):
                    click_1 = mixer.Sound("Beep_Effect.wav")
                    click_1.play()
                    Easy()

                if PLAY_MEDIUM.checkForInput(PLAY_MOUSE_POS):
                    click_1 = mixer.Sound("Beep_Effect.wav")
                    click_1.play()
                    INTERMEDIATE()


                #if PLAY_HARD.checkForInput(PLAY_MOUSE_POS):
                    #click_1 = mixer.Sound("Beep_Effect.wav")
                    #click_1.play()


                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    click = mixer.Sound("tiktok-ending.wav")
                    click.play()
                    main_menu()

        pygame.display.update()

#def maze_1():
   # while True():
  #      EASY_MOUSE_POS = pygame.mouse.get_pos()

       # SCREEN.fill("Black")

#Easy mode
def Easy():
    while True:
        EASY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        #OPTIONS_TEXT = get_font(70).render("OPTIONS", True, "White")
        #OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 120))

        #SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        LEVEL1_EASY = Button(image=None, pos=(477, 250),
                            text_input="Level 1", font=get_font(40), base_color="White", hovering_color="yellow")

        LEVEL2_MEDIUM = Button(image=None, pos=(477, 320),
                            text_input="Level 2", font=get_font(40), base_color="White", hovering_color="Green")

        OPTIONS_BACK = Button(image=None, pos=(800, 600),
                              text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")


        OPTIONS_BACK.changeColor(EASY_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        LEVEL1_EASY.changeColor(EASY_MOUSE_POS)
        LEVEL1_EASY.update(SCREEN)

        LEVEL2_MEDIUM.changeColor(EASY_MOUSE_POS)
        LEVEL2_MEDIUM.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if LEVEL1_EASY.checkForInput(EASY_MOUSE_POS):
                    LEVEL1()

                if LEVEL2_MEDIUM.checkForInput(EASY_MOUSE_POS):
                    LEVEL2()

                if OPTIONS_BACK.checkForInput(EASY_MOUSE_POS):
                    click_option = mixer.Sound("tiktok-ending.wav")
                    click_option.play()
                    main_menu()
        pygame.display.update()



def LEVEL1():
    while True:
        LEVEL1_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        #OPTIONS_TEXT = get_font(70).render("OPTIONS", True, "White")
        #OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 120))

        #SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        LEVEL1_EASY = Button(image=None, pos=(477, 250),
                            text_input="Level 1", font=get_font(40), base_color="White", hovering_color="yellow")

        OPTIONS_BACK = Button(image=None, pos=(800, 600),
                              text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")


        OPTIONS_BACK.changeColor( LEVEL1_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        LEVEL1_EASY.changeColor( LEVEL1_MOUSE_POS)
        LEVEL1_EASY.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if OPTIONS_BACK.checkForInput( LEVEL1_MOUSE_POS):
                    click_option = mixer.Sound("tiktok-ending.wav")
                    click_option.play()
                    main_menu()

        pygame.display.update()

        turtle.begin_fill()
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
                turtle.done()
                turtle.bye()

            erasable = erasableWrite(t, player.gold, font=("Press start 2p", 50, "normal"), align="center")
            erasable.clear()
            wn.update()

        # screen.title('Creating Buttons in Python Turtle')

        #turtle.done()

pygame.display.update()


def LEVEL2():
    while True:
        LEVEL2_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        #OPTIONS_TEXT = get_font(70).render("OPTIONS", True, "White")
        #OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 120))

        #SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        LEVEL2_EASY = Button(image=None, pos=(477, 320),
                            text_input="Level 1", font=get_font(40), base_color="White", hovering_color="yellow")

        OPTIONS_BACK = Button(image=None, pos=(800, 600),
                              text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")


        OPTIONS_BACK.changeColor( LEVEL2_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        LEVEL2_EASY.changeColor( LEVEL2_MOUSE_POS)
        LEVEL2_EASY.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if OPTIONS_BACK.checkForInput( LEVEL2_MOUSE_POS):
                    click_option = mixer.Sound("tiktok-ending.wav")
                    click_option.play()
                    main_menu()


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

        # turtle.register_shape("easy_maze_2.gif")

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
            [1, 3, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 5, 0, 0, 1, 1, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 5, 1],
            [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
            [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 5, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 5, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 5, 1, 1, 1, 1, 1, 0, 0, 0, 0, 5, 1, 1],
            [1, 1, 1, 1, 0, 0, 5, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 5, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 5, 1, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 1, 1],
            [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 7, 6, 9],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

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
                        screen.bgpic("easy_maze_2.png")
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
                turtle.done()
                turtle.bye()

            erasable = erasableWrite(t, player.gold, font=("Press start 2p", 50, "normal"), align="center")
            erasable.clear()
            wn.update()

        # screen.title('Creating Buttons in Python Turtle')

        pygame.display.update()

#INTERMEDIATE
def INTERMEDIATE():
    while True:
        MEDIUM_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        #OPTIONS_TEXT = get_font(70).render("OPTIONS", True, "White")
        #OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 120))

        #SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        LEVEL1_MEDIUM = Button(image=None, pos=(477, 250),
                            text_input="Level 1", font=get_font(40), base_color="White", hovering_color="yellow")

        LEVEL2_MEDIUM = Button(image=None, pos=(477, 320),
                            text_input="Level 2", font=get_font(40), base_color="White", hovering_color="Green")

        MEDIUM_BACK = Button(image=None, pos=(800, 600),
                              text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")


        MEDIUM_BACK.changeColor(MEDIUM_MOUSE_POS)
        MEDIUM_BACK.update(SCREEN)

        LEVEL1_MEDIUM.changeColor(MEDIUM_MOUSE_POS)
        LEVEL1_MEDIUM.update(SCREEN)

        LEVEL2_MEDIUM.changeColor(MEDIUM_MOUSE_POS)
        LEVEL2_MEDIUM.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if LEVEL1_MEDIUM.checkForInput(MEDIUM_MOUSE_POS):
                    LEVEL1M()

                if LEVEL2_MEDIUM.checkForInput(MEDIUM_MOUSE_POS):
                    LEVEL2M()

                if MEDIUM_BACK.checkForInput(MEDIUM_MOUSE_POS):
                    click_option = mixer.Sound("tiktok-ending.wav")
                    click_option.play()
                    main_menu()
        pygame.display.update()

def LEVEL1M():
    while True:
        LEVEL1M_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        #OPTIONS_TEXT = get_font(70).render("OPTIONS", True, "White")
        #OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 120))

        #SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        LEVEL1_M = Button(image=None, pos=(477, 320),
                            text_input="Level 1", font=get_font(40), base_color="White", hovering_color="yellow")

        OPTIONS_BACK = Button(image=None, pos=(800, 600),
                              text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")


        OPTIONS_BACK.changeColor( LEVEL1M_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        LEVEL1_M.changeColor(LEVEL1M_MOUSE_POS)
        LEVEL1_M.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if OPTIONS_BACK.checkForInput( LEVEL1M_MOUSE_POS):
                    click_option = mixer.Sound("tiktok-ending.wav")
                    click_option.play()
                    INTERMEDIATE()
        pygame.display.update()

        #Create window
        win = turtle.Screen()
        win.bgcolor("Black")
        win.title("aMAZEing Escape")
        win.setup(950,650)
        win.tracer(0)

        #Register shapes
        images = ["player_right.gif", "player_left.gif", "TREASURE.gif",
                  "BLOCK.gif", "enemy_left.gif", "enemy_right.gif", "goal.gif", "Medium_Maze1.gif"]
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
                self.shape("BLOCK.gif")
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
                self.gold = 5
                self.goto(x, y)
                self.direction = random.choice(["up", "down", "left", "right"])

            #Movement of the enemy
            def move(self):
                if self.direction == "up":
                    dx = 24
                    dy = 0
                elif self.direction == "down":
                    dx = 24
                    dy = 0
                elif self.direction == "left":
                    dx = -24
                    dy = 0
                    self.shape("enemy_left.gif")
                elif self.direction == "right":
                    dx = 24
                    dy = 0
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

        #First set
        set_1 = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 8, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 7, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
            [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 7, 1, 1, 1],
            [1, 7, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 7, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

         ]

        #Add a treasures list
        Treasures = []

        #Add enemies list
        enemies = []

        #Add maze to the list of mazes
        sets.append(set_1)

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
                        screen.bgpic("Medium_Maze1.gif")
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

        #Setup the first set of the maze
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
                    screen.bgpic('Medium_Maze1.gif')
                    mode = 'light'
                else:

                    mode = 'dark'

        screen.onclick(button_click)  # comment this to stop rectangle button and see circle button

        turtle.done()



#level2 of INTERMEDIATE
def LEVEL2M():
    while True:
        LEVEL2M_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        #OPTIONS_TEXT = get_font(70).render("OPTIONS", True, "White")
        #OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 120))

        #SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        LEVEL2_M = Button(image=None, pos=(477, 320),
                            text_input="Level 2", font=get_font(40), base_color="White", hovering_color="yellow")

        OPTIONS_BACK = Button(image=None, pos=(800, 600),
                              text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")


        OPTIONS_BACK.changeColor( LEVEL2M_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        LEVEL2_M.changeColor(LEVEL2M_MOUSE_POS)
        LEVEL2_M.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if OPTIONS_BACK.checkForInput(LEVEL2M_MOUSE_POS):
                    click_option = mixer.Sound("tiktok-ending.wav")
                    click_option.play()
                    INTERMEDIATE()
        pygame.display.update()

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



#Home page option button
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        OPTIONS_TEXT = get_font(70).render("OPTIONS", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 120))

        SOUND_TEXT = get_font(40).render("MUSIC:", True, "Orange")
        SOUND_RECT = OPTIONS_TEXT.get_rect(center=(558, 319))

        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        SCREEN.blit(SOUND_TEXT, SOUND_RECT)

        OPTIONS_BACK = Button(image=None, pos=(447, 600),
                              text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")

        space = Button(image=None, pos=(653, 300),
                              text_input="|", font=get_font(35), base_color="White", hovering_color="Red")

        SOUND_ON = Button(image=None, pos=(608, 302),
                               text_input="ON", font=get_font(30), base_color="Orange", hovering_color="Yellow")

        SOUND_OFF = Button(image=None, pos=(713, 302),
                               text_input="OFF", font=get_font(30), base_color="Orange", hovering_color="Red")

        OPTIONS_CREDITS = Button(image=None, pos=(447, 358),text_input="Credits", font=get_font(40), base_color="Orange",
                                 hovering_color="Light green")

        OPTIONS_CREDITS.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_CREDITS.update(SCREEN)

        space.changeColor(OPTIONS_MOUSE_POS)
        space.update(SCREEN)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        #Sound control
        SOUND_ON.changeColor(OPTIONS_MOUSE_POS)
        SOUND_ON.update(SCREEN)

        SOUND_OFF.changeColor(OPTIONS_MOUSE_POS)
        SOUND_OFF.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if  SOUND_OFF.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.fadeout(1000)
                    click = mixer.Sound("tiktok-ending.wav")
                    click.play()
                if SOUND_ON.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.play(-1)
                    click_1 = mixer.Sound("Beep_Effect.wav")
                    click_1.play()

                if OPTIONS_CREDITS.checkForInput(OPTIONS_MOUSE_POS):
                    click = mixer.Sound("menu.wav")
                    click.play()
                    credits()

                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    click_option = mixer.Sound("tiktok-ending.wav")
                    click_option.play()
                    main_menu()

        pygame.display.update()

#Credits
def credits():
    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        OPTIONS_TEXT1 = get_font(50).render("DATA", True, "Light Blue")
        OPTIONS_TEXT = get_font(50).render("MIN-C", True, "Pink")
        OPTIONS_RECT1 = OPTIONS_TEXT.get_rect(center=(380, 110))
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(580, 110))

        SOUND_TEXT = get_font(40).render("Members: ", True, "Green")
        SOUND_RECT = SOUND_TEXT.get_rect(center=(500, 190))

        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        SCREEN.blit(OPTIONS_TEXT1, OPTIONS_RECT1)
        SCREEN.blit(SOUND_TEXT, SOUND_RECT)

        Names_CREDITS1 = Button(image=None, pos=(500, 240),text_input="Aguado Danielle Ysabelle M.", font=get_font(30), base_color="Orange",
                                 hovering_color="Light green")
        Names_CREDITS2 = Button(image=None, pos=(425, 280),text_input="Albero justine Kate P.", font=get_font(30), base_color="Orange",
                                 hovering_color="Light green")
        Names_CREDITS3 = Button(image=None, pos=(410, 325),text_input="Alegre Ericka Jane A.", font=get_font(30), base_color="Orange",
                                 hovering_color="Light green")
        Names_CREDITS4 = Button(image=None, pos=(465, 370),text_input="Bangay Rhonan Richmond D.", font=get_font(30), base_color="Orange",
                                 hovering_color="Light green")
        Names_CREDITS5 = Button(image=None, pos=(365, 410),text_input="Mendoza Jessa Mae D.", font=get_font(30), base_color="Orange",
                                 hovering_color="Light green")
        Names_CREDITS6 = Button(image=None, pos=(350, 450),text_input="Serenio Marc Jay D.", font=get_font(30), base_color="Orange",
                                 hovering_color="Light green")
        Names_CREDITS7 = Button(image=None, pos=(320, 490),text_input="Tayab Dirk M.", font=get_font(30), base_color="Orange",
                                 hovering_color="Light green")
        credits_BACK = Button(image=None, pos=(447, 600),
                              text_input="BACK", font=get_font(50), base_color="White", hovering_color="Red")

        Names_CREDITS1.changeColor(CREDITS_MOUSE_POS)
        Names_CREDITS1.update(SCREEN)

        Names_CREDITS2.changeColor(CREDITS_MOUSE_POS)
        Names_CREDITS2.update(SCREEN)

        Names_CREDITS3.changeColor(CREDITS_MOUSE_POS)
        Names_CREDITS3.update(SCREEN)

        Names_CREDITS4.changeColor(CREDITS_MOUSE_POS)
        Names_CREDITS4.update(SCREEN)

        Names_CREDITS5.changeColor(CREDITS_MOUSE_POS)
        Names_CREDITS5.update(SCREEN)

        Names_CREDITS6.changeColor(CREDITS_MOUSE_POS)
        Names_CREDITS6.update(SCREEN)

        Names_CREDITS7.changeColor(CREDITS_MOUSE_POS)
        Names_CREDITS7.update(SCREEN)


        credits_BACK.changeColor(CREDITS_MOUSE_POS)
        credits_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if credits_BACK.checkForInput(CREDITS_MOUSE_POS):
                    click_option = mixer.Sound("tiktok-ending.wav")
                    click_option.play()
                    options()
        pygame.display.update()

def main_menu():
    class Button():
        def __init__(self, image, pos, text_input, font, base_color, hovering_color):
            self.image = image
            self.x_pos = pos[0]
            self.y_pos = pos[1]
            self.font = font
            self.base_color, self.hovering_color = base_color, hovering_color
            self.text_input = text_input
            self.text = self.font.render(self.text_input, True, self.base_color)
            if self.image is None:
                self.image = self.text
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        def update(self, screen):
            if self.image is not None:
                screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)

        def checkForInput(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                              self.rect.bottom):
                return True
            return False

        def changeColor(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                              self.rect.bottom):
                self.text = self.font.render(self.text_input, True, self.hovering_color)
            else:
                self.text = self.font.render(self.text_input, True, self.base_color)

    i = 0
    run = True
    while run:
        SCREEN.blit(BG, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Create looping background
        SCREEN.blit(BG, (i, 0))
        SCREEN.blit(BG, (width + i, 0))
        if i == -width:
            SCREEN.blit(BG, (width + i, 0))
            i = 0
        i -= 1

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(55).render("a M A Z E i n g", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(477, 100))

        MENU_TEXT2 = get_font(55).render("Escape", True, "#b68f40")
        MENU_RECT2 = MENU_TEXT.get_rect(center=(720, 170))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect2.png"), pos=(477, 279),
                             text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect2.png"), pos=(477, 370),
                                text_input="OPTIONS", font=get_font(50), base_color="#d7fcd4", hovering_color="Yellow")
        QUIT_BUTTON = Button(image=pygame.image.load("Options Rect2.png"), pos=(477, 460),
                             text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(MENU_TEXT2, MENU_RECT2)


        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click = mixer.Sound("menu.wav")
                    click.play()
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click = mixer.Sound("menu.wav")
                    click.play()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
