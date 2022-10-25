import pandas
from turtle import Turtle, Screen
from time import sleep


screen = Screen()
screen.title("GUESS ALL US STATE NAMES")
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")


def write_data(datalist, statename):
    pen = Turtle()
    pen.penup()
    pen.pensize(8)
    pen.hideturtle()
    pen.goto(x=int(datalist.x), y=int(datalist.y))
    pen.pendown()
    pen.write(statename, align="center", font=("Arial", 7, "normal"))
    del pen


missed_list = []
while True:
    state_name = screen.textinput(title="GUESS THE NAMES", prompt="State Name").title()
    state_list = data["state"].to_list()
    if state_name == "Exist":
        break
    elif state_name in state_list:
        missed_list = state_list.remove(state_name)
        data_dict = data[data.state == state_name]
        write_data(data_dict, state_name)
    else:
        tim = Turtle()
        tim.pensize(10)
        tim.color("red")
        tim.hideturtle()
        tim.write("NO SUCH STATE EXIST IN US", align="center", font=("Arial", 24, "normal"))
        sleep(2)
        tim.clear()

data_to_convt = pandas.DataFrame(missed_list)
print(data_to_convt)
# data_to_convt.to_csv()
