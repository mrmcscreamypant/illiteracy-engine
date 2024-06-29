from .getfile import get

from .regester import regesterFiles

from .textutil import info,warn

def compile_js():
  print("\nCompiling JS...")

  print("Regestering JS files...")
  chunks = regesterFiles("./build/templates/js","js")
  print("Files regestered")

  result = ""
  for chunk in chunks:
    try:
      result += get("js/"+chunk)
      info(f"Sucessfully imported JS chunk '{chunk}'")
    except Exception as e:
      warn(f"Failed to import JS chunk '{chunk}': {e}")

  print("JS complete\n")
  return result