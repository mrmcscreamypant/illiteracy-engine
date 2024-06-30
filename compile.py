from config.build import CLIENT_FILE_PATH

from build.exception import BuildException
from build.compile import full_compile

from build.textutil import warn

def go():
  print("\nIlliteracy Engine - builder version v0.0.0alpha\n")
  
  print(f"Configured build output file is '{CLIENT_FILE_PATH}'")
  warn("The file will be overwritten")
  try:
    pass#input("Press enter to continue (ctrl+c to cancel) ")
  except KeyboardInterrupt:
    raise BuildException("Build cancled")
  
  print("\nBeginning compile...")
  result = full_compile()
  print("Finished comple\n")
  
  with open(CLIENT_FILE_PATH,"w") as file:
    print("Writing to output file...")
    file.write(result)
  print("Successfully wrote to output file")
  
  print("\nBUILD COMPLETE")

if __name__ == "__main__":
  go()