import turtle as tr
import random
from fallingarrow import Falling
from confirming import Confirmingturtle, confirmturtle
import time
import threading
from heartsappear import Hearts

fontsetup = ("small-caps", 20, 'bold')

tr.register_shape('anpro.gif')
tr.register_shape('andark.gif')
tr.register_shape('karpro.gif')
tr.register_shape('kardark.gif')
tr.register_shape('sharpro.gif')
tr.register_shape('shardark.gif')


tr.register_shape('startbutton.gif')
tr.register_shape('clickedstart.gif')

tr.register_shape('uparrow.gif')
tr.register_shape('downarrow.gif')

tr.register_shape('fallleft.gif')
tr.register_shape('fallup.gif')
tr.register_shape('falldown.gif')
tr.register_shape('fallright.gif')

wn = tr.Screen()
wn.title(" ")
wn.bgpic('bgblack.gif')
wn.screensize(600,400)
wn.setup(width = 1.0, height = 1.0)

Confirmingturtle.defturt(fontsetup)

def initarrows():
  global leftarrow
  global uparrow
  global downarrow
  global rightarrow
  
  leftarrow = tr.Turtle()
  leftarrow.hideturtle()
  leftarrow.penup()
  leftarrow.shape('fallleft.gif')
  leftarrow.setheading(90)
  leftarrow.goto(-240,-75)
  
  uparrow = tr.Turtle()
  uparrow.hideturtle()
  uparrow.penup()
  uparrow.shape('fallup.gif')
  uparrow.setheading(0)
  uparrow.goto(-190,-75)
  
  downarrow = tr.Turtle()
  downarrow.hideturtle()
  downarrow.penup()
  downarrow.shape('falldown.gif')
  downarrow.setheading(180)
  downarrow.goto(-140,-75)
  
  rightarrow = tr.Turtle()
  rightarrow.hideturtle()
  rightarrow.penup()
  rightarrow.shape('fallright.gif')
  rightarrow.setheading(270)
  rightarrow.goto(-90,-75)

  leftarrow.showturtle()
  uparrow.showturtle()
  downarrow.showturtle()
  rightarrow.showturtle()

def endgame():
  global canpressstart
  canpressstart = True
  leftarrow.hideturtle()
  uparrow.hideturtle()
  downarrow.hideturtle()
  rightarrow.hideturtle()
  Falling.reportscore()

def wnanimate():
  global bganimate
  bganimate = True
  while bganimate==True:
    wn.bgpic('bgfire1.png')
    time.sleep(.4)
    wn.bgpic('bgfire2.png')
    time.sleep(.4)
  wn.bgpic('bgblack.gif')

def playclicked(x, y):
  global oogway
  global fontsetup
  global canpressstart
  if canpressstart == False:
    pass
  else:
    canpressstart = False
    oogway.shape('clickedstart.gif')
    time.sleep(.2)
    oogway.shape('startbutton.gif')
    time.sleep(.4)
    charslot1.hideturtle()
    charslot2.hideturtle()
    charslot3.hideturtle()
    oogway.hideturtle()
    oogway.clear()
    Falling.resetgamestart()
    playt = threading.Thread(target=wnanimate)
    playt.start()
    Hearts.showlives(Falling.getlives())
    initarrows()
    #
    while Falling.getlives() > 0:
      randomizednumber = random.randint(0,3)
      arrow1 = Falling(randomizednumber)
      arrow1.startfall("up",randomizednumber)
    global bganimate
    bganimate = False
    Falling.stopdeathanimation = False
    endgame()

def slot1(x,y):
  charslot1.shape('anpro.gif') # highlighted
  charslot2.shape('kardark.gif') # dark
  charslot3.shape('shardark.gif') # dark
  Falling.selectcharacter(1)

def slot2(x,y):
  charslot1.shape('andark.gif') # dark
  charslot2.shape('karpro.gif') # highlighted
  charslot3.shape('shardark.gif') # dark
  Falling.selectcharacter(2)
  
def slot3(x,y):
  charslot1.shape('andark.gif') # dark
  charslot2.shape('kardark.gif') # dark
  charslot3.shape('sharpro.gif') # highlighted
  Falling.selectcharacter(3)
  
def playscreen(x,y):
  Confirmingturtle.confirmplayscreen()
  Falling.cleararrows()
  Falling.confirmlevel()
  #
  wn.bgpic('bggray.gif')
  global oogway
  oogway = tr.Turtle()
  oogway.hideturtle()
  oogway.shape("startbutton.gif")
  oogway.penup()
  oogway.goto(220, 120)
  oogway.showturtle()
  # choose your character
  global charslot1
  global charslot2
  global charslot3
  
  charslot1 = tr.Turtle()
  charslot1.hideturtle()
  charslot1.penup()
  charslot1.shape('anpro.gif')
  charslot1.setpos(-230, -30)
  
  charslot2 = tr.Turtle()
  charslot2.hideturtle()
  charslot2.penup()
  charslot2.shape('karpro.gif')
  charslot2.setpos(-30, -30)

  charslot3 = tr.Turtle()
  charslot3.hideturtle()
  charslot3.penup()
  charslot3.shape('sharpro.gif')
  charslot3.setpos(190, -30)

  charslot1.showturtle()
  charslot2.showturtle()
  charslot3.showturtle()

  charslot1.onclick(slot1)
  charslot2.onclick(slot2)
  charslot3.onclick(slot3)
  
  #
  global canpressstart
  canpressstart = True
  oogway.onclick(playclicked)
  wn.onkeypress(Falling.clickleft, "Left")
  wn.onkeypress(Falling.clickup, "Up")
  wn.onkeypress(Falling.clickdown, "Down")
  wn.onkeypress(Falling.clickright, "Right")
  wn.listen()


Falling.getlevel()
confirmturtle.onclick(playscreen)


wn.mainloop()