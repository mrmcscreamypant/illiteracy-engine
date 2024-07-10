import os
from .textutil import info,warn

class NonMatchedExtension(Exception):
  pass

class FoundFolder(Exception):
  pass

newRegesteredObjects = []

def regesterObject(func):
  class wrapperRenderObject():
    name = func.__name__
    def call(*args, **kwargs):
      return func(*args,**kwargs)
  
  newRegesteredObjects.append(wrapperRenderObject)
  print(f"Found object {func} to regester")
  return func

def regesterObjects(path,extension,module=".",args={}):
  global newRegesteredObjects
  def dummy_func(*kw):
    pass

  regesteredObjects = [dummy_func]
  for dir in os.listdir(path):
    try:
      newRegesteredObjects = []
      name = dir.split(".")[0]
      ext = dir.split(".")[-1]

      if extension != ext:
        if os.path.isdir(path+"/"+dir):
          raise FoundFolder()
        raise NonMatchedExtension()

      exec(f"import {module}.{name}")

      for object in newRegesteredObjects:
        regesteredObjects.append(object.call(**args))
        print(f"Object '{object.name}' sucessfully regestered from file '{dir}'")
      
      info(f"'{dir}' sucessfully regestered")
    except FoundFolder:
      info(f"Sub-dir found - regestering files in dir '{path}/{dir}'")
      regesteredObjects += regesterObjects(path+f"/{dir}",extension,module+f".{dir}",args)
    except NonMatchedExtension:
      warn(f"Skipping regestering '{dir}' (.{ext} != .{extension})")
    except Exception as e:
      warn(f"Error regestering '{dir}': '{e}'")
  return regesteredObjects[1:]
  
def regesterFiles(path,extension):
  regesteredObjects = []
  for dir in os.listdir(path):
    try:
      ext = dir.split(".")[-1]

      if extension != ext:
        raise NonMatchedExtension()

      regesteredObjects.append(dir)
      info(f"'{dir}' sucessfully regestered")
    except NonMatchedExtension:
      warn(f"Skipping regestering '{dir}' (.{ext} != .{extension})")
  return regesteredObjects