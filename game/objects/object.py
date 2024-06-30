from game.utils.vec import Vec

from build.regester import regesterObject

def clientMethod(self,func):
  self.client_methods.append(func)
  return func

@regesterObject
class GameObject:
  """
  The base for all objects in the game
  To inherit from, do:
  class <...>(Object):
    def _init(self,<...>):
      <...>
  
  *IMPORTANT: all subclasses CANNOT use __init__(). They must use _init() instead.
  """
  client_methods = []

  def __init__(self,build=False,*args):
    if build:
      return
    self._init(*args)
  
  def compile_js(self):
    methods = ""
    for method in self.client_methods:
      methods += method

    return f"""
class client{self.__class__.__name__} {{
  constructor() {{}}
  {methods}
}}

    """
  
  def _init(self):
    pass