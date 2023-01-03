import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
#stops window from updating, so window manually updates, speeds up the game
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
# max speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
# max speed
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
# max speed
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# everytime it moves, moves 0.05 pixels right, and 0.05 pixels up 
ball.dx = 0.15
ball.dy = 0.10

# Pen
pen = turtle.Turtle()
# animation speed
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto (0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    # sets paddle a to new y coord (up 20)
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    # sets paddle a to new y coord (up 20)
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    # sets paddle a to new y coord (up 20)
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    # sets paddle a to new y coord (up 20)
    paddle_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
# Up and Down are arrow keys
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    # height is 600, so 300 up and down from 0, and ball is 20 high and 20 wide, so split difference = 290?
    if ball.ycor() > 290:
        ball.sety(290)
        # reverses direction of ball
        ball.dy *= -1
        winsound.PlaySound('C:/Users/jeris/Downloads/Bing Bong Sound Effects.wav', winsound.SND_ASYNC)
        
    
    if ball.ycor() < -290:
        ball.sety(-290)
        # reverses direction of ball
        ball.dy *= -1
        winsound.PlaySound('C:/Users/jeris/Downloads/Bing Bong Sound Effects.wav', winsound.SND_ASYNC)

        

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound('C:/Users/jeris/Downloads/awhellnaw.wav', winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound('C:/Users/jeris/Downloads/awhellnaw.wav', winsound.SND_ASYNC)

    # paddle and ball collision, ball 10 legnth side, paddle at 350, so basically 340 at edges
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('C:/Users/jeris/Downloads/Bing Bong Sound Effects.wav', winsound.SND_ASYNC)
    
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('C:/Users/jeris/Downloads/Bing Bong Sound Effects.wav', winsound.SND_ASYNC)