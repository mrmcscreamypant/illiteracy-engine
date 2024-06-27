from .compile_js import compile_js
from .compile_css import compile_css

import json

def full_compile():
  result = {}
  result["js"] = compile_js()
  result["css"] = compile_css()
  return json.dumps(result)