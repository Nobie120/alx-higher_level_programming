#!/usr/bin/node

const Squarep = require('./5-square.js');

class Square extends Squarep {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    if (Object.keys(this).length === 0) {
      console.log('');
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
