from game.objects.object import GameObject
from build.regester import regesterObject

_renders = []

@regesterObject
class Render(GameObject):
    def _regester(self):
        super()._init()
        print(f"Render {self.__class__} regestered")
        _renders.push(self)

    def draw(self):
        pass