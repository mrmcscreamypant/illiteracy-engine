from entities.customEntity import Entity
from entities.regester import entityObject

@entityObject
class Player(Entity):
  def __init__(self,main):
    super().__init__(main,None)