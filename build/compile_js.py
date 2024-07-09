from .getfile import get

from .regester import regesterFiles
from game.compile_js import build_game_js_files

from .textutil import info,warn

def compile_js():
  print("\nCompiling JS...")

  print("Compiling game JS files...")
  result = build_game_js_files()
  print("Game JS files compiled")

  print("Regestering build JS files...")
  chunks = regesterFiles("./build/templates/js","js")
  print("Build files regestered")

  for chunk in chunks:
    try:
      result += get("js/"+chunk)
      info(f"Sucessfully imported JS chunk '{chunk}'")
    except Exception as e:
      warn(f"Failed to import JS chunk '{chunk}': {e}")

  print("JS complete\n")
  return result