class CanvasElement {
  constructor() {
    this.element = document.getElementById("screen")
    this.fix_resolution()
    this.screen = this.element.getContext("2d")
    this.screen.scale(1,1)
  }

  fix_resolution() {
    const dimensions = this.getObjectFitSize(
      true,
      this.element.clientWidth,
      this.element.clientHeight,
      this.element.width,
      this.element.height
    );
  
    this.element.width = dimensions.width;
    this.element.height = dimensions.height;
  }

  getObjectFitSize(
    contains /* true = contain, false = cover */,
    containerWidth,
    containerHeight,
    width,
    height
  ) {
    var doRatio = width / height;
    var cRatio = containerWidth / containerHeight;
    var targetWidth = 0;
    var targetHeight = 0;
    var test = contains ? doRatio > cRatio : doRatio < cRatio;
  
    if (test) {
      targetWidth = containerWidth;
      targetHeight = targetWidth / doRatio;
    } else {
      targetHeight = containerHeight;
      targetWidth = targetHeight * doRatio;
    }
  
    return {
      width: targetWidth,
      height: targetHeight,
      x: (containerWidth - targetWidth) / 2,
      y: (containerHeight - targetHeight) / 2
    };
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
    this.drawText("No render defined...",{x:0,y:0})
  }

  drawText(text,vec,fontsize=50,font="Arial") {
    this.screen.fill = "red"
    this.screen.font = `${fontsize}px ${font}`
    this.screen.fillText(text,vec.x,vec.y+fontsize)
  }

  getMousePos(canvasDom, mouseEvent) {
    var rect = this.element.getBoundingClientRect();
    return {
      x: (mouseEvent.clientX - rect.left) * this.width/window.innerWidth,
      y: (mouseEvent.clientY - rect.top) * this.width/window.innerWidth
    };
  }
}