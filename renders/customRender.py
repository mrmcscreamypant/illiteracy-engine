class CustomRender():
  def __init__(self,main,zorder):
    self.main = main
    self.zorder = zorder
    self.main.renders.append(self)