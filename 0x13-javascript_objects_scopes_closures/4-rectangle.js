#!/usr/bin/node

class Rectangle {
  construct (w, h) {
    if ((w > 0) && (h > 0)) {
      this.weight = w;
      this.height = h;
    }
  }

  print () {
    if (Objects.keys(this).length === 0) {
      console.log("");
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log("X".repeat(this.width));
      }
    }
  }
}


module.exports = Rectangle;
