#!/usr/bin/node
function factorize (n) {
  if (n < 0) {
    return -1;
  }
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorize(n - 1);
}

console.log(factorize(Number(process.argv[2])));
