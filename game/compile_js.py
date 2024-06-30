from build.regester import regesterObjects

def build_game_js_files():
    print("Regestering client object files...")
    objects = regesterObjects("./game/objects","py","game.objects",args={"build":True})
    result = ""
    for object in objects:
        result += object.compile_js()
    print("Client object files regestered")
    return result