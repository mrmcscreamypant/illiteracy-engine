from .getfile import get

from .textutil import info,warn

chunks = [
  "document.css",
  "canvas.css",
  "loader.css",
  "loading_screen.css"
]

def compile_css():
  print("Compiling CSS...")
  result = ""
  for chunk in chunks:
    try:
      result += get("css/"+chunk)
      info(f"Sucessfully imported CSS chunk '{chunk}'")
    except FileNotFoundError:
      warn(f"Failed to import CSS chunk '{chunk}' (418)")

  print("CSS complete")
  return result