from .compile_js import compile_js
from .compile_css import compile_css

from config.webserver import PROJECT_NAME
import random


def html_wrap():
  print("Injecting into boilerplate HTML...")

  result = f"""\
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
    <canvas id="screen">Error loading HTML canvas</canvas>
  </body>\
"""

  print("HTML complete")
  return result
