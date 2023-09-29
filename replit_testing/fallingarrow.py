import turtle as tr
import time
import threading
from confirming import Confirmingturtle
from heartsappear import Hearts

class Falling:

  tr.register_shape('fallleft.gif')
  tr.register_shape('fallup.gif')
  tr.register_shape('falldown.gif')
  tr.register_shape('fallright.gif')
  
  tr.register_shape('uparrow.gif')
  tr.register_shape('downarrow.gif')

  tr.register_shape('leveleasy.gif')
  tr.register_shape('levelmed.gif')
  tr.register_shape('levelhard.gif')

  tr.register_shape('bar.gif')
  tr.register_shape('replaybutton.gif')
  
  tr.register_shape('karactive.gif')
  tr.register_shape('karidle.gif')
  tr.register_shape('anactive.gif')
  tr.register_shape('anidle.gif')
  tr.register_shape('sharactive.gif')
  tr.register_shape('sharidle.gif')

  tr.register_shape('kardeath1.gif')
  tr.register_shape('kardeath2.gif')
  tr.register_shape('shardeath1.gif')
  tr.register_shape('shardeath2.gif')
  tr.register_shape('andeath1.gif')
  tr.register_shape('andeath2.gif')
  
  global fontsetup
  fontsetup = ("small-caps", 20, 'bold')
  global directions
  directions = ["left", "up", "down", "right"]
  global levels
  levels = ['leveleasy.gif', 'levelmed.gif', 'levelhard.gif']
  global characters
  global activegifs
  global deathgifs1
  global deathgifs2
  characters = ['anidle.gif','karidle.gif', 'sharidle.gif']
  activegifs = ['anactive.gif','karactive.gif', 'sharactive.gif']
  deathgifs1 = ['andeath1.gif','kardeath1.gif','shardeath1.gif']
  deathgifs2 = ['andeath2.gif','kardeath2.gif','shardeath2.gif']
  global c
  c = 0
  global barlevel
  barlevel = 70
  global lives
  lives = 10
  global level
  global L
  L = 0
  global score
  score = 0
  global gamestart
  gamestart = False
  global stopdeathanimation
  stopdeathanimation = True
  global scoreturtle
  global levelturtle
  global upturtle
  global downturtle
  global replayconfirm
  # scribe turtles
  scoreturtle = tr.Turtle()
  scoreturtle.hideturtle()
  scoreturtle.penup()
  scoreturtle.goto(-100,100)
  #
  levelturtle = tr.Turtle()
  levelturtle.hideturtle()
  levelturtle.shape('leveleasy.gif')
  levelturtle.penup()
  levelturtle.goto(0,-5)
  # level selecting arrows
  upturtle = tr.Turtle()
  upturtle.hideturtle()
  upturtle.shape("uparrow.gif")
  upturtle.penup()
  upturtle.goto(0,90)
  upturtle.speed(10)
  upturtle.showturtle()
  #
  downturtle = tr.Turtle()
  downturtle.hideturtle()
  downturtle.shape("downarrow.gif")
  downturtle.penup()
  downturtle.goto(0,-90)
  downturtle.showturtle()
  downturtle.speed(10)
  # CHARACTER TURTLES
  global character
  character = tr.Turtle()
  character.hideturtle()
  character.penup()
  #
  global selfturtle
  selfturtle = tr.Turtle()
  selfturtle.hideturtle()
  #
  Hearts(5)
  
  def __init__(self, randomnumber):
    global selfturtle
    self.randomnumber = randomnumber
    selfturtle = tr.Turtle()
    selfturtle.hideturtle()
    selfturtle.penup()

  def getlives():
    global lives
    return lives
  
  def selectcharacter(slot):
    global c
    c = slot - 1
    
  def resetgame(x,y):
    global upturtle
    global downturtle
    global levelturtle
    global levels
    global character
    global score
    global gamestart
    global stopdeathanimation
    global level
    global L
    L = 0
    level = "easy"
    score = 0
    gamestart = False
    stopdeathanimation = True
    character.hideturtle()
    resetbutton.hideturtle()
    resetbutton.clear()
    scoreturtle.clear()
    scoreturtle.goto(-100,100)
    scoreturtle.pencolor('black')
    upturtle.goto(0,90)
    downturtle.goto(0,-90)
    upturtle.showturtle()
    downturtle.showturtle()
    levelturtle.showturtle()
    levelturtle.shape('leveleasy.gif')
    Confirmingturtle.defturt(fontsetup)
    Confirmingturtle.confirmendgame(fontsetup)
    upturtle.onclick(Falling.changelevelup)
    downturtle.onclick(Falling.changeleveldown)

  def cleararrows():
    upturtle.hideturtle()
    downturtle.hideturtle()
    upturtle.setpos(-600,-600)
    downturtle.setpos(-600,-600)

  def resetbuttonfunction():
    global startgame
    global bar
    global resetbutton
    global lives
    scoreturtle.clear()
    time.sleep(2)
    character.setpos(0,0)
    scoreturtle.goto(175, 0)
    scoreturtle.pencolor('#4CD45E')
    Hearts.resetlives(lives)
    time.sleep(2)
    scoreturtle.write("Score:\n " + str(score), font=fontsetup, align='center')
    startgame = False
    lives = 5
    time.sleep(1)
    resetbutton = tr.Turtle()
    resetbutton.hideturtle()
    resetbutton.penup()
    resetbutton.setpos(200, -100)
    resetbutton.shape('replaybutton.gif')
    resetbutton.showturtle()
    resetbutton.onclick(Falling.resetgame)

  def deathanimation():
    global c
    global stopdeathanimation
    while stopdeathanimation == False:
      character.shape(deathgifs1[c])
      time.sleep(.4)
      character.shape(deathgifs2[c])
      time.sleep(.4)
    character.hideturtle()
  
  def reportscore():
    global stopdeathanimation
    stopdeathanimation = False
    selfturtle.hideturtle()
    bar.hideturtle()
    reportscorethread1 = threading.Thread(target=Falling.deathanimation)
    reportscrorethread2 = threading.Thread(target=Falling.resetbuttonfunction)
    reportscorethread1.start()
    reportscrorethread2.start()
    
  def updatescore():
    global startgame
    global c
    if startgame == False:
      pass
    else:
      scoreturtle.clear()
      scoreturtle.write("Score: " + str(score), font=("courier",20,"bold"), align='left')
      
      
  def characteranimate():
    global stopdeathanimation
    if stopdeathanimation==True:
      character.shape(activegifs[c])
      time.sleep(.85)
      if stopdeathanimation==True:
        character.shape(characters[c])
  global t2
  t2 = threading.Thread(target=characteranimate)
    
  def changelevelup(x,y):
    global level
    global L
    L += 1
    if L > 2:
      L = 0
    Falling.getlevel()

  def changeleveldown(x,y):
    global level
    global L
    L -= 1
    if L < 0:
      L = 2
    Falling.getlevel()
  
  def confirmlevel():
    global level
    global lives
    global levelturtle
    global upturtle
    global downturtle
    if L == 0:
      level = "easy"
      lives = 5
    elif L == 1:
      level = "medium"
      lives = 3
    elif L == 2:
      level = "hard"
      lives = 1
    #
    upturtle.hideturtle()
    downturtle.hideturtle()
    upturtle.goto(-500,-500)
    downturtle.goto(-500,-500)
    levelturtle.hideturtle()
  
  def getlevel():
    levelturtle.showturtle()
    levelturtle.shape(levels[L])
    upturtle.onclick(Falling.changelevelup)
    downturtle.onclick(Falling.changeleveldown)

  def resetgamestart():
    gamestart == False
  
  def levelspeed():
    global barlevel
    global selfturtle
    global c
    global characters
    global character
    global gamestart
    if level == "easy":
      selfturtle.speed(.6)
      barlevel = 70
    elif level == "medium":
      selfturtle.speed(1)
      barlevel = 55
    elif level == "hard":
      selfturtle.speed(1.45)
      barlevel = 35
    if gamestart == False:
      global bar
      bar = tr.Turtle()
      bar.shape("bar.gif")
      bar.penup()
      bar.hideturtle()
      bar.setposition(-160, barlevel)  
      bar.showturtle()
      character = tr.Turtle()
      character.hideturtle()
      character.penup()
      character.goto(120,-20)
      character.shape(characters[c])
      character.showturtle()
    gamestart = True
    
  
  def startfall(self, direction, randomnumber):
    global selfturtle
    global falling
    falling = 'none'
    global startgame
    startgame = True
    #
    scoreturtle.write("Score: " + str(score), font=("courier",20,"bold"), align='left')
    self.direction = directions[self.randomnumber]
    if self.direction == "left":
      selfturtle.goto(-240,barlevel)
      selfturtle.shape('fallleft.gif')
      selfturtle.showturtle()
      Falling.levelspeed()
      falling = "left"
      selfturtle.goto(selfturtle.xcor(),selfturtle.ycor()+(-75-barlevel))
    elif self.direction == "up":
      selfturtle.goto(-190, barlevel)
      selfturtle.shape('fallup.gif')
      selfturtle.showturtle()
      Falling.levelspeed()
      falling = "up"
      selfturtle.goto(selfturtle.xcor(),selfturtle.ycor()+(-75-barlevel))
    elif self.direction == "down":
      selfturtle.goto(-140, barlevel)
      selfturtle.shape('falldown.gif')
      selfturtle.showturtle()
      Falling.levelspeed()
      falling = "down"
      selfturtle.goto(selfturtle.xcor(),selfturtle.ycor()+(-75-barlevel))
    elif self.direction == "right":
      selfturtle.goto(-90, barlevel)
      selfturtle.shape('fallright.gif')
      selfturtle.showturtle()
      Falling.levelspeed()
      falling = "right"
      selfturtle.goto(selfturtle.xcor(),selfturtle.ycor()+(-75-barlevel))
    selfturtle.hideturtle()
    falling = "none"

  
  def threadsgo():
    global t1
    global t2
    t1 = threading.Thread(target=Falling.updatescore)
    t2 = threading.Thread(target=Falling.characteranimate)
    t1.start()
    t2.start()

  def wrong():
    global lives
    lives -=1
    Hearts.removelife(lives)
    
  def clickleft():
    global score
    global barlevel
    global stopdethanimation
    if t2.is_alive()==False and stopdeathanimation==True:
      if falling == "left" and selfturtle.ycor()>-225 and selfturtle.ycor()<barlevel:
        score += (int(selfturtle.ycor()+75))
      else:
        Falling.wrong()
      Falling.threadsgo()
#
  def clickup():
    global score
    global barlevel
    global stopdethanimation
    if t2.is_alive()==False and stopdeathanimation==True:
      if falling == "up" and selfturtle.ycor()>-215 and selfturtle.ycor()<barlevel:
        score += (int(selfturtle.ycor()+75))
      else:
        Falling.wrong()
      Falling.threadsgo()
#
  def clickdown():
    global score
    global barlevel
    global stopdethanimation
    if t2.is_alive()==False and stopdeathanimation==True:
      if falling == "down" and selfturtle.ycor()>-235 and selfturtle.ycor()<barlevel:
        score += (int(selfturtle.ycor()+75))
      else:
        Falling.wrong()
      Falling.threadsgo()
  #    
  def clickright():
    global score
    global barlevel
    global stopdethanimation
    if t2.is_alive()==False and stopdeathanimation==True:
      if falling == "right" and selfturtle.ycor()>-225 and selfturtle.ycor()<barlevel:
        score += (int(selfturtle.ycor()+75))
      else:
        Falling.wrong()
      Falling.threadsgo()