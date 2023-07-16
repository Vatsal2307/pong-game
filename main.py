from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((375,0))
l_paddle = Paddle((-375,0))
ball = Ball()
scorebrd = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update()
    ball.move_ball()

    if ball.ycor() > 295 or ball.ycor() < -296:
        ball.bounce_y()
        ball.ball_speedup()
    if ball.distance(r_paddle) < 50 and ball.xcor()> 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        ball.ball_speedup()
    if ball.xcor() >390:
        scorebrd.l_point()
        ball.reset_pos()
        ball.ball_speedup()
    if ball.xcor() < -390:
        ball.reset_pos()
        scorebrd.r_point()
        ball.ball_speedup()

screen.exitonclick()