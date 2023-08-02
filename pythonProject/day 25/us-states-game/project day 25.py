import turtle,pandas,time
from turtle import Turtle,Screen

screen = Screen()
screen.title("U.S. STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
get_states =data["state"].tolist()
guessed_state = []

while(len(guessed_state)<50):
    user_guess = screen.textinput(title=f"{len(guessed_state)}/50 correctly guessed",prompt="What's another states name? ").title()

    if user_guess == "Exit":
        state_to_learn = [state for state in get_states if state not in guessed_state]
        print(state_to_learn)
        DATA = pandas.DataFrame(state_to_learn)
        DATA.to_csv("States_to_learn.csv")
        break

    if user_guess in get_states:
        guessed_state.append(user_guess)
        t =turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_guess)

screen.exitonclick()


