class Engine {
  constructor() {
    console.log("Engine loading...")

    this.display = new Display(this)

    console.log("Engine properly initalized")
  }
}