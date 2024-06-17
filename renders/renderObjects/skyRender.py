from renders.customRender import CustomRender
from renders.regester import renderObject
import pgzero.game as pgz

@renderObject
class SkyRender(CustomRender):
  def __init__(self,main):
    super().__init__(main,-1)

  def draw(self):
    pgz.screen.fill("skyblue")