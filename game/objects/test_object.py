from build.regester import regesterObject
from .object import GameObject, clientMethod

@regesterObject
class TestObject(GameObject):
    def _init(self):
      clientMethod(self,
        """
        constructor() {
          alert(foo)
        }
        """)