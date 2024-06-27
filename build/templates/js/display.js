class CanvasElement {
  constructor() {
    this.element = document.getElementById("screen")
    this.screen = this.element.getContext("2d")
  }
}


class Display {
  constructor() {
    console.log("Constructing display...")

    console.log("Placing HTML canvas...")
    document.getElementById("body").innerHTML = "<div id='canvas-wrap'><canvas id='screen'>Error loading HTML canvas</canvas></div>"
    console.log("HTML canvas placed")

    this.element = new CanvasElement()
    this.screen = this.element.screen

    this.display_welcome_message()
    
    console.log("Canvas properly initalized")
  }

  display_welcome_message() {
    var grd = this.screen.createLinearGradient(0, 0, 200, 0);
    grd.addColorStop(0, "red");
    grd.addColorStop(1, "white");

    // Fill with gradient
    this.screen.fillStyle = grd;
    this.screen.fillRect(0, 0, 150, 80);
  }

  getMousePos(canvasDom, mouseEvent) {
    var rect = this.element.getBoundingClientRect();
    return {
      x: (mouseEvent.clientX - rect.left) * this.width/window.innerWidth,
      y: (mouseEvent.clientY - rect.top) * this.width/window.innerWidth
    };
  }
}