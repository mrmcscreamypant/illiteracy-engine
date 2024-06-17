import pgzrun
from app import Main

app = Main()

def update():
  app.update()

def draw():
  app.draw()

pgzrun.go()