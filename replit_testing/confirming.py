import turtle as tr
import time

class Confirmingturtle:

  tr.register_shape('nextbutton.gif')
  
  fontsetup = ("small-caps", 20, 'bold')
  
  global confirmturtle
  confirmturtle = tr.Turtle()
  confirmturtle.hideturtle()
  confirmturtle.speed(10)
  
  def defturt(fontsetup):
    confirmturtle.penup()
    confirmturtle.shape('nextbutton.gif')
    confirmturtle.goto(230, 130)
    confirmturtle.showturtle()

  def confirmendgame(fontsetup):
    confirmturtle.goto(230, 130)
    confirmturtle.showturtle()

  def confirmplayscreen():
    confirmturtle.goto(500,500)
    confirmturtle.hideturtle()
    confirmturtle.clear()

  def confirmlisten():
    confirmturtle.onclick(playscreen)