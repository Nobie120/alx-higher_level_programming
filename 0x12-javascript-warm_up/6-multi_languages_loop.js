#!/usr/bin/node

/*
 * while loop
 */

const array = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let count = 0;
while (count !== array.length) {
  console.log(array[count]);
  count++;
}