#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = 0;
    do {
      i++;
      console.log(c.repeat(this.width));
    } while (i < this.height);
  }
}
module.exports = Square;
