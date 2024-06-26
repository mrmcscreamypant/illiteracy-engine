import renders.regester
import entities.regester

class Main():
  def __init__(self):

    self.initRenders()
    self.initEntities()
  
  def initRenders(self):
    self.renders = {}
    renders.regester.regesterRenders(self)

  def initEntities(self):
    self.entities = []
    entities.regester.regesterEntities(self)