class CustomRender():
  def __init__(self,main,name,zorder):
    self.main = main
    self.zorder = zorder
    self.main.renders[name]=(self)