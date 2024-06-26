class Vec():
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def __iter__(self):
    self.iter = [self.y,self.x]
    return self

  def __next__(self):
    if len(self.iter) == 0:
      raise StopIteration
    return self.iter.pop()