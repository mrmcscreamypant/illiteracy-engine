from build.regester import regesterObjects

def build_game_js_files():
    print("Regestering client object files...")
    objects = regesterObjects("./game/objects","py","game.objects",args={"build":True})

    result = "var _objects = [];"
    for object in objects:
        result += object.compile_js()
        result += f"_objects.push(new {object.__class__.__name__}(build=true));"

    print("Client object files regestered")
    return result