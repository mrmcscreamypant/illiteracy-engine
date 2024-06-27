
class Display {
  constructor() {
    this.element = document.getElementById("screen")
    this.screen = this.element.getContext2d()
  }
}