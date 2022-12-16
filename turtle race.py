from turtle import Turtle as t,Screen as s
import random
screen=s() 
screen.colormode(255)
screen.setup(width=500,height=500) 
user=screen.textinput(title="turtle race",prompt="Make a bet on any turtle you are sure to win out of \ngreen,blue,yellow,orange,red,black. ")
colors=["blue","black","orange","red","yellow","green"] 
posy=[40,20,0,-20,-40,-60] 
allturtles=[]
for i in range(0,6):
  tim=t(shape="turtle")  
  tim.color(colors[i])
  tim.penup()
  tim.goto(x=-230, y=3*posy[i]) 
  allturtles.append(tim) 
if user:
    race_on=True 
while(race_on):
    for turtle in allturtles: 
      
      if(turtle.xcor()>=230): 
          race_on=False
          winner=turtle.pencolor() 
          if(winner==user):
            print(f"You won.{winner} is the winner\n") 
          else:
            print(f"You lose.{winner} is the winner\n")
      randds=random.randint(0,10)
      turtle.forward(randds)
screen.exitonclick() 