import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. STATE GAME")
screen.setup(width=800, height=600)
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
guessed_states = []
while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f'{len(guessed_states)}/50 states correct',
                                   prompt="what's another state").title()
    answer = data[data['state'] == user_answer]

    if user_answer == 'Exit':
        data_list = data.state.to_list()

        missing_states = [missing_states for missing_states in data_list if missing_states not in guessed_states]
        # for state in data_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # states_dict = {
        #     'states': missing_states
        # }
        states_to_learn = pd.DataFrame(missing_states)
        states_to_learn.to_csv('states_to_learn.csv')
        break

    elif answer.index.size > 0:
        x_cor = answer.x.values[0]
        y_cor = answer.y.values[0]
        state = answer['state'].values[0]
        guessed_states.append(state)
        tt = turtle.Turtle()
        tt.penup()
        tt.hideturtle()
        tt.goto(x_cor, y_cor)
        tt.write(state, move=False, align='center', font=('Courier', 12, 'normal'))



# Get Screen X Y Coordinate
# def get_screen_cor(x, y):
#     print(x, y)
#
# screen.onscreenclick(get_screen_cor)