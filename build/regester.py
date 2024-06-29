import os
from .textutil import info,warn

class NonMatchedExtension(Exception):
  pass

regesteredObjects = []

def regesterObject(func):
  def wrapperRenderObject(*args, **kwargs):
    func(*args, **kwargs)
  regesteredObjects.append(wrapperRenderObject)
  return wrapperRenderObject

def regesterObjects(path,extension,module=".",args=()):
  regesteredObjects = []
  for dir in os.listdir(path):
    try:
      name = dir.split(".")[0]
      ext = dir.split(".")[-1]

      if extension != ext:
        raise NonMatchedExtension()

      __import__(f"{module}.{name}")
      regesteredObjects[-1](*args)
      info(f"'{dir}' sucessfully regestered")
    except ImportError as e:
      warn(f"Error regestering '{dir}': '{e}'")
    except NonMatchedExtension:
      warn(f"Skipping regestering '{dir}' (.{ext} != .{extension})")
  return regesteredObjects
  
def regesterFiles(path,extension):
  regesteredObjects = []
  for dir in os.listdir(path):
    try:
      ext = dir.split(".")[-1]

      if extension != ext:
        raise NonMatchedExtension()

      regesteredObjects.append(dir)
      info(f"'{dir}' sucessfully regestered")
    except ImportError as e:
      warn(f"Error regestering '{dir}': '{e}'")
    except NonMatchedExtension:
      warn(f"Skipping regestering '{dir}' (.{ext} != .{extension})")
  return regesteredObjects