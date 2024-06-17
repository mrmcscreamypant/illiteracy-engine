from pgzero.screen import SurfacePainter
from renders.customRender import CustomRender
from renders.regester import renderObject
import pgzero.game as pgzscreen
import pgzero.screen as pgzdraw

@renderObject
class PlayerRender(CustomRender):
  def __init__(self,main):
    super().__init__(main,"player",1)
    self.objects = []

  def draw(self):
    screen = pgzdraw.Screen(pgzscreen.screen)
    for object in self.objects:
      screen.draw.text("foo",object.pos)