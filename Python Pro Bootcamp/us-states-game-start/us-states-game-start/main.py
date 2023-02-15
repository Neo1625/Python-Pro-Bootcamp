import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_marker = turtle.Turtle()
state_marker.penup()
state_marker.hideturtle()

#Guess to title state
answer_state = screen.textinput(title="Guess the state", prompt="What's another states name?").title()

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
x_cor = data["x"].to_list()
y_cor = data["y"].to_list()




correct_guesses = 0
correct_answers = []


while len(correct_answers) < 50:

    if answer_state == "Exit":
        break

    if answer_state in state_list:
        correct_guesses += 1
        state_index = state_list.index(answer_state)
        x = x_cor[state_index]
        y = y_cor[state_index]
        state_marker.goto(x, y)
        state_marker.write(f"{answer_state}")
        correct_answers.append(answer_state)

    elif answer_state not in state_list:
        pass

    answer_state = screen.textinput(title=f"{correct_guesses} / 50 correct",
                                    prompt="What's another states name?").title()


remaining_states = [state for state in state_list if state not in correct_answers]
#for state in state_list:
#    if state not in correct_answers:
#        remaining_states.append(state)

states_to_learn = pandas.Series(remaining_states)
states_to_learn.to_csv("states_to_learn.csv")

print(f"Remaining states: {remaining_states}")
print(f"Guessed states: {correct_answers}")
