import turtle
from random import *
import time
turtle.hideturtle()

screen = turtle.Screen()


def drawPig():
  screen.setup(568,563)
  screen.bgpic("AskPeppa.png")
drawPig()

answer = screen.textinput("Ask a Question", "Or type quit to exit")

bank = ["Not likely", "Hm, I'm not sure", "Why do you ask", "Yes", "No", "ABSOLUTELY NOT", "Ask again", "I guess"]

while (answer != "quit"):
  turtle.write("You asked: " +answer, align="center", font=("Times New Roman",20, "bold"))
  time.sleep(2)
  reply=bank[randint(0,7)]
  turtle.write(reply, align="center", font=("Arial", 20, "bold"))
  

if (answer == "quit"):
  turtle.write("Thanks for playing!", align="center", font=("Times New Roman",10, "bold"))
