from .html_wrap import html_wrap

from .compile_js import compile_js

import json

def full_compile():
  result = {}
  result["js"] = compile_js()
  return json.dumps(result)