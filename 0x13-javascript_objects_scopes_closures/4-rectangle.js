#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w && h) && (w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const arr = [];
    for (let i = 0; i < this.width; i++) {
      arr.push('X');
    }
    for (let j = 0; j < this.height; j++) {
      console.log(arr.join(''));
    }
  }

  rotate () {
    const w = this.width;
    this.width = this.height;
    this.height = w;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
