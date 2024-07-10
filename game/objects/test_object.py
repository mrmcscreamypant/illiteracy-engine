from build.regester import regesterObject
from .object import GameObject

@regesterObject
class TestObject(GameObject):
    def _init(self,main):
      pass