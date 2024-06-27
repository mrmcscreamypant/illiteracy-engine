from bottle import route, run
from config.build import CLIENT_FILE_PATH
from config.webserver import PATH_TO_GAME

import json

def go():
  print("\nIlliteracy Engine - v0.0.0alpha\n")
  
  def get_client_file():
    print(f"fetching pre-built client file '{CLIENT_FILE_PATH}'")
    with open(CLIENT_FILE_PATH,"r") as file:
      data = file.read()
      print("client file fetched sucessfully")
    return data
  
  def get_bootstrap_client_file():
    path_to_file = "webserver/static/bootstrap_client.html"
    
    print(f"fetching bootstrap client file '{path_to_file}'")
    with open(path_to_file,"r") as file:
      data = file.read()
      print("client bootstrap file fetched sucessfully")
    return data
  
  client_file = json.loads(get_client_file())
  bootstrap_client_file = get_bootstrap_client_file()
  
  @route(PATH_TO_GAME)
  def game():
    return bootstrap_client_file
  
  @route("/bootstrap-client/js")
  def client_raw_js():
    return client_file["js"]

  @route("/bootstrap-client/css")
  def client_raw_css():
    return client_file["css"]

  
  print("\nLaunching bottle server...\n")
  
  run(host="0.0.0.0",port=8080)

if __name__ == "__main__":
  go()