from pickle import FALSE
from turtle import Turtle,Screen
import random
tim=Turtle(shape="turtle")
tim1=Turtle(shape="turtle")
tim2=Turtle(shape="turtle")
tim3=Turtle(shape="turtle")
tim4=Turtle(shape="turtle")
tim5=Turtle(shape="turtle")
tims=[tim,tim1,tim2,tim3,tim4,tim5]
screen=Screen()
screen.setup(500,400)
user_bet=screen.textinput("Make your bed","Which turtle will win the race ?enter a color:")
print(user_bet)
colors=["red","blue","green","purple","violet","black"]
angle=[100,70,40,10,-20,-50]
for i in range(6):
    tims[i].color(colors[i])
    tims[i].penup()
    tims[i].goto(-230,angle[i])
# tim.goto(-230,100)
# tim1.goto(-230,70)
# tim2.goto(-230,40)
# tim3.goto(-230,10)
# tim4.goto(-230,-20)
# tim5.goto(-230,-50)
# tim.shape("turtle")
is_race_on=False
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in tims:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"you won and the winner is{user_bet}")
            else:
                print(f"you have lost and the winner is {winning_color}")
            break
        rand_distance=random.randint(1,10)
        turtle.forward(rand_distance)


        # if turtle.goto(230,0):
        #     print("finish")
screen.exitonclick()
