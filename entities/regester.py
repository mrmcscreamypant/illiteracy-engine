import os

entityObjects = []

def entityObject(func):
  def wrapperEntityObject(*args, **kwargs):
    func(*args, **kwargs)
  entityObjects.append(wrapperEntityObject)
  return wrapperEntityObject

def regesterEntities(main):
  for dir in os.listdir("./entities/entityObjects"):
    try:
      __import__("entities.entityObjects."+dir[0:-3],fromlist=["entities.entityObjects"])
      entityObjects[-1](main)
      print(f"Custom entity '{dir}' sucessfully imported")
    except ImportError as e:
      print(f"Error importing custom entity '{dir}': '{e}'")