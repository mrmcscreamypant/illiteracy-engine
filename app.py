class Main():
  def __init__(self):
    self.renders = []

  def draw(self):
    for render in self.renders:
      render.draw()

  def update(self):
    pass