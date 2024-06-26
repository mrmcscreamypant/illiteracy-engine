def get(filename):
  with open("build/templates/"+filename,"r") as file:
    return file.read()