#!/usr/bin/node

/*
 * printing a square
 */

const size = parseInt(process.argv[2], 10);

if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    let count = '';
    for (let j = 0; j < size; j++) {
      count += 'X';
    }
    console.log(count);
  }
} else { console.log('Missing size'); }
