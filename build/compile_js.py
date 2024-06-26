from .getfile import get

from .textutil import info,warn

chunks = [
]

def compile_js():
  print("Compiling JS...")
  result = ""
  for chunk in chunks:
    try:
      result += get("js/"+chunk)
      info(f"Sucessfully imported JS chunk '{chunk}'")
    except FileNotFoundError:
      warn(f"Failed to import JS chunk '{chunk}' (418)")

  print("JS complete")
  return result