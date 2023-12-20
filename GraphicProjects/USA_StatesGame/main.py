import turtle
import pandas

# Screen setup
screen = turtle.Screen()
screen.title(f"U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Marker setup
marker = turtle.Turtle()
marker.hideturtle()
marker.penup()

# Keep user score and right answers
right_answers = []

# Obtains data from csv
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

while len(right_answers) < 50:
    answer_state = screen.textinput(title=f"{len(right_answers)}/50 States Correct",
                                    prompt="What's another state's name").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in right_answers]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break

    if answer_state in all_states and answer_state not in right_answers:
        right_answers.append(answer_state)
        state_info = data[data["state"] == answer_state]
        marker.goto(state_info.x.iloc[0], state_info.y.iloc[0])
        marker.write(f"{answer_state}", align="center")
