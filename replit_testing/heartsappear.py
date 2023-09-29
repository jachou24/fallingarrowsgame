import turtle as tr

class Hearts:
  
  tr.register_shape("heart.gif")

  global turtles
  turtles = []

  def __init__(self, lives):
    self.lives = lives
    for hearts in range(lives):
      self.name = lives - hearts
      heartsturtle = tr.Turtle()
      heartsturtle.hideturtle()
      heartsturtle.penup()
      heartsturtle.shape("heart.gif")
      heartsturtle.setx(250)
      heartsturtle.goto(heartsturtle.xcor()-(hearts*45),125)
      turtles.append(heartsturtle)

  def showlives(lives):
    for n in range(lives):
      turtles[n].showturtle()
  
  def removelife(lives):
    currentheartsturtle = turtles[lives]
    currentheartsturtle.hideturtle()

  def resetlives(lives):
    for n in range(lives):
      Hearts.removelife(lives)