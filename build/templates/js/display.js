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

var _renders = []

class Display {
  constructor() {
    console.log("Constructing display...")

    console.log("Placing HTML canvas...")
    document.getElementById("body").innerHTML = "<div id='canvas-wrap'><canvas id='screen'>Error loading HTML canvas</canvas></div>"
    console.log("HTML canvas placed")

    this.element = new CanvasElement()
    this.screen = this.element.screen

    this.display_welcome_message()

    console.log("Canvas refresh trigger regestering....")
    const self = this;setInterval(()=>{self.refresh(self)},16)
    console.log("Canvas refresh trigger regestered")
    
    console.log("Canvas properly initalized")
  }

  refresh(self) {
    for (var i=0;i<_renders.length;i++) {
      console.log(_renders[i])
    }
  }

  display_welcome_message() {
    this.drawText("Loading...",{x:5,y:this.element.element.height-25},20)
  }

  fill(color="white") {
    this.screen.fillStyle = color
    this.screen.fillRect(0,0,this.element.element.width,this.element.element.height)
  }

  drawText(text,vec,fontsize=50,font="Arial",color="black") {
    this.screen.fillStyle = color
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