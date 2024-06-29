from .getfile import get

from .regester import regesterFiles

from .textutil import info,warn

def compile_css():
  print("\nCompiling CSS...")

  print("Regestering CSS files...")
  chunks = regesterFiles("./build/templates/css","css")
  print("Files regestered")

  result = ""
  for chunk in chunks:
    try:
      result += get("css/"+chunk)
      info(f"Sucessfully imported CSS chunk '{chunk}'")
    except Exception as e:
      warn(f"Failed to import CSS chunk '{chunk}' {e}")

  print("CSS complete\n")
  return result