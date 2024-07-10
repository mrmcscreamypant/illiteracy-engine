class Engine {
  constructor() {
    console.log("Engine loading...")

    this.display = new Display(this)

    for (var i=0;i<_objects.length;i++) {
      _objects[i]._regester()
    }

    console.log("Engine properly initalized")
  }
}