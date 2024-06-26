import os

renderObjects = []

def renderObject(func):
  def wrapperRenderObject(*args, **kwargs):
    func(*args, **kwargs)
  renderObjects.append(wrapperRenderObject)
  return wrapperRenderObject

def regesterRenders(main):
  for dir in os.listdir("./renders/renderObjects"):
    try:
      __import__("renders.renderObjects."+dir[0:-3],fromlist=["render.renderObjects"])
      renderObjects[-1](main)
      print(f"Custom renderer '{dir}' sucessfully imported")
    except ImportError as e:
      print(f"Error importing custom renderer '{dir}': '{e}'")