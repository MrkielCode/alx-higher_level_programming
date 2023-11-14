#!/usr/bin/node
const Squares = require('./5-square');

class Square extends Squares {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
        console.log('C'.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
