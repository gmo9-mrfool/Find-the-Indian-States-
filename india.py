import pandas as pd
import turtle
import time

IMAGE = "india2.gif"
# screens here

screen = turtle.Screen()
screen.bgpic(IMAGE)

# turtle named tim here
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()

# data here(csv)
data = pd.read_csv("Indian_states.csv")
states = data.States.to_list()
print(states)

guessed_states = []

# timer

start = time.time()
timer = turtle.Turtle()
timer.penup()
timer.hideturtle()
timer.goto(293.0,256.0)
timer.color('black')
window = turtle.Screen()
window.tracer(0)










while len(guessed_states) < 28 and time.time() - start < 300:
    timer.clear()
    timer.write(int(time.time() - start), font=("Courier", 30, "bold"))

    window.update()

    user = turtle.textinput(title=f"Type a state {len(guessed_states)}/28",
                            prompt="Type and you have 5 minutes").title()
    if user in states and user not in guessed_states:
        guessed_states.append(user)
        state_row = data[data.States == user]
        tim.goto(int(state_row.x), int(state_row.y))
        tim.write(user)

screen.exitonclick()
