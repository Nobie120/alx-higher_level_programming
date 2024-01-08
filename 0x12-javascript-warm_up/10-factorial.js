#!/usr/bin/node

/*
 * factorial using recursion
 */

function factorial (n) {
  if (n < 0) { return undefined; }
  if (n === 1 || isNaN(n)) { return 1; }
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2], 10);
console.log(factorial(num));
