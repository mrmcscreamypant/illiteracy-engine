from .compile_js import compile_js
from .compile_css import compile_css

from config.webserver import PROJECT_NAME

def html_wrap():
  print("Injecting into boilerplate HTML...")
  
  result = f"""\
<!DOCTYPE html>
<html>
  <head>
    <title>{PROJECT_NAME}</title>
    <script>
      {compile_js()}
    </script>
    <style>
      {compile_css()}
    </style>
  </head>
  <body>
    <canvas id="screen"></canvas>
  </body>
</html>\
"""
  
  print("HTML complete")
  return result