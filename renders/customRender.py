class CustomRender():
  def __init__(self,main):
    self.main = main
    self.main.renders.append(self)