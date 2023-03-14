#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      const arr = [];
      for (let i = 0; i < this.width; i++) {
        arr.push(c);
      }
      for (let j = 0; j < this.height; j++) {
        console.log(arr.join(''));
      }
    }
  }
}
module.exports = Square;
