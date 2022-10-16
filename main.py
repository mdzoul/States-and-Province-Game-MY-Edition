import turtle
import pandas as pd


def show_state(ans):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(arg=f"{ans}", align="center", font=("Helvetica", 8, "bold"))
    
    
def states_to_learn():
    missing_states = [state for state in state_list if state not in guessed_states]
    new_data = pd.DataFrame(missing_states)
    print(new_data)


def win_game():
    turtle.goto(0, 0)
    turtle.hideturtle()
    turtle.write(arg="Congratulations!", align="center", font=("Helvetica", 72, "normal"))
    turtle.goto(0, -24)
    turtle.hideturtle()
    turtle.write(arg="You managed to guess all 13 states!", align="center", font=("Helvetica", 24, "normal"))
    
    
def exit_game(number):
    turtle.goto(0, 0)
    turtle.hideturtle()
    turtle.write(arg="Try harder!", align="center", font=("Helvetica", 72, "normal"))
    turtle.goto(0, -24)
    turtle.hideturtle()
    turtle.write(arg=f"You managed to guess {number}/13 states!", align="center", font=("Helvetica", 24, "normal"))


screen = turtle.Screen()
screen.title("Malaysia States Game")

image = "malaysia_blank_map.png"
screen.setup(width=1024, height=390)
screen.bgpic(image)

df = pd.read_csv("13_MY_states.csv")
state_list = df["state"].to_list()
guessed_states = []
score = 0

all_states = 13
while score != all_states:
    answer = screen.textinput(title=f"{score}/13 States", prompt="What's another state's name?").title()

    if answer == "Exit":
        break

    if answer in state_list and answer not in guessed_states:
        guessed_states.append(answer)
        score += 1
        correct_state = df[df.state == answer]
        index = correct_state.index
        for i in index:
            x, y = correct_state.x[i], correct_state.y[i]
            show_state(answer)

if score == all_states:
    win_game()
else:
    states_to_learn()
    exit_game(score)

turtle.mainloop()
