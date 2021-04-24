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

def reset():
  turtle.clearscreen()
  turtle.hideturtle()
  drawPig()

num = 1
while (answer != "quit"):
  reset()
  turtle.write("You asked: " +answer, align="center", font=("Times New Roman",20, "bold"))
  time.sleep(3)
  reply=bank[randint(0,7)]
  turtle.write(reply, align="center", font=("Arial", 20, "bold"))
  time.sleep(2)
  answer = screen.textinput("Ask a Question", "Wait 3s for response or type quit to exit")
  

if (answer == "quit"):
  turtle.clearscreen()
  turtle.hideturtle()
  turtle.write("I knew it. Bye-bye!", align="center", font=("Arial", 20, "bold"))
