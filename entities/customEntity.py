from utils.vec import Vec

class Entity():
  def __init__(self,main,renderer,pos=Vec(0,0)):
    self.main = main
    self.pos = pos
    try:
      self.main.renders[renderer].objects.append(self)
    except AttributeError:
      print(f"Renderer '{renderer}' does not support entities")
    except KeyError:
      print(f"Renderer '{renderer}' is not properly regestered")