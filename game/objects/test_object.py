from build.regester import regesterObject
from .object import GameObject, clientMethod

@regesterObject
class TestObject(GameObject):
    def _init(self,main):
      main.display.fill("green")
