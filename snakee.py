import turtle
import time
import random
delay = 0.08
score = 0
high_score = 0
# Set screen
wn = turtle.Screen()
wn.title("Classic Snake Game--MOMO")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("grey")
head.penup()
head.goto(0, 0)
head.direction = "stop"

border = turtle.Turtle()  # making boerder
border.up()
border.color('white')
border.goto(-320, -320)
border.down()
border.goto(320, -320)
border.goto(320, 320)
border.goto(-320, 320)
border.goto(-320, -320)

#  fooood
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 100)
segments = []
# to change score board
sb = turtle.Turtle()
sb.speed(0)
sb.shape("square")
sb.color("white")
sb.penup()
sb.hideturtle()
sb.goto(0, 260)
sb.write("Classic Snake Game", align="center", font=("Courier", 18, "bold"))
sb.goto(0, -260)
sb.write("        *Eat veggies for point* \n **Avoid Borders and Don't bite your tail**", align="center",
          font=("Courier", 18, "normal"))
sb.goto(0, 260)

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()                          #keyboard binfding
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
# Main game loop
while True:
    wn.update()
    #  hit border!!!!!!!!!!
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        # Hide the segments
        for segment in segments:
            segment.goto(380, 380)
        segments.clear()
        score = 0
        delay = 0.08
        sb.clear()
        sb.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "normal"))
    # eat your  food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        if (score+10)%50 == 0 and score!=0:
            food.shape("turtle")
            food.color("red")
        else:
            food.shape("circle")
            food.color("green")
        food.goto(x, y)
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.0019
        # Increase the score
        if (score ) % 50 == 0 and score != 0:
            score += 20
        else:
            score += 10
        if score > high_score:
            high_score = score
        sb.clear()
        sb.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "normal"))
        # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    # if bites its tail!!!!!
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(500, 500)
            segments.clear()
            score = 0
            delay = 0.08
            sb.clear()
            sb.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 18, "normal"))
    time.sleep(delay)
wn.mainloop()
