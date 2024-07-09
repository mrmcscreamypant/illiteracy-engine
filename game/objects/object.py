from game.utils.vec import Vec

from build.regester import regesterObject

from pscript import py2js

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
  
  def __init__(self,build=False,*args):
    self.client_methods = []

    if build:
      self._regester()
      return
    self._init(*args)
  
  def compile_js(self):
    return py2js(self.__class__)
  
  def _regester(self):
    pass
  
  def _init(self):
    pass