from .getfile import get

from .textutil import info,warn

chunks = [
  "vec.js",
  "engine.js",
  "bootstrap.js",
  "request.js",
  "display.js"
]

def compile_js():
  print("Compiling JS...")
  result = ""
  for chunk in chunks:
    try:
      result += f"\n\n//{chunk}\n\n"
      result += f"""\
      {get("js/"+chunk)}\
      """
      info(f"Sucessfully imported JS chunk '{chunk}'")
    except FileNotFoundError:
      warn(f"Failed to import JS chunk '{chunk}' (418)")

  print("JS complete")
  return result