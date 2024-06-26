from bottle import *
from config.build import CLIENT_FILE_PATH

print("\nIlliteracy Engine - v0.0.0alpha\n")

def get_client_file():
  print(f"fetching pre-built client file '{CLIENT_FILE_PATH}'")
  with open(CLIENT_FILE_PATH,"r") as file:
    data = file.read()
    print("client file fetched sucessfully")
  return data

client_file = get_client_file()

@route("/")
def game():
  return client_file

print("\nLaunching bottle server...\n")

run(host="0.0.0.0",port=8080)