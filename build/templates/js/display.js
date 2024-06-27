
class Display {
  constructor() {
    console.log("Constructing display...")

    console.log("Placing canvas...")
    document.getElementById("body").innerHTML = "<canvas id='screen'>Error loading HTML canvas</canvas>"
    
    this.element = document.getElementById("screen")
    this.screen = this.element.context2d()
  }
}